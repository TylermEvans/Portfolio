#pragma once

#define _USE_MATH_DEFINES
#include <cmath>
#include <random>

// some of these functions (individually noted) are based on code from TDL
// The TDL copyright is as follows:
// 
//  Copyright 2009, Google Inc.
//  All rights reserved.
// 
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
// 
//      *  Redistributions of source code must retain the above copyright
//  notice, this list of conditions and the following disclaimer.
//      *  Redistributions in binary form must reproduce the above
//  copyright notice, this list of conditions and the following disclaimer
//  in the documentation and/or other materials provided with the
//  distribution.
//      *  Neither the name of Google Inc. nor the names of its
//  contributors may be used to endorse or promote products derived from
//  this software without specific prior written permission.
// 
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
//  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
//  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
//  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
//  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
//  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
//  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
//  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
//  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
//  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
//  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//


class mat4{
    public:
    float _m[4][4];
    
    mat4(){
        memset(_m,0,sizeof(_m));
    }
    
    mat4(
        float v00, float v01, float v02, float v03,
        float v10, float v11, float v12, float v13,
        float v20, float v21, float v22, float v23,
        float v30, float v31, float v32, float v33){
            
        _m[0][0]=v00;
        _m[0][1]=v01;
        _m[0][2]=v02;
        _m[0][3]=v03;
        
        _m[1][0]=v10;
        _m[1][1]=v11;
        _m[1][2]=v12;
        _m[1][3]=v13;

        _m[2][0]=v20;
        _m[2][1]=v21;
        _m[2][2]=v22;
        _m[2][3]=v23;

        _m[3][0]=v30;
        _m[3][1]=v31;
        _m[3][2]=v32;
        _m[3][3]=v33;
    }
     

    static mat4 identity(){
        static mat4 I(1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1);
        return I;
    }
 
    class MProxy{
        public:
        mat4* m;
        int row;
        MProxy(mat4* mm, int i) : m(mm), row(i) { }
        float& operator[](int i){ return m->_m[row][i]; }
        float operator[](int i) const { return m->_m[row][i]; }
    };
 
 
    MProxy operator[](int i){
        return MProxy(this,i);
    }

    class MProxyC{
        public:
        const mat4* m;
        int row;
        MProxyC(const mat4* mm, int i) : m(mm), row(i) { }
        float operator[](int i) const { return m->_m[row][i]; }
    };


    MProxyC operator[](int i) const{
        return MProxyC(this,i);
    }
    
   
};



class mat3{
    public:
    float _m[3][3];
    
    mat3(){
        memset(_m,0,sizeof(_m));
    }
    
    mat3(
        float v00, float v01, float v02, 
        float v10, float v11, float v12,
        float v20, float v21, float v22 ){
            
        _m[0][0]=v00;
        _m[0][1]=v01;
        _m[0][2]=v02;
        
        _m[1][0]=v10;
        _m[1][1]=v11;
        _m[1][2]=v12;

        _m[2][0]=v20;
        _m[2][1]=v21;
        _m[2][2]=v22;
    }
     

    static mat3 identity(){
        static mat3 I(1,0,0,0,1,0,0,0,1);
        return I;
    }
 
    class MProxy{
        public:
        mat3* m;
        int row;
        MProxy(mat3* mm, int i) : m(mm), row(i) { }
        float& operator[](int i){ return m->_m[row][i]; }
        float operator[](int i) const { return m->_m[row][i]; }
    };
 
 
    MProxy operator[](int i){
        return MProxy(this,i);
    }

    class MProxyC{
        public:
        const mat3* m;
        int row;
        MProxyC(const mat3* mm, int i) : m(mm), row(i) { }
        float operator[](int i) const { return m->_m[row][i]; }
    };


    MProxyC operator[](int i) const{
        return MProxyC(this,i);
    }
    
   
};



class mat2{
    public:
    float _m[2][2];
    
    mat2(){
        memset(_m,0,sizeof(_m));
    }
    
    mat2(
        float v00, float v01, 
        float v10, float v11 ){
            
        _m[0][0]=v00;
        _m[0][1]=v01;
        
        _m[1][0]=v10;
        _m[1][1]=v11;

    }
     

    static mat2 identity(){
        static mat2 I(1,0,0,1);
        return I;
    }
 
