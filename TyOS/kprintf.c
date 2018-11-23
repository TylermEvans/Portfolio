
//from the newlib library
// http://sources.redhat.com/newlib/
//which came from UCB, as per this notice:

/*
 * Copyright (c) 1990 The Regents of the University of California.
 * All rights reserved.
 *
 * This code is derived from software contributed to Berkeley by
 * Chris Torek.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *	This product includes software developed by the University of
 *	California, Berkeley and its contributors.
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#include "stdarg.h"
#include "kprintf.h"

typedef unsigned long u_long ;
typedef unsigned short u_short ;
typedef unsigned int u_int ; 

void console_putc(char x);


static char* my_memchr(char* s, int c, int n)
{
	int i;
	for(i=0;i<n;++i){
		if( s[i] == c )
			return s+i;
	}
	return 0;
}

static int my_strlen(char* s)
{
	int i = 0;
	while( *s ){
		++s;
		++i;
	}
	
	return i;
}


/*
 * Actual printf innards.
 *
 * This code is large and complicated...
 */


#define	BUF		40

#define quad_t long
#define u_quad_t unsigned long

typedef quad_t * quad_ptr_t;
typedef void*     void_ptr_t;
typedef char *   char_ptr_t;
typedef long *   long_ptr_t;
typedef int  *   int_ptr_t;
typedef short *  short_ptr_t;



/*
 * Macros for converting digits to letters and vice versa
 */
#define	to_digit(c)	((c) - '0')
#define is_digit(c)	((unsigned)to_digit (c) <= 9)
#define	to_char(n)	((n) + '0')

/*
 * Flags used during conversion.
 */
#define	ALT		0x001		/* alternate form */
#define	HEXPREFIX	0x002		/* add 0x or 0X prefix */
#define	LADJUST		0x004		/* left adjustment */
#define	LONGDBL		0x008		/* long double */
#define	LONGINT		0x010		/* long integer */
#define	QUADINT		LONGINT
#define	SHORTINT	0x040		/* short integer */
#define	ZEROPAD		0x080		/* zero (as opposed to blank) pad */

static int kprintf_internal( char* dest, char* fmt0 , va_list ap );


int kprintf( char* fmt0, ... )
{
	int rv;
	va_list vv;
	va_start(vv,fmt0);
	rv = kprintf_internal( 0 , fmt0, vv );
	va_end(vv);
	return rv;
}