    class MProxy{
        public:
        mat2* m;
        int row;
        MProxy(mat2* mm, int i) : m(mm), row(i) { }
        float& operator[](int i){ return m->_m[row][i]; }
        float operator[](int i) const { return m->_m[row][i]; }
    };
 
 
    MProxy operator[](int i){
        return MProxy(this,i);
    }

    class MProxyC{
        public:
        const mat2* m;
        int row;
        MProxyC(const mat2* mm, int i) : m(mm), row(i) { }
        float operator[](int i) const { return m->_m[row][i]; }
    };


    MProxyC operator[](int i) const{
        return MProxyC(this,i);
    }
    
   
};



template<typename T>
class vec2T{
    public:
    T x,y;
    
    vec2T(){ 
        x=y=0;
    }
    vec2T(T x, T y){
        this->x=x;
        this->y=y;
    }
    
    void operator+=(const vec2T<T>& v){
        x += v.x;
        y += v.y;
    }
    void operator-=(const vec2T<T>& v){
        x -= v.x;
        y -= v.y;
    }
    void operator*=(float f){
        x *= f;
        y *= f;
    }
    void operator/=(float f){
        x /= f;
        y /= f;
    }
    T& operator[](int i){
        if( i==0 ) return x;
        else if( i==1 ) return y;
        throw runtime_error("?");
    }
    T operator[](int i) const{
        if( i==0 ) return x;
        else if( i==1 ) return y;
        throw runtime_error("?");
    }
    vec2T<T> operator-() const {
        return vec2T<T>(-x,-y);
    }
    
};
typedef vec2T<int> ivec2;
typedef vec2T<float> vec2;

template<typename T>
class vec3T{
    public:
    T x,y,z;
    
    vec3T(){ 
        x=y=z=0;
    }
    vec3T(T x, T y, T z){
        this->x=x;
        this->y=y;
        this->z=z;
    }
    
    
    void operator+=(const vec3T<T>& v){
        x += v.x;
        y += v.y;
        z += v.z;
    }
    void operator-=(const vec3T<T>& v){
        x -= v.x;
        y -= v.y;
        z -= v.z;
    }
    void operator*=(float f){
        x *= f;
        y *= f;
        z *= f;
    }
    void operator/=(float f){
        x /= f;
        y /= f;
        z /= f;
    }
    T& operator[](int i){
        if( i==0 ) return x;
        else if( i==1 ) return y;
        else if( i==2 ) return z;
        throw runtime_error("?");
    }
    T operator[](int i) const{
        if( i==0 ) return x;
        else if( i==1 ) return y;
        else if( i==2 ) return z;
        throw runtime_error("?");
    }
    vec3T<T> operator-() const {
        return vec3T<T>(-x,-y,-z);
    }
    vec2T<T> xy() const {
        return vec2T<T>(x,y);
    }
    
};

typedef vec3T<int> ivec3;
typedef vec3T<float> vec3;

template<typename T>
class vec4T{
    public:
    T x,y,z,w;
    
    vec4T(){ 
        x=y=z=w=0;
    }
    vec4T(T x, T y, T z, T w){
        this->x=x;
        this->y=y;
        this->z=z;
        this->w=w;
    }
    
    vec4T(const vec3T<T>& v, T w){
        x=v.x;
        y=v.y;
        z=v.z;
        this->w=w;
    }
    
    T& operator[](int i){
        if( i==0 ) return x;
        else if( i==1 ) return y;
        else if( i==2 ) return z;
        else if( i==3 ) return w;
        throw runtime_error("?");
    }
    T operator[](int i) const{
        if( i==0 ) return x;
        else if( i==1 ) return y;
        else if( i==2 ) return z;
        else if( i==3 ) return w;
        throw runtime_error("?");
    }
    
    vec4T<T> operator-() const {
        return vec4T<T>(-x,-y,-z,-w);
    }
    
    void operator+=(const vec4T<T>& v){
        x += v.x;
        y += v.y;
        z += v.z;
        w += v.w;
    }
    void operator-=(const vec4T<T>& v){
        x -= v.x;
        y -= v.y;
        z -= v.z;
        w -= v.w;
    }
    void operator*=(float f){
        x *= f;
        y *= f;
        z *= f;
        w *= f;
    }
    void operator/=(float f){
        x /= f;
        y /= f;
        z /= f;
        w /= f;
    }


    vec3T<T> xyz() const{
        return vec3T<T>(x,y,z);
    }
    
    vec2T<T> xy() const {
        return vec2T<T>(x,y);
    }
};

typedef vec4T<int> ivec4;
typedef vec4T<float> vec4;

class vec5{
    public:
    float x,y,z,w,v;
    
    vec5(){ 
        x=y=z=w=v=0;
    }
    vec5(float x, float y, float z, float w, float v){
        this->x=x;
        this->y=y;
        this->z=z;
        this->w=w;
        this->v=v;
    }
    
    float& operator[](int i){
        if( i==0 ) return x;
        else if( i==1 ) return y;
        else if( i==2 ) return z;
        else if( i==3 ) return w;
        else if( i==4 ) return v;
        throw runtime_error("?");
    }
    float operator[](int i) const{
        if( i==0 ) return x;
        else if( i==1 ) return y;
        else if( i==2 ) return z;
        else if( i==3 ) return w;
        else if( i==4 ) return v;
        throw runtime_error("?");
    }
    
    vec5 operator-() const {
        return vec5(-x,-y,-z,-w,-v);
    }

    vec4 xyzw() const {
        return vec4(x,y,z,w);
    }
    
    vec3 xyz() const{
        return vec3(x,y,z);
    }
    
    vec2 xy() const {
        return vec2(x,y);
    }
};

inline
ostream& operator<<(ostream& o, const mat4& m){
    for(int i=0;i<4;++i){
        o << "[ ";
        for(int j=0;j<4;++j){
            o << m[i][j] << " ";
        }
        o << "]\n";
    }
    return o;
}

template<typename T>
ostream& operator<<(ostream& o, const vec4T<T>& v){
    o << "[" << v.x << " " << v.y << " " << v.z << " " << v.w << "]";
    return o;
}

template<typename T>
ostream& operator<<(ostream& o, const vec3T<T>& v){
    o << "[" << v.x << " " << v.y << " " << v.z << "]";
    return o;
}

template<typename T>
ostream& operator<<(ostream& o, const vec2T<T>& v){
    o << "[" << v.x << " " << v.y <<  "]";
    return o;
}

class bvec2{
    public:
    bool x,y;
    bvec2(){ x=y=false;}
    bvec2(bool xx, bool yy): x(xx), y(yy) {}
};

class bvec3{
    public:
    bool x,y,z;
    bvec3(){ x=y=z=false;}
    bvec3(bool xx, bool yy,bool zz): x(xx), y(yy), z(zz) {}
};

class bvec4{
    public:
    bool x,y,z,w;
    bvec4(){ x=y=z=w=false;}
    bvec4(bool xx, bool yy, bool zz, bool ww): x(xx), y(yy), z(zz), w(ww) {}
};

inline
bool any(const bvec2& b){
    return b.x || b.y ;
}
inline
bool any(const bvec3& b){
    return b.x || b.y || b.z ;
}

inline
bool any(const bvec4& b){
    return b.x || b.y || b.z || b.w ;
}

inline
bool all(const bvec2& b){
    return b.x && b.y ;
}

inline
bool all(const bvec3& b){
    return b.x && b.y && b.z ;
}

inline
bool all(const bvec4& b){
    return b.x && b.y && b.z && b.w ;
}

inline bvec2
operator<(const vec2& a, const vec2& b){
    return bvec2(a.x<b.x, a.y<b.y);
}

inline bvec3
operator<(const vec3& a, const vec3& b){
    return bvec3(a.x<b.x, a.y<b.y, a.z<b.z);
}

inline bvec4
operator<(const vec4& a, const vec4& b){
    return bvec4(a.x<b.x, a.y<b.y, a.z<b.z, a.w<b.w);
}

inline bvec2
operator>(const vec2& a, const vec2& b){
    return bvec2(a.x>b.x, a.y>b.y);
}

inline bvec3
operator>(const vec3& a, const vec3& b){
    return bvec3(a.x>b.x, a.y>b.y, a.z>b.z);
}

inline bvec4
operator>(const vec4& a, const vec4& b){
    return bvec4(a.x>b.x, a.y>b.y, a.z>b.z, a.w>b.w);
}

inline
float clamp(float v, float n, float x){
    if( v<n ) return n;
    if( v>x ) return x;
    return v;
}

inline
vec2 clamp(const vec2& v, const vec2& n, const vec2& x){
    return vec2( 
        clamp(v.x,n.x,x.x), 
        clamp(v.y,n.y,x.y) 
    );
}