int ksprintf( char* s, char* fmt0 , ... )
{
	int rv;
	va_list vv;
	va_start(vv,fmt0);
	rv = kprintf_internal(s,fmt0,vv);
	va_end(vv);
	return rv;
}
	
	
//dest=NULL for print to console, non-null for print to string
static int kprintf_internal( char* dest, char* fmt0 , va_list ap )
{


	register char *fmt;	/* format string */
	register int ch;	/* character from fmt */
	register int n, m;	/* handy integers (short term usage) */
	register char *cp;	/* handy char pointer (short term usage) */
	register int flags;	/* flags as above */
	//char *fmt_anchor;       /* current format spec being processed */
	int N;                  /* arg number */
	int arg_index;          /* index into args processed directly */
	int ret;		/* return value accumulator */
	int width;		/* width from format (%8d), or 0 */
	int prec;		/* precision from format (%.3d), or -1 */
	char sign;		/* sign prefix (' ', '+', '-', or \0) */
	u_quad_t _uquad;	/* integer arguments %[diouxX] */
	enum { OCT, DEC, HEX } base;/* base for [diouxX] conversion */
	int dprec;		/* a copy of prec if [diouxX], 0 otherwise */
	int realsz;		/* field size expanded by dprec */
	int size=0;		/* size of converted field or string */
	char *xdigs = 0;	/* digits for [xX] conversion */
	char buf[BUF];		/* space for %c, %[diouxX], %[eEfgG] */
	char ox[2];		/* space for 0x hex-prefix */

	
	/*
	 * Choose PADSIZE to trade efficiency vs. size.  If larger printf
	 * fields occur frequently, increase PADSIZE and make the initialisers
	 * below longer.
	 */
	#define	PADSIZE	16		/* pad chunk size */
	static const char blanks[PADSIZE] =
	 {' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '};
	static const char zeroes[PADSIZE] =
	 {'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'};


	/*
	 * BEWARE, these `goto error' on error, and PAD uses `n'.
	 */
	#define	PRINT(ptr, len) { 				\
		int i;						\
		for(i=0;i<len;++i){				\
			if( dest == 0 )				\
				console_putc((ptr)[i]);		\
			else{					\
				*dest = (ptr)[i];		\
				++dest;				\
			}					\
		}						\
	}

	
	#define	PAD(howmany, with) { \
		if ((n = (howmany)) > 0) { \
			while (n > PADSIZE) { \
				PRINT (with, PADSIZE); \
				n -= PADSIZE; \
			} \
			PRINT (with, n); \
		} \
	}
	

	/* Macros to support positional arguments */

	#define GET_ARG(n, ap, type) va_arg (ap, type)

    
	/*
	 * To extend shorts properly, we need both signed and unsigned
	 * argument extraction methods.
	 */

	#define	SARG() \
		(flags&LONGINT ? GET_ARG(N, ap, long) : \
		    flags&SHORTINT ? (long)(short)GET_ARG(N, ap, int) : \
		    (long)GET_ARG(N, ap, int))
	#define	UARG() \
		(flags&LONGINT ? GET_ARG(N, ap, u_long) : \
		    flags&SHORTINT ? (u_long)(u_short)GET_ARG(N, ap, int) : \
		    (u_long)GET_ARG(N, ap, u_int))



	fmt = (char *)fmt0;
	ret = 0;
	arg_index = 0;


	/*
	 * Scan the format for conversions (`%' character).
	 */
	for (;;) {
	        cp = fmt;
	        
                while (*fmt != '\0' && *fmt != '%')
                    fmt += 1;

		if ((m = fmt - cp) != 0) {
			PRINT (cp, m);
			ret += m;
		}

                if (*fmt == '\0')
                    goto done;

		//fmt_anchor = fmt;
		fmt++;		/* skip over '%' */

		flags = 0;
		dprec = 0;
		width = 0;
		prec = -1;
		sign = '\0';
		N = arg_index;

rflag:		ch = *fmt++;
reswitch:	switch (ch) {
		case ' ':
			/*
			 * ``If the space and + flags both appear, the space
			 * flag will be ignored.''
			 *	-- ANSI X3J11
			 */
			if (!sign)
				sign = ' ';
			goto rflag;
		case '#':
			flags |= ALT;
			goto rflag;
		case '*':
			n = N;

			/*
			 * ``A negative field width argument is taken as a
			 * - flag followed by a positive field width.''
			 *	-- ANSI X3J11
			 * They don't exclude field widths read from args.
			 */
			width = va_arg( ap, int);	//GET_ARG(n, ap, int);

			if (width >= 0)
				goto rflag;
			width = -width;
			/* FALLTHROUGH */
		case '-':
			flags |= LADJUST;
			goto rflag;
		case '+':
			sign = '+';
			goto rflag;
		case '.':
			if ((ch = *fmt++) == '*') {
				n = N;

				prec = GET_ARG(n, ap, int);
				if (prec < 0)
					prec = -1;
				goto rflag;
			}
			n = 0;
			while (is_digit (ch)) {
				n = 10 * n + to_digit (ch);
				ch = *fmt++;
			}
			prec = n < 0 ? -1 : n;
			goto reswitch;
		case '0':
			/*
			 * ``Note that 0 is taken as a flag, not as the
			 * beginning of a field width.''
			 *	-- ANSI X3J11
			 */
			flags |= ZEROPAD;
			goto rflag;
		case '1': case '2': case '3': case '4':
		case '5': case '6': case '7': case '8': case '9':
			n = 0;
			do {
				n = 10 * n + to_digit (ch);
				ch = *fmt++;
			} while (is_digit (ch));

			width = n;
			goto reswitch;
		case 'h':
			flags |= SHORTINT;
			goto rflag;
		case 'l':
			if (*fmt == 'l') {
				fmt++;
				flags |= QUADINT;
			} else {
				flags |= LONGINT;
			}
			goto rflag;
		case 'q':
			flags |= QUADINT;
			goto rflag;
		case 'c':
			cp = buf;
			if (ch == 'C' || (flags & LONGINT)) {

			}
			else {
				*cp = GET_ARG(N, ap, int);
				size = 1;
			}
			sign = '\0';
			break;
		case 'D':
			flags |= LONGINT;
			/*FALLTHROUGH*/
		case 'd':
		case 'i':
			_uquad = SARG ();
			if ((long) _uquad < 0)

			{

				_uquad = -_uquad;
				sign = '-';
			}
			base = DEC;
			goto number;
		case 'n':
			if (flags & LONGINT)
				*GET_ARG(N, ap, long_ptr_t) = ret;
			else if (flags & SHORTINT)
				*GET_ARG(N, ap, short_ptr_t) = ret;
			else
				*GET_ARG(N, ap, int_ptr_t) = ret;
			continue;	/* no output */
		case 'O':
			flags |= LONGINT;
			/*FALLTHROUGH*/
		case 'o':
			_uquad = UARG ();
			base = OCT;
			goto nosign;
		case 'p':
			/*
			 * ``The argument shall be a pointer to void.  The
			 * value of the pointer is converted to a sequence
			 * of printable characters, in an implementation-
			 * defined manner.''
			 *	-- ANSI X3J11
			 */
			/* NOSTRICT */
			_uquad = (u_long)(unsigned *)GET_ARG(N, ap, void_ptr_t);
			base = HEX;
			xdigs = "0123456789abcdef";
			flags |= HEXPREFIX;
			ch = 'x';
			goto nosign;
		case 's':
			sign = '\0';
			if ((cp = GET_ARG(N, ap, char_ptr_t)) == 0) {
				cp = "(0)";
				size = 6;
			}
			else if (prec >= 0) {
				/*
				 * can't use strlen; can only look for the
				 * NUL in the first `prec' characters, and
				 * strlen () will go further.
				 */
				char *p = my_memchr (cp, 0, prec);

				if (p != 0) {
					size = p - cp;
					if (size > prec)
						size = prec;
				} else
					size = prec;
			} else
				size = my_strlen (cp);

			break;
		case 'U':
			flags |= LONGINT;
			/*FALLTHROUGH*/
		case 'u':
			_uquad = UARG ();
			base = DEC;
			goto nosign;
		case 'X':
			xdigs = "0123456789ABCDEF";
			goto hex;
		case 'x':
			xdigs = "0123456789abcdef";
hex:			_uquad = UARG ();
			base = HEX;
			/* leading 0x/X only if non-zero */
			if (flags & ALT && _uquad != 0)
				flags |= HEXPREFIX;

			/* unsigned conversions */
nosign:			sign = '\0';
			/*
			 * ``... diouXx conversions ... if a precision is
			 * specified, the 0 flag will be ignored.''
			 *	-- ANSI X3J11
			 */
number:			if ((dprec = prec) >= 0)
				flags &= ~ZEROPAD;

			/*
			 * ``The result of converting a zero value with an
			 * explicit precision of zero is no characters.''
			 *	-- ANSI X3J11
			 */
			cp = buf + BUF;
			if (_uquad != 0 || prec != 0) {
				/*
				 * Unsigned mod is hard, and unsigned mod
				 * by a constant is easier than that by
				 * a variable; hence this switch.
				 */
				switch (base) {
				case OCT:
					do {
						*--cp = to_char (_uquad & 7);
						_uquad >>= 3;
					} while (_uquad);
					/* handle octal leading 0 */
					if (flags & ALT && *cp != '0')
						*--cp = '0';
					break;

				case DEC:
					/* many numbers are 1 digit */
					while (_uquad >= 10) {
						*--cp = to_char (_uquad % 10);
						_uquad /= 10;
					}
					*--cp = to_char (_uquad);
					break;

				case HEX:
					do {
						*--cp = xdigs[_uquad & 15];
						_uquad >>= 4;
					} while (_uquad);
					break;

				default:
					cp = "bug in vfprintf: bad base";
					size = my_strlen (cp);
					goto skipsize;
				}
			}
                       /*
			* ...result is to be converted to an 'alternate form'.
			* For o conversion, it increases the precision to force
			* the first digit of the result to be a zero."
			*     -- ANSI X3J11
			*
			* To demonstrate this case, compile and run:
                        *    printf ("%#.0o",0);
			*/
                       else if (base == OCT && (flags & ALT))
                         *--cp = '0';

			size = buf + BUF - cp;
		skipsize:
			break;
		default:	/* "%?" prints ?, unless ? is NUL */
			if (ch == '\0')
				goto done;
			/* pretend it was %c with argument ch */
			cp = buf;
			*cp = ch;
			size = 1;
			sign = '\0';
			break;
		}

		/*
		 * All reasonable formats wind up here.  At this point, `cp'
		 * points to a string which (if not flags&LADJUST) should be
		 * padded out to `width' places.  If flags&ZEROPAD, it should
		 * first be prefixed by any sign or other prefix; otherwise,
		 * it should be blank padded before the prefix is emitted.
		 * After any left-hand padding and prefixing, emit zeroes
		 * required by a decimal [diouxX] precision, then print the
		 * string proper, then emit zeroes required by any leftover
		 * floating precision; finally, if LADJUST, pad with blanks.
		 *
		 * Compute actual size, so we know how much to pad.
		 * size excludes decimal prec; realsz includes it.
		 */
		realsz = dprec > size ? dprec : size;
		if (sign)
			realsz++;
		else if (flags & HEXPREFIX)
			realsz+= 2;

		/* right-adjusting blank padding */
		if ((flags & (LADJUST|ZEROPAD)) == 0)
			PAD (width - realsz, blanks);

		/* prefix */
		if (sign) {
			PRINT (&sign, 1);
		} else if (flags & HEXPREFIX) {
			ox[0] = '0';
			ox[1] = ch;
			PRINT (ox, 2);
		}

		/* right-adjusting zero padding */
		if ((flags & (LADJUST|ZEROPAD)) == ZEROPAD)
			PAD (width - realsz, zeroes);

		/* leading zeroes from decimal precision */
		PAD (dprec - size, zeroes);

		/* the string or number proper */

		PRINT (cp, size);

		/* left-adjusting padding (always blank) */
		if (flags & LADJUST)
			PAD (width - realsz, blanks);

		/* finally, adjust ret */
		ret += width > realsz ? width : realsz;

	}
done:
	
	if( dest ){
		*dest = '\0';
	}
	
	va_end(ap);
	
	return ret;
}