inline
vec3 clamp(const vec3& v, const vec3& n, const vec3& x){
    return vec3(    clamp(v.x,n.x,x.x),
                    clamp(v.y,n.y,x.y),
                    clamp(v.z,n.z,x.z)
         );
}


inline
vec4 clamp(const vec4& v, const vec4& n, const vec4& x){
    return vec4(    clamp(v.x,n.x,x.x),
                    clamp(v.y,n.y,x.y),
                    clamp(v.z,n.z,x.z),
                    clamp(v.w,n.w,x.w)
         );
}

template<typename T>
float mix(const T& a, const T& b, float t){
    return a + t * (b-a);
}


inline vec2
operator+(const vec2& v, const vec2& w){
    return vec2(v.x+w.x, v.y+w.y);
}

inline vec2
operator-(const vec2& v, const vec2& w){
    return vec2(v.x-w.x, v.y-w.y);
}

inline vec2
operator*(const float f, const vec2& w){
    return vec2(f*w.x, f*w.y);
}

inline vec2
operator*( const vec2& w, const float f){
    return vec2(f*w.x, f*w.y);
}


inline bool operator==(const vec2& a, const vec2& b){
    return a.x==b.x && a.y==b.y;
}
inline bool operator!=(const vec2& a, const vec2& b){
    return !(a==b);
}


inline vec4
operator+(const vec4& v, const vec4& w){
    return vec4(v.x+w.x, v.y+w.y, v.z+w.z, v.w+w.w);
}

inline vec4
operator-(const vec4& v, const vec4& w){
    return vec4(v.x-w.x, v.y-w.y, v.z-w.z, v.w-w.w);
}

inline vec4
operator*(const float f, const vec4& w){
    return vec4(f*w.x, f*w.y, f*w.z, f*w.w);
}

inline vec4
operator*(const vec4& v, const mat4& m){
    vec4 R;
    for(int i=0;i<4;++i){
        float total=0;
        for(int j=0;j<4;++j){
            total += v[j]*m[j][i];
        }
        R[i]=total;
    }
    return R;
}

inline vec4
operator*( const mat4& m, const vec4& v){
    vec4 R;
    for(int i=0;i<4;++i){
        float total=0;
        for(int j=0;j<4;++j){
            total += v[j]*m[i][j];
        }
        R[i]=total;
    }
    return R;
}
 

inline vec3
operator+(const vec3& v, const vec3& w){
    return vec3(v.x+w.x, v.y+w.y, v.z+w.z);
}

inline vec3
operator-(const vec3& v, const vec3& w){
    return vec3(v.x-w.x, v.y-w.y, v.z-w.z);
}


inline vec3
operator*(const float f, const vec3& w){
    return vec3(f*w.x, f*w.y, f*w.z);
}


inline vec3
operator*(const vec3& w, const float f){
    return vec3(f*w.x, f*w.y, f*w.z);
}



inline vec2
operator*(const vec2& v, const vec2& w){
    return vec2(v.x*w.x, v.y*w.y);
}

inline vec3
operator*(const vec3& v, const vec3& w){
    return vec3(v.x*w.x, v.y*w.y, v.z*w.z);
}

inline vec3
operator*(const vec3& v, const mat3& m){
    vec3 R;
    for(int i=0;i<3;++i){
        float total=0;
        for(int j=0;j<3;++j){
            total += v[j]*m[j][i];
        }
        R[i]=total;
    }
    return R;
}

inline vec3
operator*( const mat3& m, const vec3& v){
    vec3 R;
    for(int i=0;i<3;++i){
        float total=0;
        for(int j=0;j<3;++j){
            total += v[j]*m[i][j];
        }
        R[i]=total;
    }
    return R;
}


inline vec2
operator*(const vec2& v, const mat2& m){
    vec2 R;
    for(int i=0;i<2;++i){
        float total=0;
        for(int j=0;j<2;++j){
            total += v[j]*m[j][i];
        }
        R[i]=total;
    }
    return R;
}

inline vec2
operator*( const mat2& m, const vec2& v){
    vec2 R;
    for(int i=0;i<2;++i){
        float total=0;
        for(int j=0;j<2;++j){
            total += v[j]*m[i][j];
        }
        R[i]=total;
    }
    return R;
}


inline bool operator==(const vec3& a, const vec3& b){
    return a.x==b.x && a.y==b.y && a.z==b.z;
}

inline bool operator!=(const vec3& a, const vec3& b){
    return !(a==b);
}



inline bool operator==(const vec4& a, const vec4& b){
    return a.x==b.x && a.y==b.y && a.z==b.z && a.w==b.w;
}

inline bool operator!=(const vec4& a, const vec4& b){
    return !(a==b);
}


inline
float dot(const vec2& v, const vec2& w){
    return v.x*w.x + v.y*w.y;
}

inline
float dot(const vec3& v, const vec3& w){
    return v.x*w.x + v.y*w.y + v.z*w.z;
}

inline
float dot(const vec4& v, const vec4& w){
    return v.x*w.x + v.y*w.y + v.z*w.z + v.w*w.w;
}

inline
vec3 cross(const vec3& v, const vec3& w){    
    return vec3(
            v.y*w.z - w.y*v.z,
            w.x*v.z - v.x*w.z,
            v.x*w.y - w.x*v.y
        );
}

inline float radians(float d){
    return (float)((d / 180.0) * 3.14159265358979323);
}
inline float degrees(float d){
    return (float)((d / 3.14159265358979323) * 180.0);
}

template<typename T>
float length(const T& v){
    return sqrt(dot(v,v));
}

template<typename T>
T normalize(const T& v){
    float le=length(v);
    return 1.0/le * v;
}


inline
mat4 operator*(const mat4& self, const mat4& o){
    mat4 R;
    for(int i=0;i<4;++i){
        for(int j=0;j<4;++j){
            float total=0;
            for(int k=0;k<4;++k){
                total += self[i][k] * o[k][j];
            }
            R[i][j]=total;
        }
    }
    return R;
}

inline 
bool operator==(const mat4& a, const mat4& b){
    for(int i=0;i<4;++i){
        for(int j=0;j<4;++j){
            if( a[i][j] != b[i][j] )
                return false;
        }
    }
    return true;
}

inline 
bool operator!=(const mat4& a, const mat4& b){
    return !(a==b);
}

inline
mat4 transpose(const mat4& m){
    mat4 R;
    R[ 0 ][ 0 ]=m[ 0 ][ 0 ];
    R[ 0 ][ 1 ]=m[ 1 ][ 0 ];
    R[ 0 ][ 2 ]=m[ 2 ][ 0 ];
    R[ 0 ][ 3 ]=m[ 3 ][ 0 ];
    R[ 1 ][ 0 ]=m[ 0 ][ 1 ];
    R[ 1 ][ 1 ]=m[ 1 ][ 1 ];
    R[ 1 ][ 2 ]=m[ 2 ][ 1 ];
    R[ 1 ][ 3 ]=m[ 3 ][ 1 ];
    R[ 2 ][ 0 ]=m[ 0 ][ 2 ];
    R[ 2 ][ 1 ]=m[ 1 ][ 2 ];
    R[ 2 ][ 2 ]=m[ 2 ][ 2 ];
    R[ 2 ][ 3 ]=m[ 3 ][ 2 ];
    R[ 3 ][ 0 ]=m[ 0 ][ 3 ];
    R[ 3 ][ 1 ]=m[ 1 ][ 3 ];
    R[ 3 ][ 2 ]=m[ 2 ][ 3 ];
    R[ 3 ][ 3 ]=m[ 3 ][ 3 ];
    return R;
}
    
//from TDL
inline
float det(const mat2& m){
    return m[0][0]*m[1][1] - m[0][1]*m[1][0];
}

//from TDL
inline
float det(const mat3& m){
    return m[2][2] * (m[0][0] * m[1][1] - m[0][1] * m[1][0]) - m[2][1] * (m[0][0] * m[1][2] - m[0][2] * m[1][0]) +                m[2][0] * (m[0][1] * m[1][2] - m[0][2] * m[1][1]);
}


//from TDL
inline 
float det(const mat4& m){
    float t01 = m[0][0] * m[1][1] - m[0][1] * m[1][0];
    float t02 = m[0][0] * m[1][2] - m[0][2] * m[1][0];
    float t03 = m[0][0] * m[1][3] - m[0][3] * m[1][0];
    float t12 = m[0][1] * m[1][2] - m[0][2] * m[1][1];
    float t13 = m[0][1] * m[1][3] - m[0][3] * m[1][1];
    float t23 = m[0][2] * m[1][3] - m[0][3] * m[1][2];
    return (m[3][3] * (m[2][2] * t01 - m[2][1] * t02 + m[2][0] * t12) -
         m[3][2] * (m[2][3] * t01 - m[2][1] * t03 + m[2][0] * t13) +
         m[3][1] * (m[2][3] * t02 - m[2][2] * t03 + m[2][0] * t23) -
         m[3][0] * (m[2][3] * t12 - m[2][2] * t13 + m[2][1] * t23) );
}

//from TDL
inline
mat2 inverse(const mat2& m){
    float d = 1.0f / (m[0][0] * m[1][1] - m[0][1] * m[1][0]);
    return mat2(d * m[1][1], -d * m[0][1], -d * m[1][0], d * m[0][0]);
}

//from TDL
inline
mat3 inverse(const mat3& m){
    float t00 = m[1][1] * m[2][2] - m[1][2] * m[2][1];
    float t10 = m[0][1] * m[2][2] - m[0][2] * m[2][1];
    float t20 = m[0][1] * m[1][2] - m[0][2] * m[1][1];
    float d = 1.0f / (m[0][0] * t00 - m[1][0] * t10 + m[2][0] * t20);
    return mat3( d * t00, -d * t10, d * t20,
              -d * (m[1][0] * m[2][2] - m[1][2] * m[2][0]),
               d * (m[0][0] * m[2][2] - m[0][2] * m[2][0]),
              -d * (m[0][0] * m[1][2] - m[0][2] * m[1][0]),
               d * (m[1][0] * m[2][1] - m[1][1] * m[2][0]),
              -d * (m[0][0] * m[2][1] - m[0][1] * m[2][0]),
               d * (m[0][0] * m[1][1] - m[0][1] * m[1][0]) );
}

//from TDL
inline
mat4 inverse(const mat4& m){
    float tmp_0 = m[2][2] * m[3][3],
        tmp_1 = m[3][2] * m[2][3],
        tmp_2 = m[1][2] * m[3][3],
        tmp_3 = m[3][2] * m[1][3],
        tmp_4 = m[1][2] * m[2][3],
        tmp_5 = m[2][2] * m[1][3],
        tmp_6 = m[0][2] * m[3][3],
        tmp_7 = m[3][2] * m[0][3],
        tmp_8 = m[0][2] * m[2][3],
        tmp_9 = m[2][2] * m[0][3],
        tmp_10 = m[0][2] * m[1][3],
        tmp_11 = m[1][2] * m[0][3],
        tmp_12 = m[2][0] * m[3][1],
        tmp_13 = m[3][0] * m[2][1],
        tmp_14 = m[1][0] * m[3][1],
        tmp_15 = m[3][0] * m[1][1],
        tmp_16 = m[1][0] * m[2][1],
        tmp_17 = m[2][0] * m[1][1],
        tmp_18 = m[0][0] * m[3][1],
        tmp_19 = m[3][0] * m[0][1],
        tmp_20 = m[0][0] * m[2][1],
        tmp_21 = m[2][0] * m[0][1],
        tmp_22 = m[0][0] * m[1][1],
        tmp_23 = m[1][0] * m[0][1];

    float t0 = (tmp_0 * m[1][1] + tmp_3 * m[2][1] + tmp_4 * m[3][1]) -        (tmp_1 * m[1][1] + tmp_2 * m[2][1] + tmp_5 * m[3][1]);
    float t1 = (tmp_1 * m[0][1] + tmp_6 * m[2][1] + tmp_9 * m[3][1]) -        (tmp_0 * m[0][1] + tmp_7 * m[2][1] + tmp_8 * m[3][1]);
    float t2 = (tmp_2 * m[0][1] + tmp_7 * m[1][1] + tmp_10 * m[3][1]) -        (tmp_3 * m[0][1] + tmp_6 * m[1][1] + tmp_11 * m[3][1]);
    float t3 = (tmp_5 * m[0][1] + tmp_8 * m[1][1] + tmp_11 * m[2][1]) -        (tmp_4 * m[0][1] + tmp_9 * m[1][1] + tmp_10 * m[2][1]);
    float d = 1.0f / (m[0][0] * t0 + m[1][0] * t1 + m[2][0] * t2 + m[3][0] * t3);

    return mat4(d * t0, d * t1, d * t2, d * t3,
       d * ((tmp_1 * m[1][0] + tmp_2 * m[2][0] + tmp_5 * m[3][0]) -
          (tmp_0 * m[1][0] + tmp_3 * m[2][0] + tmp_4 * m[3][0])),
       d * ((tmp_0 * m[0][0] + tmp_7 * m[2][0] + tmp_8 * m[3][0]) -
          (tmp_1 * m[0][0] + tmp_6 * m[2][0] + tmp_9 * m[3][0])),
       d * ((tmp_3 * m[0][0] + tmp_6 * m[1][0] + tmp_11 * m[3][0]) -
          (tmp_2 * m[0][0] + tmp_7 * m[1][0] + tmp_10 * m[3][0])),
       d * ((tmp_4 * m[0][0] + tmp_9 * m[1][0] + tmp_10 * m[2][0]) -
          (tmp_5 * m[0][0] + tmp_8 * m[1][0] + tmp_11 * m[2][0])),
       d * ((tmp_12 * m[1][3] + tmp_15 * m[2][3] + tmp_16 * m[3][3]) -
          (tmp_13 * m[1][3] + tmp_14 * m[2][3] + tmp_17 * m[3][3])),
       d * ((tmp_13 * m[0][3] + tmp_18 * m[2][3] + tmp_21 * m[3][3]) -
          (tmp_12 * m[0][3] + tmp_19 * m[2][3] + tmp_20 * m[3][3])),
       d * ((tmp_14 * m[0][3] + tmp_19 * m[1][3] + tmp_22 * m[3][3]) -
          (tmp_15 * m[0][3] + tmp_18 * m[1][3] + tmp_23 * m[3][3])),
       d * ((tmp_17 * m[0][3] + tmp_20 * m[1][3] + tmp_23 * m[2][3]) -
          (tmp_16 * m[0][3] + tmp_21 * m[1][3] + tmp_22 * m[2][3])),
       d * ((tmp_14 * m[2][2] + tmp_17 * m[3][2] + tmp_13 * m[1][2]) -
          (tmp_16 * m[3][2] + tmp_12 * m[1][2] + tmp_15 * m[2][2])),
       d * ((tmp_20 * m[3][2] + tmp_12 * m[0][2] + tmp_19 * m[2][2]) -
          (tmp_18 * m[2][2] + tmp_21 * m[3][2] + tmp_13 * m[0][2])),
       d * ((tmp_18 * m[1][2] + tmp_23 * m[3][2] + tmp_15 * m[0][2]) -
          (tmp_22 * m[3][2] + tmp_14 * m[0][2] + tmp_19 * m[1][2])),
       d * ((tmp_22 * m[2][2] + tmp_16 * m[0][2] + tmp_21 * m[1][2]) -
          (tmp_20 * m[1][2] + tmp_23 * m[2][2] + tmp_17 * m[0][2])));
}




//from TDL
inline
mat4 axisRotation(const vec3& axis1, float angle ){
    vec3 axis=normalize(axis1);
    float x = axis[0];
    float y = axis[1];
    float z = axis[2];
    float xx = x * x;
    float yy = y * y;
    float zz = z * z;
    float c = cos(angle);
    float s = sin(angle);
    float oneMinusCosine = 1 - c;
    return mat4(
        xx + (1 - xx) * c,
        x * y * oneMinusCosine + z * s,
        x * z * oneMinusCosine - y * s,
        0,
        x * y * oneMinusCosine - z * s,
        yy + (1 - yy) * c,
        y * z * oneMinusCosine + x * s,
        0,
        x * z * oneMinusCosine + y * s,
        y * z * oneMinusCosine - x * s,
        zz + (1 - zz) * c,
        0,
        0, 0, 0, 1
    );  
}

inline
mat4 axisRotation(const vec4& axis1, float angle ){
    return axisRotation(axis1.xyz(),angle);
}


//from TDL
mat4 scaling(const vec3& v){
    return mat4( 
        v[0], 0,0,0,
        0,v[1],0,0,
        0,0,v[2],0,
        0,0,0,1);
}

//from TDL
mat4 scaling(const vec4& v){
    return mat4( 
        v[0], 0,0,0,
        0,v[1],0,0,
        0,0,v[2],0,
        0,0,0,1);
}

//from TDL
inline
mat4 scaling(float x, float y, float z){
    return mat4( 
        x, 0,0,0,
        0,y,0,0,
        0,0,z,0,
        0,0,0,1);
}

//from TDL
inline
mat4 translation(const vec3& v){
    return mat4(
        1,0,0,0,
        0,1,0,0,
        0,0,1,0,
        v[0],v[1],v[2],1);
}

//from TDL
inline
mat4 translation(const vec4& v){
    return mat4(
        1,0,0,0,
        0,1,0,0,
        0,0,1,0,
        v[0],v[1],v[2],1);
}

//from TDL
inline
mat4 translation(float x, float y, float z){
    return mat4(
        1,0,0,0,
        0,1,0,0,
        0,0,1,0,
        x,y,z,1);
}

inline
float randrange(float mn, float mx){
    static std::default_random_engine eng;
    static std::uniform_real_distribution<float> D(0,1);
    return mn + D(eng) * (mx-mn);
}

inline
void math3d_test_harness(){
    //test harness
    vec2 v2a(2,4);
    vec2 v2b(10,11);
    
    assert( v2a+v2b == vec2(12,15));
    assert( v2a-v2b == vec2(-8,-7));
    assert( v2a+v2b != vec2(12,3));
    assert( v2a+v2b != vec2(3,15));
    assert( v2a*v2b == vec2(20,44));
    assert( 5*v2a == vec2(10,20));
    assert( v2a*5 == vec2(10,20));
    
    //assert( v2a.xy == v2a);
    //assert( v2a.xx == vec2(2,2));
    //assert( v2a.yy == vec2(4,4));
    //assert( v2a.yx == vec2(4,2));
    
    
    vec3 v3a(2,4,6);
    vec3 v3b(10,11,12);
    
    assert( v3a+v3b == vec3(12,15,18));
    assert( v3a-v3b == vec3(-8,-7,-6));
    assert( v3a+v3b != vec3(12,3,18));
    assert( v3a+v3b != vec3(3,15,18));
    assert( v3a+v3b != vec3(12,3,0));
    assert( v3a*v3b == vec3(20,44,72));
    assert( 5*v3a == vec3(10,20,30));
    assert( v3a*5 == vec3(10,20,30));
    
    //assert( v3a.xyz == v3a);
    //assert( v3a.xxx == vec3(2,2,2));
    //assert( v3a.yyy == vec3(4,4,4));
    
    mat4 m4=mat4(3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3);
    vec4 v4=vec4(2,4,6,7);
    
    /*
    2 4 6 7     3 1 4 1   2
                5 9 2 6   4
                5 3 5 8   6
                9 7 9 3   7
    */
    vec4 va = v4*m4;
    vec4 vb = m4*v4;
    assert( va == vec4( 
                    2*3+4*5+6*5+7*9,
                    2*1+4*9+6*3+7*7,
                    2*4+4*2+6*5+7*9,
                    2*1+4*6+6*8+7*3)
            );
    assert( vb == vec4( 
                3*2+1*4+4*6+1*7,
                5*2+9*4+2*6+6*7,
                5*2+3*4+5*6+8*7,
                9*2+7*4+9*6+3*7));
                
    assert( transpose(m4) != m4);
    assert( transpose(transpose(m4)) == m4);
    
    /*
    m4i = inverse(m4)
    p=m4*m4i
    p2=m4i*m4
    
    for i in range(4):
        for j in range(4):
            if i == j:
                t=1
            else:
                t=0
            assert( abs(p[i][j]-t) < 0.001);
            assert( abs(p2[i][j]-t) < 0.001);
    */
    
    mat4 M=axisRotation(vec3(0,1,0),radians(90));
    vec4 v = vec4(0,0,1,0)*M;
    assert( abs(dot(v,vec4(0,0,1,0))) < 0.01);
    assert( abs(dot(v,vec4(1,0,0,0))-1) < 0.01);
    
    vec3 v1=vec3(3,1,4);
    vec3 v2=vec3(-5,2,9);
    v1=normalize(v1);
    v2=normalize(v2);
    vec3 v3 = cross(v1,v2);
    assert( abs(dot(v1,v3)) < 0.01);
    assert( abs(dot(v2,v3)) < 0.01);
    
    //M = axisRotation( vec3(0,0,0), 0 )
    //print(M)
    
    //TODO: FIXME: Finish: Write the rest of the tests
    cout << ("All tests OK");
}

static_assert(sizeof(mat4) == 16*4,"mat4 has padding");
static_assert(sizeof(vec4) == 4*4,"vec4 has padding" );
static_assert(sizeof(vec3) == 3*4,"vec3 has padding" );
static_assert(sizeof(vec2) == 2*4,"vec2 has padding" );
static_assert(sizeof(ivec2) == 2*4,"ivec2 has padding" );
