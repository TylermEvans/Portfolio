#Data from gl.xml, which has this copyright:

#Copyright (c) 2013-2016 The Khronos Group Inc.
#
#Permission is hereby granted, free of charge, to any person obtaining a
#copy of this software and/or associated documentation files (the
#"Materials"), to deal in the Materials without restriction, including
#without limitation the rights to use, copy, modify, merge, publish,
#distribute, sublicense, and/or sell copies of the Materials, and to
#permit persons to whom the Materials are furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be included
#in all copies or substantial portions of the Materials.
#
#THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#MATERIALS OR THE USE OR OTHER DEALINGS IN THE MATERIALS.
#
#------------------------------------------------------------------------
#
#This file, gl.xml, is the OpenGL and OpenGL API Registry. The older
#".spec" file format has been retired and will no longer be updated with
#new extensions and API versions. The canonical version of the registry,
#together with documentation, schema, and Python generator scripts used
#to generate C header files for OpenGL and OpenGL ES, can always be found
#in the Khronos Registry at
#        http://www.opengl.org/registry/
#    

import sys
from ctypes import *
import array

def pyglMakeCallback(fname):
    def tmp(*args):
        raise RuntimeError("The function "+fname+" is not implemented")
    return tmp
        

#http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
def pyglGetFuncAddress(funcname):
    if sys.platform.lower().find("win32") != -1:
        if "kernel32" not in pyglGetFuncAddress.__dict__:

            pyglGetFuncAddress.kernel32 = windll.kernel32

            pyglGetFuncAddress.LoadLibraryA = pyglGetFuncAddress.kernel32.LoadLibraryA
            pyglGetFuncAddress.LoadLibraryA.argtypes=[c_char_p]
            pyglGetFuncAddress.LoadLibraryA.restype = c_void_p


            pyglGetFuncAddress.GetProcAddress = pyglGetFuncAddress.kernel32.GetProcAddress
            pyglGetFuncAddress.GetProcAddress.argtypes = [c_void_p,c_char_p]
            pyglGetFuncAddress.GetProcAddress.restype = c_void_p

            pyglGetFuncAddress.opengl32 = pyglGetFuncAddress.LoadLibraryA(b"opengl32.dll")
            tmp = pyglGetFuncAddress.GetProcAddress(pyglGetFuncAddress.opengl32,b"wglGetProcAddress")
            pyglGetFuncAddress.wglGetProcAddress = WINFUNCTYPE(c_void_p,c_char_p)(tmp)    

        x = pyglGetFuncAddress.wglGetProcAddress(funcname.encode())
        if not x or x == None or x == 0 or x == 1 or x == 2 or x == 3 or x == -1 or x == 0xffffffff or x == 0xffffffffffffffff:
            x = pyglGetFuncAddress.GetProcAddress(pyglGetFuncAddress.opengl32,funcname.encode())
    else:
        if "dlopen" not in pyglGetFuncAddress.__dict__:
            pyglGetFuncAddress.dlopen = cdll.LoadLibrary("libdl.so").dlopen
            pyglGetFuncAddress.dlopen.argtypes = [c_char_p,c_int]
            pyglGetFuncAddress.dlopen.restype = c_void_p
            #2 = RTLD_NOW
            pyglGetFuncAddress.libgl = pyglGetFuncAddress.dlopen(b"libGL.so",2)
            pyglGetFuncAddress.dlsym = cdll.LoadLibrary("libdl.so").dlsym
            pyglGetFuncAddress.dlsym.argtypes = [c_void_p,c_char_p]
            pyglGetFuncAddress.dlsym.restype = c_void_p
        x = pyglGetFuncAddress.dlsym(pyglGetFuncAddress.libgl,funcname.encode())
    #endif
    return x
            
if sys.platform.lower().find('win32') != -1:
    PYGL_FUNC_TYPE = WINFUNCTYPE
else:
    PYGL_FUNC_TYPE = CFUNCTYPE
      
      
def pyglGetAsConstVoidPointer(v):
    if v == None:
        a= c_void_p(None)
    elif isinstance(v,bytes):
        a= c_char_p(v)
    elif isinstance(v,bytearray):
        a= (c_uint8*len(v)).from_buffer(v)
    elif isinstance(v,array.array):
        a= c_void_p(v.buffer_info()[0])
    else:
        raise TypeError("Invalid type:"+str(type(v)))
    return a  
    
# <command>
#            <proto>void <name>glActiveShaderProgram</name></proto>
#            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#        </command>
#        
glActiveShaderProgram_impl=None
def glActiveShaderProgram (pipeline, program):
    global glActiveShaderProgram_impl
    if not glActiveShaderProgram_impl:
        fptr = pyglGetFuncAddress('glActiveShaderProgram')
        if not fptr:
            raise RuntimeError('The function glActiveShaderProgram is not available')
        glActiveShaderProgram_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glActiveShaderProgram = glActiveShaderProgram_impl
    return glActiveShaderProgram(pipeline, program)
# <command>
#            <proto>void <name>glActiveTexture</name></proto>
#            <param group="TextureUnit"><ptype>GLenum</ptype> <name>texture</name></param>
#            <glx opcode="197" type="render" />
#        </command>
#        
glActiveTexture_impl=None
def glActiveTexture (texture):
    global glActiveTexture_impl
    if not glActiveTexture_impl:
        fptr = pyglGetFuncAddress('glActiveTexture')
        if not fptr:
            raise RuntimeError('The function glActiveTexture is not available')
        glActiveTexture_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glActiveTexture = glActiveTexture_impl
    return glActiveTexture(texture)
# <command>
#            <proto>void <name>glAttachShader</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>shader</name></param>
#        </command>
#        
glAttachShader_impl=None
def glAttachShader (program, shader):
    global glAttachShader_impl
    if not glAttachShader_impl:
        fptr = pyglGetFuncAddress('glAttachShader')
        if not fptr:
            raise RuntimeError('The function glAttachShader is not available')
        glAttachShader_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glAttachShader = glAttachShader_impl
    return glAttachShader(program, shader)
# <command>
#            <proto>void <name>glBeginConditionalRender</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param group="TypeEnum"><ptype>GLenum</ptype> <name>mode</name></param>
#        </command>
#        
glBeginConditionalRender_impl=None
def glBeginConditionalRender (id, mode):
    global glBeginConditionalRender_impl
    if not glBeginConditionalRender_impl:
        fptr = pyglGetFuncAddress('glBeginConditionalRender')
        if not fptr:
            raise RuntimeError('The function glBeginConditionalRender is not available')
        glBeginConditionalRender_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBeginConditionalRender = glBeginConditionalRender_impl
    return glBeginConditionalRender(id, mode)
# <command>
#            <proto>void <name>glBeginQuery</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <glx opcode="231" type="render" />
#        </command>
#        
glBeginQuery_impl=None
def glBeginQuery (target, id):
    global glBeginQuery_impl
    if not glBeginQuery_impl:
        fptr = pyglGetFuncAddress('glBeginQuery')
        if not fptr:
            raise RuntimeError('The function glBeginQuery is not available')
        glBeginQuery_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBeginQuery = glBeginQuery_impl
    return glBeginQuery(target, id)
# <command>
#            <proto>void <name>glBeginQueryIndexed</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#        </command>
#        
glBeginQueryIndexed_impl=None
def glBeginQueryIndexed (target, index, id):
    global glBeginQueryIndexed_impl
    if not glBeginQueryIndexed_impl:
        fptr = pyglGetFuncAddress('glBeginQueryIndexed')
        if not fptr:
            raise RuntimeError('The function glBeginQueryIndexed is not available')
        glBeginQueryIndexed_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glBeginQueryIndexed = glBeginQueryIndexed_impl
    return glBeginQueryIndexed(target, index, id)
# <command>
#            <proto>void <name>glBeginTransformFeedback</name></proto>
#            <param><ptype>GLenum</ptype> <name>primitiveMode</name></param>
#        </command>
#        
glBeginTransformFeedback_impl=None
def glBeginTransformFeedback (primitiveMode):
    global glBeginTransformFeedback_impl
    if not glBeginTransformFeedback_impl:
        fptr = pyglGetFuncAddress('glBeginTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glBeginTransformFeedback is not available')
        glBeginTransformFeedback_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glBeginTransformFeedback = glBeginTransformFeedback_impl
    return glBeginTransformFeedback(primitiveMode)
# <command>
#            <proto>void <name>glBindAttribLocation</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glBindAttribLocation_impl=None
def glBindAttribLocation (program, index, name):
    global glBindAttribLocation_impl
    if not glBindAttribLocation_impl:
        fptr = pyglGetFuncAddress('glBindAttribLocation')
        if not fptr:
            raise RuntimeError('The function glBindAttribLocation is not available')
        glBindAttribLocation_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glBindAttribLocation = (lambda program,index,name:glBindAttribLocation_impl(program,index,c_char_p( name .encode() )))
    return glBindAttribLocation(program, index, name)
# <command>
#            <proto>void <name>glBindBuffer</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glBindBuffer_impl=None
def glBindBuffer (target, buffer):
    global glBindBuffer_impl
    if not glBindBuffer_impl:
        fptr = pyglGetFuncAddress('glBindBuffer')
        if not fptr:
            raise RuntimeError('The function glBindBuffer is not available')
        glBindBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBindBuffer = glBindBuffer_impl
    return glBindBuffer(target, buffer)
# <command>
#            <proto>void <name>glBindBufferBase</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glBindBufferBase_impl=None
def glBindBufferBase (target, index, buffer):
    global glBindBufferBase_impl
    if not glBindBufferBase_impl:
        fptr = pyglGetFuncAddress('glBindBufferBase')
        if not fptr:
            raise RuntimeError('The function glBindBufferBase is not available')
        glBindBufferBase_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glBindBufferBase = glBindBufferBase_impl
    return glBindBufferBase(target, index, buffer)
# <command>
#            <proto>void <name>glBindBufferRange</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#        </command>
#        
glBindBufferRange_impl=None
def glBindBufferRange (target, index, buffer, offset, size):
    global glBindBufferRange_impl
    if not glBindBufferRange_impl:
        fptr = pyglGetFuncAddress('glBindBufferRange')
        if not fptr:
            raise RuntimeError('The function glBindBufferRange is not available')
        glBindBufferRange_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t, c_void_p)(fptr)
    glBindBufferRange = glBindBufferRange_impl
    return glBindBufferRange(target, index, buffer, offset, size)
# <command>
#            <proto>void <name>glBindBuffersBase</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>buffers</name></param>
#        </command>
#        
glBindBuffersBase_impl=None
def glBindBuffersBase (target, first, count, buffers):
    global glBindBuffersBase_impl
    if not glBindBuffersBase_impl:
        fptr = pyglGetFuncAddress('glBindBuffersBase')
        if not fptr:
            raise RuntimeError('The function glBindBuffersBase is not available')
        glBindBuffersBase_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p)(fptr)
    glBindBuffersBase = (lambda target,first,count,buffers:glBindBuffersBase_impl(target,first,count,pyglGetAsConstVoidPointer( buffers )))
    return glBindBuffersBase(target, first, count, buffers)
# <command>
#            <proto>void <name>glBindBuffersRange</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>buffers</name></param>
#            <param len="count">const <ptype>GLintptr</ptype> *<name>offsets</name></param>
#            <param len="count">const <ptype>GLsizeiptr</ptype> *<name>sizes</name></param>
#        </command>
#        
glBindBuffersRange_impl=None
def glBindBuffersRange (target, first, count, buffers, offsets, sizes):
    global glBindBuffersRange_impl
    if not glBindBuffersRange_impl:
        fptr = pyglGetFuncAddress('glBindBuffersRange')
        if not fptr:
            raise RuntimeError('The function glBindBuffersRange is not available')
        glBindBuffersRange_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p, c_void_p, c_void_p)(fptr)
    glBindBuffersRange = (lambda target,first,count,buffers,offsets,sizes:glBindBuffersRange_impl(target,first,count,pyglGetAsConstVoidPointer( buffers ),pyglGetAsConstVoidPointer( offsets ),pyglGetAsConstVoidPointer( sizes )))
    return glBindBuffersRange(target, first, count, buffers, offsets, sizes)
# <command>
#            <proto>void <name>glBindFragDataLocation</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>color</name></param>
#            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glBindFragDataLocation_impl=None
def glBindFragDataLocation (program, color, name):
    global glBindFragDataLocation_impl
    if not glBindFragDataLocation_impl:
        fptr = pyglGetFuncAddress('glBindFragDataLocation')
        if not fptr:
            raise RuntimeError('The function glBindFragDataLocation is not available')
        glBindFragDataLocation_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glBindFragDataLocation = (lambda program,color,name:glBindFragDataLocation_impl(program,color,c_char_p( name .encode() )))
    return glBindFragDataLocation(program, color, name)
# <command>
#            <proto>void <name>glBindFragDataLocationIndexed</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>colorNumber</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glBindFragDataLocationIndexed_impl=None
def glBindFragDataLocationIndexed (program, colorNumber, index, name):
    global glBindFragDataLocationIndexed_impl
    if not glBindFragDataLocationIndexed_impl:
        fptr = pyglGetFuncAddress('glBindFragDataLocationIndexed')
        if not fptr:
            raise RuntimeError('The function glBindFragDataLocationIndexed is not available')
        glBindFragDataLocationIndexed_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glBindFragDataLocationIndexed = (lambda program,colorNumber,index,name:glBindFragDataLocationIndexed_impl(program,colorNumber,index,c_char_p( name .encode() )))
    return glBindFragDataLocationIndexed(program, colorNumber, index, name)
# <command>
#            <proto>void <name>glBindFramebuffer</name></proto>
#            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <glx opcode="236" type="render" />
#        </command>
#        
glBindFramebuffer_impl=None
def glBindFramebuffer (target, framebuffer):
    global glBindFramebuffer_impl
    if not glBindFramebuffer_impl:
        fptr = pyglGetFuncAddress('glBindFramebuffer')
        if not fptr:
            raise RuntimeError('The function glBindFramebuffer is not available')
        glBindFramebuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBindFramebuffer = glBindFramebuffer_impl
    return glBindFramebuffer(target, framebuffer)
# <command>
#            <proto>void <name>glBindImageTexture</name></proto>
#            <param><ptype>GLuint</ptype> <name>unit</name></param>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>layered</name></param>
#            <param><ptype>GLint</ptype> <name>layer</name></param>
#            <param><ptype>GLenum</ptype> <name>access</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#        </command>
#        
glBindImageTexture_impl=None
def glBindImageTexture (unit, texture, level, layered, layer, access, format):
    global glBindImageTexture_impl
    if not glBindImageTexture_impl:
        fptr = pyglGetFuncAddress('glBindImageTexture')
        if not fptr:
            raise RuntimeError('The function glBindImageTexture is not available')
        glBindImageTexture_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_char, c_int, c_uint, c_uint)(fptr)
    glBindImageTexture = glBindImageTexture_impl
    return glBindImageTexture(unit, texture, level, layered, layer, access, format)
# <command>
#            <proto>void <name>glBindImageTextures</name></proto>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>textures</name></param>
#        </command>
#        
glBindImageTextures_impl=None
def glBindImageTextures (first, count, textures):
    global glBindImageTextures_impl
    if not glBindImageTextures_impl:
        fptr = pyglGetFuncAddress('glBindImageTextures')
        if not fptr:
            raise RuntimeError('The function glBindImageTextures is not available')
        glBindImageTextures_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glBindImageTextures = (lambda first,count,textures:glBindImageTextures_impl(first,count,pyglGetAsConstVoidPointer( textures )))
    return glBindImageTextures(first, count, textures)
# <command>
#            <proto>void <name>glBindProgramPipeline</name></proto>
#            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
#        </command>
#        
glBindProgramPipeline_impl=None
def glBindProgramPipeline (pipeline):
    global glBindProgramPipeline_impl
    if not glBindProgramPipeline_impl:
        fptr = pyglGetFuncAddress('glBindProgramPipeline')
        if not fptr:
            raise RuntimeError('The function glBindProgramPipeline is not available')
        glBindProgramPipeline_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glBindProgramPipeline = glBindProgramPipeline_impl
    return glBindProgramPipeline(pipeline)
# <command>
#            <proto>void <name>glBindRenderbuffer</name></proto>
#            <param group="RenderbufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
#            <glx opcode="235" type="render" />
#        </command>
#        
glBindRenderbuffer_impl=None
def glBindRenderbuffer (target, renderbuffer):
    global glBindRenderbuffer_impl
    if not glBindRenderbuffer_impl:
        fptr = pyglGetFuncAddress('glBindRenderbuffer')
        if not fptr:
            raise RuntimeError('The function glBindRenderbuffer is not available')
        glBindRenderbuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBindRenderbuffer = glBindRenderbuffer_impl
    return glBindRenderbuffer(target, renderbuffer)
# <command>
#            <proto>void <name>glBindSampler</name></proto>
#            <param><ptype>GLuint</ptype> <name>unit</name></param>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#        </command>
#        
glBindSampler_impl=None
def glBindSampler (unit, sampler):
    global glBindSampler_impl
    if not glBindSampler_impl:
        fptr = pyglGetFuncAddress('glBindSampler')
        if not fptr:
            raise RuntimeError('The function glBindSampler is not available')
        glBindSampler_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBindSampler = glBindSampler_impl
    return glBindSampler(unit, sampler)
# <command>
#            <proto>void <name>glBindSamplers</name></proto>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>samplers</name></param>
#        </command>
#        
glBindSamplers_impl=None
def glBindSamplers (first, count, samplers):
    global glBindSamplers_impl
    if not glBindSamplers_impl:
        fptr = pyglGetFuncAddress('glBindSamplers')
        if not fptr:
            raise RuntimeError('The function glBindSamplers is not available')
        glBindSamplers_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glBindSamplers = (lambda first,count,samplers:glBindSamplers_impl(first,count,pyglGetAsConstVoidPointer( samplers )))
    return glBindSamplers(first, count, samplers)
# <command>
#            <proto>void <name>glBindTexture</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="Texture"><ptype>GLuint</ptype> <name>texture</name></param>
#            <glx opcode="4117" type="render" />
#        </command>
#        
glBindTexture_impl=None
def glBindTexture (target, texture):
    global glBindTexture_impl
    if not glBindTexture_impl:
        fptr = pyglGetFuncAddress('glBindTexture')
        if not fptr:
            raise RuntimeError('The function glBindTexture is not available')
        glBindTexture_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBindTexture = glBindTexture_impl
    return glBindTexture(target, texture)
# <command>
#            <proto>void <name>glBindTextureUnit</name></proto>
#            <param><ptype>GLuint</ptype> <name>unit</name></param>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#        </command>
#        
glBindTextureUnit_impl=None
def glBindTextureUnit (unit, texture):
    global glBindTextureUnit_impl
    if not glBindTextureUnit_impl:
        fptr = pyglGetFuncAddress('glBindTextureUnit')
        if not fptr:
            raise RuntimeError('The function glBindTextureUnit is not available')
        glBindTextureUnit_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBindTextureUnit = glBindTextureUnit_impl
    return glBindTextureUnit(unit, texture)
# <command>
#            <proto>void <name>glBindTextures</name></proto>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>textures</name></param>
#        </command>
#        
glBindTextures_impl=None
def glBindTextures (first, count, textures):
    global glBindTextures_impl
    if not glBindTextures_impl:
        fptr = pyglGetFuncAddress('glBindTextures')
        if not fptr:
            raise RuntimeError('The function glBindTextures is not available')
        glBindTextures_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glBindTextures = (lambda first,count,textures:glBindTextures_impl(first,count,pyglGetAsConstVoidPointer( textures )))
    return glBindTextures(first, count, textures)
# <command>
#            <proto>void <name>glBindTransformFeedback</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#        </command>
#        
glBindTransformFeedback_impl=None
def glBindTransformFeedback (target, id):
    global glBindTransformFeedback_impl
    if not glBindTransformFeedback_impl:
        fptr = pyglGetFuncAddress('glBindTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glBindTransformFeedback is not available')
        glBindTransformFeedback_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBindTransformFeedback = glBindTransformFeedback_impl
    return glBindTransformFeedback(target, id)
# <command>
#            <proto>void <name>glBindVertexArray</name></proto>
#            <param><ptype>GLuint</ptype> <name>array</name></param>
#            <glx opcode="350" type="render" />
#        </command>
#        
glBindVertexArray_impl=None
def glBindVertexArray (array):
    global glBindVertexArray_impl
    if not glBindVertexArray_impl:
        fptr = pyglGetFuncAddress('glBindVertexArray')
        if not fptr:
            raise RuntimeError('The function glBindVertexArray is not available')
        glBindVertexArray_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glBindVertexArray = glBindVertexArray_impl
    return glBindVertexArray(array)
# <command>
#            <proto>void <name>glBindVertexBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param><ptype>GLsizei</ptype> <name>stride</name></param>
#        </command>
#        
glBindVertexBuffer_impl=None
def glBindVertexBuffer (bindingindex, buffer, offset, stride):
    global glBindVertexBuffer_impl
    if not glBindVertexBuffer_impl:
        fptr = pyglGetFuncAddress('glBindVertexBuffer')
        if not fptr:
            raise RuntimeError('The function glBindVertexBuffer is not available')
        glBindVertexBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_size_t, c_int)(fptr)
    glBindVertexBuffer = glBindVertexBuffer_impl
    return glBindVertexBuffer(bindingindex, buffer, offset, stride)
# <command>
#            <proto>void <name>glBindVertexBuffers</name></proto>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>buffers</name></param>
#            <param len="count">const <ptype>GLintptr</ptype> *<name>offsets</name></param>
#            <param len="count">const <ptype>GLsizei</ptype> *<name>strides</name></param>
#        </command>
#        
glBindVertexBuffers_impl=None
def glBindVertexBuffers (first, count, buffers, offsets, strides):
    global glBindVertexBuffers_impl
    if not glBindVertexBuffers_impl:
        fptr = pyglGetFuncAddress('glBindVertexBuffers')
        if not fptr:
            raise RuntimeError('The function glBindVertexBuffers is not available')
        glBindVertexBuffers_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_void_p, c_void_p)(fptr)
    glBindVertexBuffers = (lambda first,count,buffers,offsets,strides:glBindVertexBuffers_impl(first,count,pyglGetAsConstVoidPointer( buffers ),pyglGetAsConstVoidPointer( offsets ),pyglGetAsConstVoidPointer( strides )))
    return glBindVertexBuffers(first, count, buffers, offsets, strides)
# <command>
#            <proto>void <name>glBlendColor</name></proto>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>red</name></param>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>green</name></param>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>blue</name></param>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>alpha</name></param>
#            <glx opcode="4096" type="render" />
#        </command>
#        
glBlendColor_impl=None
def glBlendColor (red, green, blue, alpha):
    global glBlendColor_impl
    if not glBlendColor_impl:
        fptr = pyglGetFuncAddress('glBlendColor')
        if not fptr:
            raise RuntimeError('The function glBlendColor is not available')
        glBlendColor_impl = PYGL_FUNC_TYPE( None ,c_float, c_float, c_float, c_float)(fptr)
    glBlendColor = glBlendColor_impl
    return glBlendColor(red, green, blue, alpha)
# <command>
#            <proto>void <name>glBlendEquation</name></proto>
#            <param group="BlendEquationMode"><ptype>GLenum</ptype> <name>mode</name></param>
#            <glx opcode="4097" type="render" />
#        </command>
#        
glBlendEquation_impl=None
def glBlendEquation (mode):
    global glBlendEquation_impl
    if not glBlendEquation_impl:
        fptr = pyglGetFuncAddress('glBlendEquation')
        if not fptr:
            raise RuntimeError('The function glBlendEquation is not available')
        glBlendEquation_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glBlendEquation = glBlendEquation_impl
    return glBlendEquation(mode)
# <command>
#            <proto>void <name>glBlendEquationSeparate</name></proto>
#            <param group="BlendEquationModeEXT"><ptype>GLenum</ptype> <name>modeRGB</name></param>
#            <param group="BlendEquationModeEXT"><ptype>GLenum</ptype> <name>modeAlpha</name></param>
#            <glx opcode="4228" type="render" />
#        </command>
#        
glBlendEquationSeparate_impl=None
def glBlendEquationSeparate (modeRGB, modeAlpha):
    global glBlendEquationSeparate_impl
    if not glBlendEquationSeparate_impl:
        fptr = pyglGetFuncAddress('glBlendEquationSeparate')
        if not fptr:
            raise RuntimeError('The function glBlendEquationSeparate is not available')
        glBlendEquationSeparate_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBlendEquationSeparate = glBlendEquationSeparate_impl
    return glBlendEquationSeparate(modeRGB, modeAlpha)
# <command>
#            <proto>void <name>glBlendEquationSeparatei</name></proto>
#            <param><ptype>GLuint</ptype> <name>buf</name></param>
#            <param><ptype>GLenum</ptype> <name>modeRGB</name></param>
#            <param><ptype>GLenum</ptype> <name>modeAlpha</name></param>
#        </command>
#        
glBlendEquationSeparatei_impl=None
def glBlendEquationSeparatei (buf, modeRGB, modeAlpha):
    global glBlendEquationSeparatei_impl
    if not glBlendEquationSeparatei_impl:
        fptr = pyglGetFuncAddress('glBlendEquationSeparatei')
        if not fptr:
            raise RuntimeError('The function glBlendEquationSeparatei is not available')
        glBlendEquationSeparatei_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glBlendEquationSeparatei = glBlendEquationSeparatei_impl
    return glBlendEquationSeparatei(buf, modeRGB, modeAlpha)
# <command>
#            <proto>void <name>glBlendEquationi</name></proto>
#            <param><ptype>GLuint</ptype> <name>buf</name></param>
#            <param><ptype>GLenum</ptype> <name>mode</name></param>
#        </command>
#        
glBlendEquationi_impl=None
def glBlendEquationi (buf, mode):
    global glBlendEquationi_impl
    if not glBlendEquationi_impl:
        fptr = pyglGetFuncAddress('glBlendEquationi')
        if not fptr:
            raise RuntimeError('The function glBlendEquationi is not available')
        glBlendEquationi_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBlendEquationi = glBlendEquationi_impl
    return glBlendEquationi(buf, mode)
# <command>
#            <proto>void <name>glBlendFunc</name></proto>
#            <param group="BlendingFactorSrc"><ptype>GLenum</ptype> <name>sfactor</name></param>
#            <param group="BlendingFactorDest"><ptype>GLenum</ptype> <name>dfactor</name></param>
#            <glx opcode="160" type="render" />
#        </command>
#        
glBlendFunc_impl=None
def glBlendFunc (sfactor, dfactor):
    global glBlendFunc_impl
    if not glBlendFunc_impl:
        fptr = pyglGetFuncAddress('glBlendFunc')
        if not fptr:
            raise RuntimeError('The function glBlendFunc is not available')
        glBlendFunc_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glBlendFunc = glBlendFunc_impl
    return glBlendFunc(sfactor, dfactor)
# <command>
#            <proto>void <name>glBlendFuncSeparate</name></proto>
#            <param group="BlendFuncSeparateParameterEXT"><ptype>GLenum</ptype> <name>sfactorRGB</name></param>
#            <param group="BlendFuncSeparateParameterEXT"><ptype>GLenum</ptype> <name>dfactorRGB</name></param>
#            <param group="BlendFuncSeparateParameterEXT"><ptype>GLenum</ptype> <name>sfactorAlpha</name></param>
#            <param group="BlendFuncSeparateParameterEXT"><ptype>GLenum</ptype> <name>dfactorAlpha</name></param>
#            <glx opcode="4134" type="render" />
#        </command>
#        
glBlendFuncSeparate_impl=None
def glBlendFuncSeparate (sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha):
    global glBlendFuncSeparate_impl
    if not glBlendFuncSeparate_impl:
        fptr = pyglGetFuncAddress('glBlendFuncSeparate')
        if not fptr:
            raise RuntimeError('The function glBlendFuncSeparate is not available')
        glBlendFuncSeparate_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint)(fptr)
    glBlendFuncSeparate = glBlendFuncSeparate_impl
    return glBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)
# <command>
#            <proto>void <name>glBlendFuncSeparatei</name></proto>
#            <param><ptype>GLuint</ptype> <name>buf</name></param>
#            <param><ptype>GLenum</ptype> <name>srcRGB</name></param>
#            <param><ptype>GLenum</ptype> <name>dstRGB</name></param>
#            <param><ptype>GLenum</ptype> <name>srcAlpha</name></param>
#            <param><ptype>GLenum</ptype> <name>dstAlpha</name></param>
#        </command>
#        
glBlendFuncSeparatei_impl=None
def glBlendFuncSeparatei (buf, srcRGB, dstRGB, srcAlpha, dstAlpha):
    global glBlendFuncSeparatei_impl
    if not glBlendFuncSeparatei_impl:
        fptr = pyglGetFuncAddress('glBlendFuncSeparatei')
        if not fptr:
            raise RuntimeError('The function glBlendFuncSeparatei is not available')
        glBlendFuncSeparatei_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_uint)(fptr)
    glBlendFuncSeparatei = glBlendFuncSeparatei_impl
    return glBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)
# <command>
#            <proto>void <name>glBlendFunci</name></proto>
#            <param><ptype>GLuint</ptype> <name>buf</name></param>
#            <param><ptype>GLenum</ptype> <name>src</name></param>
#            <param><ptype>GLenum</ptype> <name>dst</name></param>
#        </command>
#        
glBlendFunci_impl=None
def glBlendFunci (buf, src, dst):
    global glBlendFunci_impl
    if not glBlendFunci_impl:
        fptr = pyglGetFuncAddress('glBlendFunci')
        if not fptr:
            raise RuntimeError('The function glBlendFunci is not available')
        glBlendFunci_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glBlendFunci = glBlendFunci_impl
    return glBlendFunci(buf, src, dst)
# <command>
#            <proto>void <name>glBlitFramebuffer</name></proto>
#            <param><ptype>GLint</ptype> <name>srcX0</name></param>
#            <param><ptype>GLint</ptype> <name>srcY0</name></param>
#            <param><ptype>GLint</ptype> <name>srcX1</name></param>
#            <param><ptype>GLint</ptype> <name>srcY1</name></param>
#            <param><ptype>GLint</ptype> <name>dstX0</name></param>
#            <param><ptype>GLint</ptype> <name>dstY0</name></param>
#            <param><ptype>GLint</ptype> <name>dstX1</name></param>
#            <param><ptype>GLint</ptype> <name>dstY1</name></param>
#            <param group="ClearBufferMask"><ptype>GLbitfield</ptype> <name>mask</name></param>
#            <param><ptype>GLenum</ptype> <name>filter</name></param>
#            <glx opcode="4330" type="render" />
#        </command>
#        
glBlitFramebuffer_impl=None
def glBlitFramebuffer (srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
    global glBlitFramebuffer_impl
    if not glBlitFramebuffer_impl:
        fptr = pyglGetFuncAddress('glBlitFramebuffer')
        if not fptr:
            raise RuntimeError('The function glBlitFramebuffer is not available')
        glBlitFramebuffer_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint)(fptr)
    glBlitFramebuffer = glBlitFramebuffer_impl
    return glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)
# <command>
#            <proto>void <name>glBlitNamedFramebuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>readFramebuffer</name></param>
#            <param><ptype>GLuint</ptype> <name>drawFramebuffer</name></param>
#            <param><ptype>GLint</ptype> <name>srcX0</name></param>
#            <param><ptype>GLint</ptype> <name>srcY0</name></param>
#            <param><ptype>GLint</ptype> <name>srcX1</name></param>
#            <param><ptype>GLint</ptype> <name>srcY1</name></param>
#            <param><ptype>GLint</ptype> <name>dstX0</name></param>
#            <param><ptype>GLint</ptype> <name>dstY0</name></param>
#            <param><ptype>GLint</ptype> <name>dstX1</name></param>
#            <param><ptype>GLint</ptype> <name>dstY1</name></param>
#            <param><ptype>GLbitfield</ptype> <name>mask</name></param>
#            <param><ptype>GLenum</ptype> <name>filter</name></param>
#        </command>
#        
glBlitNamedFramebuffer_impl=None
def glBlitNamedFramebuffer (readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter):
    global glBlitNamedFramebuffer_impl
    if not glBlitNamedFramebuffer_impl:
        fptr = pyglGetFuncAddress('glBlitNamedFramebuffer')
        if not fptr:
            raise RuntimeError('The function glBlitNamedFramebuffer is not available')
        glBlitNamedFramebuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint)(fptr)
    glBlitNamedFramebuffer = glBlitNamedFramebuffer_impl
    return glBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)
# <command>
#            <proto>void <name>glBufferData</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param len="size">const void *<name>data</name></param>
#            <param group="BufferUsageARB"><ptype>GLenum</ptype> <name>usage</name></param>
#        </command>
#        
glBufferData_impl=None
def glBufferData (target, size, data, usage):
    global glBufferData_impl
    if not glBufferData_impl:
        fptr = pyglGetFuncAddress('glBufferData')
        if not fptr:
            raise RuntimeError('The function glBufferData is not available')
        glBufferData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p, c_void_p, c_uint)(fptr)
    glBufferData = (lambda target,size,data,usage:glBufferData_impl(target,size,pyglGetAsConstVoidPointer( data ),usage))
    return glBufferData(target, size, data, usage)
# <command>
#            <proto>void <name>glBufferStorage</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param len="size">const void *<name>data</name></param>
#            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
#        </command>
#        
glBufferStorage_impl=None
def glBufferStorage (target, size, data, flags):
    global glBufferStorage_impl
    if not glBufferStorage_impl:
        fptr = pyglGetFuncAddress('glBufferStorage')
        if not fptr:
            raise RuntimeError('The function glBufferStorage is not available')
        glBufferStorage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p, c_void_p, c_uint)(fptr)
    glBufferStorage = (lambda target,size,data,flags:glBufferStorage_impl(target,size,pyglGetAsConstVoidPointer( data ),flags))
    return glBufferStorage(target, size, data, flags)
# <command>
#            <proto>void <name>glBufferSubData</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param len="size">const void *<name>data</name></param>
#        </command>
#        
glBufferSubData_impl=None
def glBufferSubData (target, offset, size, data):
    global glBufferSubData_impl
    if not glBufferSubData_impl:
        fptr = pyglGetFuncAddress('glBufferSubData')
        if not fptr:
            raise RuntimeError('The function glBufferSubData is not available')
        glBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_size_t, c_void_p, c_void_p)(fptr)
    glBufferSubData = (lambda target,offset,size,data:glBufferSubData_impl(target,offset,size,pyglGetAsConstVoidPointer( data )))
    return glBufferSubData(target, offset, size, data)
# <command>
#            <proto><ptype>GLenum</ptype> <name>glCheckFramebufferStatus</name></proto>
#            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <glx opcode="1427" type="vendor" />
#        </command>
#        
glCheckFramebufferStatus_impl=None
def glCheckFramebufferStatus (target):
    global glCheckFramebufferStatus_impl
    if not glCheckFramebufferStatus_impl:
        fptr = pyglGetFuncAddress('glCheckFramebufferStatus')
        if not fptr:
            raise RuntimeError('The function glCheckFramebufferStatus is not available')
        glCheckFramebufferStatus_impl = PYGL_FUNC_TYPE( c_uint ,c_uint)(fptr)
    glCheckFramebufferStatus = glCheckFramebufferStatus_impl
    return glCheckFramebufferStatus(target)
# <command>
#            <proto><ptype>GLenum</ptype> <name>glCheckNamedFramebufferStatus</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#        </command>
#        
glCheckNamedFramebufferStatus_impl=None
def glCheckNamedFramebufferStatus (framebuffer, target):
    global glCheckNamedFramebufferStatus_impl
    if not glCheckNamedFramebufferStatus_impl:
        fptr = pyglGetFuncAddress('glCheckNamedFramebufferStatus')
        if not fptr:
            raise RuntimeError('The function glCheckNamedFramebufferStatus is not available')
        glCheckNamedFramebufferStatus_impl = PYGL_FUNC_TYPE( c_uint ,c_uint, c_uint)(fptr)
    glCheckNamedFramebufferStatus = glCheckNamedFramebufferStatus_impl
    return glCheckNamedFramebufferStatus(framebuffer, target)
# <command>
#            <proto>void <name>glClampColor</name></proto>
#            <param group="ClampColorTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="ClampColorModeARB"><ptype>GLenum</ptype> <name>clamp</name></param>
#            <glx opcode="234" type="render" />
#        </command>
#        
glClampColor_impl=None
def glClampColor (target, clamp):
    global glClampColor_impl
    if not glClampColor_impl:
        fptr = pyglGetFuncAddress('glClampColor')
        if not fptr:
            raise RuntimeError('The function glClampColor is not available')
        glClampColor_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glClampColor = glClampColor_impl
    return glClampColor(target, clamp)
# <command>
#            <proto>void <name>glClear</name></proto>
#            <param group="ClearBufferMask"><ptype>GLbitfield</ptype> <name>mask</name></param>
#            <glx opcode="127" type="render" />
#        </command>
#        
glClear_impl=None
def glClear (mask):
    global glClear_impl
    if not glClear_impl:
        fptr = pyglGetFuncAddress('glClear')
        if not fptr:
            raise RuntimeError('The function glClear is not available')
        glClear_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glClear = glClear_impl
    return glClear(mask)
# <command>
#            <proto>void <name>glClearBufferData</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type)">const void *<name>data</name></param>
#        </command>
#        
glClearBufferData_impl=None
def glClearBufferData (target, internalformat, format, type, data):
    global glClearBufferData_impl
    if not glClearBufferData_impl:
        fptr = pyglGetFuncAddress('glClearBufferData')
        if not fptr:
            raise RuntimeError('The function glClearBufferData is not available')
        glClearBufferData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_void_p)(fptr)
    glClearBufferData = (lambda target,internalformat,format,type,data:glClearBufferData_impl(target,internalformat,format,type,pyglGetAsConstVoidPointer( data )))
    return glClearBufferData(target, internalformat, format, type, data)
# <command>
#            <proto>void <name>glClearBufferSubData</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type)">const void *<name>data</name></param>
#        </command>
#        
glClearBufferSubData_impl=None
def glClearBufferSubData (target, internalformat, offset, size, format, type, data):
    global glClearBufferSubData_impl
    if not glClearBufferSubData_impl:
        fptr = pyglGetFuncAddress('glClearBufferSubData')
        if not fptr:
            raise RuntimeError('The function glClearBufferSubData is not available')
        glClearBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_size_t, c_void_p, c_uint, c_uint, c_void_p)(fptr)
    glClearBufferSubData = (lambda target,internalformat,offset,size,format,type,data:glClearBufferSubData_impl(target,internalformat,offset,size,format,type,pyglGetAsConstVoidPointer( data )))
    return glClearBufferSubData(target, internalformat, offset, size, format, type, data)
# <command>
#            <proto>void <name>glClearBufferfi</name></proto>
#            <param><ptype>GLenum</ptype> <name>buffer</name></param>
#            <param group="DrawBufferName"><ptype>GLint</ptype> <name>drawbuffer</name></param>
#            <param><ptype>GLfloat</ptype> <name>depth</name></param>
#            <param><ptype>GLint</ptype> <name>stencil</name></param>
#        </command>
#        
glClearBufferfi_impl=None
def glClearBufferfi (buffer, drawbuffer, depth, stencil):
    global glClearBufferfi_impl
    if not glClearBufferfi_impl:
        fptr = pyglGetFuncAddress('glClearBufferfi')
        if not fptr:
            raise RuntimeError('The function glClearBufferfi is not available')
        glClearBufferfi_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_float, c_int)(fptr)
    glClearBufferfi = glClearBufferfi_impl
    return glClearBufferfi(buffer, drawbuffer, depth, stencil)
# <command>
#            <proto>void <name>glClearBufferfv</name></proto>
#            <param><ptype>GLenum</ptype> <name>buffer</name></param>
#            <param group="DrawBufferName"><ptype>GLint</ptype> <name>drawbuffer</name></param>
#            <param len="COMPSIZE(buffer)">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glClearBufferfv_impl=None
def glClearBufferfv (buffer, drawbuffer, value):
    global glClearBufferfv_impl
    if not glClearBufferfv_impl:
        fptr = pyglGetFuncAddress('glClearBufferfv')
        if not fptr:
            raise RuntimeError('The function glClearBufferfv is not available')
        glClearBufferfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glClearBufferfv = (lambda buffer,drawbuffer,value:glClearBufferfv_impl(buffer,drawbuffer,pyglGetAsConstVoidPointer( value )))
    return glClearBufferfv(buffer, drawbuffer, value)
# <command>
#            <proto>void <name>glClearBufferiv</name></proto>
#            <param><ptype>GLenum</ptype> <name>buffer</name></param>
#            <param group="DrawBufferName"><ptype>GLint</ptype> <name>drawbuffer</name></param>
#            <param len="COMPSIZE(buffer)">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glClearBufferiv_impl=None
def glClearBufferiv (buffer, drawbuffer, value):
    global glClearBufferiv_impl
    if not glClearBufferiv_impl:
        fptr = pyglGetFuncAddress('glClearBufferiv')
        if not fptr:
            raise RuntimeError('The function glClearBufferiv is not available')
        glClearBufferiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glClearBufferiv = (lambda buffer,drawbuffer,value:glClearBufferiv_impl(buffer,drawbuffer,pyglGetAsConstVoidPointer( value )))
    return glClearBufferiv(buffer, drawbuffer, value)
# <command>
#            <proto>void <name>glClearBufferuiv</name></proto>
#            <param><ptype>GLenum</ptype> <name>buffer</name></param>
#            <param group="DrawBufferName"><ptype>GLint</ptype> <name>drawbuffer</name></param>
#            <param len="COMPSIZE(buffer)">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glClearBufferuiv_impl=None
def glClearBufferuiv (buffer, drawbuffer, value):
    global glClearBufferuiv_impl
    if not glClearBufferuiv_impl:
        fptr = pyglGetFuncAddress('glClearBufferuiv')
        if not fptr:
            raise RuntimeError('The function glClearBufferuiv is not available')
        glClearBufferuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glClearBufferuiv = (lambda buffer,drawbuffer,value:glClearBufferuiv_impl(buffer,drawbuffer,pyglGetAsConstVoidPointer( value )))
    return glClearBufferuiv(buffer, drawbuffer, value)
# <command>
#            <proto>void <name>glClearColor</name></proto>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>red</name></param>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>green</name></param>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>blue</name></param>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>alpha</name></param>
#            <glx opcode="130" type="render" />
#        </command>
#        
glClearColor_impl=None
def glClearColor (red, green, blue, alpha):
    global glClearColor_impl
    if not glClearColor_impl:
        fptr = pyglGetFuncAddress('glClearColor')
        if not fptr:
            raise RuntimeError('The function glClearColor is not available')
        glClearColor_impl = PYGL_FUNC_TYPE( None ,c_float, c_float, c_float, c_float)(fptr)
    glClearColor = glClearColor_impl
    return glClearColor(red, green, blue, alpha)
# <command>
#            <proto>void <name>glClearDepth</name></proto>
#            <param><ptype>GLdouble</ptype> <name>depth</name></param>
#            <glx opcode="132" type="render" />
#        </command>
#        
glClearDepth_impl=None
def glClearDepth (depth):
    global glClearDepth_impl
    if not glClearDepth_impl:
        fptr = pyglGetFuncAddress('glClearDepth')
        if not fptr:
            raise RuntimeError('The function glClearDepth is not available')
        glClearDepth_impl = PYGL_FUNC_TYPE( None ,c_double)(fptr)
    glClearDepth = glClearDepth_impl
    return glClearDepth(depth)
# <command>
#            <proto>void <name>glClearDepthf</name></proto>
#            <param><ptype>GLfloat</ptype> <name>d</name></param>
#        </command>
#        
glClearDepthf_impl=None
def glClearDepthf (d):
    global glClearDepthf_impl
    if not glClearDepthf_impl:
        fptr = pyglGetFuncAddress('glClearDepthf')
        if not fptr:
            raise RuntimeError('The function glClearDepthf is not available')
        glClearDepthf_impl = PYGL_FUNC_TYPE( None ,c_float)(fptr)
    glClearDepthf = glClearDepthf_impl
    return glClearDepthf(d)
# <command>
#            <proto>void <name>glClearNamedBufferData</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param>const void *<name>data</name></param>
#        </command>
#        
glClearNamedBufferData_impl=None
def glClearNamedBufferData (buffer, internalformat, format, type, data):
    global glClearNamedBufferData_impl
    if not glClearNamedBufferData_impl:
        fptr = pyglGetFuncAddress('glClearNamedBufferData')
        if not fptr:
            raise RuntimeError('The function glClearNamedBufferData is not available')
        glClearNamedBufferData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_void_p)(fptr)
    glClearNamedBufferData = (lambda buffer,internalformat,format,type,data:glClearNamedBufferData_impl(buffer,internalformat,format,type,pyglGetAsConstVoidPointer( data )))
    return glClearNamedBufferData(buffer, internalformat, format, type, data)
# <command>
#            <proto>void <name>glClearNamedBufferSubData</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param>const void *<name>data</name></param>
#        </command>
#        
glClearNamedBufferSubData_impl=None
def glClearNamedBufferSubData (buffer, internalformat, offset, size, format, type, data):
    global glClearNamedBufferSubData_impl
    if not glClearNamedBufferSubData_impl:
        fptr = pyglGetFuncAddress('glClearNamedBufferSubData')
        if not fptr:
            raise RuntimeError('The function glClearNamedBufferSubData is not available')
        glClearNamedBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_size_t, c_void_p, c_uint, c_uint, c_void_p)(fptr)
    glClearNamedBufferSubData = (lambda buffer,internalformat,offset,size,format,type,data:glClearNamedBufferSubData_impl(buffer,internalformat,offset,size,format,type,pyglGetAsConstVoidPointer( data )))
    return glClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data)
# <command>
#            <proto>void <name>glClearNamedFramebufferfi</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>buffer</name></param>
#            <param><ptype>GLint</ptype> <name>drawbuffer</name></param>
#            <param><ptype>GLfloat</ptype> <name>depth</name></param>
#            <param><ptype>GLint</ptype> <name>stencil</name></param>
#        </command>
#        
glClearNamedFramebufferfi_impl=None
def glClearNamedFramebufferfi (framebuffer, buffer, drawbuffer, depth, stencil):
    global glClearNamedFramebufferfi_impl
    if not glClearNamedFramebufferfi_impl:
        fptr = pyglGetFuncAddress('glClearNamedFramebufferfi')
        if not fptr:
            raise RuntimeError('The function glClearNamedFramebufferfi is not available')
        glClearNamedFramebufferfi_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_float, c_int)(fptr)
    glClearNamedFramebufferfi = glClearNamedFramebufferfi_impl
    return glClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil)
# <command>
#            <proto>void <name>glClearNamedFramebufferfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>buffer</name></param>
#            <param><ptype>GLint</ptype> <name>drawbuffer</name></param>
#            <param>const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glClearNamedFramebufferfv_impl=None
def glClearNamedFramebufferfv (framebuffer, buffer, drawbuffer, value):
    global glClearNamedFramebufferfv_impl
    if not glClearNamedFramebufferfv_impl:
        fptr = pyglGetFuncAddress('glClearNamedFramebufferfv')
        if not fptr:
            raise RuntimeError('The function glClearNamedFramebufferfv is not available')
        glClearNamedFramebufferfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p)(fptr)
    glClearNamedFramebufferfv = (lambda framebuffer,buffer,drawbuffer,value:glClearNamedFramebufferfv_impl(framebuffer,buffer,drawbuffer,pyglGetAsConstVoidPointer( value )))
    return glClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value)
# <command>
#            <proto>void <name>glClearNamedFramebufferiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>buffer</name></param>
#            <param><ptype>GLint</ptype> <name>drawbuffer</name></param>
#            <param>const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glClearNamedFramebufferiv_impl=None
def glClearNamedFramebufferiv (framebuffer, buffer, drawbuffer, value):
    global glClearNamedFramebufferiv_impl
    if not glClearNamedFramebufferiv_impl:
        fptr = pyglGetFuncAddress('glClearNamedFramebufferiv')
        if not fptr:
            raise RuntimeError('The function glClearNamedFramebufferiv is not available')
        glClearNamedFramebufferiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p)(fptr)
    glClearNamedFramebufferiv = (lambda framebuffer,buffer,drawbuffer,value:glClearNamedFramebufferiv_impl(framebuffer,buffer,drawbuffer,pyglGetAsConstVoidPointer( value )))
    return glClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value)
# <command>
#            <proto>void <name>glClearNamedFramebufferuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>buffer</name></param>
#            <param><ptype>GLint</ptype> <name>drawbuffer</name></param>
#            <param>const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glClearNamedFramebufferuiv_impl=None
def glClearNamedFramebufferuiv (framebuffer, buffer, drawbuffer, value):
    global glClearNamedFramebufferuiv_impl
    if not glClearNamedFramebufferuiv_impl:
        fptr = pyglGetFuncAddress('glClearNamedFramebufferuiv')
        if not fptr:
            raise RuntimeError('The function glClearNamedFramebufferuiv is not available')
        glClearNamedFramebufferuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p)(fptr)
    glClearNamedFramebufferuiv = (lambda framebuffer,buffer,drawbuffer,value:glClearNamedFramebufferuiv_impl(framebuffer,buffer,drawbuffer,pyglGetAsConstVoidPointer( value )))
    return glClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value)
# <command>
#            <proto>void <name>glClearStencil</name></proto>
#            <param group="StencilValue"><ptype>GLint</ptype> <name>s</name></param>
#            <glx opcode="131" type="render" />
#        </command>
#        
glClearStencil_impl=None
def glClearStencil (s):
    global glClearStencil_impl
    if not glClearStencil_impl:
        fptr = pyglGetFuncAddress('glClearStencil')
        if not fptr:
            raise RuntimeError('The function glClearStencil is not available')
        glClearStencil_impl = PYGL_FUNC_TYPE( None ,c_int)(fptr)
    glClearStencil = glClearStencil_impl
    return glClearStencil(s)
# <command>
#            <proto>void <name>glClearTexImage</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type)">const void *<name>data</name></param>
#        </command>
#        
glClearTexImage_impl=None
def glClearTexImage (texture, level, format, type, data):
    global glClearTexImage_impl
    if not glClearTexImage_impl:
        fptr = pyglGetFuncAddress('glClearTexImage')
        if not fptr:
            raise RuntimeError('The function glClearTexImage is not available')
        glClearTexImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_uint, c_void_p)(fptr)
    glClearTexImage = (lambda texture,level,format,type,data:glClearTexImage_impl(texture,level,format,type,pyglGetAsConstVoidPointer( data )))
    return glClearTexImage(texture, level, format, type, data)
# <command>
#            <proto>void <name>glClearTexSubImage</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type)">const void *<name>data</name></param>
#        </command>
#        
glClearTexSubImage_impl=None
def glClearTexSubImage (texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data):
    global glClearTexSubImage_impl
    if not glClearTexSubImage_impl:
        fptr = pyglGetFuncAddress('glClearTexSubImage')
        if not fptr:
            raise RuntimeError('The function glClearTexSubImage is not available')
        glClearTexSubImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glClearTexSubImage = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,data:glClearTexSubImage_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pyglGetAsConstVoidPointer( data )))
    return glClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data)
# <command>
#            <proto><ptype>GLenum</ptype> <name>glClientWaitSync</name></proto>
#            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
#            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
#            <param><ptype>GLuint64</ptype> <name>timeout</name></param>
#        </command>
#        
glClientWaitSync_impl=None
def glClientWaitSync (sync, flags, timeout):
    global glClientWaitSync_impl
    if not glClientWaitSync_impl:
        fptr = pyglGetFuncAddress('glClientWaitSync')
        if not fptr:
            raise RuntimeError('The function glClientWaitSync is not available')
        glClientWaitSync_impl = PYGL_FUNC_TYPE( c_uint ,c_void_p, c_uint, c_ulonglong)(fptr)
    glClientWaitSync = glClientWaitSync_impl
    return glClientWaitSync(sync, flags, timeout)
# <command>
#            <proto>void <name>glClipControl</name></proto>
#            <param><ptype>GLenum</ptype> <name>origin</name></param>
#            <param><ptype>GLenum</ptype> <name>depth</name></param>
#        </command>
#        
glClipControl_impl=None
def glClipControl (origin, depth):
    global glClipControl_impl
    if not glClipControl_impl:
        fptr = pyglGetFuncAddress('glClipControl')
        if not fptr:
            raise RuntimeError('The function glClipControl is not available')
        glClipControl_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glClipControl = glClipControl_impl
    return glClipControl(origin, depth)
# <command>
#            <proto>void <name>glColorMask</name></proto>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>red</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>green</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>blue</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>alpha</name></param>
#            <glx opcode="134" type="render" />
#        </command>
#        
glColorMask_impl=None
def glColorMask (red, green, blue, alpha):
    global glColorMask_impl
    if not glColorMask_impl:
        fptr = pyglGetFuncAddress('glColorMask')
        if not fptr:
            raise RuntimeError('The function glColorMask is not available')
        glColorMask_impl = PYGL_FUNC_TYPE( None ,c_char, c_char, c_char, c_char)(fptr)
    glColorMask = glColorMask_impl
    return glColorMask(red, green, blue, alpha)
# <command>
#            <proto>void <name>glColorMaski</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>r</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>g</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>b</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>a</name></param>
#        </command>
#        
glColorMaski_impl=None
def glColorMaski (index, r, g, b, a):
    global glColorMaski_impl
    if not glColorMaski_impl:
        fptr = pyglGetFuncAddress('glColorMaski')
        if not fptr:
            raise RuntimeError('The function glColorMaski is not available')
        glColorMaski_impl = PYGL_FUNC_TYPE( None ,c_uint, c_char, c_char, c_char, c_char)(fptr)
    glColorMaski = glColorMaski_impl
    return glColorMaski(index, r, g, b, a)
# <command>
#            <proto>void <name>glCompileShader</name></proto>
#            <param><ptype>GLuint</ptype> <name>shader</name></param>
#        </command>
#        
glCompileShader_impl=None
def glCompileShader (shader):
    global glCompileShader_impl
    if not glCompileShader_impl:
        fptr = pyglGetFuncAddress('glCompileShader')
        if not fptr:
            raise RuntimeError('The function glCompileShader is not available')
        glCompileShader_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glCompileShader = glCompileShader_impl
    return glCompileShader(shader)
# <command>
#            <proto>void <name>glCompressedTexImage1D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
#            <glx opcode="214" type="render" />
#            <glx comment="PBO protocol" name="glCompressedTexImage1DPBO" opcode="314" type="render" />
#        </command>
#        
glCompressedTexImage1D_impl=None
def glCompressedTexImage1D (target, level, internalformat, width, border, imageSize, data):
    global glCompressedTexImage1D_impl
    if not glCompressedTexImage1D_impl:
        fptr = pyglGetFuncAddress('glCompressedTexImage1D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexImage1D is not available')
        glCompressedTexImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int, c_int, c_void_p)(fptr)
    glCompressedTexImage1D = (lambda target,level,internalformat,width,border,imageSize,data:glCompressedTexImage1D_impl(target,level,internalformat,width,border,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data)
# <command>
#            <proto>void <name>glCompressedTexImage2D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
#            <glx opcode="215" type="render" />
#            <glx comment="PBO protocol" name="glCompressedTexImage2DPBO" opcode="315" type="render" />
#        </command>
#        
glCompressedTexImage2D_impl=None
def glCompressedTexImage2D (target, level, internalformat, width, height, border, imageSize, data):
    global glCompressedTexImage2D_impl
    if not glCompressedTexImage2D_impl:
        fptr = pyglGetFuncAddress('glCompressedTexImage2D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexImage2D is not available')
        glCompressedTexImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int, c_int, c_int, c_void_p)(fptr)
    glCompressedTexImage2D = (lambda target,level,internalformat,width,height,border,imageSize,data:glCompressedTexImage2D_impl(target,level,internalformat,width,height,border,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)
# <command>
#            <proto>void <name>glCompressedTexImage3D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
#            <glx opcode="216" type="render" />
#            <glx comment="PBO protocol" name="glCompressedTexImage3DPBO" opcode="316" type="render" />
#        </command>
#        
glCompressedTexImage3D_impl=None
def glCompressedTexImage3D (target, level, internalformat, width, height, depth, border, imageSize, data):
    global glCompressedTexImage3D_impl
    if not glCompressedTexImage3D_impl:
        fptr = pyglGetFuncAddress('glCompressedTexImage3D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexImage3D is not available')
        glCompressedTexImage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int, c_int, c_int, c_int, c_void_p)(fptr)
    glCompressedTexImage3D = (lambda target,level,internalformat,width,height,depth,border,imageSize,data:glCompressedTexImage3D_impl(target,level,internalformat,width,height,depth,border,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data)
# <command>
#            <proto>void <name>glCompressedTexSubImage1D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
#            <glx opcode="217" type="render" />
#            <glx comment="PBO protocol" name="glCompressedTexSubImage1DPBO" opcode="317" type="render" />
#        </command>
#        
glCompressedTexSubImage1D_impl=None
def glCompressedTexSubImage1D (target, level, xoffset, width, format, imageSize, data):
    global glCompressedTexSubImage1D_impl
    if not glCompressedTexSubImage1D_impl:
        fptr = pyglGetFuncAddress('glCompressedTexSubImage1D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexSubImage1D is not available')
        glCompressedTexSubImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_uint, c_int, c_void_p)(fptr)
    glCompressedTexSubImage1D = (lambda target,level,xoffset,width,format,imageSize,data:glCompressedTexSubImage1D_impl(target,level,xoffset,width,format,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data)
# <command>
#            <proto>void <name>glCompressedTexSubImage2D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
#            <glx opcode="218" type="render" />
#            <glx comment="PBO protocol" name="glCompressedTexSubImage2DPBO" opcode="318" type="render" />
#        </command>
#        
glCompressedTexSubImage2D_impl=None
def glCompressedTexSubImage2D (target, level, xoffset, yoffset, width, height, format, imageSize, data):
    global glCompressedTexSubImage2D_impl
    if not glCompressedTexSubImage2D_impl:
        fptr = pyglGetFuncAddress('glCompressedTexSubImage2D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexSubImage2D is not available')
        glCompressedTexSubImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_int, c_void_p)(fptr)
    glCompressedTexSubImage2D = (lambda target,level,xoffset,yoffset,width,height,format,imageSize,data:glCompressedTexSubImage2D_impl(target,level,xoffset,yoffset,width,height,format,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)
# <command>
#            <proto>void <name>glCompressedTexSubImage3D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
#            <glx opcode="219" type="render" />
#            <glx comment="PBO protocol" name="glCompressedTexSubImage3DPBO" opcode="319" type="render" />
#        </command>
#        
glCompressedTexSubImage3D_impl=None
def glCompressedTexSubImage3D (target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
    global glCompressedTexSubImage3D_impl
    if not glCompressedTexSubImage3D_impl:
        fptr = pyglGetFuncAddress('glCompressedTexSubImage3D')
        if not fptr:
            raise RuntimeError('The function glCompressedTexSubImage3D is not available')
        glCompressedTexSubImage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_int, c_void_p)(fptr)
    glCompressedTexSubImage3D = (lambda target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data:glCompressedTexSubImage3D_impl(target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)
# <command>
#            <proto>void <name>glCompressedTextureSubImage1D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param>const void *<name>data</name></param>
#        </command>
#        
glCompressedTextureSubImage1D_impl=None
def glCompressedTextureSubImage1D (texture, level, xoffset, width, format, imageSize, data):
    global glCompressedTextureSubImage1D_impl
    if not glCompressedTextureSubImage1D_impl:
        fptr = pyglGetFuncAddress('glCompressedTextureSubImage1D')
        if not fptr:
            raise RuntimeError('The function glCompressedTextureSubImage1D is not available')
        glCompressedTextureSubImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_uint, c_int, c_void_p)(fptr)
    glCompressedTextureSubImage1D = (lambda texture,level,xoffset,width,format,imageSize,data:glCompressedTextureSubImage1D_impl(texture,level,xoffset,width,format,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data)
# <command>
#            <proto>void <name>glCompressedTextureSubImage2D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param>const void *<name>data</name></param>
#        </command>
#        
glCompressedTextureSubImage2D_impl=None
def glCompressedTextureSubImage2D (texture, level, xoffset, yoffset, width, height, format, imageSize, data):
    global glCompressedTextureSubImage2D_impl
    if not glCompressedTextureSubImage2D_impl:
        fptr = pyglGetFuncAddress('glCompressedTextureSubImage2D')
        if not fptr:
            raise RuntimeError('The function glCompressedTextureSubImage2D is not available')
        glCompressedTextureSubImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_int, c_void_p)(fptr)
    glCompressedTextureSubImage2D = (lambda texture,level,xoffset,yoffset,width,height,format,imageSize,data:glCompressedTextureSubImage2D_impl(texture,level,xoffset,yoffset,width,height,format,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data)
# <command>
#            <proto>void <name>glCompressedTextureSubImage3D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
#            <param>const void *<name>data</name></param>
#        </command>
#        
glCompressedTextureSubImage3D_impl=None
def glCompressedTextureSubImage3D (texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data):
    global glCompressedTextureSubImage3D_impl
    if not glCompressedTextureSubImage3D_impl:
        fptr = pyglGetFuncAddress('glCompressedTextureSubImage3D')
        if not fptr:
            raise RuntimeError('The function glCompressedTextureSubImage3D is not available')
        glCompressedTextureSubImage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_int, c_void_p)(fptr)
    glCompressedTextureSubImage3D = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data:glCompressedTextureSubImage3D_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,pyglGetAsConstVoidPointer( data )))
    return glCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)
# <command>
#            <proto>void <name>glCopyBufferSubData</name></proto>
#            <param><ptype>GLenum</ptype> <name>readTarget</name></param>
#            <param><ptype>GLenum</ptype> <name>writeTarget</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>readOffset</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>writeOffset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#        </command>
#        
glCopyBufferSubData_impl=None
def glCopyBufferSubData (readTarget, writeTarget, readOffset, writeOffset, size):
    global glCopyBufferSubData_impl
    if not glCopyBufferSubData_impl:
        fptr = pyglGetFuncAddress('glCopyBufferSubData')
        if not fptr:
            raise RuntimeError('The function glCopyBufferSubData is not available')
        glCopyBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_size_t, c_size_t, c_void_p)(fptr)
    glCopyBufferSubData = glCopyBufferSubData_impl
    return glCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size)
# <command>
#            <proto>void <name>glCopyImageSubData</name></proto>
#            <param><ptype>GLuint</ptype> <name>srcName</name></param>
#            <param><ptype>GLenum</ptype> <name>srcTarget</name></param>
#            <param><ptype>GLint</ptype> <name>srcLevel</name></param>
#            <param><ptype>GLint</ptype> <name>srcX</name></param>
#            <param><ptype>GLint</ptype> <name>srcY</name></param>
#            <param><ptype>GLint</ptype> <name>srcZ</name></param>
#            <param><ptype>GLuint</ptype> <name>dstName</name></param>
#            <param><ptype>GLenum</ptype> <name>dstTarget</name></param>
#            <param><ptype>GLint</ptype> <name>dstLevel</name></param>
#            <param><ptype>GLint</ptype> <name>dstX</name></param>
#            <param><ptype>GLint</ptype> <name>dstY</name></param>
#            <param><ptype>GLint</ptype> <name>dstZ</name></param>
#            <param><ptype>GLsizei</ptype> <name>srcWidth</name></param>
#            <param><ptype>GLsizei</ptype> <name>srcHeight</name></param>
#            <param><ptype>GLsizei</ptype> <name>srcDepth</name></param>
#        </command>
#        
glCopyImageSubData_impl=None
def glCopyImageSubData (srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth):
    global glCopyImageSubData_impl
    if not glCopyImageSubData_impl:
        fptr = pyglGetFuncAddress('glCopyImageSubData')
        if not fptr:
            raise RuntimeError('The function glCopyImageSubData is not available')
        glCopyImageSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_int, c_int, c_int, c_uint, c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(fptr)
    glCopyImageSubData = glCopyImageSubData_impl
    return glCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth)
# <command>
#            <proto>void <name>glCopyNamedBufferSubData</name></proto>
#            <param><ptype>GLuint</ptype> <name>readBuffer</name></param>
#            <param><ptype>GLuint</ptype> <name>writeBuffer</name></param>
#            <param><ptype>GLintptr</ptype> <name>readOffset</name></param>
#            <param><ptype>GLintptr</ptype> <name>writeOffset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#        </command>
#        
glCopyNamedBufferSubData_impl=None
def glCopyNamedBufferSubData (readBuffer, writeBuffer, readOffset, writeOffset, size):
    global glCopyNamedBufferSubData_impl
    if not glCopyNamedBufferSubData_impl:
        fptr = pyglGetFuncAddress('glCopyNamedBufferSubData')
        if not fptr:
            raise RuntimeError('The function glCopyNamedBufferSubData is not available')
        glCopyNamedBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_size_t, c_size_t, c_void_p)(fptr)
    glCopyNamedBufferSubData = glCopyNamedBufferSubData_impl
    return glCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size)
# <command>
#            <proto>void <name>glCopyTexImage1D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
#            <glx opcode="4119" type="render" />
#        </command>
#        
glCopyTexImage1D_impl=None
def glCopyTexImage1D (target, level, internalformat, x, y, width, border):
    global glCopyTexImage1D_impl
    if not glCopyTexImage1D_impl:
        fptr = pyglGetFuncAddress('glCopyTexImage1D')
        if not fptr:
            raise RuntimeError('The function glCopyTexImage1D is not available')
        glCopyTexImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int, c_int, c_int)(fptr)
    glCopyTexImage1D = glCopyTexImage1D_impl
    return glCopyTexImage1D(target, level, internalformat, x, y, width, border)
# <command>
#            <proto>void <name>glCopyTexImage2D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
#            <glx opcode="4120" type="render" />
#        </command>
#        
glCopyTexImage2D_impl=None
def glCopyTexImage2D (target, level, internalformat, x, y, width, height, border):
    global glCopyTexImage2D_impl
    if not glCopyTexImage2D_impl:
        fptr = pyglGetFuncAddress('glCopyTexImage2D')
        if not fptr:
            raise RuntimeError('The function glCopyTexImage2D is not available')
        glCopyTexImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int, c_int, c_int, c_int)(fptr)
    glCopyTexImage2D = glCopyTexImage2D_impl
    return glCopyTexImage2D(target, level, internalformat, x, y, width, height, border)
# <command>
#            <proto>void <name>glCopyTexSubImage1D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <glx opcode="4121" type="render" />
#        </command>
#        
glCopyTexSubImage1D_impl=None
def glCopyTexSubImage1D (target, level, xoffset, x, y, width):
    global glCopyTexSubImage1D_impl
    if not glCopyTexSubImage1D_impl:
        fptr = pyglGetFuncAddress('glCopyTexSubImage1D')
        if not fptr:
            raise RuntimeError('The function glCopyTexSubImage1D is not available')
        glCopyTexSubImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int)(fptr)
    glCopyTexSubImage1D = glCopyTexSubImage1D_impl
    return glCopyTexSubImage1D(target, level, xoffset, x, y, width)
# <command>
#            <proto>void <name>glCopyTexSubImage2D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <glx opcode="4122" type="render" />
#        </command>
#        
glCopyTexSubImage2D_impl=None
def glCopyTexSubImage2D (target, level, xoffset, yoffset, x, y, width, height):
    global glCopyTexSubImage2D_impl
    if not glCopyTexSubImage2D_impl:
        fptr = pyglGetFuncAddress('glCopyTexSubImage2D')
        if not fptr:
            raise RuntimeError('The function glCopyTexSubImage2D is not available')
        glCopyTexSubImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(fptr)
    glCopyTexSubImage2D = glCopyTexSubImage2D_impl
    return glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)
# <command>
#            <proto>void <name>glCopyTexSubImage3D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <glx opcode="4123" type="render" />
#        </command>
#        
glCopyTexSubImage3D_impl=None
def glCopyTexSubImage3D (target, level, xoffset, yoffset, zoffset, x, y, width, height):
    global glCopyTexSubImage3D_impl
    if not glCopyTexSubImage3D_impl:
        fptr = pyglGetFuncAddress('glCopyTexSubImage3D')
        if not fptr:
            raise RuntimeError('The function glCopyTexSubImage3D is not available')
        glCopyTexSubImage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(fptr)
    glCopyTexSubImage3D = glCopyTexSubImage3D_impl
    return glCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height)
# <command>
#            <proto>void <name>glCopyTextureSubImage1D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#        </command>
#        
glCopyTextureSubImage1D_impl=None
def glCopyTextureSubImage1D (texture, level, xoffset, x, y, width):
    global glCopyTextureSubImage1D_impl
    if not glCopyTextureSubImage1D_impl:
        fptr = pyglGetFuncAddress('glCopyTextureSubImage1D')
        if not fptr:
            raise RuntimeError('The function glCopyTextureSubImage1D is not available')
        glCopyTextureSubImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int)(fptr)
    glCopyTextureSubImage1D = glCopyTextureSubImage1D_impl
    return glCopyTextureSubImage1D(texture, level, xoffset, x, y, width)
# <command>
#            <proto>void <name>glCopyTextureSubImage2D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glCopyTextureSubImage2D_impl=None
def glCopyTextureSubImage2D (texture, level, xoffset, yoffset, x, y, width, height):
    global glCopyTextureSubImage2D_impl
    if not glCopyTextureSubImage2D_impl:
        fptr = pyglGetFuncAddress('glCopyTextureSubImage2D')
        if not fptr:
            raise RuntimeError('The function glCopyTextureSubImage2D is not available')
        glCopyTextureSubImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(fptr)
    glCopyTextureSubImage2D = glCopyTextureSubImage2D_impl
    return glCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height)
# <command>
#            <proto>void <name>glCopyTextureSubImage3D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glCopyTextureSubImage3D_impl=None
def glCopyTextureSubImage3D (texture, level, xoffset, yoffset, zoffset, x, y, width, height):
    global glCopyTextureSubImage3D_impl
    if not glCopyTextureSubImage3D_impl:
        fptr = pyglGetFuncAddress('glCopyTextureSubImage3D')
        if not fptr:
            raise RuntimeError('The function glCopyTextureSubImage3D is not available')
        glCopyTextureSubImage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(fptr)
    glCopyTextureSubImage3D = glCopyTextureSubImage3D_impl
    return glCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height)
# <command>
#            <proto>void <name>glCreateBuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>buffers</name></param>
#        </command>
#        
glCreateBuffers_impl=None
def glCreateBuffers (n, buffers):
    global glCreateBuffers_impl
    if not glCreateBuffers_impl:
        fptr = pyglGetFuncAddress('glCreateBuffers')
        if not fptr:
            raise RuntimeError('The function glCreateBuffers is not available')
        glCreateBuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glCreateBuffers = (lambda n,buffers:glCreateBuffers_impl(n,(c_uint8*len( buffers )).from_buffer( buffers )))
    return glCreateBuffers(n, buffers)
# <command>
#            <proto>void <name>glCreateFramebuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>framebuffers</name></param>
#        </command>
#        
glCreateFramebuffers_impl=None
def glCreateFramebuffers (n, framebuffers):
    global glCreateFramebuffers_impl
    if not glCreateFramebuffers_impl:
        fptr = pyglGetFuncAddress('glCreateFramebuffers')
        if not fptr:
            raise RuntimeError('The function glCreateFramebuffers is not available')
        glCreateFramebuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glCreateFramebuffers = (lambda n,framebuffers:glCreateFramebuffers_impl(n,(c_uint8*len( framebuffers )).from_buffer( framebuffers )))
    return glCreateFramebuffers(n, framebuffers)
# <command>
#            <proto><ptype>GLuint</ptype> <name>glCreateProgram</name></proto>
#        </command>
#        
glCreateProgram_impl=None
def glCreateProgram ():
    global glCreateProgram_impl
    if not glCreateProgram_impl:
        fptr = pyglGetFuncAddress('glCreateProgram')
        if not fptr:
            raise RuntimeError('The function glCreateProgram is not available')
        glCreateProgram_impl = PYGL_FUNC_TYPE( c_uint ,)(fptr)
    glCreateProgram = glCreateProgram_impl
    return glCreateProgram()
# <command>
#            <proto>void <name>glCreateProgramPipelines</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>pipelines</name></param>
#        </command>
#        
glCreateProgramPipelines_impl=None
def glCreateProgramPipelines (n, pipelines):
    global glCreateProgramPipelines_impl
    if not glCreateProgramPipelines_impl:
        fptr = pyglGetFuncAddress('glCreateProgramPipelines')
        if not fptr:
            raise RuntimeError('The function glCreateProgramPipelines is not available')
        glCreateProgramPipelines_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glCreateProgramPipelines = (lambda n,pipelines:glCreateProgramPipelines_impl(n,(c_uint8*len( pipelines )).from_buffer( pipelines )))
    return glCreateProgramPipelines(n, pipelines)
# <command>
#            <proto>void <name>glCreateQueries</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>ids</name></param>
#        </command>
#        
glCreateQueries_impl=None
def glCreateQueries (target, n, ids):
    global glCreateQueries_impl
    if not glCreateQueries_impl:
        fptr = pyglGetFuncAddress('glCreateQueries')
        if not fptr:
            raise RuntimeError('The function glCreateQueries is not available')
        glCreateQueries_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glCreateQueries = (lambda target,n,ids:glCreateQueries_impl(target,n,(c_uint8*len( ids )).from_buffer( ids )))
    return glCreateQueries(target, n, ids)
# <command>
#            <proto>void <name>glCreateRenderbuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>renderbuffers</name></param>
#        </command>
#        
glCreateRenderbuffers_impl=None
def glCreateRenderbuffers (n, renderbuffers):
    global glCreateRenderbuffers_impl
    if not glCreateRenderbuffers_impl:
        fptr = pyglGetFuncAddress('glCreateRenderbuffers')
        if not fptr:
            raise RuntimeError('The function glCreateRenderbuffers is not available')
        glCreateRenderbuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glCreateRenderbuffers = (lambda n,renderbuffers:glCreateRenderbuffers_impl(n,(c_uint8*len( renderbuffers )).from_buffer( renderbuffers )))
    return glCreateRenderbuffers(n, renderbuffers)
# <command>
#            <proto>void <name>glCreateSamplers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>samplers</name></param>
#        </command>
#        
glCreateSamplers_impl=None
def glCreateSamplers (n, samplers):
    global glCreateSamplers_impl
    if not glCreateSamplers_impl:
        fptr = pyglGetFuncAddress('glCreateSamplers')
        if not fptr:
            raise RuntimeError('The function glCreateSamplers is not available')
        glCreateSamplers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glCreateSamplers = (lambda n,samplers:glCreateSamplers_impl(n,(c_uint8*len( samplers )).from_buffer( samplers )))
    return glCreateSamplers(n, samplers)
# <command>
#            <proto><ptype>GLuint</ptype> <name>glCreateShader</name></proto>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#        </command>
#        
glCreateShader_impl=None
def glCreateShader (type):
    global glCreateShader_impl
    if not glCreateShader_impl:
        fptr = pyglGetFuncAddress('glCreateShader')
        if not fptr:
            raise RuntimeError('The function glCreateShader is not available')
        glCreateShader_impl = PYGL_FUNC_TYPE( c_uint ,c_uint)(fptr)
    glCreateShader = glCreateShader_impl
    return glCreateShader(type)
# <command>
#            <proto><ptype>GLuint</ptype> <name>glCreateShaderProgramv</name></proto>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLchar</ptype> *const*<name>strings</name></param>
#        </command>
#        
glCreateShaderProgramv_impl=None
def glCreateShaderProgramv (type, count, strings):
    global glCreateShaderProgramv_impl
    if not glCreateShaderProgramv_impl:
        fptr = pyglGetFuncAddress('glCreateShaderProgramv')
        if not fptr:
            raise RuntimeError('The function glCreateShaderProgramv is not available')
        glCreateShaderProgramv_impl = PYGL_FUNC_TYPE( c_uint ,c_uint, c_int, c_void_p)(fptr)
    glCreateShaderProgramv = (lambda type,count,strings:glCreateShaderProgramv_impl(type,count,c_char_p( strings .encode() )))
    return glCreateShaderProgramv(type, count, strings)
# <command>
#            <proto>void <name>glCreateTextures</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>textures</name></param>
#        </command>
#        
glCreateTextures_impl=None
def glCreateTextures (target, n, textures):
    global glCreateTextures_impl
    if not glCreateTextures_impl:
        fptr = pyglGetFuncAddress('glCreateTextures')
        if not fptr:
            raise RuntimeError('The function glCreateTextures is not available')
        glCreateTextures_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glCreateTextures = (lambda target,n,textures:glCreateTextures_impl(target,n,(c_uint8*len( textures )).from_buffer( textures )))
    return glCreateTextures(target, n, textures)
# <command>
#            <proto>void <name>glCreateTransformFeedbacks</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>ids</name></param>
#        </command>
#        
glCreateTransformFeedbacks_impl=None
def glCreateTransformFeedbacks (n, ids):
    global glCreateTransformFeedbacks_impl
    if not glCreateTransformFeedbacks_impl:
        fptr = pyglGetFuncAddress('glCreateTransformFeedbacks')
        if not fptr:
            raise RuntimeError('The function glCreateTransformFeedbacks is not available')
        glCreateTransformFeedbacks_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glCreateTransformFeedbacks = (lambda n,ids:glCreateTransformFeedbacks_impl(n,(c_uint8*len( ids )).from_buffer( ids )))
    return glCreateTransformFeedbacks(n, ids)
# <command>
#            <proto>void <name>glCreateVertexArrays</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param><ptype>GLuint</ptype> *<name>arrays</name></param>
#        </command>
#        
glCreateVertexArrays_impl=None
def glCreateVertexArrays (n, arrays):
    global glCreateVertexArrays_impl
    if not glCreateVertexArrays_impl:
        fptr = pyglGetFuncAddress('glCreateVertexArrays')
        if not fptr:
            raise RuntimeError('The function glCreateVertexArrays is not available')
        glCreateVertexArrays_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glCreateVertexArrays = (lambda n,arrays:glCreateVertexArrays_impl(n,(c_uint8*len( arrays )).from_buffer( arrays )))
    return glCreateVertexArrays(n, arrays)
# <command>
#            <proto>void <name>glCullFace</name></proto>
#            <param group="CullFaceMode"><ptype>GLenum</ptype> <name>mode</name></param>
#            <glx opcode="79" type="render" />
#        </command>
#        
glCullFace_impl=None
def glCullFace (mode):
    global glCullFace_impl
    if not glCullFace_impl:
        fptr = pyglGetFuncAddress('glCullFace')
        if not fptr:
            raise RuntimeError('The function glCullFace is not available')
        glCullFace_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glCullFace = glCullFace_impl
    return glCullFace(mode)
# <command>
#            <proto>void <name>glDebugMessageControl</name></proto>
#            <param><ptype>GLenum</ptype> <name>source</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param><ptype>GLenum</ptype> <name>severity</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>ids</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>enabled</name></param>
#        </command>
#        
glDebugMessageControl_impl=None
def glDebugMessageControl (source, type, severity, count, ids, enabled):
    global glDebugMessageControl_impl
    if not glDebugMessageControl_impl:
        fptr = pyglGetFuncAddress('glDebugMessageControl')
        if not fptr:
            raise RuntimeError('The function glDebugMessageControl is not available')
        glDebugMessageControl_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_void_p, c_char)(fptr)
    glDebugMessageControl = (lambda source,type,severity,count,ids,enabled:glDebugMessageControl_impl(source,type,severity,count,pyglGetAsConstVoidPointer( ids ),enabled))
    return glDebugMessageControl(source, type, severity, count, ids, enabled)
# <command>
#            <proto>void <name>glDebugMessageInsert</name></proto>
#            <param><ptype>GLenum</ptype> <name>source</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLenum</ptype> <name>severity</name></param>
#            <param><ptype>GLsizei</ptype> <name>length</name></param>
#            <param len="COMPSIZE(buf,length)">const <ptype>GLchar</ptype> *<name>buf</name></param>
#        </command>
#        
glDebugMessageInsert_impl=None
def glDebugMessageInsert (source, type, id, severity, length, buf):
    global glDebugMessageInsert_impl
    if not glDebugMessageInsert_impl:
        fptr = pyglGetFuncAddress('glDebugMessageInsert')
        if not fptr:
            raise RuntimeError('The function glDebugMessageInsert is not available')
        glDebugMessageInsert_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_int, c_void_p)(fptr)
    glDebugMessageInsert = (lambda source,type,id,severity,length,buf:glDebugMessageInsert_impl(source,type,id,severity,length,c_char_p( buf .encode() )))
    return glDebugMessageInsert(source, type, id, severity, length, buf)
# <command>
#            <proto>void <name>glDeleteBuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n">const <ptype>GLuint</ptype> *<name>buffers</name></param>
#        </command>
#        
glDeleteBuffers_impl=None
def glDeleteBuffers (n, buffers):
    global glDeleteBuffers_impl
    if not glDeleteBuffers_impl:
        fptr = pyglGetFuncAddress('glDeleteBuffers')
        if not fptr:
            raise RuntimeError('The function glDeleteBuffers is not available')
        glDeleteBuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteBuffers = (lambda n,buffers:glDeleteBuffers_impl(n,pyglGetAsConstVoidPointer( buffers )))
    return glDeleteBuffers(n, buffers)
# <command>
#            <proto>void <name>glDeleteFramebuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n">const <ptype>GLuint</ptype> *<name>framebuffers</name></param>
#            <glx opcode="4320" type="render" />
#        </command>
#        
glDeleteFramebuffers_impl=None
def glDeleteFramebuffers (n, framebuffers):
    global glDeleteFramebuffers_impl
    if not glDeleteFramebuffers_impl:
        fptr = pyglGetFuncAddress('glDeleteFramebuffers')
        if not fptr:
            raise RuntimeError('The function glDeleteFramebuffers is not available')
        glDeleteFramebuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteFramebuffers = (lambda n,framebuffers:glDeleteFramebuffers_impl(n,pyglGetAsConstVoidPointer( framebuffers )))
    return glDeleteFramebuffers(n, framebuffers)
# <command>
#            <proto>void <name>glDeleteProgram</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <glx opcode="202" type="single" />
#        </command>
#        
glDeleteProgram_impl=None
def glDeleteProgram (program):
    global glDeleteProgram_impl
    if not glDeleteProgram_impl:
        fptr = pyglGetFuncAddress('glDeleteProgram')
        if not fptr:
            raise RuntimeError('The function glDeleteProgram is not available')
        glDeleteProgram_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glDeleteProgram = glDeleteProgram_impl
    return glDeleteProgram(program)
# <command>
#            <proto>void <name>glDeleteProgramPipelines</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n">const <ptype>GLuint</ptype> *<name>pipelines</name></param>
#        </command>
#        
glDeleteProgramPipelines_impl=None
def glDeleteProgramPipelines (n, pipelines):
    global glDeleteProgramPipelines_impl
    if not glDeleteProgramPipelines_impl:
        fptr = pyglGetFuncAddress('glDeleteProgramPipelines')
        if not fptr:
            raise RuntimeError('The function glDeleteProgramPipelines is not available')
        glDeleteProgramPipelines_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteProgramPipelines = (lambda n,pipelines:glDeleteProgramPipelines_impl(n,pyglGetAsConstVoidPointer( pipelines )))
    return glDeleteProgramPipelines(n, pipelines)
# <command>
#            <proto>void <name>glDeleteQueries</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n">const <ptype>GLuint</ptype> *<name>ids</name></param>
#            <glx opcode="161" type="single" />
#        </command>
#        
glDeleteQueries_impl=None
def glDeleteQueries (n, ids):
    global glDeleteQueries_impl
    if not glDeleteQueries_impl:
        fptr = pyglGetFuncAddress('glDeleteQueries')
        if not fptr:
            raise RuntimeError('The function glDeleteQueries is not available')
        glDeleteQueries_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteQueries = (lambda n,ids:glDeleteQueries_impl(n,pyglGetAsConstVoidPointer( ids )))
    return glDeleteQueries(n, ids)
# <command>
#            <proto>void <name>glDeleteRenderbuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n">const <ptype>GLuint</ptype> *<name>renderbuffers</name></param>
#            <glx opcode="4317" type="render" />
#        </command>
#        
glDeleteRenderbuffers_impl=None
def glDeleteRenderbuffers (n, renderbuffers):
    global glDeleteRenderbuffers_impl
    if not glDeleteRenderbuffers_impl:
        fptr = pyglGetFuncAddress('glDeleteRenderbuffers')
        if not fptr:
            raise RuntimeError('The function glDeleteRenderbuffers is not available')
        glDeleteRenderbuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteRenderbuffers = (lambda n,renderbuffers:glDeleteRenderbuffers_impl(n,pyglGetAsConstVoidPointer( renderbuffers )))
    return glDeleteRenderbuffers(n, renderbuffers)
# <command>
#            <proto>void <name>glDeleteSamplers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>samplers</name></param>
#        </command>
#        
glDeleteSamplers_impl=None
def glDeleteSamplers (count, samplers):
    global glDeleteSamplers_impl
    if not glDeleteSamplers_impl:
        fptr = pyglGetFuncAddress('glDeleteSamplers')
        if not fptr:
            raise RuntimeError('The function glDeleteSamplers is not available')
        glDeleteSamplers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteSamplers = (lambda count,samplers:glDeleteSamplers_impl(count,pyglGetAsConstVoidPointer( samplers )))
    return glDeleteSamplers(count, samplers)
# <command>
#            <proto>void <name>glDeleteShader</name></proto>
#            <param><ptype>GLuint</ptype> <name>shader</name></param>
#            <glx opcode="195" type="single" />
#        </command>
#        
glDeleteShader_impl=None
def glDeleteShader (shader):
    global glDeleteShader_impl
    if not glDeleteShader_impl:
        fptr = pyglGetFuncAddress('glDeleteShader')
        if not fptr:
            raise RuntimeError('The function glDeleteShader is not available')
        glDeleteShader_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glDeleteShader = glDeleteShader_impl
    return glDeleteShader(shader)
# <command>
#            <proto>void <name>glDeleteSync</name></proto>
#            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
#        </command>
#        
glDeleteSync_impl=None
def glDeleteSync (sync):
    global glDeleteSync_impl
    if not glDeleteSync_impl:
        fptr = pyglGetFuncAddress('glDeleteSync')
        if not fptr:
            raise RuntimeError('The function glDeleteSync is not available')
        glDeleteSync_impl = PYGL_FUNC_TYPE( None ,c_void_p)(fptr)
    glDeleteSync = glDeleteSync_impl
    return glDeleteSync(sync)
# <command>
#            <proto>void <name>glDeleteTextures</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param group="Texture" len="n">const <ptype>GLuint</ptype> *<name>textures</name></param>
#            <glx opcode="144" type="single" />
#        </command>
#        
glDeleteTextures_impl=None
def glDeleteTextures (n, textures):
    global glDeleteTextures_impl
    if not glDeleteTextures_impl:
        fptr = pyglGetFuncAddress('glDeleteTextures')
        if not fptr:
            raise RuntimeError('The function glDeleteTextures is not available')
        glDeleteTextures_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteTextures = (lambda n,textures:glDeleteTextures_impl(n,pyglGetAsConstVoidPointer( textures )))
    return glDeleteTextures(n, textures)
# <command>
#            <proto>void <name>glDeleteTransformFeedbacks</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n">const <ptype>GLuint</ptype> *<name>ids</name></param>
#        </command>
#        
glDeleteTransformFeedbacks_impl=None
def glDeleteTransformFeedbacks (n, ids):
    global glDeleteTransformFeedbacks_impl
    if not glDeleteTransformFeedbacks_impl:
        fptr = pyglGetFuncAddress('glDeleteTransformFeedbacks')
        if not fptr:
            raise RuntimeError('The function glDeleteTransformFeedbacks is not available')
        glDeleteTransformFeedbacks_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteTransformFeedbacks = (lambda n,ids:glDeleteTransformFeedbacks_impl(n,pyglGetAsConstVoidPointer( ids )))
    return glDeleteTransformFeedbacks(n, ids)
# <command>
#            <proto>void <name>glDeleteVertexArrays</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n">const <ptype>GLuint</ptype> *<name>arrays</name></param>
#            <glx opcode="351" type="render" />
#        </command>
#        
glDeleteVertexArrays_impl=None
def glDeleteVertexArrays (n, arrays):
    global glDeleteVertexArrays_impl
    if not glDeleteVertexArrays_impl:
        fptr = pyglGetFuncAddress('glDeleteVertexArrays')
        if not fptr:
            raise RuntimeError('The function glDeleteVertexArrays is not available')
        glDeleteVertexArrays_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDeleteVertexArrays = (lambda n,arrays:glDeleteVertexArrays_impl(n,pyglGetAsConstVoidPointer( arrays )))
    return glDeleteVertexArrays(n, arrays)
# <command>
#            <proto>void <name>glDepthFunc</name></proto>
#            <param group="DepthFunction"><ptype>GLenum</ptype> <name>func</name></param>
#            <glx opcode="164" type="render" />
#        </command>
#        
glDepthFunc_impl=None
def glDepthFunc (func):
    global glDepthFunc_impl
    if not glDepthFunc_impl:
        fptr = pyglGetFuncAddress('glDepthFunc')
        if not fptr:
            raise RuntimeError('The function glDepthFunc is not available')
        glDepthFunc_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glDepthFunc = glDepthFunc_impl
    return glDepthFunc(func)
# <command>
#            <proto>void <name>glDepthMask</name></proto>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>flag</name></param>
#            <glx opcode="135" type="render" />
#        </command>
#        
glDepthMask_impl=None
def glDepthMask (flag):
    global glDepthMask_impl
    if not glDepthMask_impl:
        fptr = pyglGetFuncAddress('glDepthMask')
        if not fptr:
            raise RuntimeError('The function glDepthMask is not available')
        glDepthMask_impl = PYGL_FUNC_TYPE( None ,c_char)(fptr)
    glDepthMask = glDepthMask_impl
    return glDepthMask(flag)
# <command>
#            <proto>void <name>glDepthRange</name></proto>
#            <param><ptype>GLdouble</ptype> <name>near</name></param>
#            <param><ptype>GLdouble</ptype> <name>far</name></param>
#            <glx opcode="174" type="render" />
#        </command>
#        
glDepthRange_impl=None
def glDepthRange (near, far):
    global glDepthRange_impl
    if not glDepthRange_impl:
        fptr = pyglGetFuncAddress('glDepthRange')
        if not fptr:
            raise RuntimeError('The function glDepthRange is not available')
        glDepthRange_impl = PYGL_FUNC_TYPE( None ,c_double, c_double)(fptr)
    glDepthRange = glDepthRange_impl
    return glDepthRange(near, far)
# <command>
#            <proto>void <name>glDepthRangeArrayv</name></proto>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="COMPSIZE(count)">const <ptype>GLdouble</ptype> *<name>v</name></param>
#        </command>
#        
glDepthRangeArrayv_impl=None
def glDepthRangeArrayv (first, count, v):
    global glDepthRangeArrayv_impl
    if not glDepthRangeArrayv_impl:
        fptr = pyglGetFuncAddress('glDepthRangeArrayv')
        if not fptr:
            raise RuntimeError('The function glDepthRangeArrayv is not available')
        glDepthRangeArrayv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glDepthRangeArrayv = (lambda first,count,v:glDepthRangeArrayv_impl(first,count,pyglGetAsConstVoidPointer( v )))
    return glDepthRangeArrayv(first, count, v)
# <command>
#            <proto>void <name>glDepthRangeIndexed</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>n</name></param>
#            <param><ptype>GLdouble</ptype> <name>f</name></param>
#        </command>
#        
glDepthRangeIndexed_impl=None
def glDepthRangeIndexed (index, n, f):
    global glDepthRangeIndexed_impl
    if not glDepthRangeIndexed_impl:
        fptr = pyglGetFuncAddress('glDepthRangeIndexed')
        if not fptr:
            raise RuntimeError('The function glDepthRangeIndexed is not available')
        glDepthRangeIndexed_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double, c_double)(fptr)
    glDepthRangeIndexed = glDepthRangeIndexed_impl
    return glDepthRangeIndexed(index, n, f)
# <command>
#            <proto>void <name>glDepthRangef</name></proto>
#            <param><ptype>GLfloat</ptype> <name>n</name></param>
#            <param><ptype>GLfloat</ptype> <name>f</name></param>
#        </command>
#        
glDepthRangef_impl=None
def glDepthRangef (n, f):
    global glDepthRangef_impl
    if not glDepthRangef_impl:
        fptr = pyglGetFuncAddress('glDepthRangef')
        if not fptr:
            raise RuntimeError('The function glDepthRangef is not available')
        glDepthRangef_impl = PYGL_FUNC_TYPE( None ,c_float, c_float)(fptr)
    glDepthRangef = glDepthRangef_impl
    return glDepthRangef(n, f)
# <command>
#            <proto>void <name>glDetachShader</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>shader</name></param>
#        </command>
#        
glDetachShader_impl=None
def glDetachShader (program, shader):
    global glDetachShader_impl
    if not glDetachShader_impl:
        fptr = pyglGetFuncAddress('glDetachShader')
        if not fptr:
            raise RuntimeError('The function glDetachShader is not available')
        glDetachShader_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glDetachShader = glDetachShader_impl
    return glDetachShader(program, shader)
# <command>
#            <proto>void <name>glDisable</name></proto>
#            <param group="EnableCap"><ptype>GLenum</ptype> <name>cap</name></param>
#            <glx opcode="138" type="render" />
#        </command>
#        
glDisable_impl=None
def glDisable (cap):
    global glDisable_impl
    if not glDisable_impl:
        fptr = pyglGetFuncAddress('glDisable')
        if not fptr:
            raise RuntimeError('The function glDisable is not available')
        glDisable_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glDisable = glDisable_impl
    return glDisable(cap)
# <command>
#            <proto>void <name>glDisableVertexArrayAttrib</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glDisableVertexArrayAttrib_impl=None
def glDisableVertexArrayAttrib (vaobj, index):
    global glDisableVertexArrayAttrib_impl
    if not glDisableVertexArrayAttrib_impl:
        fptr = pyglGetFuncAddress('glDisableVertexArrayAttrib')
        if not fptr:
            raise RuntimeError('The function glDisableVertexArrayAttrib is not available')
        glDisableVertexArrayAttrib_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glDisableVertexArrayAttrib = glDisableVertexArrayAttrib_impl
    return glDisableVertexArrayAttrib(vaobj, index)
# <command>
#            <proto>void <name>glDisableVertexAttribArray</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glDisableVertexAttribArray_impl=None
def glDisableVertexAttribArray (index):
    global glDisableVertexAttribArray_impl
    if not glDisableVertexAttribArray_impl:
        fptr = pyglGetFuncAddress('glDisableVertexAttribArray')
        if not fptr:
            raise RuntimeError('The function glDisableVertexAttribArray is not available')
        glDisableVertexAttribArray_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glDisableVertexAttribArray = glDisableVertexAttribArray_impl
    return glDisableVertexAttribArray(index)
# <command>
#            <proto>void <name>glDisablei</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glDisablei_impl=None
def glDisablei (target, index):
    global glDisablei_impl
    if not glDisablei_impl:
        fptr = pyglGetFuncAddress('glDisablei')
        if not fptr:
            raise RuntimeError('The function glDisablei is not available')
        glDisablei_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glDisablei = glDisablei_impl
    return glDisablei(target, index)
# <command>
#            <proto>void <name>glDispatchCompute</name></proto>
#            <param><ptype>GLuint</ptype> <name>num_groups_x</name></param>
#            <param><ptype>GLuint</ptype> <name>num_groups_y</name></param>
#            <param><ptype>GLuint</ptype> <name>num_groups_z</name></param>
#        </command>
#        
glDispatchCompute_impl=None
def glDispatchCompute (num_groups_x, num_groups_y, num_groups_z):
    global glDispatchCompute_impl
    if not glDispatchCompute_impl:
        fptr = pyglGetFuncAddress('glDispatchCompute')
        if not fptr:
            raise RuntimeError('The function glDispatchCompute is not available')
        glDispatchCompute_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glDispatchCompute = glDispatchCompute_impl
    return glDispatchCompute(num_groups_x, num_groups_y, num_groups_z)
# <command>
#            <proto>void <name>glDispatchComputeIndirect</name></proto>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>indirect</name></param>
#        </command>
#        
glDispatchComputeIndirect_impl=None
def glDispatchComputeIndirect (indirect):
    global glDispatchComputeIndirect_impl
    if not glDispatchComputeIndirect_impl:
        fptr = pyglGetFuncAddress('glDispatchComputeIndirect')
        if not fptr:
            raise RuntimeError('The function glDispatchComputeIndirect is not available')
        glDispatchComputeIndirect_impl = PYGL_FUNC_TYPE( None ,c_size_t)(fptr)
    glDispatchComputeIndirect = glDispatchComputeIndirect_impl
    return glDispatchComputeIndirect(indirect)
# <command>
#            <proto>void <name>glDrawArrays</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <glx opcode="193" type="render" />
#        </command>
#        
glDrawArrays_impl=None
def glDrawArrays (mode, first, count):
    global glDrawArrays_impl
    if not glDrawArrays_impl:
        fptr = pyglGetFuncAddress('glDrawArrays')
        if not fptr:
            raise RuntimeError('The function glDrawArrays is not available')
        glDrawArrays_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int)(fptr)
    glDrawArrays = glDrawArrays_impl
    return glDrawArrays(mode, first, count)
# <command>
#            <proto>void <name>glDrawArraysIndirect</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param>const void *<name>indirect</name></param>
#        </command>
#        
glDrawArraysIndirect_impl=None
def glDrawArraysIndirect (mode, indirect):
    global glDrawArraysIndirect_impl
    if not glDrawArraysIndirect_impl:
        fptr = pyglGetFuncAddress('glDrawArraysIndirect')
        if not fptr:
            raise RuntimeError('The function glDrawArraysIndirect is not available')
        glDrawArraysIndirect_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glDrawArraysIndirect = (lambda mode,indirect:glDrawArraysIndirect_impl(mode,pyglGetAsConstVoidPointer( indirect )))
    return glDrawArraysIndirect(mode, indirect)
# <command>
#            <proto>void <name>glDrawArraysInstanced</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
#        </command>
#        
glDrawArraysInstanced_impl=None
def glDrawArraysInstanced (mode, first, count, instancecount):
    global glDrawArraysInstanced_impl
    if not glDrawArraysInstanced_impl:
        fptr = pyglGetFuncAddress('glDrawArraysInstanced')
        if not fptr:
            raise RuntimeError('The function glDrawArraysInstanced is not available')
        glDrawArraysInstanced_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int)(fptr)
    glDrawArraysInstanced = glDrawArraysInstanced_impl
    return glDrawArraysInstanced(mode, first, count, instancecount)
# <command>
#            <proto>void <name>glDrawArraysInstancedBaseInstance</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
#            <param><ptype>GLuint</ptype> <name>baseinstance</name></param>
#        </command>
#        
glDrawArraysInstancedBaseInstance_impl=None
def glDrawArraysInstancedBaseInstance (mode, first, count, instancecount, baseinstance):
    global glDrawArraysInstancedBaseInstance_impl
    if not glDrawArraysInstancedBaseInstance_impl:
        fptr = pyglGetFuncAddress('glDrawArraysInstancedBaseInstance')
        if not fptr:
            raise RuntimeError('The function glDrawArraysInstancedBaseInstance is not available')
        glDrawArraysInstancedBaseInstance_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_uint)(fptr)
    glDrawArraysInstancedBaseInstance = glDrawArraysInstancedBaseInstance_impl
    return glDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance)
# <command>
#            <proto>void <name>glDrawBuffer</name></proto>
#            <param group="DrawBufferMode"><ptype>GLenum</ptype> <name>buf</name></param>
#            <glx opcode="126" type="render" />
#        </command>
#        
glDrawBuffer_impl=None
def glDrawBuffer (buf):
    global glDrawBuffer_impl
    if not glDrawBuffer_impl:
        fptr = pyglGetFuncAddress('glDrawBuffer')
        if not fptr:
            raise RuntimeError('The function glDrawBuffer is not available')
        glDrawBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glDrawBuffer = glDrawBuffer_impl
    return glDrawBuffer(buf)
# <command>
#            <proto>void <name>glDrawBuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param group="DrawBufferModeATI" len="n">const <ptype>GLenum</ptype> *<name>bufs</name></param>
#            <glx opcode="233" type="render" />
#        </command>
#        
glDrawBuffers_impl=None
def glDrawBuffers (n, bufs):
    global glDrawBuffers_impl
    if not glDrawBuffers_impl:
        fptr = pyglGetFuncAddress('glDrawBuffers')
        if not fptr:
            raise RuntimeError('The function glDrawBuffers is not available')
        glDrawBuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glDrawBuffers = (lambda n,bufs:glDrawBuffers_impl(n,pyglGetAsConstVoidPointer( bufs )))
    return glDrawBuffers(n, bufs)
# <command>
#            <proto>void <name>glDrawElements</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
#        </command>
#        
glDrawElements_impl=None
def glDrawElements (mode, count, type, indices):
    global glDrawElements_impl
    if not glDrawElements_impl:
        fptr = pyglGetFuncAddress('glDrawElements')
        if not fptr:
            raise RuntimeError('The function glDrawElements is not available')
        glDrawElements_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p)(fptr)
    glDrawElements = glDrawElements_impl
    return glDrawElements(mode, count, type, indices)
# <command>
#            <proto>void <name>glDrawElementsBaseVertex</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
#            <param><ptype>GLint</ptype> <name>basevertex</name></param>
#        </command>
#        
glDrawElementsBaseVertex_impl=None
def glDrawElementsBaseVertex (mode, count, type, indices, basevertex):
    global glDrawElementsBaseVertex_impl
    if not glDrawElementsBaseVertex_impl:
        fptr = pyglGetFuncAddress('glDrawElementsBaseVertex')
        if not fptr:
            raise RuntimeError('The function glDrawElementsBaseVertex is not available')
        glDrawElementsBaseVertex_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p, c_int)(fptr)
    glDrawElementsBaseVertex = (lambda mode,count,type,indices,basevertex:glDrawElementsBaseVertex_impl(mode,count,type,pyglGetAsConstVoidPointer( indices ),basevertex))
    return glDrawElementsBaseVertex(mode, count, type, indices, basevertex)
# <command>
#            <proto>void <name>glDrawElementsIndirect</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param>const void *<name>indirect</name></param>
#        </command>
#        
glDrawElementsIndirect_impl=None
def glDrawElementsIndirect (mode, type, indirect):
    global glDrawElementsIndirect_impl
    if not glDrawElementsIndirect_impl:
        fptr = pyglGetFuncAddress('glDrawElementsIndirect')
        if not fptr:
            raise RuntimeError('The function glDrawElementsIndirect is not available')
        glDrawElementsIndirect_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glDrawElementsIndirect = (lambda mode,type,indirect:glDrawElementsIndirect_impl(mode,type,pyglGetAsConstVoidPointer( indirect )))
    return glDrawElementsIndirect(mode, type, indirect)
# <command>
#            <proto>void <name>glDrawElementsInstanced</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
#            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
#        </command>
#        
glDrawElementsInstanced_impl=None
def glDrawElementsInstanced (mode, count, type, indices, instancecount):
    global glDrawElementsInstanced_impl
    if not glDrawElementsInstanced_impl:
        fptr = pyglGetFuncAddress('glDrawElementsInstanced')
        if not fptr:
            raise RuntimeError('The function glDrawElementsInstanced is not available')
        glDrawElementsInstanced_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p, c_int)(fptr)
    glDrawElementsInstanced = (lambda mode,count,type,indices,instancecount:glDrawElementsInstanced_impl(mode,count,type,pyglGetAsConstVoidPointer( indices ),instancecount))
    return glDrawElementsInstanced(mode, count, type, indices, instancecount)
# <command>
#            <proto>void <name>glDrawElementsInstancedBaseInstance</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="count">const void *<name>indices</name></param>
#            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
#            <param><ptype>GLuint</ptype> <name>baseinstance</name></param>
#        </command>
#        
glDrawElementsInstancedBaseInstance_impl=None
def glDrawElementsInstancedBaseInstance (mode, count, type, indices, instancecount, baseinstance):
    global glDrawElementsInstancedBaseInstance_impl
    if not glDrawElementsInstancedBaseInstance_impl:
        fptr = pyglGetFuncAddress('glDrawElementsInstancedBaseInstance')
        if not fptr:
            raise RuntimeError('The function glDrawElementsInstancedBaseInstance is not available')
        glDrawElementsInstancedBaseInstance_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p, c_int, c_uint)(fptr)
    glDrawElementsInstancedBaseInstance = (lambda mode,count,type,indices,instancecount,baseinstance:glDrawElementsInstancedBaseInstance_impl(mode,count,type,pyglGetAsConstVoidPointer( indices ),instancecount,baseinstance))
    return glDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance)
# <command>
#            <proto>void <name>glDrawElementsInstancedBaseVertex</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
#            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
#            <param><ptype>GLint</ptype> <name>basevertex</name></param>
#        </command>
#        
glDrawElementsInstancedBaseVertex_impl=None
def glDrawElementsInstancedBaseVertex (mode, count, type, indices, instancecount, basevertex):
    global glDrawElementsInstancedBaseVertex_impl
    if not glDrawElementsInstancedBaseVertex_impl:
        fptr = pyglGetFuncAddress('glDrawElementsInstancedBaseVertex')
        if not fptr:
            raise RuntimeError('The function glDrawElementsInstancedBaseVertex is not available')
        glDrawElementsInstancedBaseVertex_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p, c_int, c_int)(fptr)
    glDrawElementsInstancedBaseVertex = (lambda mode,count,type,indices,instancecount,basevertex:glDrawElementsInstancedBaseVertex_impl(mode,count,type,pyglGetAsConstVoidPointer( indices ),instancecount,basevertex))
    return glDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex)
# <command>
#            <proto>void <name>glDrawElementsInstancedBaseVertexBaseInstance</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="count">const void *<name>indices</name></param>
#            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
#            <param><ptype>GLint</ptype> <name>basevertex</name></param>
#            <param><ptype>GLuint</ptype> <name>baseinstance</name></param>
#        </command>
#        
glDrawElementsInstancedBaseVertexBaseInstance_impl=None
def glDrawElementsInstancedBaseVertexBaseInstance (mode, count, type, indices, instancecount, basevertex, baseinstance):
    global glDrawElementsInstancedBaseVertexBaseInstance_impl
    if not glDrawElementsInstancedBaseVertexBaseInstance_impl:
        fptr = pyglGetFuncAddress('glDrawElementsInstancedBaseVertexBaseInstance')
        if not fptr:
            raise RuntimeError('The function glDrawElementsInstancedBaseVertexBaseInstance is not available')
        glDrawElementsInstancedBaseVertexBaseInstance_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p, c_int, c_int, c_uint)(fptr)
    glDrawElementsInstancedBaseVertexBaseInstance = (lambda mode,count,type,indices,instancecount,basevertex,baseinstance:glDrawElementsInstancedBaseVertexBaseInstance_impl(mode,count,type,pyglGetAsConstVoidPointer( indices ),instancecount,basevertex,baseinstance))
    return glDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance)
# <command>
#            <proto>void <name>glDrawRangeElements</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLuint</ptype> <name>start</name></param>
#            <param><ptype>GLuint</ptype> <name>end</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
#        </command>
#        
glDrawRangeElements_impl=None
def glDrawRangeElements (mode, start, end, count, type, indices):
    global glDrawRangeElements_impl
    if not glDrawRangeElements_impl:
        fptr = pyglGetFuncAddress('glDrawRangeElements')
        if not fptr:
            raise RuntimeError('The function glDrawRangeElements is not available')
        glDrawRangeElements_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_uint, c_void_p)(fptr)
    glDrawRangeElements = (lambda mode,start,end,count,type,indices:glDrawRangeElements_impl(mode,start,end,count,type,pyglGetAsConstVoidPointer( indices )))
    return glDrawRangeElements(mode, start, end, count, type, indices)
# <command>
#            <proto>void <name>glDrawRangeElementsBaseVertex</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLuint</ptype> <name>start</name></param>
#            <param><ptype>GLuint</ptype> <name>end</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
#            <param><ptype>GLint</ptype> <name>basevertex</name></param>
#        </command>
#        
glDrawRangeElementsBaseVertex_impl=None
def glDrawRangeElementsBaseVertex (mode, start, end, count, type, indices, basevertex):
    global glDrawRangeElementsBaseVertex_impl
    if not glDrawRangeElementsBaseVertex_impl:
        fptr = pyglGetFuncAddress('glDrawRangeElementsBaseVertex')
        if not fptr:
            raise RuntimeError('The function glDrawRangeElementsBaseVertex is not available')
        glDrawRangeElementsBaseVertex_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_uint, c_void_p, c_int)(fptr)
    glDrawRangeElementsBaseVertex = (lambda mode,start,end,count,type,indices,basevertex:glDrawRangeElementsBaseVertex_impl(mode,start,end,count,type,pyglGetAsConstVoidPointer( indices ),basevertex))
    return glDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex)
# <command>
#            <proto>void <name>glDrawTransformFeedback</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#        </command>
#        
glDrawTransformFeedback_impl=None
def glDrawTransformFeedback (mode, id):
    global glDrawTransformFeedback_impl
    if not glDrawTransformFeedback_impl:
        fptr = pyglGetFuncAddress('glDrawTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glDrawTransformFeedback is not available')
        glDrawTransformFeedback_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glDrawTransformFeedback = glDrawTransformFeedback_impl
    return glDrawTransformFeedback(mode, id)
# <command>
#            <proto>void <name>glDrawTransformFeedbackInstanced</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
#        </command>
#        
glDrawTransformFeedbackInstanced_impl=None
def glDrawTransformFeedbackInstanced (mode, id, instancecount):
    global glDrawTransformFeedbackInstanced_impl
    if not glDrawTransformFeedbackInstanced_impl:
        fptr = pyglGetFuncAddress('glDrawTransformFeedbackInstanced')
        if not fptr:
            raise RuntimeError('The function glDrawTransformFeedbackInstanced is not available')
        glDrawTransformFeedbackInstanced_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int)(fptr)
    glDrawTransformFeedbackInstanced = glDrawTransformFeedbackInstanced_impl
    return glDrawTransformFeedbackInstanced(mode, id, instancecount)
# <command>
#            <proto>void <name>glDrawTransformFeedbackStream</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLuint</ptype> <name>stream</name></param>
#        </command>
#        
glDrawTransformFeedbackStream_impl=None
def glDrawTransformFeedbackStream (mode, id, stream):
    global glDrawTransformFeedbackStream_impl
    if not glDrawTransformFeedbackStream_impl:
        fptr = pyglGetFuncAddress('glDrawTransformFeedbackStream')
        if not fptr:
            raise RuntimeError('The function glDrawTransformFeedbackStream is not available')
        glDrawTransformFeedbackStream_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glDrawTransformFeedbackStream = glDrawTransformFeedbackStream_impl
    return glDrawTransformFeedbackStream(mode, id, stream)
# <command>
#            <proto>void <name>glDrawTransformFeedbackStreamInstanced</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLuint</ptype> <name>stream</name></param>
#            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
#        </command>
#        
glDrawTransformFeedbackStreamInstanced_impl=None
def glDrawTransformFeedbackStreamInstanced (mode, id, stream, instancecount):
    global glDrawTransformFeedbackStreamInstanced_impl
    if not glDrawTransformFeedbackStreamInstanced_impl:
        fptr = pyglGetFuncAddress('glDrawTransformFeedbackStreamInstanced')
        if not fptr:
            raise RuntimeError('The function glDrawTransformFeedbackStreamInstanced is not available')
        glDrawTransformFeedbackStreamInstanced_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int)(fptr)
    glDrawTransformFeedbackStreamInstanced = glDrawTransformFeedbackStreamInstanced_impl
    return glDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount)
# <command>
#            <proto>void <name>glEnable</name></proto>
#            <param group="EnableCap"><ptype>GLenum</ptype> <name>cap</name></param>
#            <glx opcode="139" type="render" />
#        </command>
#        
glEnable_impl=None
def glEnable (cap):
    global glEnable_impl
    if not glEnable_impl:
        fptr = pyglGetFuncAddress('glEnable')
        if not fptr:
            raise RuntimeError('The function glEnable is not available')
        glEnable_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glEnable = glEnable_impl
    return glEnable(cap)
# <command>
#            <proto>void <name>glEnableVertexArrayAttrib</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glEnableVertexArrayAttrib_impl=None
def glEnableVertexArrayAttrib (vaobj, index):
    global glEnableVertexArrayAttrib_impl
    if not glEnableVertexArrayAttrib_impl:
        fptr = pyglGetFuncAddress('glEnableVertexArrayAttrib')
        if not fptr:
            raise RuntimeError('The function glEnableVertexArrayAttrib is not available')
        glEnableVertexArrayAttrib_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glEnableVertexArrayAttrib = glEnableVertexArrayAttrib_impl
    return glEnableVertexArrayAttrib(vaobj, index)
# <command>
#            <proto>void <name>glEnableVertexAttribArray</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glEnableVertexAttribArray_impl=None
def glEnableVertexAttribArray (index):
    global glEnableVertexAttribArray_impl
    if not glEnableVertexAttribArray_impl:
        fptr = pyglGetFuncAddress('glEnableVertexAttribArray')
        if not fptr:
            raise RuntimeError('The function glEnableVertexAttribArray is not available')
        glEnableVertexAttribArray_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glEnableVertexAttribArray = glEnableVertexAttribArray_impl
    return glEnableVertexAttribArray(index)
# <command>
#            <proto>void <name>glEnablei</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glEnablei_impl=None
def glEnablei (target, index):
    global glEnablei_impl
    if not glEnablei_impl:
        fptr = pyglGetFuncAddress('glEnablei')
        if not fptr:
            raise RuntimeError('The function glEnablei is not available')
        glEnablei_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glEnablei = glEnablei_impl
    return glEnablei(target, index)
# <command>
#            <proto>void <name>glEndConditionalRender</name></proto>
#            <glx opcode="349" type="render" />
#        </command>
#        
glEndConditionalRender_impl=None
def glEndConditionalRender ():
    global glEndConditionalRender_impl
    if not glEndConditionalRender_impl:
        fptr = pyglGetFuncAddress('glEndConditionalRender')
        if not fptr:
            raise RuntimeError('The function glEndConditionalRender is not available')
        glEndConditionalRender_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glEndConditionalRender = glEndConditionalRender_impl
    return glEndConditionalRender()
# <command>
#            <proto>void <name>glEndQuery</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <glx opcode="232" type="render" />
#        </command>
#        
glEndQuery_impl=None
def glEndQuery (target):
    global glEndQuery_impl
    if not glEndQuery_impl:
        fptr = pyglGetFuncAddress('glEndQuery')
        if not fptr:
            raise RuntimeError('The function glEndQuery is not available')
        glEndQuery_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glEndQuery = glEndQuery_impl
    return glEndQuery(target)
# <command>
#            <proto>void <name>glEndQueryIndexed</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glEndQueryIndexed_impl=None
def glEndQueryIndexed (target, index):
    global glEndQueryIndexed_impl
    if not glEndQueryIndexed_impl:
        fptr = pyglGetFuncAddress('glEndQueryIndexed')
        if not fptr:
            raise RuntimeError('The function glEndQueryIndexed is not available')
        glEndQueryIndexed_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glEndQueryIndexed = glEndQueryIndexed_impl
    return glEndQueryIndexed(target, index)
# <command>
#            <proto>void <name>glEndTransformFeedback</name></proto>
#        </command>
#        
glEndTransformFeedback_impl=None
def glEndTransformFeedback ():
    global glEndTransformFeedback_impl
    if not glEndTransformFeedback_impl:
        fptr = pyglGetFuncAddress('glEndTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glEndTransformFeedback is not available')
        glEndTransformFeedback_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glEndTransformFeedback = glEndTransformFeedback_impl
    return glEndTransformFeedback()
# <command>
#            <proto group="sync"><ptype>GLsync</ptype> <name>glFenceSync</name></proto>
#            <param><ptype>GLenum</ptype> <name>condition</name></param>
#            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
#        </command>
#        
glFenceSync_impl=None
def glFenceSync (condition, flags):
    global glFenceSync_impl
    if not glFenceSync_impl:
        fptr = pyglGetFuncAddress('glFenceSync')
        if not fptr:
            raise RuntimeError('The function glFenceSync is not available')
        glFenceSync_impl = PYGL_FUNC_TYPE( c_void_p ,c_uint, c_uint)(fptr)
    glFenceSync = glFenceSync_impl
    return glFenceSync(condition, flags)
# <command>
#            <proto>void <name>glFinish</name></proto>
#            <glx opcode="108" type="single" />
#        </command>
#        
glFinish_impl=None
def glFinish ():
    global glFinish_impl
    if not glFinish_impl:
        fptr = pyglGetFuncAddress('glFinish')
        if not fptr:
            raise RuntimeError('The function glFinish is not available')
        glFinish_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glFinish = glFinish_impl
    return glFinish()
# <command>
#            <proto>void <name>glFlush</name></proto>
#            <glx opcode="142" type="single" />
#        </command>
#        
glFlush_impl=None
def glFlush ():
    global glFlush_impl
    if not glFlush_impl:
        fptr = pyglGetFuncAddress('glFlush')
        if not fptr:
            raise RuntimeError('The function glFlush is not available')
        glFlush_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glFlush = glFlush_impl
    return glFlush()
# <command>
#            <proto>void <name>glFlushMappedBufferRange</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
#        </command>
#        
glFlushMappedBufferRange_impl=None
def glFlushMappedBufferRange (target, offset, length):
    global glFlushMappedBufferRange_impl
    if not glFlushMappedBufferRange_impl:
        fptr = pyglGetFuncAddress('glFlushMappedBufferRange')
        if not fptr:
            raise RuntimeError('The function glFlushMappedBufferRange is not available')
        glFlushMappedBufferRange_impl = PYGL_FUNC_TYPE( None ,c_uint, c_size_t, c_void_p)(fptr)
    glFlushMappedBufferRange = glFlushMappedBufferRange_impl
    return glFlushMappedBufferRange(target, offset, length)
# <command>
#            <proto>void <name>glFlushMappedNamedBufferRange</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
#        </command>
#        
glFlushMappedNamedBufferRange_impl=None
def glFlushMappedNamedBufferRange (buffer, offset, length):
    global glFlushMappedNamedBufferRange_impl
    if not glFlushMappedNamedBufferRange_impl:
        fptr = pyglGetFuncAddress('glFlushMappedNamedBufferRange')
        if not fptr:
            raise RuntimeError('The function glFlushMappedNamedBufferRange is not available')
        glFlushMappedNamedBufferRange_impl = PYGL_FUNC_TYPE( None ,c_uint, c_size_t, c_void_p)(fptr)
    glFlushMappedNamedBufferRange = glFlushMappedNamedBufferRange_impl
    return glFlushMappedNamedBufferRange(buffer, offset, length)
# <command>
#            <proto>void <name>glFramebufferParameteri</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> <name>param</name></param>
#        </command>
#        
glFramebufferParameteri_impl=None
def glFramebufferParameteri (target, pname, param):
    global glFramebufferParameteri_impl
    if not glFramebufferParameteri_impl:
        fptr = pyglGetFuncAddress('glFramebufferParameteri')
        if not fptr:
            raise RuntimeError('The function glFramebufferParameteri is not available')
        glFramebufferParameteri_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int)(fptr)
    glFramebufferParameteri = glFramebufferParameteri_impl
    return glFramebufferParameteri(target, pname, param)
# <command>
#            <proto>void <name>glFramebufferRenderbuffer</name></proto>
#            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param group="RenderbufferTarget"><ptype>GLenum</ptype> <name>renderbuffertarget</name></param>
#            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
#            <glx opcode="4324" type="render" />
#        </command>
#        
glFramebufferRenderbuffer_impl=None
def glFramebufferRenderbuffer (target, attachment, renderbuffertarget, renderbuffer):
    global glFramebufferRenderbuffer_impl
    if not glFramebufferRenderbuffer_impl:
        fptr = pyglGetFuncAddress('glFramebufferRenderbuffer')
        if not fptr:
            raise RuntimeError('The function glFramebufferRenderbuffer is not available')
        glFramebufferRenderbuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint)(fptr)
    glFramebufferRenderbuffer = glFramebufferRenderbuffer_impl
    return glFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)
# <command>
#            <proto>void <name>glFramebufferTexture</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#        </command>
#        
glFramebufferTexture_impl=None
def glFramebufferTexture (target, attachment, texture, level):
    global glFramebufferTexture_impl
    if not glFramebufferTexture_impl:
        fptr = pyglGetFuncAddress('glFramebufferTexture')
        if not fptr:
            raise RuntimeError('The function glFramebufferTexture is not available')
        glFramebufferTexture_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int)(fptr)
    glFramebufferTexture = glFramebufferTexture_impl
    return glFramebufferTexture(target, attachment, texture, level)
# <command>
#            <proto>void <name>glFramebufferTexture1D</name></proto>
#            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLenum</ptype> <name>textarget</name></param>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <glx opcode="4321" type="render" />
#        </command>
#        
glFramebufferTexture1D_impl=None
def glFramebufferTexture1D (target, attachment, textarget, texture, level):
    global glFramebufferTexture1D_impl
    if not glFramebufferTexture1D_impl:
        fptr = pyglGetFuncAddress('glFramebufferTexture1D')
        if not fptr:
            raise RuntimeError('The function glFramebufferTexture1D is not available')
        glFramebufferTexture1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_int)(fptr)
    glFramebufferTexture1D = glFramebufferTexture1D_impl
    return glFramebufferTexture1D(target, attachment, textarget, texture, level)
# <command>
#            <proto>void <name>glFramebufferTexture2D</name></proto>
#            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLenum</ptype> <name>textarget</name></param>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <glx opcode="4322" type="render" />
#        </command>
#        
glFramebufferTexture2D_impl=None
def glFramebufferTexture2D (target, attachment, textarget, texture, level):
    global glFramebufferTexture2D_impl
    if not glFramebufferTexture2D_impl:
        fptr = pyglGetFuncAddress('glFramebufferTexture2D')
        if not fptr:
            raise RuntimeError('The function glFramebufferTexture2D is not available')
        glFramebufferTexture2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_int)(fptr)
    glFramebufferTexture2D = glFramebufferTexture2D_impl
    return glFramebufferTexture2D(target, attachment, textarget, texture, level)
# <command>
#            <proto>void <name>glFramebufferTexture3D</name></proto>
#            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLenum</ptype> <name>textarget</name></param>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>zoffset</name></param>
#            <glx opcode="4323" type="render" />
#        </command>
#        
glFramebufferTexture3D_impl=None
def glFramebufferTexture3D (target, attachment, textarget, texture, level, zoffset):
    global glFramebufferTexture3D_impl
    if not glFramebufferTexture3D_impl:
        fptr = pyglGetFuncAddress('glFramebufferTexture3D')
        if not fptr:
            raise RuntimeError('The function glFramebufferTexture3D is not available')
        glFramebufferTexture3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_int, c_int)(fptr)
    glFramebufferTexture3D = glFramebufferTexture3D_impl
    return glFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset)
# <command>
#            <proto>void <name>glFramebufferTextureLayer</name></proto>
#            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param group="Texture"><ptype>GLuint</ptype> <name>texture</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>layer</name></param>
#            <glx opcode="237" type="render" />
#        </command>
#        
glFramebufferTextureLayer_impl=None
def glFramebufferTextureLayer (target, attachment, texture, level, layer):
    global glFramebufferTextureLayer_impl
    if not glFramebufferTextureLayer_impl:
        fptr = pyglGetFuncAddress('glFramebufferTextureLayer')
        if not fptr:
            raise RuntimeError('The function glFramebufferTextureLayer is not available')
        glFramebufferTextureLayer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_int)(fptr)
    glFramebufferTextureLayer = glFramebufferTextureLayer_impl
    return glFramebufferTextureLayer(target, attachment, texture, level, layer)
# <command>
#            <proto>void <name>glFrontFace</name></proto>
#            <param group="FrontFaceDirection"><ptype>GLenum</ptype> <name>mode</name></param>
#            <glx opcode="84" type="render" />
#        </command>
#        
glFrontFace_impl=None
def glFrontFace (mode):
    global glFrontFace_impl
    if not glFrontFace_impl:
        fptr = pyglGetFuncAddress('glFrontFace')
        if not fptr:
            raise RuntimeError('The function glFrontFace is not available')
        glFrontFace_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glFrontFace = glFrontFace_impl
    return glFrontFace(mode)
# <command>
#            <proto>void <name>glGenBuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n"><ptype>GLuint</ptype> *<name>buffers</name></param>
#        </command>
#        
glGenBuffers_impl=None
def glGenBuffers (n, buffers):
    global glGenBuffers_impl
    if not glGenBuffers_impl:
        fptr = pyglGetFuncAddress('glGenBuffers')
        if not fptr:
            raise RuntimeError('The function glGenBuffers is not available')
        glGenBuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenBuffers = (lambda n,buffers:glGenBuffers_impl(n,(c_uint8*len( buffers )).from_buffer( buffers )))
    return glGenBuffers(n, buffers)
# <command>
#            <proto>void <name>glGenFramebuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n"><ptype>GLuint</ptype> *<name>framebuffers</name></param>
#            <glx opcode="1426" type="vendor" />
#        </command>
#        
glGenFramebuffers_impl=None
def glGenFramebuffers (n, framebuffers):
    global glGenFramebuffers_impl
    if not glGenFramebuffers_impl:
        fptr = pyglGetFuncAddress('glGenFramebuffers')
        if not fptr:
            raise RuntimeError('The function glGenFramebuffers is not available')
        glGenFramebuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenFramebuffers = (lambda n,framebuffers:glGenFramebuffers_impl(n,(c_uint8*len( framebuffers )).from_buffer( framebuffers )))
    return glGenFramebuffers(n, framebuffers)
# <command>
#            <proto>void <name>glGenProgramPipelines</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n"><ptype>GLuint</ptype> *<name>pipelines</name></param>
#        </command>
#        
glGenProgramPipelines_impl=None
def glGenProgramPipelines (n, pipelines):
    global glGenProgramPipelines_impl
    if not glGenProgramPipelines_impl:
        fptr = pyglGetFuncAddress('glGenProgramPipelines')
        if not fptr:
            raise RuntimeError('The function glGenProgramPipelines is not available')
        glGenProgramPipelines_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenProgramPipelines = (lambda n,pipelines:glGenProgramPipelines_impl(n,(c_uint8*len( pipelines )).from_buffer( pipelines )))
    return glGenProgramPipelines(n, pipelines)
# <command>
#            <proto>void <name>glGenQueries</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n"><ptype>GLuint</ptype> *<name>ids</name></param>
#            <glx opcode="162" type="single" />
#        </command>
#        
glGenQueries_impl=None
def glGenQueries (n, ids):
    global glGenQueries_impl
    if not glGenQueries_impl:
        fptr = pyglGetFuncAddress('glGenQueries')
        if not fptr:
            raise RuntimeError('The function glGenQueries is not available')
        glGenQueries_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenQueries = (lambda n,ids:glGenQueries_impl(n,(c_uint8*len( ids )).from_buffer( ids )))
    return glGenQueries(n, ids)
# <command>
#            <proto>void <name>glGenRenderbuffers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n"><ptype>GLuint</ptype> *<name>renderbuffers</name></param>
#            <glx opcode="1423" type="vendor" />
#        </command>
#        
glGenRenderbuffers_impl=None
def glGenRenderbuffers (n, renderbuffers):
    global glGenRenderbuffers_impl
    if not glGenRenderbuffers_impl:
        fptr = pyglGetFuncAddress('glGenRenderbuffers')
        if not fptr:
            raise RuntimeError('The function glGenRenderbuffers is not available')
        glGenRenderbuffers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenRenderbuffers = (lambda n,renderbuffers:glGenRenderbuffers_impl(n,(c_uint8*len( renderbuffers )).from_buffer( renderbuffers )))
    return glGenRenderbuffers(n, renderbuffers)
# <command>
#            <proto>void <name>glGenSamplers</name></proto>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count"><ptype>GLuint</ptype> *<name>samplers</name></param>
#        </command>
#        
glGenSamplers_impl=None
def glGenSamplers (count, samplers):
    global glGenSamplers_impl
    if not glGenSamplers_impl:
        fptr = pyglGetFuncAddress('glGenSamplers')
        if not fptr:
            raise RuntimeError('The function glGenSamplers is not available')
        glGenSamplers_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenSamplers = (lambda count,samplers:glGenSamplers_impl(count,(c_uint8*len( samplers )).from_buffer( samplers )))
    return glGenSamplers(count, samplers)
# <command>
#            <proto>void <name>glGenTextures</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param group="Texture" len="n"><ptype>GLuint</ptype> *<name>textures</name></param>
#            <glx opcode="145" type="single" />
#        </command>
#        
glGenTextures_impl=None
def glGenTextures (n, textures):
    global glGenTextures_impl
    if not glGenTextures_impl:
        fptr = pyglGetFuncAddress('glGenTextures')
        if not fptr:
            raise RuntimeError('The function glGenTextures is not available')
        glGenTextures_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenTextures = (lambda n,textures:glGenTextures_impl(n,(c_uint8*len( textures )).from_buffer( textures )))
    return glGenTextures(n, textures)
# <command>
#            <proto>void <name>glGenTransformFeedbacks</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n"><ptype>GLuint</ptype> *<name>ids</name></param>
#        </command>
#        
glGenTransformFeedbacks_impl=None
def glGenTransformFeedbacks (n, ids):
    global glGenTransformFeedbacks_impl
    if not glGenTransformFeedbacks_impl:
        fptr = pyglGetFuncAddress('glGenTransformFeedbacks')
        if not fptr:
            raise RuntimeError('The function glGenTransformFeedbacks is not available')
        glGenTransformFeedbacks_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenTransformFeedbacks = (lambda n,ids:glGenTransformFeedbacks_impl(n,(c_uint8*len( ids )).from_buffer( ids )))
    return glGenTransformFeedbacks(n, ids)
# <command>
#            <proto>void <name>glGenVertexArrays</name></proto>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param len="n"><ptype>GLuint</ptype> *<name>arrays</name></param>
#            <glx opcode="206" type="single" />
#        </command>
#        
glGenVertexArrays_impl=None
def glGenVertexArrays (n, arrays):
    global glGenVertexArrays_impl
    if not glGenVertexArrays_impl:
        fptr = pyglGetFuncAddress('glGenVertexArrays')
        if not fptr:
            raise RuntimeError('The function glGenVertexArrays is not available')
        glGenVertexArrays_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p)(fptr)
    glGenVertexArrays = (lambda n,arrays:glGenVertexArrays_impl(n,(c_uint8*len( arrays )).from_buffer( arrays )))
    return glGenVertexArrays(n, arrays)
# <command>
#            <proto>void <name>glGenerateMipmap</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <glx opcode="4325" type="render" />
#        </command>
#        
glGenerateMipmap_impl=None
def glGenerateMipmap (target):
    global glGenerateMipmap_impl
    if not glGenerateMipmap_impl:
        fptr = pyglGetFuncAddress('glGenerateMipmap')
        if not fptr:
            raise RuntimeError('The function glGenerateMipmap is not available')
        glGenerateMipmap_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glGenerateMipmap = glGenerateMipmap_impl
    return glGenerateMipmap(target)
# <command>
#            <proto>void <name>glGenerateTextureMipmap</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#        </command>
#        
glGenerateTextureMipmap_impl=None
def glGenerateTextureMipmap (texture):
    global glGenerateTextureMipmap_impl
    if not glGenerateTextureMipmap_impl:
        fptr = pyglGetFuncAddress('glGenerateTextureMipmap')
        if not fptr:
            raise RuntimeError('The function glGenerateTextureMipmap is not available')
        glGenerateTextureMipmap_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glGenerateTextureMipmap = glGenerateTextureMipmap_impl
    return glGenerateTextureMipmap(texture)
# <command>
#            <proto>void <name>glGetActiveAtomicCounterBufferiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>bufferIndex</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetActiveAtomicCounterBufferiv_impl=None
def glGetActiveAtomicCounterBufferiv (program, bufferIndex, pname, params):
    global glGetActiveAtomicCounterBufferiv_impl
    if not glGetActiveAtomicCounterBufferiv_impl:
        fptr = pyglGetFuncAddress('glGetActiveAtomicCounterBufferiv')
        if not fptr:
            raise RuntimeError('The function glGetActiveAtomicCounterBufferiv is not available')
        glGetActiveAtomicCounterBufferiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetActiveAtomicCounterBufferiv = (lambda program,bufferIndex,pname,params:glGetActiveAtomicCounterBufferiv_impl(program,bufferIndex,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetActiveAtomicCounterBufferiv(program, bufferIndex, pname, params)
# <command>
#            <proto>void <name>glGetActiveAttrib</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="1"><ptype>GLint</ptype> *<name>size</name></param>
#            <param len="1"><ptype>GLenum</ptype> *<name>type</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetActiveAttrib_impl=None
def glGetActiveAttrib (program, index, bufSize, length, size, type, name):
    global glGetActiveAttrib_impl
    if not glGetActiveAttrib_impl:
        fptr = pyglGetFuncAddress('glGetActiveAttrib')
        if not fptr:
            raise RuntimeError('The function glGetActiveAttrib is not available')
        glGetActiveAttrib_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(fptr)
    glGetActiveAttrib = (lambda program,index,bufSize,length,size,type,name:glGetActiveAttrib_impl(program,index,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( size )).from_buffer( size ),(c_uint8*len( type )).from_buffer( type ),(c_uint8*len( name )).from_buffer( name )))
    return glGetActiveAttrib(program, index, bufSize, length, size, type, name)
# <command>
#            <proto>void <name>glGetActiveSubroutineName</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufsize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufsize"><ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetActiveSubroutineName_impl=None
def glGetActiveSubroutineName (program, shadertype, index, bufsize, length, name):
    global glGetActiveSubroutineName_impl
    if not glGetActiveSubroutineName_impl:
        fptr = pyglGetFuncAddress('glGetActiveSubroutineName')
        if not fptr:
            raise RuntimeError('The function glGetActiveSubroutineName is not available')
        glGetActiveSubroutineName_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetActiveSubroutineName = (lambda program,shadertype,index,bufsize,length,name:glGetActiveSubroutineName_impl(program,shadertype,index,bufsize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( name )).from_buffer( name )))
    return glGetActiveSubroutineName(program, shadertype, index, bufsize, length, name)
# <command>
#            <proto>void <name>glGetActiveSubroutineUniformName</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufsize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufsize"><ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetActiveSubroutineUniformName_impl=None
def glGetActiveSubroutineUniformName (program, shadertype, index, bufsize, length, name):
    global glGetActiveSubroutineUniformName_impl
    if not glGetActiveSubroutineUniformName_impl:
        fptr = pyglGetFuncAddress('glGetActiveSubroutineUniformName')
        if not fptr:
            raise RuntimeError('The function glGetActiveSubroutineUniformName is not available')
        glGetActiveSubroutineUniformName_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetActiveSubroutineUniformName = (lambda program,shadertype,index,bufsize,length,name:glGetActiveSubroutineUniformName_impl(program,shadertype,index,bufsize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( name )).from_buffer( name )))
    return glGetActiveSubroutineUniformName(program, shadertype, index, bufsize, length, name)
# <command>
#            <proto>void <name>glGetActiveSubroutineUniformiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>values</name></param>
#        </command>
#        
glGetActiveSubroutineUniformiv_impl=None
def glGetActiveSubroutineUniformiv (program, shadertype, index, pname, values):
    global glGetActiveSubroutineUniformiv_impl
    if not glGetActiveSubroutineUniformiv_impl:
        fptr = pyglGetFuncAddress('glGetActiveSubroutineUniformiv')
        if not fptr:
            raise RuntimeError('The function glGetActiveSubroutineUniformiv is not available')
        glGetActiveSubroutineUniformiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetActiveSubroutineUniformiv = (lambda program,shadertype,index,pname,values:glGetActiveSubroutineUniformiv_impl(program,shadertype,index,pname,(c_uint8*len( values )).from_buffer( values )))
    return glGetActiveSubroutineUniformiv(program, shadertype, index, pname, values)
# <command>
#            <proto>void <name>glGetActiveUniform</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="1"><ptype>GLint</ptype> *<name>size</name></param>
#            <param len="1"><ptype>GLenum</ptype> *<name>type</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetActiveUniform_impl=None
def glGetActiveUniform (program, index, bufSize, length, size, type, name):
    global glGetActiveUniform_impl
    if not glGetActiveUniform_impl:
        fptr = pyglGetFuncAddress('glGetActiveUniform')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniform is not available')
        glGetActiveUniform_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(fptr)
    glGetActiveUniform = (lambda program,index,bufSize,length,size,type,name:glGetActiveUniform_impl(program,index,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( size )).from_buffer( size ),(c_uint8*len( type )).from_buffer( type ),(c_uint8*len( name )).from_buffer( name )))
    return glGetActiveUniform(program, index, bufSize, length, size, type, name)
# <command>
#            <proto>void <name>glGetActiveUniformBlockName</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>uniformBlockIndex</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>uniformBlockName</name></param>
#        </command>
#        
glGetActiveUniformBlockName_impl=None
def glGetActiveUniformBlockName (program, uniformBlockIndex, bufSize, length, uniformBlockName):
    global glGetActiveUniformBlockName_impl
    if not glGetActiveUniformBlockName_impl:
        fptr = pyglGetFuncAddress('glGetActiveUniformBlockName')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniformBlockName is not available')
        glGetActiveUniformBlockName_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetActiveUniformBlockName = (lambda program,uniformBlockIndex,bufSize,length,uniformBlockName:glGetActiveUniformBlockName_impl(program,uniformBlockIndex,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( uniformBlockName )).from_buffer( uniformBlockName )))
    return glGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName)
# <command>
#            <proto>void <name>glGetActiveUniformBlockiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>uniformBlockIndex</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(program,uniformBlockIndex,pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetActiveUniformBlockiv_impl=None
def glGetActiveUniformBlockiv (program, uniformBlockIndex, pname, params):
    global glGetActiveUniformBlockiv_impl
    if not glGetActiveUniformBlockiv_impl:
        fptr = pyglGetFuncAddress('glGetActiveUniformBlockiv')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniformBlockiv is not available')
        glGetActiveUniformBlockiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetActiveUniformBlockiv = (lambda program,uniformBlockIndex,pname,params:glGetActiveUniformBlockiv_impl(program,uniformBlockIndex,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params)
# <command>
#            <proto>void <name>glGetActiveUniformName</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>uniformIndex</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>uniformName</name></param>
#        </command>
#        
glGetActiveUniformName_impl=None
def glGetActiveUniformName (program, uniformIndex, bufSize, length, uniformName):
    global glGetActiveUniformName_impl
    if not glGetActiveUniformName_impl:
        fptr = pyglGetFuncAddress('glGetActiveUniformName')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniformName is not available')
        glGetActiveUniformName_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetActiveUniformName = (lambda program,uniformIndex,bufSize,length,uniformName:glGetActiveUniformName_impl(program,uniformIndex,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( uniformName )).from_buffer( uniformName )))
    return glGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName)
# <command>
#            <proto>void <name>glGetActiveUniformsiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLsizei</ptype> <name>uniformCount</name></param>
#            <param len="uniformCount">const <ptype>GLuint</ptype> *<name>uniformIndices</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(uniformCount,pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetActiveUniformsiv_impl=None
def glGetActiveUniformsiv (program, uniformCount, uniformIndices, pname, params):
    global glGetActiveUniformsiv_impl
    if not glGetActiveUniformsiv_impl:
        fptr = pyglGetFuncAddress('glGetActiveUniformsiv')
        if not fptr:
            raise RuntimeError('The function glGetActiveUniformsiv is not available')
        glGetActiveUniformsiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_uint, c_void_p)(fptr)
    glGetActiveUniformsiv = (lambda program,uniformCount,uniformIndices,pname,params:glGetActiveUniformsiv_impl(program,uniformCount,pyglGetAsConstVoidPointer( uniformIndices ),pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params)
# <command>
#            <proto>void <name>glGetAttachedShaders</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLsizei</ptype> <name>maxCount</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>count</name></param>
#            <param len="maxCount"><ptype>GLuint</ptype> *<name>shaders</name></param>
#        </command>
#        
glGetAttachedShaders_impl=None
def glGetAttachedShaders (program, maxCount, count, shaders):
    global glGetAttachedShaders_impl
    if not glGetAttachedShaders_impl:
        fptr = pyglGetFuncAddress('glGetAttachedShaders')
        if not fptr:
            raise RuntimeError('The function glGetAttachedShaders is not available')
        glGetAttachedShaders_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetAttachedShaders = (lambda program,maxCount,count,shaders:glGetAttachedShaders_impl(program,maxCount,(c_uint8*len( count )).from_buffer( count ),(c_uint8*len( shaders )).from_buffer( shaders )))
    return glGetAttachedShaders(program, maxCount, count, shaders)
# <command>
#            <proto><ptype>GLint</ptype> <name>glGetAttribLocation</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetAttribLocation_impl=None
def glGetAttribLocation (program, name):
    global glGetAttribLocation_impl
    if not glGetAttribLocation_impl:
        fptr = pyglGetFuncAddress('glGetAttribLocation')
        if not fptr:
            raise RuntimeError('The function glGetAttribLocation is not available')
        glGetAttribLocation_impl = PYGL_FUNC_TYPE( c_int ,c_uint, c_void_p)(fptr)
    glGetAttribLocation = (lambda program,name:glGetAttribLocation_impl(program,c_char_p( name .encode() )))
    return glGetAttribLocation(program, name)
# <command>
#            <proto>void <name>glGetBooleani_v</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param group="Boolean" len="COMPSIZE(target)"><ptype>GLboolean</ptype> *<name>data</name></param>
#        </command>
#        
glGetBooleani_v_impl=None
def glGetBooleani_v (target, index, data):
    global glGetBooleani_v_impl
    if not glGetBooleani_v_impl:
        fptr = pyglGetFuncAddress('glGetBooleani_v')
        if not fptr:
            raise RuntimeError('The function glGetBooleani_v is not available')
        glGetBooleani_v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetBooleani_v = (lambda target,index,data:glGetBooleani_v_impl(target,index,(c_uint8*len( data )).from_buffer( data )))
    return glGetBooleani_v(target, index, data)
# <command>
#            <proto>void <name>glGetBooleanv</name></proto>
#            <param group="GetPName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="Boolean" len="COMPSIZE(pname)"><ptype>GLboolean</ptype> *<name>data</name></param>
#            <glx opcode="112" type="single" />
#        </command>
#        
glGetBooleanv_impl=None
def glGetBooleanv (pname, data):
    global glGetBooleanv_impl
    if not glGetBooleanv_impl:
        fptr = pyglGetFuncAddress('glGetBooleanv')
        if not fptr:
            raise RuntimeError('The function glGetBooleanv is not available')
        glGetBooleanv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glGetBooleanv = (lambda pname,data:glGetBooleanv_impl(pname,(c_uint8*len( data )).from_buffer( data )))
    return glGetBooleanv(pname, data)
# <command>
#            <proto>void <name>glGetBufferParameteri64v</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferPNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint64</ptype> *<name>params</name></param>
#        </command>
#        
glGetBufferParameteri64v_impl=None
def glGetBufferParameteri64v (target, pname, params):
    global glGetBufferParameteri64v_impl
    if not glGetBufferParameteri64v_impl:
        fptr = pyglGetFuncAddress('glGetBufferParameteri64v')
        if not fptr:
            raise RuntimeError('The function glGetBufferParameteri64v is not available')
        glGetBufferParameteri64v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetBufferParameteri64v = (lambda target,pname,params:glGetBufferParameteri64v_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetBufferParameteri64v(target, pname, params)
# <command>
#            <proto>void <name>glGetBufferParameteriv</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferPNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetBufferParameteriv_impl=None
def glGetBufferParameteriv (target, pname, params):
    global glGetBufferParameteriv_impl
    if not glGetBufferParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetBufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetBufferParameteriv is not available')
        glGetBufferParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetBufferParameteriv = (lambda target,pname,params:glGetBufferParameteriv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetBufferParameteriv(target, pname, params)
# <command>
#            <proto>void <name>glGetBufferPointerv</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferPointerNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="1">void **<name>params</name></param>
#        </command>
#        
glGetBufferPointerv_impl=None
def glGetBufferPointerv (target, pname, params):
    global glGetBufferPointerv_impl
    if not glGetBufferPointerv_impl:
        fptr = pyglGetFuncAddress('glGetBufferPointerv')
        if not fptr:
            raise RuntimeError('The function glGetBufferPointerv is not available')
        glGetBufferPointerv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetBufferPointerv = (lambda target,pname,params:glGetBufferPointerv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetBufferPointerv(target, pname, params)
# <command>
#            <proto>void <name>glGetBufferSubData</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param len="size">void *<name>data</name></param>
#        </command>
#        
glGetBufferSubData_impl=None
def glGetBufferSubData (target, offset, size, data):
    global glGetBufferSubData_impl
    if not glGetBufferSubData_impl:
        fptr = pyglGetFuncAddress('glGetBufferSubData')
        if not fptr:
            raise RuntimeError('The function glGetBufferSubData is not available')
        glGetBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_size_t, c_void_p, c_void_p)(fptr)
    glGetBufferSubData = (lambda target,offset,size,data:glGetBufferSubData_impl(target,offset,size,(c_uint8*len( data )).from_buffer( data )))
    return glGetBufferSubData(target, offset, size, data)
# <command>
#            <proto>void <name>glGetCompressedTexImage</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CompressedTextureARB" len="COMPSIZE(target,level)">void *<name>img</name></param>
#            <glx opcode="160" type="single" />
#            <glx comment="PBO protocol" name="glGetCompressedTexImagePBO" opcode="335" type="render" />
#        </command>
#        
glGetCompressedTexImage_impl=None
def glGetCompressedTexImage (target, level, img):
    global glGetCompressedTexImage_impl
    if not glGetCompressedTexImage_impl:
        fptr = pyglGetFuncAddress('glGetCompressedTexImage')
        if not fptr:
            raise RuntimeError('The function glGetCompressedTexImage is not available')
        glGetCompressedTexImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glGetCompressedTexImage = (lambda target,level,img:glGetCompressedTexImage_impl(target,level,(c_uint8*len( img )).from_buffer( img )))
    return glGetCompressedTexImage(target, level, img)
# <command>
#            <proto>void <name>glGetCompressedTextureImage</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param>void *<name>pixels</name></param>
#        </command>
#        
glGetCompressedTextureImage_impl=None
def glGetCompressedTextureImage (texture, level, bufSize, pixels):
    global glGetCompressedTextureImage_impl
    if not glGetCompressedTextureImage_impl:
        fptr = pyglGetFuncAddress('glGetCompressedTextureImage')
        if not fptr:
            raise RuntimeError('The function glGetCompressedTextureImage is not available')
        glGetCompressedTextureImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glGetCompressedTextureImage = (lambda texture,level,bufSize,pixels:glGetCompressedTextureImage_impl(texture,level,bufSize,(c_uint8*len( pixels )).from_buffer( pixels )))
    return glGetCompressedTextureImage(texture, level, bufSize, pixels)
# <command>
#            <proto>void <name>glGetCompressedTextureSubImage</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param>void *<name>pixels</name></param>
#        </command>
#        
glGetCompressedTextureSubImage_impl=None
def glGetCompressedTextureSubImage (texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels):
    global glGetCompressedTextureSubImage_impl
    if not glGetCompressedTextureSubImage_impl:
        fptr = pyglGetFuncAddress('glGetCompressedTextureSubImage')
        if not fptr:
            raise RuntimeError('The function glGetCompressedTextureSubImage is not available')
        glGetCompressedTextureSubImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_void_p)(fptr)
    glGetCompressedTextureSubImage = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,bufSize,pixels:glGetCompressedTextureSubImage_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,bufSize,(c_uint8*len( pixels )).from_buffer( pixels )))
    return glGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels)
# <command>
#            <proto><ptype>GLuint</ptype> <name>glGetDebugMessageLog</name></proto>
#            <param><ptype>GLuint</ptype> <name>count</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="count"><ptype>GLenum</ptype> *<name>sources</name></param>
#            <param len="count"><ptype>GLenum</ptype> *<name>types</name></param>
#            <param len="count"><ptype>GLuint</ptype> *<name>ids</name></param>
#            <param len="count"><ptype>GLenum</ptype> *<name>severities</name></param>
#            <param len="count"><ptype>GLsizei</ptype> *<name>lengths</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>messageLog</name></param>
#        </command>
#        
glGetDebugMessageLog_impl=None
def glGetDebugMessageLog (count, bufSize, sources, types, ids, severities, lengths, messageLog):
    global glGetDebugMessageLog_impl
    if not glGetDebugMessageLog_impl:
        fptr = pyglGetFuncAddress('glGetDebugMessageLog')
        if not fptr:
            raise RuntimeError('The function glGetDebugMessageLog is not available')
        glGetDebugMessageLog_impl = PYGL_FUNC_TYPE( c_uint ,c_uint, c_int, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_void_p)(fptr)
    glGetDebugMessageLog = (lambda count,bufSize,sources,types,ids,severities,lengths,messageLog:glGetDebugMessageLog_impl(count,bufSize,(c_uint8*len( sources )).from_buffer( sources ),(c_uint8*len( types )).from_buffer( types ),(c_uint8*len( ids )).from_buffer( ids ),(c_uint8*len( severities )).from_buffer( severities ),(c_uint8*len( lengths )).from_buffer( lengths ),(c_uint8*len( messageLog )).from_buffer( messageLog )))
    return glGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog)
# <command>
#            <proto>void <name>glGetDoublei_v</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="COMPSIZE(target)"><ptype>GLdouble</ptype> *<name>data</name></param>
#        </command>
#        
glGetDoublei_v_impl=None
def glGetDoublei_v (target, index, data):
    global glGetDoublei_v_impl
    if not glGetDoublei_v_impl:
        fptr = pyglGetFuncAddress('glGetDoublei_v')
        if not fptr:
            raise RuntimeError('The function glGetDoublei_v is not available')
        glGetDoublei_v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetDoublei_v = (lambda target,index,data:glGetDoublei_v_impl(target,index,(c_uint8*len( data )).from_buffer( data )))
    return glGetDoublei_v(target, index, data)
# <command>
#            <proto>void <name>glGetDoublev</name></proto>
#            <param group="GetPName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLdouble</ptype> *<name>data</name></param>
#            <glx opcode="114" type="single" />
#        </command>
#        
glGetDoublev_impl=None
def glGetDoublev (pname, data):
    global glGetDoublev_impl
    if not glGetDoublev_impl:
        fptr = pyglGetFuncAddress('glGetDoublev')
        if not fptr:
            raise RuntimeError('The function glGetDoublev is not available')
        glGetDoublev_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glGetDoublev = (lambda pname,data:glGetDoublev_impl(pname,(c_uint8*len( data )).from_buffer( data )))
    return glGetDoublev(pname, data)
# <command>
#            <proto group="ErrorCode"><ptype>GLenum</ptype> <name>glGetError</name></proto>
#            <glx opcode="115" type="single" />
#        </command>
#        
glGetError_impl=None
def glGetError ():
    global glGetError_impl
    if not glGetError_impl:
        fptr = pyglGetFuncAddress('glGetError')
        if not fptr:
            raise RuntimeError('The function glGetError is not available')
        glGetError_impl = PYGL_FUNC_TYPE( c_uint ,)(fptr)
    glGetError = glGetError_impl
    return glGetError()
# <command>
#            <proto>void <name>glGetFloati_v</name></proto>
#            <param group="TypeEnum"><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="COMPSIZE(target)"><ptype>GLfloat</ptype> *<name>data</name></param>
#        </command>
#        
glGetFloati_v_impl=None
def glGetFloati_v (target, index, data):
    global glGetFloati_v_impl
    if not glGetFloati_v_impl:
        fptr = pyglGetFuncAddress('glGetFloati_v')
        if not fptr:
            raise RuntimeError('The function glGetFloati_v is not available')
        glGetFloati_v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetFloati_v = (lambda target,index,data:glGetFloati_v_impl(target,index,(c_uint8*len( data )).from_buffer( data )))
    return glGetFloati_v(target, index, data)
# <command>
#            <proto>void <name>glGetFloatv</name></proto>
#            <param group="GetPName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>data</name></param>
#            <glx opcode="116" type="single" />
#        </command>
#        
glGetFloatv_impl=None
def glGetFloatv (pname, data):
    global glGetFloatv_impl
    if not glGetFloatv_impl:
        fptr = pyglGetFuncAddress('glGetFloatv')
        if not fptr:
            raise RuntimeError('The function glGetFloatv is not available')
        glGetFloatv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glGetFloatv = (lambda pname,data:glGetFloatv_impl(pname,(c_uint8*len( data )).from_buffer( data )))
    return glGetFloatv(pname, data)
# <command>
#            <proto><ptype>GLint</ptype> <name>glGetFragDataIndex</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetFragDataIndex_impl=None
def glGetFragDataIndex (program, name):
    global glGetFragDataIndex_impl
    if not glGetFragDataIndex_impl:
        fptr = pyglGetFuncAddress('glGetFragDataIndex')
        if not fptr:
            raise RuntimeError('The function glGetFragDataIndex is not available')
        glGetFragDataIndex_impl = PYGL_FUNC_TYPE( c_int ,c_uint, c_void_p)(fptr)
    glGetFragDataIndex = (lambda program,name:glGetFragDataIndex_impl(program,c_char_p( name .encode() )))
    return glGetFragDataIndex(program, name)
# <command>
#            <proto><ptype>GLint</ptype> <name>glGetFragDataLocation</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetFragDataLocation_impl=None
def glGetFragDataLocation (program, name):
    global glGetFragDataLocation_impl
    if not glGetFragDataLocation_impl:
        fptr = pyglGetFuncAddress('glGetFragDataLocation')
        if not fptr:
            raise RuntimeError('The function glGetFragDataLocation is not available')
        glGetFragDataLocation_impl = PYGL_FUNC_TYPE( c_int ,c_uint, c_void_p)(fptr)
    glGetFragDataLocation = (lambda program,name:glGetFragDataLocation_impl(program,c_char_p( name .encode() )))
    return glGetFragDataLocation(program, name)
# <command>
#            <proto>void <name>glGetFramebufferAttachmentParameteriv</name></proto>
#            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="1428" type="vendor" />
#        </command>
#        
glGetFramebufferAttachmentParameteriv_impl=None
def glGetFramebufferAttachmentParameteriv (target, attachment, pname, params):
    global glGetFramebufferAttachmentParameteriv_impl
    if not glGetFramebufferAttachmentParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetFramebufferAttachmentParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetFramebufferAttachmentParameteriv is not available')
        glGetFramebufferAttachmentParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetFramebufferAttachmentParameteriv = (lambda target,attachment,pname,params:glGetFramebufferAttachmentParameteriv_impl(target,attachment,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetFramebufferAttachmentParameteriv(target, attachment, pname, params)
# <command>
#            <proto>void <name>glGetFramebufferParameteriv</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetFramebufferParameteriv_impl=None
def glGetFramebufferParameteriv (target, pname, params):
    global glGetFramebufferParameteriv_impl
    if not glGetFramebufferParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetFramebufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetFramebufferParameteriv is not available')
        glGetFramebufferParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetFramebufferParameteriv = (lambda target,pname,params:glGetFramebufferParameteriv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetFramebufferParameteriv(target, pname, params)
# <command>
#            <proto><ptype>GLenum</ptype> <name>glGetGraphicsResetStatus</name></proto>
#        </command>
#        
glGetGraphicsResetStatus_impl=None
def glGetGraphicsResetStatus ():
    global glGetGraphicsResetStatus_impl
    if not glGetGraphicsResetStatus_impl:
        fptr = pyglGetFuncAddress('glGetGraphicsResetStatus')
        if not fptr:
            raise RuntimeError('The function glGetGraphicsResetStatus is not available')
        glGetGraphicsResetStatus_impl = PYGL_FUNC_TYPE( c_uint ,)(fptr)
    glGetGraphicsResetStatus = glGetGraphicsResetStatus_impl
    return glGetGraphicsResetStatus()
# <command>
#            <proto>void <name>glGetInteger64i_v</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="COMPSIZE(target)"><ptype>GLint64</ptype> *<name>data</name></param>
#        </command>
#        
glGetInteger64i_v_impl=None
def glGetInteger64i_v (target, index, data):
    global glGetInteger64i_v_impl
    if not glGetInteger64i_v_impl:
        fptr = pyglGetFuncAddress('glGetInteger64i_v')
        if not fptr:
            raise RuntimeError('The function glGetInteger64i_v is not available')
        glGetInteger64i_v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetInteger64i_v = (lambda target,index,data:glGetInteger64i_v_impl(target,index,(c_uint8*len( data )).from_buffer( data )))
    return glGetInteger64i_v(target, index, data)
# <command>
#            <proto>void <name>glGetInteger64v</name></proto>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint64</ptype> *<name>data</name></param>
#        </command>
#        
glGetInteger64v_impl=None
def glGetInteger64v (pname, data):
    global glGetInteger64v_impl
    if not glGetInteger64v_impl:
        fptr = pyglGetFuncAddress('glGetInteger64v')
        if not fptr:
            raise RuntimeError('The function glGetInteger64v is not available')
        glGetInteger64v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glGetInteger64v = (lambda pname,data:glGetInteger64v_impl(pname,(c_uint8*len( data )).from_buffer( data )))
    return glGetInteger64v(pname, data)
# <command>
#            <proto>void <name>glGetIntegeri_v</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="COMPSIZE(target)"><ptype>GLint</ptype> *<name>data</name></param>
#        </command>
#        
glGetIntegeri_v_impl=None
def glGetIntegeri_v (target, index, data):
    global glGetIntegeri_v_impl
    if not glGetIntegeri_v_impl:
        fptr = pyglGetFuncAddress('glGetIntegeri_v')
        if not fptr:
            raise RuntimeError('The function glGetIntegeri_v is not available')
        glGetIntegeri_v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetIntegeri_v = (lambda target,index,data:glGetIntegeri_v_impl(target,index,(c_uint8*len( data )).from_buffer( data )))
    return glGetIntegeri_v(target, index, data)
# <command>
#            <proto>void <name>glGetIntegerv</name></proto>
#            <param group="GetPName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>data</name></param>
#            <glx opcode="117" type="single" />
#        </command>
#        
glGetIntegerv_impl=None
def glGetIntegerv (pname, data):
    global glGetIntegerv_impl
    if not glGetIntegerv_impl:
        fptr = pyglGetFuncAddress('glGetIntegerv')
        if not fptr:
            raise RuntimeError('The function glGetIntegerv is not available')
        glGetIntegerv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glGetIntegerv = (lambda pname,data:glGetIntegerv_impl(pname,(c_uint8*len( data )).from_buffer( data )))
    return glGetIntegerv(pname, data)
# <command>
#            <proto>void <name>glGetInternalformati64v</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="bufSize"><ptype>GLint64</ptype> *<name>params</name></param>
#        </command>
#        
glGetInternalformati64v_impl=None
def glGetInternalformati64v (target, internalformat, pname, bufSize, params):
    global glGetInternalformati64v_impl
    if not glGetInternalformati64v_impl:
        fptr = pyglGetFuncAddress('glGetInternalformati64v')
        if not fptr:
            raise RuntimeError('The function glGetInternalformati64v is not available')
        glGetInternalformati64v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_void_p)(fptr)
    glGetInternalformati64v = (lambda target,internalformat,pname,bufSize,params:glGetInternalformati64v_impl(target,internalformat,pname,bufSize,(c_uint8*len( params )).from_buffer( params )))
    return glGetInternalformati64v(target, internalformat, pname, bufSize, params)
# <command>
#            <proto>void <name>glGetInternalformativ</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="bufSize"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetInternalformativ_impl=None
def glGetInternalformativ (target, internalformat, pname, bufSize, params):
    global glGetInternalformativ_impl
    if not glGetInternalformativ_impl:
        fptr = pyglGetFuncAddress('glGetInternalformativ')
        if not fptr:
            raise RuntimeError('The function glGetInternalformativ is not available')
        glGetInternalformativ_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_void_p)(fptr)
    glGetInternalformativ = (lambda target,internalformat,pname,bufSize,params:glGetInternalformativ_impl(target,internalformat,pname,bufSize,(c_uint8*len( params )).from_buffer( params )))
    return glGetInternalformativ(target, internalformat, pname, bufSize, params)
# <command>
#            <proto>void <name>glGetMultisamplefv</name></proto>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>val</name></param>
#        </command>
#        
glGetMultisamplefv_impl=None
def glGetMultisamplefv (pname, index, val):
    global glGetMultisamplefv_impl
    if not glGetMultisamplefv_impl:
        fptr = pyglGetFuncAddress('glGetMultisamplefv')
        if not fptr:
            raise RuntimeError('The function glGetMultisamplefv is not available')
        glGetMultisamplefv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetMultisamplefv = (lambda pname,index,val:glGetMultisamplefv_impl(pname,index,(c_uint8*len( val )).from_buffer( val )))
    return glGetMultisamplefv(pname, index, val)
# <command>
#            <proto>void <name>glGetNamedBufferParameteri64v</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint64</ptype> *<name>params</name></param>
#        </command>
#        
glGetNamedBufferParameteri64v_impl=None
def glGetNamedBufferParameteri64v (buffer, pname, params):
    global glGetNamedBufferParameteri64v_impl
    if not glGetNamedBufferParameteri64v_impl:
        fptr = pyglGetFuncAddress('glGetNamedBufferParameteri64v')
        if not fptr:
            raise RuntimeError('The function glGetNamedBufferParameteri64v is not available')
        glGetNamedBufferParameteri64v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetNamedBufferParameteri64v = (lambda buffer,pname,params:glGetNamedBufferParameteri64v_impl(buffer,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetNamedBufferParameteri64v(buffer, pname, params)
# <command>
#            <proto>void <name>glGetNamedBufferParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetNamedBufferParameteriv_impl=None
def glGetNamedBufferParameteriv (buffer, pname, params):
    global glGetNamedBufferParameteriv_impl
    if not glGetNamedBufferParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetNamedBufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetNamedBufferParameteriv is not available')
        glGetNamedBufferParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetNamedBufferParameteriv = (lambda buffer,pname,params:glGetNamedBufferParameteriv_impl(buffer,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetNamedBufferParameteriv(buffer, pname, params)
# <command>
#            <proto>void <name>glGetNamedBufferPointerv</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param>void **<name>params</name></param>
#        </command>
#        
glGetNamedBufferPointerv_impl=None
def glGetNamedBufferPointerv (buffer, pname, params):
    global glGetNamedBufferPointerv_impl
    if not glGetNamedBufferPointerv_impl:
        fptr = pyglGetFuncAddress('glGetNamedBufferPointerv')
        if not fptr:
            raise RuntimeError('The function glGetNamedBufferPointerv is not available')
        glGetNamedBufferPointerv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetNamedBufferPointerv = (lambda buffer,pname,params:glGetNamedBufferPointerv_impl(buffer,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetNamedBufferPointerv(buffer, pname, params)
# <command>
#            <proto>void <name>glGetNamedBufferSubData</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param>void *<name>data</name></param>
#        </command>
#        
glGetNamedBufferSubData_impl=None
def glGetNamedBufferSubData (buffer, offset, size, data):
    global glGetNamedBufferSubData_impl
    if not glGetNamedBufferSubData_impl:
        fptr = pyglGetFuncAddress('glGetNamedBufferSubData')
        if not fptr:
            raise RuntimeError('The function glGetNamedBufferSubData is not available')
        glGetNamedBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_size_t, c_void_p, c_void_p)(fptr)
    glGetNamedBufferSubData = (lambda buffer,offset,size,data:glGetNamedBufferSubData_impl(buffer,offset,size,(c_uint8*len( data )).from_buffer( data )))
    return glGetNamedBufferSubData(buffer, offset, size, data)
# <command>
#            <proto>void <name>glGetNamedFramebufferAttachmentParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetNamedFramebufferAttachmentParameteriv_impl=None
def glGetNamedFramebufferAttachmentParameteriv (framebuffer, attachment, pname, params):
    global glGetNamedFramebufferAttachmentParameteriv_impl
    if not glGetNamedFramebufferAttachmentParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetNamedFramebufferAttachmentParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetNamedFramebufferAttachmentParameteriv is not available')
        glGetNamedFramebufferAttachmentParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetNamedFramebufferAttachmentParameteriv = (lambda framebuffer,attachment,pname,params:glGetNamedFramebufferAttachmentParameteriv_impl(framebuffer,attachment,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params)
# <command>
#            <proto>void <name>glGetNamedFramebufferParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>param</name></param>
#        </command>
#        
glGetNamedFramebufferParameteriv_impl=None
def glGetNamedFramebufferParameteriv (framebuffer, pname, param):
    global glGetNamedFramebufferParameteriv_impl
    if not glGetNamedFramebufferParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetNamedFramebufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetNamedFramebufferParameteriv is not available')
        glGetNamedFramebufferParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetNamedFramebufferParameteriv = (lambda framebuffer,pname,param:glGetNamedFramebufferParameteriv_impl(framebuffer,pname,(c_uint8*len( param )).from_buffer( param )))
    return glGetNamedFramebufferParameteriv(framebuffer, pname, param)
# <command>
#            <proto>void <name>glGetNamedRenderbufferParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetNamedRenderbufferParameteriv_impl=None
def glGetNamedRenderbufferParameteriv (renderbuffer, pname, params):
    global glGetNamedRenderbufferParameteriv_impl
    if not glGetNamedRenderbufferParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetNamedRenderbufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetNamedRenderbufferParameteriv is not available')
        glGetNamedRenderbufferParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetNamedRenderbufferParameteriv = (lambda renderbuffer,pname,params:glGetNamedRenderbufferParameteriv_impl(renderbuffer,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetNamedRenderbufferParameteriv(renderbuffer, pname, params)
# <command>
#            <proto>void <name>glGetObjectLabel</name></proto>
#            <param><ptype>GLenum</ptype> <name>identifier</name></param>
#            <param><ptype>GLuint</ptype> <name>name</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>label</name></param>
#        </command>
#        
glGetObjectLabel_impl=None
def glGetObjectLabel (identifier, name, bufSize, length, label):
    global glGetObjectLabel_impl
    if not glGetObjectLabel_impl:
        fptr = pyglGetFuncAddress('glGetObjectLabel')
        if not fptr:
            raise RuntimeError('The function glGetObjectLabel is not available')
        glGetObjectLabel_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetObjectLabel = (lambda identifier,name,bufSize,length,label:glGetObjectLabel_impl(identifier,name,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( label )).from_buffer( label )))
    return glGetObjectLabel(identifier, name, bufSize, length, label)
# <command>
#            <proto>void <name>glGetObjectPtrLabel</name></proto>
#            <param>const void *<name>ptr</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>label</name></param>
#        </command>
#        
glGetObjectPtrLabel_impl=None
def glGetObjectPtrLabel (ptr, bufSize, length, label):
    global glGetObjectPtrLabel_impl
    if not glGetObjectPtrLabel_impl:
        fptr = pyglGetFuncAddress('glGetObjectPtrLabel')
        if not fptr:
            raise RuntimeError('The function glGetObjectPtrLabel is not available')
        glGetObjectPtrLabel_impl = PYGL_FUNC_TYPE( None ,c_void_p, c_int, c_void_p, c_void_p)(fptr)
    glGetObjectPtrLabel = (lambda ptr,bufSize,length,label:glGetObjectPtrLabel_impl(pyglGetAsConstVoidPointer( ptr ),bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( label )).from_buffer( label )))
    return glGetObjectPtrLabel(ptr, bufSize, length, label)
# <command>
#            <proto>void <name>glGetProgramBinary</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="1"><ptype>GLenum</ptype> *<name>binaryFormat</name></param>
#            <param len="bufSize">void *<name>binary</name></param>
#        </command>
#        
glGetProgramBinary_impl=None
def glGetProgramBinary (program, bufSize, length, binaryFormat, binary):
    global glGetProgramBinary_impl
    if not glGetProgramBinary_impl:
        fptr = pyglGetFuncAddress('glGetProgramBinary')
        if not fptr:
            raise RuntimeError('The function glGetProgramBinary is not available')
        glGetProgramBinary_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_void_p, c_void_p)(fptr)
    glGetProgramBinary = (lambda program,bufSize,length,binaryFormat,binary:glGetProgramBinary_impl(program,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( binaryFormat )).from_buffer( binaryFormat ),(c_uint8*len( binary )).from_buffer( binary )))
    return glGetProgramBinary(program, bufSize, length, binaryFormat, binary)
# <command>
#            <proto>void <name>glGetProgramInfoLog</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>infoLog</name></param>
#            <glx opcode="201" type="single" />
#        </command>
#        
glGetProgramInfoLog_impl=None
def glGetProgramInfoLog (program, bufSize, length, infoLog):
    global glGetProgramInfoLog_impl
    if not glGetProgramInfoLog_impl:
        fptr = pyglGetFuncAddress('glGetProgramInfoLog')
        if not fptr:
            raise RuntimeError('The function glGetProgramInfoLog is not available')
        glGetProgramInfoLog_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetProgramInfoLog = (lambda program,bufSize,length,infoLog:glGetProgramInfoLog_impl(program,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( infoLog )).from_buffer( infoLog )))
    return glGetProgramInfoLog(program, bufSize, length, infoLog)
# <command>
#            <proto>void <name>glGetProgramInterfaceiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetProgramInterfaceiv_impl=None
def glGetProgramInterfaceiv (program, programInterface, pname, params):
    global glGetProgramInterfaceiv_impl
    if not glGetProgramInterfaceiv_impl:
        fptr = pyglGetFuncAddress('glGetProgramInterfaceiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramInterfaceiv is not available')
        glGetProgramInterfaceiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetProgramInterfaceiv = (lambda program,programInterface,pname,params:glGetProgramInterfaceiv_impl(program,programInterface,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetProgramInterfaceiv(program, programInterface, pname, params)
# <command>
#            <proto>void <name>glGetProgramPipelineInfoLog</name></proto>
#            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>infoLog</name></param>
#        </command>
#        
glGetProgramPipelineInfoLog_impl=None
def glGetProgramPipelineInfoLog (pipeline, bufSize, length, infoLog):
    global glGetProgramPipelineInfoLog_impl
    if not glGetProgramPipelineInfoLog_impl:
        fptr = pyglGetFuncAddress('glGetProgramPipelineInfoLog')
        if not fptr:
            raise RuntimeError('The function glGetProgramPipelineInfoLog is not available')
        glGetProgramPipelineInfoLog_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetProgramPipelineInfoLog = (lambda pipeline,bufSize,length,infoLog:glGetProgramPipelineInfoLog_impl(pipeline,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( infoLog )).from_buffer( infoLog )))
    return glGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog)
# <command>
#            <proto>void <name>glGetProgramPipelineiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetProgramPipelineiv_impl=None
def glGetProgramPipelineiv (pipeline, pname, params):
    global glGetProgramPipelineiv_impl
    if not glGetProgramPipelineiv_impl:
        fptr = pyglGetFuncAddress('glGetProgramPipelineiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramPipelineiv is not available')
        glGetProgramPipelineiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetProgramPipelineiv = (lambda pipeline,pname,params:glGetProgramPipelineiv_impl(pipeline,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetProgramPipelineiv(pipeline, pname, params)
# <command>
#            <proto><ptype>GLuint</ptype> <name>glGetProgramResourceIndex</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
#            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetProgramResourceIndex_impl=None
def glGetProgramResourceIndex (program, programInterface, name):
    global glGetProgramResourceIndex_impl
    if not glGetProgramResourceIndex_impl:
        fptr = pyglGetFuncAddress('glGetProgramResourceIndex')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceIndex is not available')
        glGetProgramResourceIndex_impl = PYGL_FUNC_TYPE( c_uint ,c_uint, c_uint, c_void_p)(fptr)
    glGetProgramResourceIndex = (lambda program,programInterface,name:glGetProgramResourceIndex_impl(program,programInterface,c_char_p( name .encode() )))
    return glGetProgramResourceIndex(program, programInterface, name)
# <command>
#            <proto><ptype>GLint</ptype> <name>glGetProgramResourceLocation</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
#            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetProgramResourceLocation_impl=None
def glGetProgramResourceLocation (program, programInterface, name):
    global glGetProgramResourceLocation_impl
    if not glGetProgramResourceLocation_impl:
        fptr = pyglGetFuncAddress('glGetProgramResourceLocation')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceLocation is not available')
        glGetProgramResourceLocation_impl = PYGL_FUNC_TYPE( c_int ,c_uint, c_uint, c_void_p)(fptr)
    glGetProgramResourceLocation = (lambda program,programInterface,name:glGetProgramResourceLocation_impl(program,programInterface,c_char_p( name .encode() )))
    return glGetProgramResourceLocation(program, programInterface, name)
# <command>
#            <proto><ptype>GLint</ptype> <name>glGetProgramResourceLocationIndex</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
#            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetProgramResourceLocationIndex_impl=None
def glGetProgramResourceLocationIndex (program, programInterface, name):
    global glGetProgramResourceLocationIndex_impl
    if not glGetProgramResourceLocationIndex_impl:
        fptr = pyglGetFuncAddress('glGetProgramResourceLocationIndex')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceLocationIndex is not available')
        glGetProgramResourceLocationIndex_impl = PYGL_FUNC_TYPE( c_int ,c_uint, c_uint, c_void_p)(fptr)
    glGetProgramResourceLocationIndex = (lambda program,programInterface,name:glGetProgramResourceLocationIndex_impl(program,programInterface,c_char_p( name .encode() )))
    return glGetProgramResourceLocationIndex(program, programInterface, name)
# <command>
#            <proto>void <name>glGetProgramResourceName</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetProgramResourceName_impl=None
def glGetProgramResourceName (program, programInterface, index, bufSize, length, name):
    global glGetProgramResourceName_impl
    if not glGetProgramResourceName_impl:
        fptr = pyglGetFuncAddress('glGetProgramResourceName')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceName is not available')
        glGetProgramResourceName_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetProgramResourceName = (lambda program,programInterface,index,bufSize,length,name:glGetProgramResourceName_impl(program,programInterface,index,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( name )).from_buffer( name )))
    return glGetProgramResourceName(program, programInterface, index, bufSize, length, name)
# <command>
#            <proto>void <name>glGetProgramResourceiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLsizei</ptype> <name>propCount</name></param>
#            <param len="propCount">const <ptype>GLenum</ptype> *<name>props</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetProgramResourceiv_impl=None
def glGetProgramResourceiv (program, programInterface, index, propCount, props, bufSize, length, params):
    global glGetProgramResourceiv_impl
    if not glGetProgramResourceiv_impl:
        fptr = pyglGetFuncAddress('glGetProgramResourceiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramResourceiv is not available')
        glGetProgramResourceiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_void_p, c_int, c_void_p, c_void_p)(fptr)
    glGetProgramResourceiv = (lambda program,programInterface,index,propCount,props,bufSize,length,params:glGetProgramResourceiv_impl(program,programInterface,index,propCount,pyglGetAsConstVoidPointer( props ),bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( params )).from_buffer( params )))
    return glGetProgramResourceiv(program, programInterface, index, propCount, props, bufSize, length, params)
# <command>
#            <proto>void <name>glGetProgramStageiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="1"><ptype>GLint</ptype> *<name>values</name></param>
#        </command>
#        
glGetProgramStageiv_impl=None
def glGetProgramStageiv (program, shadertype, pname, values):
    global glGetProgramStageiv_impl
    if not glGetProgramStageiv_impl:
        fptr = pyglGetFuncAddress('glGetProgramStageiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramStageiv is not available')
        glGetProgramStageiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetProgramStageiv = (lambda program,shadertype,pname,values:glGetProgramStageiv_impl(program,shadertype,pname,(c_uint8*len( values )).from_buffer( values )))
    return glGetProgramStageiv(program, shadertype, pname, values)
# <command>
#            <proto>void <name>glGetProgramiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="199" type="single" />
#        </command>
#        
glGetProgramiv_impl=None
def glGetProgramiv (program, pname, params):
    global glGetProgramiv_impl
    if not glGetProgramiv_impl:
        fptr = pyglGetFuncAddress('glGetProgramiv')
        if not fptr:
            raise RuntimeError('The function glGetProgramiv is not available')
        glGetProgramiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetProgramiv = (lambda program,pname,params:glGetProgramiv_impl(program,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetProgramiv(program, pname, params)
# <command>
#            <proto>void <name>glGetQueryBufferObjecti64v</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#        </command>
#        
glGetQueryBufferObjecti64v_impl=None
def glGetQueryBufferObjecti64v (id, buffer, pname, offset):
    global glGetQueryBufferObjecti64v_impl
    if not glGetQueryBufferObjecti64v_impl:
        fptr = pyglGetFuncAddress('glGetQueryBufferObjecti64v')
        if not fptr:
            raise RuntimeError('The function glGetQueryBufferObjecti64v is not available')
        glGetQueryBufferObjecti64v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t)(fptr)
    glGetQueryBufferObjecti64v = glGetQueryBufferObjecti64v_impl
    return glGetQueryBufferObjecti64v(id, buffer, pname, offset)
# <command>
#            <proto>void <name>glGetQueryBufferObjectiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#        </command>
#        
glGetQueryBufferObjectiv_impl=None
def glGetQueryBufferObjectiv (id, buffer, pname, offset):
    global glGetQueryBufferObjectiv_impl
    if not glGetQueryBufferObjectiv_impl:
        fptr = pyglGetFuncAddress('glGetQueryBufferObjectiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryBufferObjectiv is not available')
        glGetQueryBufferObjectiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t)(fptr)
    glGetQueryBufferObjectiv = glGetQueryBufferObjectiv_impl
    return glGetQueryBufferObjectiv(id, buffer, pname, offset)
# <command>
#            <proto>void <name>glGetQueryBufferObjectui64v</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#        </command>
#        
glGetQueryBufferObjectui64v_impl=None
def glGetQueryBufferObjectui64v (id, buffer, pname, offset):
    global glGetQueryBufferObjectui64v_impl
    if not glGetQueryBufferObjectui64v_impl:
        fptr = pyglGetFuncAddress('glGetQueryBufferObjectui64v')
        if not fptr:
            raise RuntimeError('The function glGetQueryBufferObjectui64v is not available')
        glGetQueryBufferObjectui64v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t)(fptr)
    glGetQueryBufferObjectui64v = glGetQueryBufferObjectui64v_impl
    return glGetQueryBufferObjectui64v(id, buffer, pname, offset)
# <command>
#            <proto>void <name>glGetQueryBufferObjectuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#        </command>
#        
glGetQueryBufferObjectuiv_impl=None
def glGetQueryBufferObjectuiv (id, buffer, pname, offset):
    global glGetQueryBufferObjectuiv_impl
    if not glGetQueryBufferObjectuiv_impl:
        fptr = pyglGetFuncAddress('glGetQueryBufferObjectuiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryBufferObjectuiv is not available')
        glGetQueryBufferObjectuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t)(fptr)
    glGetQueryBufferObjectuiv = glGetQueryBufferObjectuiv_impl
    return glGetQueryBufferObjectuiv(id, buffer, pname, offset)
# <command>
#            <proto>void <name>glGetQueryIndexediv</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetQueryIndexediv_impl=None
def glGetQueryIndexediv (target, index, pname, params):
    global glGetQueryIndexediv_impl
    if not glGetQueryIndexediv_impl:
        fptr = pyglGetFuncAddress('glGetQueryIndexediv')
        if not fptr:
            raise RuntimeError('The function glGetQueryIndexediv is not available')
        glGetQueryIndexediv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetQueryIndexediv = (lambda target,index,pname,params:glGetQueryIndexediv_impl(target,index,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetQueryIndexediv(target, index, pname, params)
# <command>
#            <proto>void <name>glGetQueryObjecti64v</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint64</ptype> *<name>params</name></param>
#        </command>
#        
glGetQueryObjecti64v_impl=None
def glGetQueryObjecti64v (id, pname, params):
    global glGetQueryObjecti64v_impl
    if not glGetQueryObjecti64v_impl:
        fptr = pyglGetFuncAddress('glGetQueryObjecti64v')
        if not fptr:
            raise RuntimeError('The function glGetQueryObjecti64v is not available')
        glGetQueryObjecti64v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetQueryObjecti64v = (lambda id,pname,params:glGetQueryObjecti64v_impl(id,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetQueryObjecti64v(id, pname, params)
# <command>
#            <proto>void <name>glGetQueryObjectiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="165" type="single" />
#        </command>
#        
glGetQueryObjectiv_impl=None
def glGetQueryObjectiv (id, pname, params):
    global glGetQueryObjectiv_impl
    if not glGetQueryObjectiv_impl:
        fptr = pyglGetFuncAddress('glGetQueryObjectiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryObjectiv is not available')
        glGetQueryObjectiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetQueryObjectiv = (lambda id,pname,params:glGetQueryObjectiv_impl(id,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetQueryObjectiv(id, pname, params)
# <command>
#            <proto>void <name>glGetQueryObjectui64v</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLuint64</ptype> *<name>params</name></param>
#        </command>
#        
glGetQueryObjectui64v_impl=None
def glGetQueryObjectui64v (id, pname, params):
    global glGetQueryObjectui64v_impl
    if not glGetQueryObjectui64v_impl:
        fptr = pyglGetFuncAddress('glGetQueryObjectui64v')
        if not fptr:
            raise RuntimeError('The function glGetQueryObjectui64v is not available')
        glGetQueryObjectui64v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetQueryObjectui64v = (lambda id,pname,params:glGetQueryObjectui64v_impl(id,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetQueryObjectui64v(id, pname, params)
# <command>
#            <proto>void <name>glGetQueryObjectuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLuint</ptype> *<name>params</name></param>
#            <glx opcode="166" type="single" />
#        </command>
#        
glGetQueryObjectuiv_impl=None
def glGetQueryObjectuiv (id, pname, params):
    global glGetQueryObjectuiv_impl
    if not glGetQueryObjectuiv_impl:
        fptr = pyglGetFuncAddress('glGetQueryObjectuiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryObjectuiv is not available')
        glGetQueryObjectuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetQueryObjectuiv = (lambda id,pname,params:glGetQueryObjectuiv_impl(id,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetQueryObjectuiv(id, pname, params)
# <command>
#            <proto>void <name>glGetQueryiv</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="164" type="single" />
#        </command>
#        
glGetQueryiv_impl=None
def glGetQueryiv (target, pname, params):
    global glGetQueryiv_impl
    if not glGetQueryiv_impl:
        fptr = pyglGetFuncAddress('glGetQueryiv')
        if not fptr:
            raise RuntimeError('The function glGetQueryiv is not available')
        glGetQueryiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetQueryiv = (lambda target,pname,params:glGetQueryiv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetQueryiv(target, pname, params)
# <command>
#            <proto>void <name>glGetRenderbufferParameteriv</name></proto>
#            <param group="RenderbufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="1424" type="vendor" />
#        </command>
#        
glGetRenderbufferParameteriv_impl=None
def glGetRenderbufferParameteriv (target, pname, params):
    global glGetRenderbufferParameteriv_impl
    if not glGetRenderbufferParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetRenderbufferParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetRenderbufferParameteriv is not available')
        glGetRenderbufferParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetRenderbufferParameteriv = (lambda target,pname,params:glGetRenderbufferParameteriv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetRenderbufferParameteriv(target, pname, params)
# <command>
#            <proto>void <name>glGetSamplerParameterIiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetSamplerParameterIiv_impl=None
def glGetSamplerParameterIiv (sampler, pname, params):
    global glGetSamplerParameterIiv_impl
    if not glGetSamplerParameterIiv_impl:
        fptr = pyglGetFuncAddress('glGetSamplerParameterIiv')
        if not fptr:
            raise RuntimeError('The function glGetSamplerParameterIiv is not available')
        glGetSamplerParameterIiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetSamplerParameterIiv = (lambda sampler,pname,params:glGetSamplerParameterIiv_impl(sampler,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetSamplerParameterIiv(sampler, pname, params)
# <command>
#            <proto>void <name>glGetSamplerParameterIuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLuint</ptype> *<name>params</name></param>
#        </command>
#        
glGetSamplerParameterIuiv_impl=None
def glGetSamplerParameterIuiv (sampler, pname, params):
    global glGetSamplerParameterIuiv_impl
    if not glGetSamplerParameterIuiv_impl:
        fptr = pyglGetFuncAddress('glGetSamplerParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glGetSamplerParameterIuiv is not available')
        glGetSamplerParameterIuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetSamplerParameterIuiv = (lambda sampler,pname,params:glGetSamplerParameterIuiv_impl(sampler,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetSamplerParameterIuiv(sampler, pname, params)
# <command>
#            <proto>void <name>glGetSamplerParameterfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>params</name></param>
#        </command>
#        
glGetSamplerParameterfv_impl=None
def glGetSamplerParameterfv (sampler, pname, params):
    global glGetSamplerParameterfv_impl
    if not glGetSamplerParameterfv_impl:
        fptr = pyglGetFuncAddress('glGetSamplerParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetSamplerParameterfv is not available')
        glGetSamplerParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetSamplerParameterfv = (lambda sampler,pname,params:glGetSamplerParameterfv_impl(sampler,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetSamplerParameterfv(sampler, pname, params)
# <command>
#            <proto>void <name>glGetSamplerParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetSamplerParameteriv_impl=None
def glGetSamplerParameteriv (sampler, pname, params):
    global glGetSamplerParameteriv_impl
    if not glGetSamplerParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetSamplerParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetSamplerParameteriv is not available')
        glGetSamplerParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetSamplerParameteriv = (lambda sampler,pname,params:glGetSamplerParameteriv_impl(sampler,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetSamplerParameteriv(sampler, pname, params)
# <command>
#            <proto>void <name>glGetShaderInfoLog</name></proto>
#            <param><ptype>GLuint</ptype> <name>shader</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>infoLog</name></param>
#            <glx opcode="200" type="single" />
#        </command>
#        
glGetShaderInfoLog_impl=None
def glGetShaderInfoLog (shader, bufSize, length, infoLog):
    global glGetShaderInfoLog_impl
    if not glGetShaderInfoLog_impl:
        fptr = pyglGetFuncAddress('glGetShaderInfoLog')
        if not fptr:
            raise RuntimeError('The function glGetShaderInfoLog is not available')
        glGetShaderInfoLog_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetShaderInfoLog = (lambda shader,bufSize,length,infoLog:glGetShaderInfoLog_impl(shader,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( infoLog )).from_buffer( infoLog )))
    return glGetShaderInfoLog(shader, bufSize, length, infoLog)
# <command>
#            <proto>void <name>glGetShaderPrecisionFormat</name></proto>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param><ptype>GLenum</ptype> <name>precisiontype</name></param>
#            <param len="2"><ptype>GLint</ptype> *<name>range</name></param>
#            <param len="2"><ptype>GLint</ptype> *<name>precision</name></param>
#        </command>
#        
glGetShaderPrecisionFormat_impl=None
def glGetShaderPrecisionFormat (shadertype, precisiontype, range, precision):
    global glGetShaderPrecisionFormat_impl
    if not glGetShaderPrecisionFormat_impl:
        fptr = pyglGetFuncAddress('glGetShaderPrecisionFormat')
        if not fptr:
            raise RuntimeError('The function glGetShaderPrecisionFormat is not available')
        glGetShaderPrecisionFormat_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p, c_void_p)(fptr)
    glGetShaderPrecisionFormat = (lambda shadertype,precisiontype,range,precision:glGetShaderPrecisionFormat_impl(shadertype,precisiontype,(c_uint8*len( range )).from_buffer( range ),(c_uint8*len( precision )).from_buffer( precision )))
    return glGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)
# <command>
#            <proto>void <name>glGetShaderSource</name></proto>
#            <param><ptype>GLuint</ptype> <name>shader</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>source</name></param>
#        </command>
#        
glGetShaderSource_impl=None
def glGetShaderSource (shader, bufSize, length, source):
    global glGetShaderSource_impl
    if not glGetShaderSource_impl:
        fptr = pyglGetFuncAddress('glGetShaderSource')
        if not fptr:
            raise RuntimeError('The function glGetShaderSource is not available')
        glGetShaderSource_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetShaderSource = (lambda shader,bufSize,length,source:glGetShaderSource_impl(shader,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( source )).from_buffer( source )))
    return glGetShaderSource(shader, bufSize, length, source)
# <command>
#            <proto>void <name>glGetShaderiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>shader</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="198" type="single" />
#        </command>
#        
glGetShaderiv_impl=None
def glGetShaderiv (shader, pname, params):
    global glGetShaderiv_impl
    if not glGetShaderiv_impl:
        fptr = pyglGetFuncAddress('glGetShaderiv')
        if not fptr:
            raise RuntimeError('The function glGetShaderiv is not available')
        glGetShaderiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetShaderiv = (lambda shader,pname,params:glGetShaderiv_impl(shader,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetShaderiv(shader, pname, params)
# <command>
#            <proto group="String">const <ptype>GLubyte</ptype> *<name>glGetString</name></proto>
#            <param group="StringName"><ptype>GLenum</ptype> <name>name</name></param>
#            <glx opcode="129" type="single" />
#        </command>
#        
glGetString_impl=None
def glGetString (name):
    global glGetString_impl
    if not glGetString_impl:
        fptr = pyglGetFuncAddress('glGetString')
        if not fptr:
            raise RuntimeError('The function glGetString is not available')
        glGetString_impl = PYGL_FUNC_TYPE( c_char_p ,c_uint)(fptr)
    glGetString = glGetString_impl
    return glGetString(name)
# <command>
#            <proto group="String">const <ptype>GLubyte</ptype> *<name>glGetStringi</name></proto>
#            <param><ptype>GLenum</ptype> <name>name</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glGetStringi_impl=None
def glGetStringi (name, index):
    global glGetStringi_impl
    if not glGetStringi_impl:
        fptr = pyglGetFuncAddress('glGetStringi')
        if not fptr:
            raise RuntimeError('The function glGetStringi is not available')
        glGetStringi_impl = PYGL_FUNC_TYPE( c_char_p ,c_uint, c_uint)(fptr)
    glGetStringi = glGetStringi_impl
    return glGetStringi(name, index)
# <command>
#            <proto><ptype>GLuint</ptype> <name>glGetSubroutineIndex</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetSubroutineIndex_impl=None
def glGetSubroutineIndex (program, shadertype, name):
    global glGetSubroutineIndex_impl
    if not glGetSubroutineIndex_impl:
        fptr = pyglGetFuncAddress('glGetSubroutineIndex')
        if not fptr:
            raise RuntimeError('The function glGetSubroutineIndex is not available')
        glGetSubroutineIndex_impl = PYGL_FUNC_TYPE( c_uint ,c_uint, c_uint, c_void_p)(fptr)
    glGetSubroutineIndex = (lambda program,shadertype,name:glGetSubroutineIndex_impl(program,shadertype,c_char_p( name .encode() )))
    return glGetSubroutineIndex(program, shadertype, name)
# <command>
#            <proto><ptype>GLint</ptype> <name>glGetSubroutineUniformLocation</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetSubroutineUniformLocation_impl=None
def glGetSubroutineUniformLocation (program, shadertype, name):
    global glGetSubroutineUniformLocation_impl
    if not glGetSubroutineUniformLocation_impl:
        fptr = pyglGetFuncAddress('glGetSubroutineUniformLocation')
        if not fptr:
            raise RuntimeError('The function glGetSubroutineUniformLocation is not available')
        glGetSubroutineUniformLocation_impl = PYGL_FUNC_TYPE( c_int ,c_uint, c_uint, c_void_p)(fptr)
    glGetSubroutineUniformLocation = (lambda program,shadertype,name:glGetSubroutineUniformLocation_impl(program,shadertype,c_char_p( name .encode() )))
    return glGetSubroutineUniformLocation(program, shadertype, name)
# <command>
#            <proto>void <name>glGetSynciv</name></proto>
#            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="bufSize"><ptype>GLint</ptype> *<name>values</name></param>
#        </command>
#        
glGetSynciv_impl=None
def glGetSynciv (sync, pname, bufSize, length, values):
    global glGetSynciv_impl
    if not glGetSynciv_impl:
        fptr = pyglGetFuncAddress('glGetSynciv')
        if not fptr:
            raise RuntimeError('The function glGetSynciv is not available')
        glGetSynciv_impl = PYGL_FUNC_TYPE( None ,c_void_p, c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetSynciv = (lambda sync,pname,bufSize,length,values:glGetSynciv_impl(sync,pname,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( values )).from_buffer( values )))
    return glGetSynciv(sync, pname, bufSize, length, values)
# <command>
#            <proto>void <name>glGetTexImage</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(target,level,format,type)">void *<name>pixels</name></param>
#            <glx opcode="135" type="single" />
#            <glx comment="PBO protocol" name="glGetTexImagePBO" opcode="344" type="render" />
#        </command>
#        
glGetTexImage_impl=None
def glGetTexImage (target, level, format, type, pixels):
    global glGetTexImage_impl
    if not glGetTexImage_impl:
        fptr = pyglGetFuncAddress('glGetTexImage')
        if not fptr:
            raise RuntimeError('The function glGetTexImage is not available')
        glGetTexImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_uint, c_void_p)(fptr)
    glGetTexImage = (lambda target,level,format,type,pixels:glGetTexImage_impl(target,level,format,type,(c_uint8*len( pixels )).from_buffer( pixels )))
    return glGetTexImage(target, level, format, type, pixels)
# <command>
#            <proto>void <name>glGetTexLevelParameterfv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>params</name></param>
#            <glx opcode="138" type="single" />
#        </command>
#        
glGetTexLevelParameterfv_impl=None
def glGetTexLevelParameterfv (target, level, pname, params):
    global glGetTexLevelParameterfv_impl
    if not glGetTexLevelParameterfv_impl:
        fptr = pyglGetFuncAddress('glGetTexLevelParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetTexLevelParameterfv is not available')
        glGetTexLevelParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p)(fptr)
    glGetTexLevelParameterfv = (lambda target,level,pname,params:glGetTexLevelParameterfv_impl(target,level,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTexLevelParameterfv(target, level, pname, params)
# <command>
#            <proto>void <name>glGetTexLevelParameteriv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="139" type="single" />
#        </command>
#        
glGetTexLevelParameteriv_impl=None
def glGetTexLevelParameteriv (target, level, pname, params):
    global glGetTexLevelParameteriv_impl
    if not glGetTexLevelParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetTexLevelParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetTexLevelParameteriv is not available')
        glGetTexLevelParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p)(fptr)
    glGetTexLevelParameteriv = (lambda target,level,pname,params:glGetTexLevelParameteriv_impl(target,level,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTexLevelParameteriv(target, level, pname, params)
# <command>
#            <proto>void <name>glGetTexParameterIiv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="203" type="single" />
#        </command>
#        
glGetTexParameterIiv_impl=None
def glGetTexParameterIiv (target, pname, params):
    global glGetTexParameterIiv_impl
    if not glGetTexParameterIiv_impl:
        fptr = pyglGetFuncAddress('glGetTexParameterIiv')
        if not fptr:
            raise RuntimeError('The function glGetTexParameterIiv is not available')
        glGetTexParameterIiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTexParameterIiv = (lambda target,pname,params:glGetTexParameterIiv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTexParameterIiv(target, pname, params)
# <command>
#            <proto>void <name>glGetTexParameterIuiv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLuint</ptype> *<name>params</name></param>
#            <glx opcode="204" type="single" />
#        </command>
#        
glGetTexParameterIuiv_impl=None
def glGetTexParameterIuiv (target, pname, params):
    global glGetTexParameterIuiv_impl
    if not glGetTexParameterIuiv_impl:
        fptr = pyglGetFuncAddress('glGetTexParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glGetTexParameterIuiv is not available')
        glGetTexParameterIuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTexParameterIuiv = (lambda target,pname,params:glGetTexParameterIuiv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTexParameterIuiv(target, pname, params)
# <command>
#            <proto>void <name>glGetTexParameterfv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>params</name></param>
#            <glx opcode="136" type="single" />
#        </command>
#        
glGetTexParameterfv_impl=None
def glGetTexParameterfv (target, pname, params):
    global glGetTexParameterfv_impl
    if not glGetTexParameterfv_impl:
        fptr = pyglGetFuncAddress('glGetTexParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetTexParameterfv is not available')
        glGetTexParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTexParameterfv = (lambda target,pname,params:glGetTexParameterfv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTexParameterfv(target, pname, params)
# <command>
#            <proto>void <name>glGetTexParameteriv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="137" type="single" />
#        </command>
#        
glGetTexParameteriv_impl=None
def glGetTexParameteriv (target, pname, params):
    global glGetTexParameteriv_impl
    if not glGetTexParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetTexParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetTexParameteriv is not available')
        glGetTexParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTexParameteriv = (lambda target,pname,params:glGetTexParameteriv_impl(target,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTexParameteriv(target, pname, params)
# <command>
#            <proto>void <name>glGetTextureImage</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param>void *<name>pixels</name></param>
#        </command>
#        
glGetTextureImage_impl=None
def glGetTextureImage (texture, level, format, type, bufSize, pixels):
    global glGetTextureImage_impl
    if not glGetTextureImage_impl:
        fptr = pyglGetFuncAddress('glGetTextureImage')
        if not fptr:
            raise RuntimeError('The function glGetTextureImage is not available')
        glGetTextureImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_uint, c_int, c_void_p)(fptr)
    glGetTextureImage = (lambda texture,level,format,type,bufSize,pixels:glGetTextureImage_impl(texture,level,format,type,bufSize,(c_uint8*len( pixels )).from_buffer( pixels )))
    return glGetTextureImage(texture, level, format, type, bufSize, pixels)
# <command>
#            <proto>void <name>glGetTextureLevelParameterfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLfloat</ptype> *<name>params</name></param>
#        </command>
#        
glGetTextureLevelParameterfv_impl=None
def glGetTextureLevelParameterfv (texture, level, pname, params):
    global glGetTextureLevelParameterfv_impl
    if not glGetTextureLevelParameterfv_impl:
        fptr = pyglGetFuncAddress('glGetTextureLevelParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetTextureLevelParameterfv is not available')
        glGetTextureLevelParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p)(fptr)
    glGetTextureLevelParameterfv = (lambda texture,level,pname,params:glGetTextureLevelParameterfv_impl(texture,level,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTextureLevelParameterfv(texture, level, pname, params)
# <command>
#            <proto>void <name>glGetTextureLevelParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetTextureLevelParameteriv_impl=None
def glGetTextureLevelParameteriv (texture, level, pname, params):
    global glGetTextureLevelParameteriv_impl
    if not glGetTextureLevelParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetTextureLevelParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetTextureLevelParameteriv is not available')
        glGetTextureLevelParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_void_p)(fptr)
    glGetTextureLevelParameteriv = (lambda texture,level,pname,params:glGetTextureLevelParameteriv_impl(texture,level,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTextureLevelParameteriv(texture, level, pname, params)
# <command>
#            <proto>void <name>glGetTextureParameterIiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetTextureParameterIiv_impl=None
def glGetTextureParameterIiv (texture, pname, params):
    global glGetTextureParameterIiv_impl
    if not glGetTextureParameterIiv_impl:
        fptr = pyglGetFuncAddress('glGetTextureParameterIiv')
        if not fptr:
            raise RuntimeError('The function glGetTextureParameterIiv is not available')
        glGetTextureParameterIiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTextureParameterIiv = (lambda texture,pname,params:glGetTextureParameterIiv_impl(texture,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTextureParameterIiv(texture, pname, params)
# <command>
#            <proto>void <name>glGetTextureParameterIuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLuint</ptype> *<name>params</name></param>
#        </command>
#        
glGetTextureParameterIuiv_impl=None
def glGetTextureParameterIuiv (texture, pname, params):
    global glGetTextureParameterIuiv_impl
    if not glGetTextureParameterIuiv_impl:
        fptr = pyglGetFuncAddress('glGetTextureParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glGetTextureParameterIuiv is not available')
        glGetTextureParameterIuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTextureParameterIuiv = (lambda texture,pname,params:glGetTextureParameterIuiv_impl(texture,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTextureParameterIuiv(texture, pname, params)
# <command>
#            <proto>void <name>glGetTextureParameterfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLfloat</ptype> *<name>params</name></param>
#        </command>
#        
glGetTextureParameterfv_impl=None
def glGetTextureParameterfv (texture, pname, params):
    global glGetTextureParameterfv_impl
    if not glGetTextureParameterfv_impl:
        fptr = pyglGetFuncAddress('glGetTextureParameterfv')
        if not fptr:
            raise RuntimeError('The function glGetTextureParameterfv is not available')
        glGetTextureParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTextureParameterfv = (lambda texture,pname,params:glGetTextureParameterfv_impl(texture,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTextureParameterfv(texture, pname, params)
# <command>
#            <proto>void <name>glGetTextureParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetTextureParameteriv_impl=None
def glGetTextureParameteriv (texture, pname, params):
    global glGetTextureParameteriv_impl
    if not glGetTextureParameteriv_impl:
        fptr = pyglGetFuncAddress('glGetTextureParameteriv')
        if not fptr:
            raise RuntimeError('The function glGetTextureParameteriv is not available')
        glGetTextureParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTextureParameteriv = (lambda texture,pname,params:glGetTextureParameteriv_impl(texture,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetTextureParameteriv(texture, pname, params)
# <command>
#            <proto>void <name>glGetTextureSubImage</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param>void *<name>pixels</name></param>
#        </command>
#        
glGetTextureSubImage_impl=None
def glGetTextureSubImage (texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels):
    global glGetTextureSubImage_impl
    if not glGetTextureSubImage_impl:
        fptr = pyglGetFuncAddress('glGetTextureSubImage')
        if not fptr:
            raise RuntimeError('The function glGetTextureSubImage is not available')
        glGetTextureSubImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_int, c_void_p)(fptr)
    glGetTextureSubImage = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,bufSize,pixels:glGetTextureSubImage_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,bufSize,(c_uint8*len( pixels )).from_buffer( pixels )))
    return glGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels)
# <command>
#            <proto>void <name>glGetTransformFeedbackVarying</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
#            <param len="1"><ptype>GLsizei</ptype> *<name>size</name></param>
#            <param len="1"><ptype>GLenum</ptype> *<name>type</name></param>
#            <param len="bufSize"><ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetTransformFeedbackVarying_impl=None
def glGetTransformFeedbackVarying (program, index, bufSize, length, size, type, name):
    global glGetTransformFeedbackVarying_impl
    if not glGetTransformFeedbackVarying_impl:
        fptr = pyglGetFuncAddress('glGetTransformFeedbackVarying')
        if not fptr:
            raise RuntimeError('The function glGetTransformFeedbackVarying is not available')
        glGetTransformFeedbackVarying_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p, c_void_p, c_void_p, c_void_p)(fptr)
    glGetTransformFeedbackVarying = (lambda program,index,bufSize,length,size,type,name:glGetTransformFeedbackVarying_impl(program,index,bufSize,(c_uint8*len( length )).from_buffer( length ),(c_uint8*len( size )).from_buffer( size ),(c_uint8*len( type )).from_buffer( type ),(c_uint8*len( name )).from_buffer( name )))
    return glGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name)
# <command>
#            <proto>void <name>glGetTransformFeedbacki64_v</name></proto>
#            <param><ptype>GLuint</ptype> <name>xfb</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLint64</ptype> *<name>param</name></param>
#        </command>
#        
glGetTransformFeedbacki64_v_impl=None
def glGetTransformFeedbacki64_v (xfb, pname, index, param):
    global glGetTransformFeedbacki64_v_impl
    if not glGetTransformFeedbacki64_v_impl:
        fptr = pyglGetFuncAddress('glGetTransformFeedbacki64_v')
        if not fptr:
            raise RuntimeError('The function glGetTransformFeedbacki64_v is not available')
        glGetTransformFeedbacki64_v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetTransformFeedbacki64_v = (lambda xfb,pname,index,param:glGetTransformFeedbacki64_v_impl(xfb,pname,index,(c_uint8*len( param )).from_buffer( param )))
    return glGetTransformFeedbacki64_v(xfb, pname, index, param)
# <command>
#            <proto>void <name>glGetTransformFeedbacki_v</name></proto>
#            <param><ptype>GLuint</ptype> <name>xfb</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLint</ptype> *<name>param</name></param>
#        </command>
#        
glGetTransformFeedbacki_v_impl=None
def glGetTransformFeedbacki_v (xfb, pname, index, param):
    global glGetTransformFeedbacki_v_impl
    if not glGetTransformFeedbacki_v_impl:
        fptr = pyglGetFuncAddress('glGetTransformFeedbacki_v')
        if not fptr:
            raise RuntimeError('The function glGetTransformFeedbacki_v is not available')
        glGetTransformFeedbacki_v_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetTransformFeedbacki_v = (lambda xfb,pname,index,param:glGetTransformFeedbacki_v_impl(xfb,pname,index,(c_uint8*len( param )).from_buffer( param )))
    return glGetTransformFeedbacki_v(xfb, pname, index, param)
# <command>
#            <proto>void <name>glGetTransformFeedbackiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>xfb</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>param</name></param>
#        </command>
#        
glGetTransformFeedbackiv_impl=None
def glGetTransformFeedbackiv (xfb, pname, param):
    global glGetTransformFeedbackiv_impl
    if not glGetTransformFeedbackiv_impl:
        fptr = pyglGetFuncAddress('glGetTransformFeedbackiv')
        if not fptr:
            raise RuntimeError('The function glGetTransformFeedbackiv is not available')
        glGetTransformFeedbackiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetTransformFeedbackiv = (lambda xfb,pname,param:glGetTransformFeedbackiv_impl(xfb,pname,(c_uint8*len( param )).from_buffer( param )))
    return glGetTransformFeedbackiv(xfb, pname, param)
# <command>
#            <proto><ptype>GLuint</ptype> <name>glGetUniformBlockIndex</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param len="COMPSIZE()">const <ptype>GLchar</ptype> *<name>uniformBlockName</name></param>
#        </command>
#        
glGetUniformBlockIndex_impl=None
def glGetUniformBlockIndex (program, uniformBlockName):
    global glGetUniformBlockIndex_impl
    if not glGetUniformBlockIndex_impl:
        fptr = pyglGetFuncAddress('glGetUniformBlockIndex')
        if not fptr:
            raise RuntimeError('The function glGetUniformBlockIndex is not available')
        glGetUniformBlockIndex_impl = PYGL_FUNC_TYPE( c_uint ,c_uint, c_void_p)(fptr)
    glGetUniformBlockIndex = (lambda program,uniformBlockName:glGetUniformBlockIndex_impl(program,c_char_p( uniformBlockName .encode() )))
    return glGetUniformBlockIndex(program, uniformBlockName)
# <command>
#            <proto>void <name>glGetUniformIndices</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLsizei</ptype> <name>uniformCount</name></param>
#            <param len="COMPSIZE(uniformCount)">const <ptype>GLchar</ptype> *const*<name>uniformNames</name></param>
#            <param len="COMPSIZE(uniformCount)"><ptype>GLuint</ptype> *<name>uniformIndices</name></param>
#        </command>
#        
glGetUniformIndices_impl=None
def glGetUniformIndices (program, uniformCount, uniformNames, uniformIndices):
    global glGetUniformIndices_impl
    if not glGetUniformIndices_impl:
        fptr = pyglGetFuncAddress('glGetUniformIndices')
        if not fptr:
            raise RuntimeError('The function glGetUniformIndices is not available')
        glGetUniformIndices_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_void_p)(fptr)
    glGetUniformIndices = (lambda program,uniformCount,uniformNames,uniformIndices:glGetUniformIndices_impl(program,uniformCount,c_char_p( uniformNames .encode() ),(c_uint8*len( uniformIndices )).from_buffer( uniformIndices )))
    return glGetUniformIndices(program, uniformCount, uniformNames, uniformIndices)
# <command>
#            <proto><ptype>GLint</ptype> <name>glGetUniformLocation</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
#        </command>
#        
glGetUniformLocation_impl=None
def glGetUniformLocation (program, name):
    global glGetUniformLocation_impl
    if not glGetUniformLocation_impl:
        fptr = pyglGetFuncAddress('glGetUniformLocation')
        if not fptr:
            raise RuntimeError('The function glGetUniformLocation is not available')
        glGetUniformLocation_impl = PYGL_FUNC_TYPE( c_int ,c_uint, c_void_p)(fptr)
    glGetUniformLocation = (lambda program,name:glGetUniformLocation_impl(program,c_char_p( name .encode() )))
    return glGetUniformLocation(program, name)
# <command>
#            <proto>void <name>glGetUniformSubroutineuiv</name></proto>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param len="1"><ptype>GLuint</ptype> *<name>params</name></param>
#        </command>
#        
glGetUniformSubroutineuiv_impl=None
def glGetUniformSubroutineuiv (shadertype, location, params):
    global glGetUniformSubroutineuiv_impl
    if not glGetUniformSubroutineuiv_impl:
        fptr = pyglGetFuncAddress('glGetUniformSubroutineuiv')
        if not fptr:
            raise RuntimeError('The function glGetUniformSubroutineuiv is not available')
        glGetUniformSubroutineuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glGetUniformSubroutineuiv = (lambda shadertype,location,params:glGetUniformSubroutineuiv_impl(shadertype,location,(c_uint8*len( params )).from_buffer( params )))
    return glGetUniformSubroutineuiv(shadertype, location, params)
# <command>
#            <proto>void <name>glGetUniformdv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param len="COMPSIZE(program,location)"><ptype>GLdouble</ptype> *<name>params</name></param>
#        </command>
#        
glGetUniformdv_impl=None
def glGetUniformdv (program, location, params):
    global glGetUniformdv_impl
    if not glGetUniformdv_impl:
        fptr = pyglGetFuncAddress('glGetUniformdv')
        if not fptr:
            raise RuntimeError('The function glGetUniformdv is not available')
        glGetUniformdv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glGetUniformdv = (lambda program,location,params:glGetUniformdv_impl(program,location,(c_uint8*len( params )).from_buffer( params )))
    return glGetUniformdv(program, location, params)
# <command>
#            <proto>void <name>glGetUniformfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param len="COMPSIZE(program,location)"><ptype>GLfloat</ptype> *<name>params</name></param>
#        </command>
#        
glGetUniformfv_impl=None
def glGetUniformfv (program, location, params):
    global glGetUniformfv_impl
    if not glGetUniformfv_impl:
        fptr = pyglGetFuncAddress('glGetUniformfv')
        if not fptr:
            raise RuntimeError('The function glGetUniformfv is not available')
        glGetUniformfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glGetUniformfv = (lambda program,location,params:glGetUniformfv_impl(program,location,(c_uint8*len( params )).from_buffer( params )))
    return glGetUniformfv(program, location, params)
# <command>
#            <proto>void <name>glGetUniformiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param len="COMPSIZE(program,location)"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetUniformiv_impl=None
def glGetUniformiv (program, location, params):
    global glGetUniformiv_impl
    if not glGetUniformiv_impl:
        fptr = pyglGetFuncAddress('glGetUniformiv')
        if not fptr:
            raise RuntimeError('The function glGetUniformiv is not available')
        glGetUniformiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glGetUniformiv = (lambda program,location,params:glGetUniformiv_impl(program,location,(c_uint8*len( params )).from_buffer( params )))
    return glGetUniformiv(program, location, params)
# <command>
#            <proto>void <name>glGetUniformuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param len="COMPSIZE(program,location)"><ptype>GLuint</ptype> *<name>params</name></param>
#        </command>
#        
glGetUniformuiv_impl=None
def glGetUniformuiv (program, location, params):
    global glGetUniformuiv_impl
    if not glGetUniformuiv_impl:
        fptr = pyglGetFuncAddress('glGetUniformuiv')
        if not fptr:
            raise RuntimeError('The function glGetUniformuiv is not available')
        glGetUniformuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glGetUniformuiv = (lambda program,location,params:glGetUniformuiv_impl(program,location,(c_uint8*len( params )).from_buffer( params )))
    return glGetUniformuiv(program, location, params)
# <command>
#            <proto>void <name>glGetVertexArrayIndexed64iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint64</ptype> *<name>param</name></param>
#        </command>
#        
glGetVertexArrayIndexed64iv_impl=None
def glGetVertexArrayIndexed64iv (vaobj, index, pname, param):
    global glGetVertexArrayIndexed64iv_impl
    if not glGetVertexArrayIndexed64iv_impl:
        fptr = pyglGetFuncAddress('glGetVertexArrayIndexed64iv')
        if not fptr:
            raise RuntimeError('The function glGetVertexArrayIndexed64iv is not available')
        glGetVertexArrayIndexed64iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetVertexArrayIndexed64iv = (lambda vaobj,index,pname,param:glGetVertexArrayIndexed64iv_impl(vaobj,index,pname,(c_uint8*len( param )).from_buffer( param )))
    return glGetVertexArrayIndexed64iv(vaobj, index, pname, param)
# <command>
#            <proto>void <name>glGetVertexArrayIndexediv</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>param</name></param>
#        </command>
#        
glGetVertexArrayIndexediv_impl=None
def glGetVertexArrayIndexediv (vaobj, index, pname, param):
    global glGetVertexArrayIndexediv_impl
    if not glGetVertexArrayIndexediv_impl:
        fptr = pyglGetFuncAddress('glGetVertexArrayIndexediv')
        if not fptr:
            raise RuntimeError('The function glGetVertexArrayIndexediv is not available')
        glGetVertexArrayIndexediv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_void_p)(fptr)
    glGetVertexArrayIndexediv = (lambda vaobj,index,pname,param:glGetVertexArrayIndexediv_impl(vaobj,index,pname,(c_uint8*len( param )).from_buffer( param )))
    return glGetVertexArrayIndexediv(vaobj, index, pname, param)
# <command>
#            <proto>void <name>glGetVertexArrayiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> *<name>param</name></param>
#        </command>
#        
glGetVertexArrayiv_impl=None
def glGetVertexArrayiv (vaobj, pname, param):
    global glGetVertexArrayiv_impl
    if not glGetVertexArrayiv_impl:
        fptr = pyglGetFuncAddress('glGetVertexArrayiv')
        if not fptr:
            raise RuntimeError('The function glGetVertexArrayiv is not available')
        glGetVertexArrayiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetVertexArrayiv = (lambda vaobj,pname,param:glGetVertexArrayiv_impl(vaobj,pname,(c_uint8*len( param )).from_buffer( param )))
    return glGetVertexArrayiv(vaobj, pname, param)
# <command>
#            <proto>void <name>glGetVertexAttribIiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param group="VertexAttribEnum"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="1"><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetVertexAttribIiv_impl=None
def glGetVertexAttribIiv (index, pname, params):
    global glGetVertexAttribIiv_impl
    if not glGetVertexAttribIiv_impl:
        fptr = pyglGetFuncAddress('glGetVertexAttribIiv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribIiv is not available')
        glGetVertexAttribIiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetVertexAttribIiv = (lambda index,pname,params:glGetVertexAttribIiv_impl(index,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetVertexAttribIiv(index, pname, params)
# <command>
#            <proto>void <name>glGetVertexAttribIuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param group="VertexAttribEnum"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="1"><ptype>GLuint</ptype> *<name>params</name></param>
#        </command>
#        
glGetVertexAttribIuiv_impl=None
def glGetVertexAttribIuiv (index, pname, params):
    global glGetVertexAttribIuiv_impl
    if not glGetVertexAttribIuiv_impl:
        fptr = pyglGetFuncAddress('glGetVertexAttribIuiv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribIuiv is not available')
        glGetVertexAttribIuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetVertexAttribIuiv = (lambda index,pname,params:glGetVertexAttribIuiv_impl(index,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetVertexAttribIuiv(index, pname, params)
# <command>
#            <proto>void <name>glGetVertexAttribLdv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)"><ptype>GLdouble</ptype> *<name>params</name></param>
#        </command>
#        
glGetVertexAttribLdv_impl=None
def glGetVertexAttribLdv (index, pname, params):
    global glGetVertexAttribLdv_impl
    if not glGetVertexAttribLdv_impl:
        fptr = pyglGetFuncAddress('glGetVertexAttribLdv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribLdv is not available')
        glGetVertexAttribLdv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetVertexAttribLdv = (lambda index,pname,params:glGetVertexAttribLdv_impl(index,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetVertexAttribLdv(index, pname, params)
# <command>
#            <proto>void <name>glGetVertexAttribPointerv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param group="VertexAttribPointerPropertyARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="1">void **<name>pointer</name></param>
#            <glx opcode="209" type="single" />
#        </command>
#        
glGetVertexAttribPointerv_impl=None
def glGetVertexAttribPointerv (index, pname, pointer):
    global glGetVertexAttribPointerv_impl
    if not glGetVertexAttribPointerv_impl:
        fptr = pyglGetFuncAddress('glGetVertexAttribPointerv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribPointerv is not available')
        glGetVertexAttribPointerv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetVertexAttribPointerv = (lambda index,pname,pointer:glGetVertexAttribPointerv_impl(index,pname,(c_uint8*len( pointer )).from_buffer( pointer )))
    return glGetVertexAttribPointerv(index, pname, pointer)
# <command>
#            <proto>void <name>glGetVertexAttribdv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param group="VertexAttribPropertyARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="4"><ptype>GLdouble</ptype> *<name>params</name></param>
#            <glx opcode="1301" type="vendor" />
#        </command>
#        
glGetVertexAttribdv_impl=None
def glGetVertexAttribdv (index, pname, params):
    global glGetVertexAttribdv_impl
    if not glGetVertexAttribdv_impl:
        fptr = pyglGetFuncAddress('glGetVertexAttribdv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribdv is not available')
        glGetVertexAttribdv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetVertexAttribdv = (lambda index,pname,params:glGetVertexAttribdv_impl(index,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetVertexAttribdv(index, pname, params)
# <command>
#            <proto>void <name>glGetVertexAttribfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param group="VertexAttribPropertyARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="4"><ptype>GLfloat</ptype> *<name>params</name></param>
#            <glx opcode="1302" type="vendor" />
#        </command>
#        
glGetVertexAttribfv_impl=None
def glGetVertexAttribfv (index, pname, params):
    global glGetVertexAttribfv_impl
    if not glGetVertexAttribfv_impl:
        fptr = pyglGetFuncAddress('glGetVertexAttribfv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribfv is not available')
        glGetVertexAttribfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetVertexAttribfv = (lambda index,pname,params:glGetVertexAttribfv_impl(index,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetVertexAttribfv(index, pname, params)
# <command>
#            <proto>void <name>glGetVertexAttribiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param group="VertexAttribPropertyARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="4"><ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="1303" type="vendor" />
#        </command>
#        
glGetVertexAttribiv_impl=None
def glGetVertexAttribiv (index, pname, params):
    global glGetVertexAttribiv_impl
    if not glGetVertexAttribiv_impl:
        fptr = pyglGetFuncAddress('glGetVertexAttribiv')
        if not fptr:
            raise RuntimeError('The function glGetVertexAttribiv is not available')
        glGetVertexAttribiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glGetVertexAttribiv = (lambda index,pname,params:glGetVertexAttribiv_impl(index,pname,(c_uint8*len( params )).from_buffer( params )))
    return glGetVertexAttribiv(index, pname, params)
# <command>
#            <proto>void <name>glGetnCompressedTexImage</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLint</ptype> <name>lod</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param>void *<name>pixels</name></param>
#        </command>
#        
glGetnCompressedTexImage_impl=None
def glGetnCompressedTexImage (target, lod, bufSize, pixels):
    global glGetnCompressedTexImage_impl
    if not glGetnCompressedTexImage_impl:
        fptr = pyglGetFuncAddress('glGetnCompressedTexImage')
        if not fptr:
            raise RuntimeError('The function glGetnCompressedTexImage is not available')
        glGetnCompressedTexImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glGetnCompressedTexImage = (lambda target,lod,bufSize,pixels:glGetnCompressedTexImage_impl(target,lod,bufSize,(c_uint8*len( pixels )).from_buffer( pixels )))
    return glGetnCompressedTexImage(target, lod, bufSize, pixels)
# <command>
#            <proto>void <name>glGetnTexImage</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param>void *<name>pixels</name></param>
#        </command>
#        
glGetnTexImage_impl=None
def glGetnTexImage (target, level, format, type, bufSize, pixels):
    global glGetnTexImage_impl
    if not glGetnTexImage_impl:
        fptr = pyglGetFuncAddress('glGetnTexImage')
        if not fptr:
            raise RuntimeError('The function glGetnTexImage is not available')
        glGetnTexImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_uint, c_int, c_void_p)(fptr)
    glGetnTexImage = (lambda target,level,format,type,bufSize,pixels:glGetnTexImage_impl(target,level,format,type,bufSize,(c_uint8*len( pixels )).from_buffer( pixels )))
    return glGetnTexImage(target, level, format, type, bufSize, pixels)
# <command>
#            <proto>void <name>glGetnUniformdv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param><ptype>GLdouble</ptype> *<name>params</name></param>
#        </command>
#        
glGetnUniformdv_impl=None
def glGetnUniformdv (program, location, bufSize, params):
    global glGetnUniformdv_impl
    if not glGetnUniformdv_impl:
        fptr = pyglGetFuncAddress('glGetnUniformdv')
        if not fptr:
            raise RuntimeError('The function glGetnUniformdv is not available')
        glGetnUniformdv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glGetnUniformdv = (lambda program,location,bufSize,params:glGetnUniformdv_impl(program,location,bufSize,(c_uint8*len( params )).from_buffer( params )))
    return glGetnUniformdv(program, location, bufSize, params)
# <command>
#            <proto>void <name>glGetnUniformfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param><ptype>GLfloat</ptype> *<name>params</name></param>
#        </command>
#        
glGetnUniformfv_impl=None
def glGetnUniformfv (program, location, bufSize, params):
    global glGetnUniformfv_impl
    if not glGetnUniformfv_impl:
        fptr = pyglGetFuncAddress('glGetnUniformfv')
        if not fptr:
            raise RuntimeError('The function glGetnUniformfv is not available')
        glGetnUniformfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glGetnUniformfv = (lambda program,location,bufSize,params:glGetnUniformfv_impl(program,location,bufSize,(c_uint8*len( params )).from_buffer( params )))
    return glGetnUniformfv(program, location, bufSize, params)
# <command>
#            <proto>void <name>glGetnUniformiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param><ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glGetnUniformiv_impl=None
def glGetnUniformiv (program, location, bufSize, params):
    global glGetnUniformiv_impl
    if not glGetnUniformiv_impl:
        fptr = pyglGetFuncAddress('glGetnUniformiv')
        if not fptr:
            raise RuntimeError('The function glGetnUniformiv is not available')
        glGetnUniformiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glGetnUniformiv = (lambda program,location,bufSize,params:glGetnUniformiv_impl(program,location,bufSize,(c_uint8*len( params )).from_buffer( params )))
    return glGetnUniformiv(program, location, bufSize, params)
# <command>
#            <proto>void <name>glGetnUniformuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param><ptype>GLuint</ptype> *<name>params</name></param>
#        </command>
#        
glGetnUniformuiv_impl=None
def glGetnUniformuiv (program, location, bufSize, params):
    global glGetnUniformuiv_impl
    if not glGetnUniformuiv_impl:
        fptr = pyglGetFuncAddress('glGetnUniformuiv')
        if not fptr:
            raise RuntimeError('The function glGetnUniformuiv is not available')
        glGetnUniformuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glGetnUniformuiv = (lambda program,location,bufSize,params:glGetnUniformuiv_impl(program,location,bufSize,(c_uint8*len( params )).from_buffer( params )))
    return glGetnUniformuiv(program, location, bufSize, params)
# <command>
#            <proto>void <name>glHint</name></proto>
#            <param group="HintTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="HintMode"><ptype>GLenum</ptype> <name>mode</name></param>
#            <glx opcode="85" type="render" />
#        </command>
#        
glHint_impl=None
def glHint (target, mode):
    global glHint_impl
    if not glHint_impl:
        fptr = pyglGetFuncAddress('glHint')
        if not fptr:
            raise RuntimeError('The function glHint is not available')
        glHint_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glHint = glHint_impl
    return glHint(target, mode)
# <command>
#            <proto>void <name>glInvalidateBufferData</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glInvalidateBufferData_impl=None
def glInvalidateBufferData (buffer):
    global glInvalidateBufferData_impl
    if not glInvalidateBufferData_impl:
        fptr = pyglGetFuncAddress('glInvalidateBufferData')
        if not fptr:
            raise RuntimeError('The function glInvalidateBufferData is not available')
        glInvalidateBufferData_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glInvalidateBufferData = glInvalidateBufferData_impl
    return glInvalidateBufferData(buffer)
# <command>
#            <proto>void <name>glInvalidateBufferSubData</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
#        </command>
#        
glInvalidateBufferSubData_impl=None
def glInvalidateBufferSubData (buffer, offset, length):
    global glInvalidateBufferSubData_impl
    if not glInvalidateBufferSubData_impl:
        fptr = pyglGetFuncAddress('glInvalidateBufferSubData')
        if not fptr:
            raise RuntimeError('The function glInvalidateBufferSubData is not available')
        glInvalidateBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_size_t, c_void_p)(fptr)
    glInvalidateBufferSubData = glInvalidateBufferSubData_impl
    return glInvalidateBufferSubData(buffer, offset, length)
# <command>
#            <proto>void <name>glInvalidateFramebuffer</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizei</ptype> <name>numAttachments</name></param>
#            <param len="numAttachments">const <ptype>GLenum</ptype> *<name>attachments</name></param>
#        </command>
#        
glInvalidateFramebuffer_impl=None
def glInvalidateFramebuffer (target, numAttachments, attachments):
    global glInvalidateFramebuffer_impl
    if not glInvalidateFramebuffer_impl:
        fptr = pyglGetFuncAddress('glInvalidateFramebuffer')
        if not fptr:
            raise RuntimeError('The function glInvalidateFramebuffer is not available')
        glInvalidateFramebuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glInvalidateFramebuffer = (lambda target,numAttachments,attachments:glInvalidateFramebuffer_impl(target,numAttachments,pyglGetAsConstVoidPointer( attachments )))
    return glInvalidateFramebuffer(target, numAttachments, attachments)
# <command>
#            <proto>void <name>glInvalidateNamedFramebufferData</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLsizei</ptype> <name>numAttachments</name></param>
#            <param>const <ptype>GLenum</ptype> *<name>attachments</name></param>
#        </command>
#        
glInvalidateNamedFramebufferData_impl=None
def glInvalidateNamedFramebufferData (framebuffer, numAttachments, attachments):
    global glInvalidateNamedFramebufferData_impl
    if not glInvalidateNamedFramebufferData_impl:
        fptr = pyglGetFuncAddress('glInvalidateNamedFramebufferData')
        if not fptr:
            raise RuntimeError('The function glInvalidateNamedFramebufferData is not available')
        glInvalidateNamedFramebufferData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glInvalidateNamedFramebufferData = (lambda framebuffer,numAttachments,attachments:glInvalidateNamedFramebufferData_impl(framebuffer,numAttachments,pyglGetAsConstVoidPointer( attachments )))
    return glInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments)
# <command>
#            <proto>void <name>glInvalidateNamedFramebufferSubData</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLsizei</ptype> <name>numAttachments</name></param>
#            <param>const <ptype>GLenum</ptype> *<name>attachments</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glInvalidateNamedFramebufferSubData_impl=None
def glInvalidateNamedFramebufferSubData (framebuffer, numAttachments, attachments, x, y, width, height):
    global glInvalidateNamedFramebufferSubData_impl
    if not glInvalidateNamedFramebufferSubData_impl:
        fptr = pyglGetFuncAddress('glInvalidateNamedFramebufferSubData')
        if not fptr:
            raise RuntimeError('The function glInvalidateNamedFramebufferSubData is not available')
        glInvalidateNamedFramebufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_int, c_int, c_int, c_int)(fptr)
    glInvalidateNamedFramebufferSubData = (lambda framebuffer,numAttachments,attachments,x,y,width,height:glInvalidateNamedFramebufferSubData_impl(framebuffer,numAttachments,pyglGetAsConstVoidPointer( attachments ),x,y,width,height))
    return glInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height)
# <command>
#            <proto>void <name>glInvalidateSubFramebuffer</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizei</ptype> <name>numAttachments</name></param>
#            <param len="numAttachments">const <ptype>GLenum</ptype> *<name>attachments</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glInvalidateSubFramebuffer_impl=None
def glInvalidateSubFramebuffer (target, numAttachments, attachments, x, y, width, height):
    global glInvalidateSubFramebuffer_impl
    if not glInvalidateSubFramebuffer_impl:
        fptr = pyglGetFuncAddress('glInvalidateSubFramebuffer')
        if not fptr:
            raise RuntimeError('The function glInvalidateSubFramebuffer is not available')
        glInvalidateSubFramebuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_int, c_int, c_int, c_int)(fptr)
    glInvalidateSubFramebuffer = (lambda target,numAttachments,attachments,x,y,width,height:glInvalidateSubFramebuffer_impl(target,numAttachments,pyglGetAsConstVoidPointer( attachments ),x,y,width,height))
    return glInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height)
# <command>
#            <proto>void <name>glInvalidateTexImage</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#        </command>
#        
glInvalidateTexImage_impl=None
def glInvalidateTexImage (texture, level):
    global glInvalidateTexImage_impl
    if not glInvalidateTexImage_impl:
        fptr = pyglGetFuncAddress('glInvalidateTexImage')
        if not fptr:
            raise RuntimeError('The function glInvalidateTexImage is not available')
        glInvalidateTexImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int)(fptr)
    glInvalidateTexImage = glInvalidateTexImage_impl
    return glInvalidateTexImage(texture, level)
# <command>
#            <proto>void <name>glInvalidateTexSubImage</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#        </command>
#        
glInvalidateTexSubImage_impl=None
def glInvalidateTexSubImage (texture, level, xoffset, yoffset, zoffset, width, height, depth):
    global glInvalidateTexSubImage_impl
    if not glInvalidateTexSubImage_impl:
        fptr = pyglGetFuncAddress('glInvalidateTexSubImage')
        if not fptr:
            raise RuntimeError('The function glInvalidateTexSubImage is not available')
        glInvalidateTexSubImage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int)(fptr)
    glInvalidateTexSubImage = glInvalidateTexSubImage_impl
    return glInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glIsBuffer_impl=None
def glIsBuffer (buffer):
    global glIsBuffer_impl
    if not glIsBuffer_impl:
        fptr = pyglGetFuncAddress('glIsBuffer')
        if not fptr:
            raise RuntimeError('The function glIsBuffer is not available')
        glIsBuffer_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsBuffer = glIsBuffer_impl
    return glIsBuffer(buffer)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsEnabled</name></proto>
#            <param group="EnableCap"><ptype>GLenum</ptype> <name>cap</name></param>
#            <glx opcode="140" type="single" />
#        </command>
#        
glIsEnabled_impl=None
def glIsEnabled (cap):
    global glIsEnabled_impl
    if not glIsEnabled_impl:
        fptr = pyglGetFuncAddress('glIsEnabled')
        if not fptr:
            raise RuntimeError('The function glIsEnabled is not available')
        glIsEnabled_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsEnabled = glIsEnabled_impl
    return glIsEnabled(cap)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsEnabledi</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glIsEnabledi_impl=None
def glIsEnabledi (target, index):
    global glIsEnabledi_impl
    if not glIsEnabledi_impl:
        fptr = pyglGetFuncAddress('glIsEnabledi')
        if not fptr:
            raise RuntimeError('The function glIsEnabledi is not available')
        glIsEnabledi_impl = PYGL_FUNC_TYPE( c_char ,c_uint, c_uint)(fptr)
    glIsEnabledi = glIsEnabledi_impl
    return glIsEnabledi(target, index)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsFramebuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <glx opcode="1425" type="vendor" />
#        </command>
#        
glIsFramebuffer_impl=None
def glIsFramebuffer (framebuffer):
    global glIsFramebuffer_impl
    if not glIsFramebuffer_impl:
        fptr = pyglGetFuncAddress('glIsFramebuffer')
        if not fptr:
            raise RuntimeError('The function glIsFramebuffer is not available')
        glIsFramebuffer_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsFramebuffer = glIsFramebuffer_impl
    return glIsFramebuffer(framebuffer)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsProgram</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <glx opcode="197" type="single" />
#        </command>
#        
glIsProgram_impl=None
def glIsProgram (program):
    global glIsProgram_impl
    if not glIsProgram_impl:
        fptr = pyglGetFuncAddress('glIsProgram')
        if not fptr:
            raise RuntimeError('The function glIsProgram is not available')
        glIsProgram_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsProgram = glIsProgram_impl
    return glIsProgram(program)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsProgramPipeline</name></proto>
#            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
#        </command>
#        
glIsProgramPipeline_impl=None
def glIsProgramPipeline (pipeline):
    global glIsProgramPipeline_impl
    if not glIsProgramPipeline_impl:
        fptr = pyglGetFuncAddress('glIsProgramPipeline')
        if not fptr:
            raise RuntimeError('The function glIsProgramPipeline is not available')
        glIsProgramPipeline_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsProgramPipeline = glIsProgramPipeline_impl
    return glIsProgramPipeline(pipeline)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsQuery</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <glx opcode="163" type="single" />
#        </command>
#        
glIsQuery_impl=None
def glIsQuery (id):
    global glIsQuery_impl
    if not glIsQuery_impl:
        fptr = pyglGetFuncAddress('glIsQuery')
        if not fptr:
            raise RuntimeError('The function glIsQuery is not available')
        glIsQuery_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsQuery = glIsQuery_impl
    return glIsQuery(id)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsRenderbuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
#            <glx opcode="1422" type="vendor" />
#        </command>
#        
glIsRenderbuffer_impl=None
def glIsRenderbuffer (renderbuffer):
    global glIsRenderbuffer_impl
    if not glIsRenderbuffer_impl:
        fptr = pyglGetFuncAddress('glIsRenderbuffer')
        if not fptr:
            raise RuntimeError('The function glIsRenderbuffer is not available')
        glIsRenderbuffer_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsRenderbuffer = glIsRenderbuffer_impl
    return glIsRenderbuffer(renderbuffer)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsSampler</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#        </command>
#        
glIsSampler_impl=None
def glIsSampler (sampler):
    global glIsSampler_impl
    if not glIsSampler_impl:
        fptr = pyglGetFuncAddress('glIsSampler')
        if not fptr:
            raise RuntimeError('The function glIsSampler is not available')
        glIsSampler_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsSampler = glIsSampler_impl
    return glIsSampler(sampler)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsShader</name></proto>
#            <param><ptype>GLuint</ptype> <name>shader</name></param>
#            <glx opcode="196" type="single" />
#        </command>
#        
glIsShader_impl=None
def glIsShader (shader):
    global glIsShader_impl
    if not glIsShader_impl:
        fptr = pyglGetFuncAddress('glIsShader')
        if not fptr:
            raise RuntimeError('The function glIsShader is not available')
        glIsShader_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsShader = glIsShader_impl
    return glIsShader(shader)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsSync</name></proto>
#            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
#        </command>
#        
glIsSync_impl=None
def glIsSync (sync):
    global glIsSync_impl
    if not glIsSync_impl:
        fptr = pyglGetFuncAddress('glIsSync')
        if not fptr:
            raise RuntimeError('The function glIsSync is not available')
        glIsSync_impl = PYGL_FUNC_TYPE( c_char ,c_void_p)(fptr)
    glIsSync = glIsSync_impl
    return glIsSync(sync)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsTexture</name></proto>
#            <param group="Texture"><ptype>GLuint</ptype> <name>texture</name></param>
#            <glx opcode="146" type="single" />
#        </command>
#        
glIsTexture_impl=None
def glIsTexture (texture):
    global glIsTexture_impl
    if not glIsTexture_impl:
        fptr = pyglGetFuncAddress('glIsTexture')
        if not fptr:
            raise RuntimeError('The function glIsTexture is not available')
        glIsTexture_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsTexture = glIsTexture_impl
    return glIsTexture(texture)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsTransformFeedback</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#        </command>
#        
glIsTransformFeedback_impl=None
def glIsTransformFeedback (id):
    global glIsTransformFeedback_impl
    if not glIsTransformFeedback_impl:
        fptr = pyglGetFuncAddress('glIsTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glIsTransformFeedback is not available')
        glIsTransformFeedback_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsTransformFeedback = glIsTransformFeedback_impl
    return glIsTransformFeedback(id)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsVertexArray</name></proto>
#            <param><ptype>GLuint</ptype> <name>array</name></param>
#            <glx opcode="207" type="single" />
#        </command>
#        
glIsVertexArray_impl=None
def glIsVertexArray (array):
    global glIsVertexArray_impl
    if not glIsVertexArray_impl:
        fptr = pyglGetFuncAddress('glIsVertexArray')
        if not fptr:
            raise RuntimeError('The function glIsVertexArray is not available')
        glIsVertexArray_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glIsVertexArray = glIsVertexArray_impl
    return glIsVertexArray(array)
# <command>
#            <proto>void <name>glLineWidth</name></proto>
#            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>width</name></param>
#            <glx opcode="95" type="render" />
#        </command>
#        
glLineWidth_impl=None
def glLineWidth (width):
    global glLineWidth_impl
    if not glLineWidth_impl:
        fptr = pyglGetFuncAddress('glLineWidth')
        if not fptr:
            raise RuntimeError('The function glLineWidth is not available')
        glLineWidth_impl = PYGL_FUNC_TYPE( None ,c_float)(fptr)
    glLineWidth = glLineWidth_impl
    return glLineWidth(width)
# <command>
#            <proto>void <name>glLinkProgram</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#        </command>
#        
glLinkProgram_impl=None
def glLinkProgram (program):
    global glLinkProgram_impl
    if not glLinkProgram_impl:
        fptr = pyglGetFuncAddress('glLinkProgram')
        if not fptr:
            raise RuntimeError('The function glLinkProgram is not available')
        glLinkProgram_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glLinkProgram = glLinkProgram_impl
    return glLinkProgram(program)
# <command>
#            <proto>void <name>glLogicOp</name></proto>
#            <param group="LogicOp"><ptype>GLenum</ptype> <name>opcode</name></param>
#            <glx opcode="161" type="render" />
#        </command>
#        
glLogicOp_impl=None
def glLogicOp (opcode):
    global glLogicOp_impl
    if not glLogicOp_impl:
        fptr = pyglGetFuncAddress('glLogicOp')
        if not fptr:
            raise RuntimeError('The function glLogicOp is not available')
        glLogicOp_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glLogicOp = glLogicOp_impl
    return glLogicOp(opcode)
# <command>
#            <proto>void *<name>glMapBuffer</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferAccessARB"><ptype>GLenum</ptype> <name>access</name></param>
#        </command>
#        
glMapBuffer_impl=None
def glMapBuffer (target, access):
    global glMapBuffer_impl
    if not glMapBuffer_impl:
        fptr = pyglGetFuncAddress('glMapBuffer')
        if not fptr:
            raise RuntimeError('The function glMapBuffer is not available')
        glMapBuffer_impl = PYGL_FUNC_TYPE( c_void_p ,c_uint, c_uint)(fptr)
    glMapBuffer = glMapBuffer_impl
    return glMapBuffer(target, access)
# <command>
#            <proto>void *<name>glMapBufferRange</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
#            <param group="BufferAccessMask"><ptype>GLbitfield</ptype> <name>access</name></param>
#            <glx opcode="205" type="single" />
#        </command>
#        
glMapBufferRange_impl=None
def glMapBufferRange (target, offset, length, access):
    global glMapBufferRange_impl
    if not glMapBufferRange_impl:
        fptr = pyglGetFuncAddress('glMapBufferRange')
        if not fptr:
            raise RuntimeError('The function glMapBufferRange is not available')
        glMapBufferRange_impl = PYGL_FUNC_TYPE( c_void_p ,c_uint, c_size_t, c_void_p, c_uint)(fptr)
    glMapBufferRange = glMapBufferRange_impl
    return glMapBufferRange(target, offset, length, access)
# <command>
#            <proto>void *<name>glMapNamedBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLenum</ptype> <name>access</name></param>
#        </command>
#        
glMapNamedBuffer_impl=None
def glMapNamedBuffer (buffer, access):
    global glMapNamedBuffer_impl
    if not glMapNamedBuffer_impl:
        fptr = pyglGetFuncAddress('glMapNamedBuffer')
        if not fptr:
            raise RuntimeError('The function glMapNamedBuffer is not available')
        glMapNamedBuffer_impl = PYGL_FUNC_TYPE( c_void_p ,c_uint, c_uint)(fptr)
    glMapNamedBuffer = glMapNamedBuffer_impl
    return glMapNamedBuffer(buffer, access)
# <command>
#            <proto>void *<name>glMapNamedBufferRange</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
#            <param><ptype>GLbitfield</ptype> <name>access</name></param>
#        </command>
#        
glMapNamedBufferRange_impl=None
def glMapNamedBufferRange (buffer, offset, length, access):
    global glMapNamedBufferRange_impl
    if not glMapNamedBufferRange_impl:
        fptr = pyglGetFuncAddress('glMapNamedBufferRange')
        if not fptr:
            raise RuntimeError('The function glMapNamedBufferRange is not available')
        glMapNamedBufferRange_impl = PYGL_FUNC_TYPE( c_void_p ,c_uint, c_size_t, c_void_p, c_uint)(fptr)
    glMapNamedBufferRange = glMapNamedBufferRange_impl
    return glMapNamedBufferRange(buffer, offset, length, access)
# <command>
#            <proto>void <name>glMemoryBarrier</name></proto>
#            <param><ptype>GLbitfield</ptype> <name>barriers</name></param>
#        </command>
#        
glMemoryBarrier_impl=None
def glMemoryBarrier (barriers):
    global glMemoryBarrier_impl
    if not glMemoryBarrier_impl:
        fptr = pyglGetFuncAddress('glMemoryBarrier')
        if not fptr:
            raise RuntimeError('The function glMemoryBarrier is not available')
        glMemoryBarrier_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glMemoryBarrier = glMemoryBarrier_impl
    return glMemoryBarrier(barriers)
# <command>
#            <proto>void <name>glMemoryBarrierByRegion</name></proto>
#            <param><ptype>GLbitfield</ptype> <name>barriers</name></param>
#        </command>
#        
glMemoryBarrierByRegion_impl=None
def glMemoryBarrierByRegion (barriers):
    global glMemoryBarrierByRegion_impl
    if not glMemoryBarrierByRegion_impl:
        fptr = pyglGetFuncAddress('glMemoryBarrierByRegion')
        if not fptr:
            raise RuntimeError('The function glMemoryBarrierByRegion is not available')
        glMemoryBarrierByRegion_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glMemoryBarrierByRegion = glMemoryBarrierByRegion_impl
    return glMemoryBarrierByRegion(barriers)
# <command>
#            <proto>void <name>glMinSampleShading</name></proto>
#            <param group="ColorF"><ptype>GLfloat</ptype> <name>value</name></param>
#        </command>
#        
glMinSampleShading_impl=None
def glMinSampleShading (value):
    global glMinSampleShading_impl
    if not glMinSampleShading_impl:
        fptr = pyglGetFuncAddress('glMinSampleShading')
        if not fptr:
            raise RuntimeError('The function glMinSampleShading is not available')
        glMinSampleShading_impl = PYGL_FUNC_TYPE( None ,c_float)(fptr)
    glMinSampleShading = glMinSampleShading_impl
    return glMinSampleShading(value)
# <command>
#            <proto>void <name>glMultiDrawArrays</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param len="COMPSIZE(count)">const <ptype>GLint</ptype> *<name>first</name></param>
#            <param len="COMPSIZE(drawcount)">const <ptype>GLsizei</ptype> *<name>count</name></param>
#            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
#        </command>
#        
glMultiDrawArrays_impl=None
def glMultiDrawArrays (mode, first, count, drawcount):
    global glMultiDrawArrays_impl
    if not glMultiDrawArrays_impl:
        fptr = pyglGetFuncAddress('glMultiDrawArrays')
        if not fptr:
            raise RuntimeError('The function glMultiDrawArrays is not available')
        glMultiDrawArrays_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p, c_void_p, c_int)(fptr)
    glMultiDrawArrays = (lambda mode,first,count,drawcount:glMultiDrawArrays_impl(mode,pyglGetAsConstVoidPointer( first ),pyglGetAsConstVoidPointer( count ),drawcount))
    return glMultiDrawArrays(mode, first, count, drawcount)
# <command>
#            <proto>void <name>glMultiDrawArraysIndirect</name></proto>
#            <param><ptype>GLenum</ptype> <name>mode</name></param>
#            <param len="COMPSIZE(drawcount,stride)">const void *<name>indirect</name></param>
#            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
#            <param><ptype>GLsizei</ptype> <name>stride</name></param>
#        </command>
#        
glMultiDrawArraysIndirect_impl=None
def glMultiDrawArraysIndirect (mode, indirect, drawcount, stride):
    global glMultiDrawArraysIndirect_impl
    if not glMultiDrawArraysIndirect_impl:
        fptr = pyglGetFuncAddress('glMultiDrawArraysIndirect')
        if not fptr:
            raise RuntimeError('The function glMultiDrawArraysIndirect is not available')
        glMultiDrawArraysIndirect_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p, c_int, c_int)(fptr)
    glMultiDrawArraysIndirect = (lambda mode,indirect,drawcount,stride:glMultiDrawArraysIndirect_impl(mode,pyglGetAsConstVoidPointer( indirect ),drawcount,stride))
    return glMultiDrawArraysIndirect(mode, indirect, drawcount, stride)
# <command>
#            <proto>void <name>glMultiDrawElements</name></proto>
#            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
#            <param len="COMPSIZE(drawcount)">const <ptype>GLsizei</ptype> *<name>count</name></param>
#            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(drawcount)">const void *const*<name>indices</name></param>
#            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
#        </command>
#        
glMultiDrawElements_impl=None
def glMultiDrawElements (mode, count, type, indices, drawcount):
    global glMultiDrawElements_impl
    if not glMultiDrawElements_impl:
        fptr = pyglGetFuncAddress('glMultiDrawElements')
        if not fptr:
            raise RuntimeError('The function glMultiDrawElements is not available')
        glMultiDrawElements_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p, c_uint, c_void_p, c_int)(fptr)
    glMultiDrawElements = (lambda mode,count,type,indices,drawcount:glMultiDrawElements_impl(mode,pyglGetAsConstVoidPointer( count ),type,pyglGetAsConstVoidPointer( indices ),drawcount))
    return glMultiDrawElements(mode, count, type, indices, drawcount)
# <command>
#            <proto>void <name>glMultiDrawElementsBaseVertex</name></proto>
#            <param><ptype>GLenum</ptype> <name>mode</name></param>
#            <param len="COMPSIZE(drawcount)">const <ptype>GLsizei</ptype> *<name>count</name></param>
#            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(drawcount)">const void *const*<name>indices</name></param>
#            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
#            <param len="COMPSIZE(drawcount)">const <ptype>GLint</ptype> *<name>basevertex</name></param>
#        </command>
#        
glMultiDrawElementsBaseVertex_impl=None
def glMultiDrawElementsBaseVertex (mode, count, type, indices, drawcount, basevertex):
    global glMultiDrawElementsBaseVertex_impl
    if not glMultiDrawElementsBaseVertex_impl:
        fptr = pyglGetFuncAddress('glMultiDrawElementsBaseVertex')
        if not fptr:
            raise RuntimeError('The function glMultiDrawElementsBaseVertex is not available')
        glMultiDrawElementsBaseVertex_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p, c_uint, c_void_p, c_int, c_void_p)(fptr)
    glMultiDrawElementsBaseVertex = (lambda mode,count,type,indices,drawcount,basevertex:glMultiDrawElementsBaseVertex_impl(mode,pyglGetAsConstVoidPointer( count ),type,pyglGetAsConstVoidPointer( indices ),drawcount,pyglGetAsConstVoidPointer( basevertex )))
    return glMultiDrawElementsBaseVertex(mode, count, type, indices, drawcount, basevertex)
# <command>
#            <proto>void <name>glMultiDrawElementsIndirect</name></proto>
#            <param><ptype>GLenum</ptype> <name>mode</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(drawcount,stride)">const void *<name>indirect</name></param>
#            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
#            <param><ptype>GLsizei</ptype> <name>stride</name></param>
#        </command>
#        
glMultiDrawElementsIndirect_impl=None
def glMultiDrawElementsIndirect (mode, type, indirect, drawcount, stride):
    global glMultiDrawElementsIndirect_impl
    if not glMultiDrawElementsIndirect_impl:
        fptr = pyglGetFuncAddress('glMultiDrawElementsIndirect')
        if not fptr:
            raise RuntimeError('The function glMultiDrawElementsIndirect is not available')
        glMultiDrawElementsIndirect_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p, c_int, c_int)(fptr)
    glMultiDrawElementsIndirect = (lambda mode,type,indirect,drawcount,stride:glMultiDrawElementsIndirect_impl(mode,type,pyglGetAsConstVoidPointer( indirect ),drawcount,stride))
    return glMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride)
# <command>
#            <proto>void <name>glNamedBufferData</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param>const void *<name>data</name></param>
#            <param><ptype>GLenum</ptype> <name>usage</name></param>
#        </command>
#        
glNamedBufferData_impl=None
def glNamedBufferData (buffer, size, data, usage):
    global glNamedBufferData_impl
    if not glNamedBufferData_impl:
        fptr = pyglGetFuncAddress('glNamedBufferData')
        if not fptr:
            raise RuntimeError('The function glNamedBufferData is not available')
        glNamedBufferData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p, c_void_p, c_uint)(fptr)
    glNamedBufferData = (lambda buffer,size,data,usage:glNamedBufferData_impl(buffer,size,pyglGetAsConstVoidPointer( data ),usage))
    return glNamedBufferData(buffer, size, data, usage)
# <command>
#            <proto>void <name>glNamedBufferStorage</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param len="size">const void *<name>data</name></param>
#            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
#        </command>
#        
glNamedBufferStorage_impl=None
def glNamedBufferStorage (buffer, size, data, flags):
    global glNamedBufferStorage_impl
    if not glNamedBufferStorage_impl:
        fptr = pyglGetFuncAddress('glNamedBufferStorage')
        if not fptr:
            raise RuntimeError('The function glNamedBufferStorage is not available')
        glNamedBufferStorage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p, c_void_p, c_uint)(fptr)
    glNamedBufferStorage = (lambda buffer,size,data,flags:glNamedBufferStorage_impl(buffer,size,pyglGetAsConstVoidPointer( data ),flags))
    return glNamedBufferStorage(buffer, size, data, flags)
# <command>
#            <proto>void <name>glNamedBufferSubData</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#            <param len="COMPSIZE(size)">const void *<name>data</name></param>
#        </command>
#        
glNamedBufferSubData_impl=None
def glNamedBufferSubData (buffer, offset, size, data):
    global glNamedBufferSubData_impl
    if not glNamedBufferSubData_impl:
        fptr = pyglGetFuncAddress('glNamedBufferSubData')
        if not fptr:
            raise RuntimeError('The function glNamedBufferSubData is not available')
        glNamedBufferSubData_impl = PYGL_FUNC_TYPE( None ,c_uint, c_size_t, c_void_p, c_void_p)(fptr)
    glNamedBufferSubData = (lambda buffer,offset,size,data:glNamedBufferSubData_impl(buffer,offset,size,pyglGetAsConstVoidPointer( data )))
    return glNamedBufferSubData(buffer, offset, size, data)
# <command>
#            <proto>void <name>glNamedFramebufferDrawBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>buf</name></param>
#        </command>
#        
glNamedFramebufferDrawBuffer_impl=None
def glNamedFramebufferDrawBuffer (framebuffer, buf):
    global glNamedFramebufferDrawBuffer_impl
    if not glNamedFramebufferDrawBuffer_impl:
        fptr = pyglGetFuncAddress('glNamedFramebufferDrawBuffer')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferDrawBuffer is not available')
        glNamedFramebufferDrawBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glNamedFramebufferDrawBuffer = glNamedFramebufferDrawBuffer_impl
    return glNamedFramebufferDrawBuffer(framebuffer, buf)
# <command>
#            <proto>void <name>glNamedFramebufferDrawBuffers</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLsizei</ptype> <name>n</name></param>
#            <param>const <ptype>GLenum</ptype> *<name>bufs</name></param>
#        </command>
#        
glNamedFramebufferDrawBuffers_impl=None
def glNamedFramebufferDrawBuffers (framebuffer, n, bufs):
    global glNamedFramebufferDrawBuffers_impl
    if not glNamedFramebufferDrawBuffers_impl:
        fptr = pyglGetFuncAddress('glNamedFramebufferDrawBuffers')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferDrawBuffers is not available')
        glNamedFramebufferDrawBuffers_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glNamedFramebufferDrawBuffers = (lambda framebuffer,n,bufs:glNamedFramebufferDrawBuffers_impl(framebuffer,n,pyglGetAsConstVoidPointer( bufs )))
    return glNamedFramebufferDrawBuffers(framebuffer, n, bufs)
# <command>
#            <proto>void <name>glNamedFramebufferParameteri</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> <name>param</name></param>
#        </command>
#        
glNamedFramebufferParameteri_impl=None
def glNamedFramebufferParameteri (framebuffer, pname, param):
    global glNamedFramebufferParameteri_impl
    if not glNamedFramebufferParameteri_impl:
        fptr = pyglGetFuncAddress('glNamedFramebufferParameteri')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferParameteri is not available')
        glNamedFramebufferParameteri_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int)(fptr)
    glNamedFramebufferParameteri = glNamedFramebufferParameteri_impl
    return glNamedFramebufferParameteri(framebuffer, pname, param)
# <command>
#            <proto>void <name>glNamedFramebufferReadBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>src</name></param>
#        </command>
#        
glNamedFramebufferReadBuffer_impl=None
def glNamedFramebufferReadBuffer (framebuffer, src):
    global glNamedFramebufferReadBuffer_impl
    if not glNamedFramebufferReadBuffer_impl:
        fptr = pyglGetFuncAddress('glNamedFramebufferReadBuffer')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferReadBuffer is not available')
        glNamedFramebufferReadBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glNamedFramebufferReadBuffer = glNamedFramebufferReadBuffer_impl
    return glNamedFramebufferReadBuffer(framebuffer, src)
# <command>
#            <proto>void <name>glNamedFramebufferRenderbuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLenum</ptype> <name>renderbuffertarget</name></param>
#            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
#        </command>
#        
glNamedFramebufferRenderbuffer_impl=None
def glNamedFramebufferRenderbuffer (framebuffer, attachment, renderbuffertarget, renderbuffer):
    global glNamedFramebufferRenderbuffer_impl
    if not glNamedFramebufferRenderbuffer_impl:
        fptr = pyglGetFuncAddress('glNamedFramebufferRenderbuffer')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferRenderbuffer is not available')
        glNamedFramebufferRenderbuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint)(fptr)
    glNamedFramebufferRenderbuffer = glNamedFramebufferRenderbuffer_impl
    return glNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer)
# <command>
#            <proto>void <name>glNamedFramebufferTexture</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#        </command>
#        
glNamedFramebufferTexture_impl=None
def glNamedFramebufferTexture (framebuffer, attachment, texture, level):
    global glNamedFramebufferTexture_impl
    if not glNamedFramebufferTexture_impl:
        fptr = pyglGetFuncAddress('glNamedFramebufferTexture')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferTexture is not available')
        glNamedFramebufferTexture_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int)(fptr)
    glNamedFramebufferTexture = glNamedFramebufferTexture_impl
    return glNamedFramebufferTexture(framebuffer, attachment, texture, level)
# <command>
#            <proto>void <name>glNamedFramebufferTextureLayer</name></proto>
#            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>attachment</name></param>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>layer</name></param>
#        </command>
#        
glNamedFramebufferTextureLayer_impl=None
def glNamedFramebufferTextureLayer (framebuffer, attachment, texture, level, layer):
    global glNamedFramebufferTextureLayer_impl
    if not glNamedFramebufferTextureLayer_impl:
        fptr = pyglGetFuncAddress('glNamedFramebufferTextureLayer')
        if not fptr:
            raise RuntimeError('The function glNamedFramebufferTextureLayer is not available')
        glNamedFramebufferTextureLayer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_int, c_int)(fptr)
    glNamedFramebufferTextureLayer = glNamedFramebufferTextureLayer_impl
    return glNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer)
# <command>
#            <proto>void <name>glNamedRenderbufferStorage</name></proto>
#            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glNamedRenderbufferStorage_impl=None
def glNamedRenderbufferStorage (renderbuffer, internalformat, width, height):
    global glNamedRenderbufferStorage_impl
    if not glNamedRenderbufferStorage_impl:
        fptr = pyglGetFuncAddress('glNamedRenderbufferStorage')
        if not fptr:
            raise RuntimeError('The function glNamedRenderbufferStorage is not available')
        glNamedRenderbufferStorage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_int)(fptr)
    glNamedRenderbufferStorage = glNamedRenderbufferStorage_impl
    return glNamedRenderbufferStorage(renderbuffer, internalformat, width, height)
# <command>
#            <proto>void <name>glNamedRenderbufferStorageMultisample</name></proto>
#            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
#            <param><ptype>GLsizei</ptype> <name>samples</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glNamedRenderbufferStorageMultisample_impl=None
def glNamedRenderbufferStorageMultisample (renderbuffer, samples, internalformat, width, height):
    global glNamedRenderbufferStorageMultisample_impl
    if not glNamedRenderbufferStorageMultisample_impl:
        fptr = pyglGetFuncAddress('glNamedRenderbufferStorageMultisample')
        if not fptr:
            raise RuntimeError('The function glNamedRenderbufferStorageMultisample is not available')
        glNamedRenderbufferStorageMultisample_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int)(fptr)
    glNamedRenderbufferStorageMultisample = glNamedRenderbufferStorageMultisample_impl
    return glNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height)
# <command>
#            <proto>void <name>glObjectLabel</name></proto>
#            <param><ptype>GLenum</ptype> <name>identifier</name></param>
#            <param><ptype>GLuint</ptype> <name>name</name></param>
#            <param><ptype>GLsizei</ptype> <name>length</name></param>
#            <param len="COMPSIZE(label,length)">const <ptype>GLchar</ptype> *<name>label</name></param>
#        </command>
#        
glObjectLabel_impl=None
def glObjectLabel (identifier, name, length, label):
    global glObjectLabel_impl
    if not glObjectLabel_impl:
        fptr = pyglGetFuncAddress('glObjectLabel')
        if not fptr:
            raise RuntimeError('The function glObjectLabel is not available')
        glObjectLabel_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p)(fptr)
    glObjectLabel = (lambda identifier,name,length,label:glObjectLabel_impl(identifier,name,length,c_char_p( label .encode() )))
    return glObjectLabel(identifier, name, length, label)
# <command>
#            <proto>void <name>glObjectPtrLabel</name></proto>
#            <param>const void *<name>ptr</name></param>
#            <param><ptype>GLsizei</ptype> <name>length</name></param>
#            <param len="COMPSIZE(label,length)">const <ptype>GLchar</ptype> *<name>label</name></param>
#        </command>
#        
glObjectPtrLabel_impl=None
def glObjectPtrLabel (ptr, length, label):
    global glObjectPtrLabel_impl
    if not glObjectPtrLabel_impl:
        fptr = pyglGetFuncAddress('glObjectPtrLabel')
        if not fptr:
            raise RuntimeError('The function glObjectPtrLabel is not available')
        glObjectPtrLabel_impl = PYGL_FUNC_TYPE( None ,c_void_p, c_int, c_void_p)(fptr)
    glObjectPtrLabel = (lambda ptr,length,label:glObjectPtrLabel_impl(pyglGetAsConstVoidPointer( ptr ),length,c_char_p( label .encode() )))
    return glObjectPtrLabel(ptr, length, label)
# <command>
#            <proto>void <name>glPatchParameterfv</name></proto>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)">const <ptype>GLfloat</ptype> *<name>values</name></param>
#        </command>
#        
glPatchParameterfv_impl=None
def glPatchParameterfv (pname, values):
    global glPatchParameterfv_impl
    if not glPatchParameterfv_impl:
        fptr = pyglGetFuncAddress('glPatchParameterfv')
        if not fptr:
            raise RuntimeError('The function glPatchParameterfv is not available')
        glPatchParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glPatchParameterfv = (lambda pname,values:glPatchParameterfv_impl(pname,pyglGetAsConstVoidPointer( values )))
    return glPatchParameterfv(pname, values)
# <command>
#            <proto>void <name>glPatchParameteri</name></proto>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> <name>value</name></param>
#        </command>
#        
glPatchParameteri_impl=None
def glPatchParameteri (pname, value):
    global glPatchParameteri_impl
    if not glPatchParameteri_impl:
        fptr = pyglGetFuncAddress('glPatchParameteri')
        if not fptr:
            raise RuntimeError('The function glPatchParameteri is not available')
        glPatchParameteri_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int)(fptr)
    glPatchParameteri = glPatchParameteri_impl
    return glPatchParameteri(pname, value)
# <command>
#            <proto>void <name>glPauseTransformFeedback</name></proto>
#        </command>
#        
glPauseTransformFeedback_impl=None
def glPauseTransformFeedback ():
    global glPauseTransformFeedback_impl
    if not glPauseTransformFeedback_impl:
        fptr = pyglGetFuncAddress('glPauseTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glPauseTransformFeedback is not available')
        glPauseTransformFeedback_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glPauseTransformFeedback = glPauseTransformFeedback_impl
    return glPauseTransformFeedback()
# <command>
#            <proto>void <name>glPixelStoref</name></proto>
#            <param group="PixelStoreParameter"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>param</name></param>
#            <glx opcode="109" type="single" />
#        </command>
#        
glPixelStoref_impl=None
def glPixelStoref (pname, param):
    global glPixelStoref_impl
    if not glPixelStoref_impl:
        fptr = pyglGetFuncAddress('glPixelStoref')
        if not fptr:
            raise RuntimeError('The function glPixelStoref is not available')
        glPixelStoref_impl = PYGL_FUNC_TYPE( None ,c_uint, c_float)(fptr)
    glPixelStoref = glPixelStoref_impl
    return glPixelStoref(pname, param)
# <command>
#            <proto>void <name>glPixelStorei</name></proto>
#            <param group="PixelStoreParameter"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>param</name></param>
#            <glx opcode="110" type="single" />
#        </command>
#        
glPixelStorei_impl=None
def glPixelStorei (pname, param):
    global glPixelStorei_impl
    if not glPixelStorei_impl:
        fptr = pyglGetFuncAddress('glPixelStorei')
        if not fptr:
            raise RuntimeError('The function glPixelStorei is not available')
        glPixelStorei_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int)(fptr)
    glPixelStorei = glPixelStorei_impl
    return glPixelStorei(pname, param)
# <command>
#            <proto>void <name>glPointParameterf</name></proto>
#            <param group="PointParameterNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>param</name></param>
#            <glx opcode="2065" type="render" />
#        </command>
#        
glPointParameterf_impl=None
def glPointParameterf (pname, param):
    global glPointParameterf_impl
    if not glPointParameterf_impl:
        fptr = pyglGetFuncAddress('glPointParameterf')
        if not fptr:
            raise RuntimeError('The function glPointParameterf is not available')
        glPointParameterf_impl = PYGL_FUNC_TYPE( None ,c_uint, c_float)(fptr)
    glPointParameterf = glPointParameterf_impl
    return glPointParameterf(pname, param)
# <command>
#            <proto>void <name>glPointParameterfv</name></proto>
#            <param group="PointParameterNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="CheckedFloat32" len="COMPSIZE(pname)">const <ptype>GLfloat</ptype> *<name>params</name></param>
#            <glx opcode="2066" type="render" />
#        </command>
#        
glPointParameterfv_impl=None
def glPointParameterfv (pname, params):
    global glPointParameterfv_impl
    if not glPointParameterfv_impl:
        fptr = pyglGetFuncAddress('glPointParameterfv')
        if not fptr:
            raise RuntimeError('The function glPointParameterfv is not available')
        glPointParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glPointParameterfv = (lambda pname,params:glPointParameterfv_impl(pname,pyglGetAsConstVoidPointer( params )))
    return glPointParameterfv(pname, params)
# <command>
#            <proto>void <name>glPointParameteri</name></proto>
#            <param group="PointParameterNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> <name>param</name></param>
#            <glx opcode="4221" type="render" />
#        </command>
#        
glPointParameteri_impl=None
def glPointParameteri (pname, param):
    global glPointParameteri_impl
    if not glPointParameteri_impl:
        fptr = pyglGetFuncAddress('glPointParameteri')
        if not fptr:
            raise RuntimeError('The function glPointParameteri is not available')
        glPointParameteri_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int)(fptr)
    glPointParameteri = glPointParameteri_impl
    return glPointParameteri(pname, param)
# <command>
#            <proto>void <name>glPointParameteriv</name></proto>
#            <param group="PointParameterNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="4222" type="render" />
#        </command>
#        
glPointParameteriv_impl=None
def glPointParameteriv (pname, params):
    global glPointParameteriv_impl
    if not glPointParameteriv_impl:
        fptr = pyglGetFuncAddress('glPointParameteriv')
        if not fptr:
            raise RuntimeError('The function glPointParameteriv is not available')
        glPointParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glPointParameteriv = (lambda pname,params:glPointParameteriv_impl(pname,pyglGetAsConstVoidPointer( params )))
    return glPointParameteriv(pname, params)
# <command>
#            <proto>void <name>glPointSize</name></proto>
#            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>size</name></param>
#            <glx opcode="100" type="render" />
#        </command>
#        
glPointSize_impl=None
def glPointSize (size):
    global glPointSize_impl
    if not glPointSize_impl:
        fptr = pyglGetFuncAddress('glPointSize')
        if not fptr:
            raise RuntimeError('The function glPointSize is not available')
        glPointSize_impl = PYGL_FUNC_TYPE( None ,c_float)(fptr)
    glPointSize = glPointSize_impl
    return glPointSize(size)
# <command>
#            <proto>void <name>glPolygonMode</name></proto>
#            <param group="MaterialFace"><ptype>GLenum</ptype> <name>face</name></param>
#            <param group="PolygonMode"><ptype>GLenum</ptype> <name>mode</name></param>
#            <glx opcode="101" type="render" />
#        </command>
#        
glPolygonMode_impl=None
def glPolygonMode (face, mode):
    global glPolygonMode_impl
    if not glPolygonMode_impl:
        fptr = pyglGetFuncAddress('glPolygonMode')
        if not fptr:
            raise RuntimeError('The function glPolygonMode is not available')
        glPolygonMode_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glPolygonMode = glPolygonMode_impl
    return glPolygonMode(face, mode)
# <command>
#            <proto>void <name>glPolygonOffset</name></proto>
#            <param><ptype>GLfloat</ptype> <name>factor</name></param>
#            <param><ptype>GLfloat</ptype> <name>units</name></param>
#            <glx opcode="192" type="render" />
#        </command>
#        
glPolygonOffset_impl=None
def glPolygonOffset (factor, units):
    global glPolygonOffset_impl
    if not glPolygonOffset_impl:
        fptr = pyglGetFuncAddress('glPolygonOffset')
        if not fptr:
            raise RuntimeError('The function glPolygonOffset is not available')
        glPolygonOffset_impl = PYGL_FUNC_TYPE( None ,c_float, c_float)(fptr)
    glPolygonOffset = glPolygonOffset_impl
    return glPolygonOffset(factor, units)
# <command>
#            <proto>void <name>glPopDebugGroup</name></proto>
#        </command>
#        
glPopDebugGroup_impl=None
def glPopDebugGroup ():
    global glPopDebugGroup_impl
    if not glPopDebugGroup_impl:
        fptr = pyglGetFuncAddress('glPopDebugGroup')
        if not fptr:
            raise RuntimeError('The function glPopDebugGroup is not available')
        glPopDebugGroup_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glPopDebugGroup = glPopDebugGroup_impl
    return glPopDebugGroup()
# <command>
#            <proto>void <name>glPrimitiveRestartIndex</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#        </command>
#        
glPrimitiveRestartIndex_impl=None
def glPrimitiveRestartIndex (index):
    global glPrimitiveRestartIndex_impl
    if not glPrimitiveRestartIndex_impl:
        fptr = pyglGetFuncAddress('glPrimitiveRestartIndex')
        if not fptr:
            raise RuntimeError('The function glPrimitiveRestartIndex is not available')
        glPrimitiveRestartIndex_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glPrimitiveRestartIndex = glPrimitiveRestartIndex_impl
    return glPrimitiveRestartIndex(index)
# <command>
#            <proto>void <name>glProgramBinary</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLenum</ptype> <name>binaryFormat</name></param>
#            <param len="length">const void *<name>binary</name></param>
#            <param><ptype>GLsizei</ptype> <name>length</name></param>
#        </command>
#        
glProgramBinary_impl=None
def glProgramBinary (program, binaryFormat, binary, length):
    global glProgramBinary_impl
    if not glProgramBinary_impl:
        fptr = pyglGetFuncAddress('glProgramBinary')
        if not fptr:
            raise RuntimeError('The function glProgramBinary is not available')
        glProgramBinary_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p, c_int)(fptr)
    glProgramBinary = (lambda program,binaryFormat,binary,length:glProgramBinary_impl(program,binaryFormat,pyglGetAsConstVoidPointer( binary ),length))
    return glProgramBinary(program, binaryFormat, binary, length)
# <command>
#            <proto>void <name>glProgramParameteri</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param group="ProgramParameterPName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> <name>value</name></param>
#        </command>
#        
glProgramParameteri_impl=None
def glProgramParameteri (program, pname, value):
    global glProgramParameteri_impl
    if not glProgramParameteri_impl:
        fptr = pyglGetFuncAddress('glProgramParameteri')
        if not fptr:
            raise RuntimeError('The function glProgramParameteri is not available')
        glProgramParameteri_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int)(fptr)
    glProgramParameteri = glProgramParameteri_impl
    return glProgramParameteri(program, pname, value)
# <command>
#            <proto>void <name>glProgramUniform1d</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLdouble</ptype> <name>v0</name></param>
#        </command>
#        
glProgramUniform1d_impl=None
def glProgramUniform1d (program, location, v0):
    global glProgramUniform1d_impl
    if not glProgramUniform1d_impl:
        fptr = pyglGetFuncAddress('glProgramUniform1d')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1d is not available')
        glProgramUniform1d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_double)(fptr)
    glProgramUniform1d = glProgramUniform1d_impl
    return glProgramUniform1d(program, location, v0)
# <command>
#            <proto>void <name>glProgramUniform1dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="1">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform1dv_impl=None
def glProgramUniform1dv (program, location, count, value):
    global glProgramUniform1dv_impl
    if not glProgramUniform1dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform1dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1dv is not available')
        glProgramUniform1dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform1dv = (lambda program,location,count,value:glProgramUniform1dv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform1dv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform1f</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLfloat</ptype> <name>v0</name></param>
#        </command>
#        
glProgramUniform1f_impl=None
def glProgramUniform1f (program, location, v0):
    global glProgramUniform1f_impl
    if not glProgramUniform1f_impl:
        fptr = pyglGetFuncAddress('glProgramUniform1f')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1f is not available')
        glProgramUniform1f_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_float)(fptr)
    glProgramUniform1f = glProgramUniform1f_impl
    return glProgramUniform1f(program, location, v0)
# <command>
#            <proto>void <name>glProgramUniform1fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="1">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform1fv_impl=None
def glProgramUniform1fv (program, location, count, value):
    global glProgramUniform1fv_impl
    if not glProgramUniform1fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform1fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1fv is not available')
        glProgramUniform1fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform1fv = (lambda program,location,count,value:glProgramUniform1fv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform1fv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform1i</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLint</ptype> <name>v0</name></param>
#        </command>
#        
glProgramUniform1i_impl=None
def glProgramUniform1i (program, location, v0):
    global glProgramUniform1i_impl
    if not glProgramUniform1i_impl:
        fptr = pyglGetFuncAddress('glProgramUniform1i')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1i is not available')
        glProgramUniform1i_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int)(fptr)
    glProgramUniform1i = glProgramUniform1i_impl
    return glProgramUniform1i(program, location, v0)
# <command>
#            <proto>void <name>glProgramUniform1iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="1">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform1iv_impl=None
def glProgramUniform1iv (program, location, count, value):
    global glProgramUniform1iv_impl
    if not glProgramUniform1iv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform1iv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1iv is not available')
        glProgramUniform1iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform1iv = (lambda program,location,count,value:glProgramUniform1iv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform1iv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform1ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLuint</ptype> <name>v0</name></param>
#        </command>
#        
glProgramUniform1ui_impl=None
def glProgramUniform1ui (program, location, v0):
    global glProgramUniform1ui_impl
    if not glProgramUniform1ui_impl:
        fptr = pyglGetFuncAddress('glProgramUniform1ui')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1ui is not available')
        glProgramUniform1ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint)(fptr)
    glProgramUniform1ui = glProgramUniform1ui_impl
    return glProgramUniform1ui(program, location, v0)
# <command>
#            <proto>void <name>glProgramUniform1uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform1uiv_impl=None
def glProgramUniform1uiv (program, location, count, value):
    global glProgramUniform1uiv_impl
    if not glProgramUniform1uiv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform1uiv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform1uiv is not available')
        glProgramUniform1uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform1uiv = (lambda program,location,count,value:glProgramUniform1uiv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform1uiv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform2d</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLdouble</ptype> <name>v0</name></param>
#            <param><ptype>GLdouble</ptype> <name>v1</name></param>
#        </command>
#        
glProgramUniform2d_impl=None
def glProgramUniform2d (program, location, v0, v1):
    global glProgramUniform2d_impl
    if not glProgramUniform2d_impl:
        fptr = pyglGetFuncAddress('glProgramUniform2d')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2d is not available')
        glProgramUniform2d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_double, c_double)(fptr)
    glProgramUniform2d = glProgramUniform2d_impl
    return glProgramUniform2d(program, location, v0, v1)
# <command>
#            <proto>void <name>glProgramUniform2dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="2">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform2dv_impl=None
def glProgramUniform2dv (program, location, count, value):
    global glProgramUniform2dv_impl
    if not glProgramUniform2dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform2dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2dv is not available')
        glProgramUniform2dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform2dv = (lambda program,location,count,value:glProgramUniform2dv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform2dv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform2f</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLfloat</ptype> <name>v0</name></param>
#            <param><ptype>GLfloat</ptype> <name>v1</name></param>
#        </command>
#        
glProgramUniform2f_impl=None
def glProgramUniform2f (program, location, v0, v1):
    global glProgramUniform2f_impl
    if not glProgramUniform2f_impl:
        fptr = pyglGetFuncAddress('glProgramUniform2f')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2f is not available')
        glProgramUniform2f_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_float, c_float)(fptr)
    glProgramUniform2f = glProgramUniform2f_impl
    return glProgramUniform2f(program, location, v0, v1)
# <command>
#            <proto>void <name>glProgramUniform2fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="2">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform2fv_impl=None
def glProgramUniform2fv (program, location, count, value):
    global glProgramUniform2fv_impl
    if not glProgramUniform2fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform2fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2fv is not available')
        glProgramUniform2fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform2fv = (lambda program,location,count,value:glProgramUniform2fv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform2fv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform2i</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLint</ptype> <name>v0</name></param>
#            <param><ptype>GLint</ptype> <name>v1</name></param>
#        </command>
#        
glProgramUniform2i_impl=None
def glProgramUniform2i (program, location, v0, v1):
    global glProgramUniform2i_impl
    if not glProgramUniform2i_impl:
        fptr = pyglGetFuncAddress('glProgramUniform2i')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2i is not available')
        glProgramUniform2i_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int)(fptr)
    glProgramUniform2i = glProgramUniform2i_impl
    return glProgramUniform2i(program, location, v0, v1)
# <command>
#            <proto>void <name>glProgramUniform2iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="2">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform2iv_impl=None
def glProgramUniform2iv (program, location, count, value):
    global glProgramUniform2iv_impl
    if not glProgramUniform2iv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform2iv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2iv is not available')
        glProgramUniform2iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform2iv = (lambda program,location,count,value:glProgramUniform2iv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform2iv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform2ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLuint</ptype> <name>v0</name></param>
#            <param><ptype>GLuint</ptype> <name>v1</name></param>
#        </command>
#        
glProgramUniform2ui_impl=None
def glProgramUniform2ui (program, location, v0, v1):
    global glProgramUniform2ui_impl
    if not glProgramUniform2ui_impl:
        fptr = pyglGetFuncAddress('glProgramUniform2ui')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2ui is not available')
        glProgramUniform2ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_uint)(fptr)
    glProgramUniform2ui = glProgramUniform2ui_impl
    return glProgramUniform2ui(program, location, v0, v1)
# <command>
#            <proto>void <name>glProgramUniform2uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="2">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform2uiv_impl=None
def glProgramUniform2uiv (program, location, count, value):
    global glProgramUniform2uiv_impl
    if not glProgramUniform2uiv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform2uiv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform2uiv is not available')
        glProgramUniform2uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform2uiv = (lambda program,location,count,value:glProgramUniform2uiv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform2uiv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform3d</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLdouble</ptype> <name>v0</name></param>
#            <param><ptype>GLdouble</ptype> <name>v1</name></param>
#            <param><ptype>GLdouble</ptype> <name>v2</name></param>
#        </command>
#        
glProgramUniform3d_impl=None
def glProgramUniform3d (program, location, v0, v1, v2):
    global glProgramUniform3d_impl
    if not glProgramUniform3d_impl:
        fptr = pyglGetFuncAddress('glProgramUniform3d')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3d is not available')
        glProgramUniform3d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_double, c_double, c_double)(fptr)
    glProgramUniform3d = glProgramUniform3d_impl
    return glProgramUniform3d(program, location, v0, v1, v2)
# <command>
#            <proto>void <name>glProgramUniform3dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="3">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform3dv_impl=None
def glProgramUniform3dv (program, location, count, value):
    global glProgramUniform3dv_impl
    if not glProgramUniform3dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform3dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3dv is not available')
        glProgramUniform3dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform3dv = (lambda program,location,count,value:glProgramUniform3dv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform3dv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform3f</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLfloat</ptype> <name>v0</name></param>
#            <param><ptype>GLfloat</ptype> <name>v1</name></param>
#            <param><ptype>GLfloat</ptype> <name>v2</name></param>
#        </command>
#        
glProgramUniform3f_impl=None
def glProgramUniform3f (program, location, v0, v1, v2):
    global glProgramUniform3f_impl
    if not glProgramUniform3f_impl:
        fptr = pyglGetFuncAddress('glProgramUniform3f')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3f is not available')
        glProgramUniform3f_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_float, c_float, c_float)(fptr)
    glProgramUniform3f = glProgramUniform3f_impl
    return glProgramUniform3f(program, location, v0, v1, v2)
# <command>
#            <proto>void <name>glProgramUniform3fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="3">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform3fv_impl=None
def glProgramUniform3fv (program, location, count, value):
    global glProgramUniform3fv_impl
    if not glProgramUniform3fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform3fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3fv is not available')
        glProgramUniform3fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform3fv = (lambda program,location,count,value:glProgramUniform3fv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform3fv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform3i</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLint</ptype> <name>v0</name></param>
#            <param><ptype>GLint</ptype> <name>v1</name></param>
#            <param><ptype>GLint</ptype> <name>v2</name></param>
#        </command>
#        
glProgramUniform3i_impl=None
def glProgramUniform3i (program, location, v0, v1, v2):
    global glProgramUniform3i_impl
    if not glProgramUniform3i_impl:
        fptr = pyglGetFuncAddress('glProgramUniform3i')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3i is not available')
        glProgramUniform3i_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int)(fptr)
    glProgramUniform3i = glProgramUniform3i_impl
    return glProgramUniform3i(program, location, v0, v1, v2)
# <command>
#            <proto>void <name>glProgramUniform3iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="3">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform3iv_impl=None
def glProgramUniform3iv (program, location, count, value):
    global glProgramUniform3iv_impl
    if not glProgramUniform3iv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform3iv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3iv is not available')
        glProgramUniform3iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform3iv = (lambda program,location,count,value:glProgramUniform3iv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform3iv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform3ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLuint</ptype> <name>v0</name></param>
#            <param><ptype>GLuint</ptype> <name>v1</name></param>
#            <param><ptype>GLuint</ptype> <name>v2</name></param>
#        </command>
#        
glProgramUniform3ui_impl=None
def glProgramUniform3ui (program, location, v0, v1, v2):
    global glProgramUniform3ui_impl
    if not glProgramUniform3ui_impl:
        fptr = pyglGetFuncAddress('glProgramUniform3ui')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3ui is not available')
        glProgramUniform3ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_uint, c_uint)(fptr)
    glProgramUniform3ui = glProgramUniform3ui_impl
    return glProgramUniform3ui(program, location, v0, v1, v2)
# <command>
#            <proto>void <name>glProgramUniform3uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="3">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform3uiv_impl=None
def glProgramUniform3uiv (program, location, count, value):
    global glProgramUniform3uiv_impl
    if not glProgramUniform3uiv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform3uiv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform3uiv is not available')
        glProgramUniform3uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform3uiv = (lambda program,location,count,value:glProgramUniform3uiv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform3uiv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform4d</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLdouble</ptype> <name>v0</name></param>
#            <param><ptype>GLdouble</ptype> <name>v1</name></param>
#            <param><ptype>GLdouble</ptype> <name>v2</name></param>
#            <param><ptype>GLdouble</ptype> <name>v3</name></param>
#        </command>
#        
glProgramUniform4d_impl=None
def glProgramUniform4d (program, location, v0, v1, v2, v3):
    global glProgramUniform4d_impl
    if not glProgramUniform4d_impl:
        fptr = pyglGetFuncAddress('glProgramUniform4d')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4d is not available')
        glProgramUniform4d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_double, c_double, c_double, c_double)(fptr)
    glProgramUniform4d = glProgramUniform4d_impl
    return glProgramUniform4d(program, location, v0, v1, v2, v3)
# <command>
#            <proto>void <name>glProgramUniform4dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="4">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform4dv_impl=None
def glProgramUniform4dv (program, location, count, value):
    global glProgramUniform4dv_impl
    if not glProgramUniform4dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform4dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4dv is not available')
        glProgramUniform4dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform4dv = (lambda program,location,count,value:glProgramUniform4dv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform4dv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform4f</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLfloat</ptype> <name>v0</name></param>
#            <param><ptype>GLfloat</ptype> <name>v1</name></param>
#            <param><ptype>GLfloat</ptype> <name>v2</name></param>
#            <param><ptype>GLfloat</ptype> <name>v3</name></param>
#        </command>
#        
glProgramUniform4f_impl=None
def glProgramUniform4f (program, location, v0, v1, v2, v3):
    global glProgramUniform4f_impl
    if not glProgramUniform4f_impl:
        fptr = pyglGetFuncAddress('glProgramUniform4f')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4f is not available')
        glProgramUniform4f_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_float, c_float, c_float, c_float)(fptr)
    glProgramUniform4f = glProgramUniform4f_impl
    return glProgramUniform4f(program, location, v0, v1, v2, v3)
# <command>
#            <proto>void <name>glProgramUniform4fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="4">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform4fv_impl=None
def glProgramUniform4fv (program, location, count, value):
    global glProgramUniform4fv_impl
    if not glProgramUniform4fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform4fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4fv is not available')
        glProgramUniform4fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform4fv = (lambda program,location,count,value:glProgramUniform4fv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform4fv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform4i</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLint</ptype> <name>v0</name></param>
#            <param><ptype>GLint</ptype> <name>v1</name></param>
#            <param><ptype>GLint</ptype> <name>v2</name></param>
#            <param><ptype>GLint</ptype> <name>v3</name></param>
#        </command>
#        
glProgramUniform4i_impl=None
def glProgramUniform4i (program, location, v0, v1, v2, v3):
    global glProgramUniform4i_impl
    if not glProgramUniform4i_impl:
        fptr = pyglGetFuncAddress('glProgramUniform4i')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4i is not available')
        glProgramUniform4i_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int)(fptr)
    glProgramUniform4i = glProgramUniform4i_impl
    return glProgramUniform4i(program, location, v0, v1, v2, v3)
# <command>
#            <proto>void <name>glProgramUniform4iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="4">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform4iv_impl=None
def glProgramUniform4iv (program, location, count, value):
    global glProgramUniform4iv_impl
    if not glProgramUniform4iv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform4iv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4iv is not available')
        glProgramUniform4iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform4iv = (lambda program,location,count,value:glProgramUniform4iv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform4iv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniform4ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLuint</ptype> <name>v0</name></param>
#            <param><ptype>GLuint</ptype> <name>v1</name></param>
#            <param><ptype>GLuint</ptype> <name>v2</name></param>
#            <param><ptype>GLuint</ptype> <name>v3</name></param>
#        </command>
#        
glProgramUniform4ui_impl=None
def glProgramUniform4ui (program, location, v0, v1, v2, v3):
    global glProgramUniform4ui_impl
    if not glProgramUniform4ui_impl:
        fptr = pyglGetFuncAddress('glProgramUniform4ui')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4ui is not available')
        glProgramUniform4ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_uint, c_uint, c_uint)(fptr)
    glProgramUniform4ui = glProgramUniform4ui_impl
    return glProgramUniform4ui(program, location, v0, v1, v2, v3)
# <command>
#            <proto>void <name>glProgramUniform4uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="4">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniform4uiv_impl=None
def glProgramUniform4uiv (program, location, count, value):
    global glProgramUniform4uiv_impl
    if not glProgramUniform4uiv_impl:
        fptr = pyglGetFuncAddress('glProgramUniform4uiv')
        if not fptr:
            raise RuntimeError('The function glProgramUniform4uiv is not available')
        glProgramUniform4uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_void_p)(fptr)
    glProgramUniform4uiv = (lambda program,location,count,value:glProgramUniform4uiv_impl(program,location,count,pyglGetAsConstVoidPointer( value )))
    return glProgramUniform4uiv(program, location, count, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix2dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="2">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix2dv_impl=None
def glProgramUniformMatrix2dv (program, location, count, transpose, value):
    global glProgramUniformMatrix2dv_impl
    if not glProgramUniformMatrix2dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix2dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2dv is not available')
        glProgramUniformMatrix2dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix2dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix2dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix2dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix2fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="2">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix2fv_impl=None
def glProgramUniformMatrix2fv (program, location, count, transpose, value):
    global glProgramUniformMatrix2fv_impl
    if not glProgramUniformMatrix2fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix2fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2fv is not available')
        glProgramUniformMatrix2fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix2fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix2fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix2fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix2x3dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix2x3dv_impl=None
def glProgramUniformMatrix2x3dv (program, location, count, transpose, value):
    global glProgramUniformMatrix2x3dv_impl
    if not glProgramUniformMatrix2x3dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix2x3dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2x3dv is not available')
        glProgramUniformMatrix2x3dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix2x3dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix2x3dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix2x3dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix2x3fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix2x3fv_impl=None
def glProgramUniformMatrix2x3fv (program, location, count, transpose, value):
    global glProgramUniformMatrix2x3fv_impl
    if not glProgramUniformMatrix2x3fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix2x3fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2x3fv is not available')
        glProgramUniformMatrix2x3fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix2x3fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix2x3fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix2x3fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix2x4dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix2x4dv_impl=None
def glProgramUniformMatrix2x4dv (program, location, count, transpose, value):
    global glProgramUniformMatrix2x4dv_impl
    if not glProgramUniformMatrix2x4dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix2x4dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2x4dv is not available')
        glProgramUniformMatrix2x4dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix2x4dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix2x4dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix2x4dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix2x4fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix2x4fv_impl=None
def glProgramUniformMatrix2x4fv (program, location, count, transpose, value):
    global glProgramUniformMatrix2x4fv_impl
    if not glProgramUniformMatrix2x4fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix2x4fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix2x4fv is not available')
        glProgramUniformMatrix2x4fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix2x4fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix2x4fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix2x4fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix3dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="3">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix3dv_impl=None
def glProgramUniformMatrix3dv (program, location, count, transpose, value):
    global glProgramUniformMatrix3dv_impl
    if not glProgramUniformMatrix3dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix3dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3dv is not available')
        glProgramUniformMatrix3dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix3dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix3dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix3dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix3fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="3">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix3fv_impl=None
def glProgramUniformMatrix3fv (program, location, count, transpose, value):
    global glProgramUniformMatrix3fv_impl
    if not glProgramUniformMatrix3fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix3fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3fv is not available')
        glProgramUniformMatrix3fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix3fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix3fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix3fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix3x2dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix3x2dv_impl=None
def glProgramUniformMatrix3x2dv (program, location, count, transpose, value):
    global glProgramUniformMatrix3x2dv_impl
    if not glProgramUniformMatrix3x2dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix3x2dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3x2dv is not available')
        glProgramUniformMatrix3x2dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix3x2dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix3x2dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix3x2dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix3x2fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix3x2fv_impl=None
def glProgramUniformMatrix3x2fv (program, location, count, transpose, value):
    global glProgramUniformMatrix3x2fv_impl
    if not glProgramUniformMatrix3x2fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix3x2fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3x2fv is not available')
        glProgramUniformMatrix3x2fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix3x2fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix3x2fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix3x2fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix3x4dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix3x4dv_impl=None
def glProgramUniformMatrix3x4dv (program, location, count, transpose, value):
    global glProgramUniformMatrix3x4dv_impl
    if not glProgramUniformMatrix3x4dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix3x4dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3x4dv is not available')
        glProgramUniformMatrix3x4dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix3x4dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix3x4dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix3x4dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix3x4fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix3x4fv_impl=None
def glProgramUniformMatrix3x4fv (program, location, count, transpose, value):
    global glProgramUniformMatrix3x4fv_impl
    if not glProgramUniformMatrix3x4fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix3x4fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix3x4fv is not available')
        glProgramUniformMatrix3x4fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix3x4fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix3x4fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix3x4fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix4dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="4">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix4dv_impl=None
def glProgramUniformMatrix4dv (program, location, count, transpose, value):
    global glProgramUniformMatrix4dv_impl
    if not glProgramUniformMatrix4dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix4dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4dv is not available')
        glProgramUniformMatrix4dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix4dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix4dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix4dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix4fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="4">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix4fv_impl=None
def glProgramUniformMatrix4fv (program, location, count, transpose, value):
    global glProgramUniformMatrix4fv_impl
    if not glProgramUniformMatrix4fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix4fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4fv is not available')
        glProgramUniformMatrix4fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix4fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix4fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix4fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix4x2dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix4x2dv_impl=None
def glProgramUniformMatrix4x2dv (program, location, count, transpose, value):
    global glProgramUniformMatrix4x2dv_impl
    if not glProgramUniformMatrix4x2dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix4x2dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4x2dv is not available')
        glProgramUniformMatrix4x2dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix4x2dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix4x2dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix4x2dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix4x2fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix4x2fv_impl=None
def glProgramUniformMatrix4x2fv (program, location, count, transpose, value):
    global glProgramUniformMatrix4x2fv_impl
    if not glProgramUniformMatrix4x2fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix4x2fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4x2fv is not available')
        glProgramUniformMatrix4x2fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix4x2fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix4x2fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix4x2fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix4x3dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix4x3dv_impl=None
def glProgramUniformMatrix4x3dv (program, location, count, transpose, value):
    global glProgramUniformMatrix4x3dv_impl
    if not glProgramUniformMatrix4x3dv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix4x3dv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4x3dv is not available')
        glProgramUniformMatrix4x3dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix4x3dv = (lambda program,location,count,transpose,value:glProgramUniformMatrix4x3dv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix4x3dv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProgramUniformMatrix4x3fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glProgramUniformMatrix4x3fv_impl=None
def glProgramUniformMatrix4x3fv (program, location, count, transpose, value):
    global glProgramUniformMatrix4x3fv_impl
    if not glProgramUniformMatrix4x3fv_impl:
        fptr = pyglGetFuncAddress('glProgramUniformMatrix4x3fv')
        if not fptr:
            raise RuntimeError('The function glProgramUniformMatrix4x3fv is not available')
        glProgramUniformMatrix4x3fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_char, c_void_p)(fptr)
    glProgramUniformMatrix4x3fv = (lambda program,location,count,transpose,value:glProgramUniformMatrix4x3fv_impl(program,location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glProgramUniformMatrix4x3fv(program, location, count, transpose, value)
# <command>
#            <proto>void <name>glProvokingVertex</name></proto>
#            <param><ptype>GLenum</ptype> <name>mode</name></param>
#        </command>
#        
glProvokingVertex_impl=None
def glProvokingVertex (mode):
    global glProvokingVertex_impl
    if not glProvokingVertex_impl:
        fptr = pyglGetFuncAddress('glProvokingVertex')
        if not fptr:
            raise RuntimeError('The function glProvokingVertex is not available')
        glProvokingVertex_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glProvokingVertex = glProvokingVertex_impl
    return glProvokingVertex(mode)
# <command>
#            <proto>void <name>glPushDebugGroup</name></proto>
#            <param><ptype>GLenum</ptype> <name>source</name></param>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLsizei</ptype> <name>length</name></param>
#            <param len="COMPSIZE(message,length)">const <ptype>GLchar</ptype> *<name>message</name></param>
#        </command>
#        
glPushDebugGroup_impl=None
def glPushDebugGroup (source, id, length, message):
    global glPushDebugGroup_impl
    if not glPushDebugGroup_impl:
        fptr = pyglGetFuncAddress('glPushDebugGroup')
        if not fptr:
            raise RuntimeError('The function glPushDebugGroup is not available')
        glPushDebugGroup_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p)(fptr)
    glPushDebugGroup = (lambda source,id,length,message:glPushDebugGroup_impl(source,id,length,c_char_p( message .encode() )))
    return glPushDebugGroup(source, id, length, message)
# <command>
#            <proto>void <name>glQueryCounter</name></proto>
#            <param><ptype>GLuint</ptype> <name>id</name></param>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#        </command>
#        
glQueryCounter_impl=None
def glQueryCounter (id, target):
    global glQueryCounter_impl
    if not glQueryCounter_impl:
        fptr = pyglGetFuncAddress('glQueryCounter')
        if not fptr:
            raise RuntimeError('The function glQueryCounter is not available')
        glQueryCounter_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glQueryCounter = glQueryCounter_impl
    return glQueryCounter(id, target)
# <command>
#            <proto>void <name>glReadBuffer</name></proto>
#            <param group="ReadBufferMode"><ptype>GLenum</ptype> <name>src</name></param>
#            <glx opcode="171" type="render" />
#        </command>
#        
glReadBuffer_impl=None
def glReadBuffer (src):
    global glReadBuffer_impl
    if not glReadBuffer_impl:
        fptr = pyglGetFuncAddress('glReadBuffer')
        if not fptr:
            raise RuntimeError('The function glReadBuffer is not available')
        glReadBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glReadBuffer = glReadBuffer_impl
    return glReadBuffer(src)
# <command>
#            <proto>void <name>glReadPixels</name></proto>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type,width,height)">void *<name>pixels</name></param>
#            <glx opcode="111" type="single" />
#            <glx comment="PBO protocol" name="glReadPixelsPBO" opcode="345" type="render" />
#        </command>
#        
glReadPixels_impl=None
def glReadPixels (x, y, width, height, format, type, pixels):
    global glReadPixels_impl
    if not glReadPixels_impl:
        fptr = pyglGetFuncAddress('glReadPixels')
        if not fptr:
            raise RuntimeError('The function glReadPixels is not available')
        glReadPixels_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glReadPixels = (lambda x,y,width,height,format,type,pixels:glReadPixels_impl(x,y,width,height,format,type,(c_uint8*len( pixels )).from_buffer( pixels )))
    return glReadPixels(x, y, width, height, format, type, pixels)
# <command>
#            <proto>void <name>glReadnPixels</name></proto>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
#            <param>void *<name>data</name></param>
#        </command>
#        
glReadnPixels_impl=None
def glReadnPixels (x, y, width, height, format, type, bufSize, data):
    global glReadnPixels_impl
    if not glReadnPixels_impl:
        fptr = pyglGetFuncAddress('glReadnPixels')
        if not fptr:
            raise RuntimeError('The function glReadnPixels is not available')
        glReadnPixels_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_int, c_int, c_uint, c_uint, c_int, c_void_p)(fptr)
    glReadnPixels = (lambda x,y,width,height,format,type,bufSize,data:glReadnPixels_impl(x,y,width,height,format,type,bufSize,(c_uint8*len( data )).from_buffer( data )))
    return glReadnPixels(x, y, width, height, format, type, bufSize, data)
# <command>
#            <proto>void <name>glReleaseShaderCompiler</name></proto>
#        </command>
#        
glReleaseShaderCompiler_impl=None
def glReleaseShaderCompiler ():
    global glReleaseShaderCompiler_impl
    if not glReleaseShaderCompiler_impl:
        fptr = pyglGetFuncAddress('glReleaseShaderCompiler')
        if not fptr:
            raise RuntimeError('The function glReleaseShaderCompiler is not available')
        glReleaseShaderCompiler_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glReleaseShaderCompiler = glReleaseShaderCompiler_impl
    return glReleaseShaderCompiler()
# <command>
#            <proto>void <name>glRenderbufferStorage</name></proto>
#            <param group="RenderbufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <glx opcode="4318" type="render" />
#        </command>
#        
glRenderbufferStorage_impl=None
def glRenderbufferStorage (target, internalformat, width, height):
    global glRenderbufferStorage_impl
    if not glRenderbufferStorage_impl:
        fptr = pyglGetFuncAddress('glRenderbufferStorage')
        if not fptr:
            raise RuntimeError('The function glRenderbufferStorage is not available')
        glRenderbufferStorage_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_int)(fptr)
    glRenderbufferStorage = glRenderbufferStorage_impl
    return glRenderbufferStorage(target, internalformat, width, height)
# <command>
#            <proto>void <name>glRenderbufferStorageMultisample</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizei</ptype> <name>samples</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <glx opcode="4331" type="render" />
#        </command>
#        
glRenderbufferStorageMultisample_impl=None
def glRenderbufferStorageMultisample (target, samples, internalformat, width, height):
    global glRenderbufferStorageMultisample_impl
    if not glRenderbufferStorageMultisample_impl:
        fptr = pyglGetFuncAddress('glRenderbufferStorageMultisample')
        if not fptr:
            raise RuntimeError('The function glRenderbufferStorageMultisample is not available')
        glRenderbufferStorageMultisample_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int)(fptr)
    glRenderbufferStorageMultisample = glRenderbufferStorageMultisample_impl
    return glRenderbufferStorageMultisample(target, samples, internalformat, width, height)
# <command>
#            <proto>void <name>glResumeTransformFeedback</name></proto>
#        </command>
#        
glResumeTransformFeedback_impl=None
def glResumeTransformFeedback ():
    global glResumeTransformFeedback_impl
    if not glResumeTransformFeedback_impl:
        fptr = pyglGetFuncAddress('glResumeTransformFeedback')
        if not fptr:
            raise RuntimeError('The function glResumeTransformFeedback is not available')
        glResumeTransformFeedback_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glResumeTransformFeedback = glResumeTransformFeedback_impl
    return glResumeTransformFeedback()
# <command>
#            <proto>void <name>glSampleCoverage</name></proto>
#            <param><ptype>GLfloat</ptype> <name>value</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>invert</name></param>
#            <glx opcode="229" type="render" />
#        </command>
#        
glSampleCoverage_impl=None
def glSampleCoverage (value, invert):
    global glSampleCoverage_impl
    if not glSampleCoverage_impl:
        fptr = pyglGetFuncAddress('glSampleCoverage')
        if not fptr:
            raise RuntimeError('The function glSampleCoverage is not available')
        glSampleCoverage_impl = PYGL_FUNC_TYPE( None ,c_float, c_char)(fptr)
    glSampleCoverage = glSampleCoverage_impl
    return glSampleCoverage(value, invert)
# <command>
#            <proto>void <name>glSampleMaski</name></proto>
#            <param><ptype>GLuint</ptype> <name>maskNumber</name></param>
#            <param><ptype>GLbitfield</ptype> <name>mask</name></param>
#        </command>
#        
glSampleMaski_impl=None
def glSampleMaski (maskNumber, mask):
    global glSampleMaski_impl
    if not glSampleMaski_impl:
        fptr = pyglGetFuncAddress('glSampleMaski')
        if not fptr:
            raise RuntimeError('The function glSampleMaski is not available')
        glSampleMaski_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glSampleMaski = glSampleMaski_impl
    return glSampleMaski(maskNumber, mask)
# <command>
#            <proto>void <name>glSamplerParameterIiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>param</name></param>
#        </command>
#        
glSamplerParameterIiv_impl=None
def glSamplerParameterIiv (sampler, pname, param):
    global glSamplerParameterIiv_impl
    if not glSamplerParameterIiv_impl:
        fptr = pyglGetFuncAddress('glSamplerParameterIiv')
        if not fptr:
            raise RuntimeError('The function glSamplerParameterIiv is not available')
        glSamplerParameterIiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glSamplerParameterIiv = (lambda sampler,pname,param:glSamplerParameterIiv_impl(sampler,pname,pyglGetAsConstVoidPointer( param )))
    return glSamplerParameterIiv(sampler, pname, param)
# <command>
#            <proto>void <name>glSamplerParameterIuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)">const <ptype>GLuint</ptype> *<name>param</name></param>
#        </command>
#        
glSamplerParameterIuiv_impl=None
def glSamplerParameterIuiv (sampler, pname, param):
    global glSamplerParameterIuiv_impl
    if not glSamplerParameterIuiv_impl:
        fptr = pyglGetFuncAddress('glSamplerParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glSamplerParameterIuiv is not available')
        glSamplerParameterIuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glSamplerParameterIuiv = (lambda sampler,pname,param:glSamplerParameterIuiv_impl(sampler,pname,pyglGetAsConstVoidPointer( param )))
    return glSamplerParameterIuiv(sampler, pname, param)
# <command>
#            <proto>void <name>glSamplerParameterf</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLfloat</ptype> <name>param</name></param>
#        </command>
#        
glSamplerParameterf_impl=None
def glSamplerParameterf (sampler, pname, param):
    global glSamplerParameterf_impl
    if not glSamplerParameterf_impl:
        fptr = pyglGetFuncAddress('glSamplerParameterf')
        if not fptr:
            raise RuntimeError('The function glSamplerParameterf is not available')
        glSamplerParameterf_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_float)(fptr)
    glSamplerParameterf = glSamplerParameterf_impl
    return glSamplerParameterf(sampler, pname, param)
# <command>
#            <proto>void <name>glSamplerParameterfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)">const <ptype>GLfloat</ptype> *<name>param</name></param>
#        </command>
#        
glSamplerParameterfv_impl=None
def glSamplerParameterfv (sampler, pname, param):
    global glSamplerParameterfv_impl
    if not glSamplerParameterfv_impl:
        fptr = pyglGetFuncAddress('glSamplerParameterfv')
        if not fptr:
            raise RuntimeError('The function glSamplerParameterfv is not available')
        glSamplerParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glSamplerParameterfv = (lambda sampler,pname,param:glSamplerParameterfv_impl(sampler,pname,pyglGetAsConstVoidPointer( param )))
    return glSamplerParameterfv(sampler, pname, param)
# <command>
#            <proto>void <name>glSamplerParameteri</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> <name>param</name></param>
#        </command>
#        
glSamplerParameteri_impl=None
def glSamplerParameteri (sampler, pname, param):
    global glSamplerParameteri_impl
    if not glSamplerParameteri_impl:
        fptr = pyglGetFuncAddress('glSamplerParameteri')
        if not fptr:
            raise RuntimeError('The function glSamplerParameteri is not available')
        glSamplerParameteri_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int)(fptr)
    glSamplerParameteri = glSamplerParameteri_impl
    return glSamplerParameteri(sampler, pname, param)
# <command>
#            <proto>void <name>glSamplerParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>sampler</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>param</name></param>
#        </command>
#        
glSamplerParameteriv_impl=None
def glSamplerParameteriv (sampler, pname, param):
    global glSamplerParameteriv_impl
    if not glSamplerParameteriv_impl:
        fptr = pyglGetFuncAddress('glSamplerParameteriv')
        if not fptr:
            raise RuntimeError('The function glSamplerParameteriv is not available')
        glSamplerParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glSamplerParameteriv = (lambda sampler,pname,param:glSamplerParameteriv_impl(sampler,pname,pyglGetAsConstVoidPointer( param )))
    return glSamplerParameteriv(sampler, pname, param)
# <command>
#            <proto>void <name>glScissor</name></proto>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <glx opcode="103" type="render" />
#        </command>
#        
glScissor_impl=None
def glScissor (x, y, width, height):
    global glScissor_impl
    if not glScissor_impl:
        fptr = pyglGetFuncAddress('glScissor')
        if not fptr:
            raise RuntimeError('The function glScissor is not available')
        glScissor_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_int, c_int)(fptr)
    glScissor = glScissor_impl
    return glScissor(x, y, width, height)
# <command>
#            <proto>void <name>glScissorArrayv</name></proto>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="COMPSIZE(count)">const <ptype>GLint</ptype> *<name>v</name></param>
#        </command>
#        
glScissorArrayv_impl=None
def glScissorArrayv (first, count, v):
    global glScissorArrayv_impl
    if not glScissorArrayv_impl:
        fptr = pyglGetFuncAddress('glScissorArrayv')
        if not fptr:
            raise RuntimeError('The function glScissorArrayv is not available')
        glScissorArrayv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glScissorArrayv = (lambda first,count,v:glScissorArrayv_impl(first,count,pyglGetAsConstVoidPointer( v )))
    return glScissorArrayv(first, count, v)
# <command>
#            <proto>void <name>glScissorIndexed</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLint</ptype> <name>left</name></param>
#            <param><ptype>GLint</ptype> <name>bottom</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glScissorIndexed_impl=None
def glScissorIndexed (index, left, bottom, width, height):
    global glScissorIndexed_impl
    if not glScissorIndexed_impl:
        fptr = pyglGetFuncAddress('glScissorIndexed')
        if not fptr:
            raise RuntimeError('The function glScissorIndexed is not available')
        glScissorIndexed_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int)(fptr)
    glScissorIndexed = glScissorIndexed_impl
    return glScissorIndexed(index, left, bottom, width, height)
# <command>
#            <proto>void <name>glScissorIndexedv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLint</ptype> *<name>v</name></param>
#        </command>
#        
glScissorIndexedv_impl=None
def glScissorIndexedv (index, v):
    global glScissorIndexedv_impl
    if not glScissorIndexedv_impl:
        fptr = pyglGetFuncAddress('glScissorIndexedv')
        if not fptr:
            raise RuntimeError('The function glScissorIndexedv is not available')
        glScissorIndexedv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glScissorIndexedv = (lambda index,v:glScissorIndexedv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glScissorIndexedv(index, v)
# <command>
#            <proto>void <name>glShaderBinary</name></proto>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>shaders</name></param>
#            <param><ptype>GLenum</ptype> <name>binaryformat</name></param>
#            <param len="length">const void *<name>binary</name></param>
#            <param><ptype>GLsizei</ptype> <name>length</name></param>
#        </command>
#        
glShaderBinary_impl=None
def glShaderBinary (count, shaders, binaryformat, binary, length):
    global glShaderBinary_impl
    if not glShaderBinary_impl:
        fptr = pyglGetFuncAddress('glShaderBinary')
        if not fptr:
            raise RuntimeError('The function glShaderBinary is not available')
        glShaderBinary_impl = PYGL_FUNC_TYPE( None ,c_int, c_void_p, c_uint, c_void_p, c_int)(fptr)
    glShaderBinary = (lambda count,shaders,binaryformat,binary,length:glShaderBinary_impl(count,pyglGetAsConstVoidPointer( shaders ),binaryformat,pyglGetAsConstVoidPointer( binary ),length))
    return glShaderBinary(count, shaders, binaryformat, binary, length)
# <command>
#            <proto>void <name>glShaderStorageBlockBinding</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>storageBlockIndex</name></param>
#            <param><ptype>GLuint</ptype> <name>storageBlockBinding</name></param>
#        </command>
#        
glShaderStorageBlockBinding_impl=None
def glShaderStorageBlockBinding (program, storageBlockIndex, storageBlockBinding):
    global glShaderStorageBlockBinding_impl
    if not glShaderStorageBlockBinding_impl:
        fptr = pyglGetFuncAddress('glShaderStorageBlockBinding')
        if not fptr:
            raise RuntimeError('The function glShaderStorageBlockBinding is not available')
        glShaderStorageBlockBinding_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glShaderStorageBlockBinding = glShaderStorageBlockBinding_impl
    return glShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding)
# <command>
#            <proto>void <name>glStencilFunc</name></proto>
#            <param group="StencilFunction"><ptype>GLenum</ptype> <name>func</name></param>
#            <param group="StencilValue"><ptype>GLint</ptype> <name>ref</name></param>
#            <param group="MaskedStencilValue"><ptype>GLuint</ptype> <name>mask</name></param>
#            <glx opcode="162" type="render" />
#        </command>
#        
glStencilFunc_impl=None
def glStencilFunc (func, ref, mask):
    global glStencilFunc_impl
    if not glStencilFunc_impl:
        fptr = pyglGetFuncAddress('glStencilFunc')
        if not fptr:
            raise RuntimeError('The function glStencilFunc is not available')
        glStencilFunc_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint)(fptr)
    glStencilFunc = glStencilFunc_impl
    return glStencilFunc(func, ref, mask)
# <command>
#            <proto>void <name>glStencilFuncSeparate</name></proto>
#            <param group="StencilFaceDirection"><ptype>GLenum</ptype> <name>face</name></param>
#            <param group="StencilFunction"><ptype>GLenum</ptype> <name>func</name></param>
#            <param group="StencilValue"><ptype>GLint</ptype> <name>ref</name></param>
#            <param group="MaskedStencilValue"><ptype>GLuint</ptype> <name>mask</name></param>
#        </command>
#        
glStencilFuncSeparate_impl=None
def glStencilFuncSeparate (face, func, ref, mask):
    global glStencilFuncSeparate_impl
    if not glStencilFuncSeparate_impl:
        fptr = pyglGetFuncAddress('glStencilFuncSeparate')
        if not fptr:
            raise RuntimeError('The function glStencilFuncSeparate is not available')
        glStencilFuncSeparate_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_uint)(fptr)
    glStencilFuncSeparate = glStencilFuncSeparate_impl
    return glStencilFuncSeparate(face, func, ref, mask)
# <command>
#            <proto>void <name>glStencilMask</name></proto>
#            <param group="MaskedStencilValue"><ptype>GLuint</ptype> <name>mask</name></param>
#            <glx opcode="133" type="render" />
#        </command>
#        
glStencilMask_impl=None
def glStencilMask (mask):
    global glStencilMask_impl
    if not glStencilMask_impl:
        fptr = pyglGetFuncAddress('glStencilMask')
        if not fptr:
            raise RuntimeError('The function glStencilMask is not available')
        glStencilMask_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glStencilMask = glStencilMask_impl
    return glStencilMask(mask)
# <command>
#            <proto>void <name>glStencilMaskSeparate</name></proto>
#            <param group="StencilFaceDirection"><ptype>GLenum</ptype> <name>face</name></param>
#            <param group="MaskedStencilValue"><ptype>GLuint</ptype> <name>mask</name></param>
#        </command>
#        
glStencilMaskSeparate_impl=None
def glStencilMaskSeparate (face, mask):
    global glStencilMaskSeparate_impl
    if not glStencilMaskSeparate_impl:
        fptr = pyglGetFuncAddress('glStencilMaskSeparate')
        if not fptr:
            raise RuntimeError('The function glStencilMaskSeparate is not available')
        glStencilMaskSeparate_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glStencilMaskSeparate = glStencilMaskSeparate_impl
    return glStencilMaskSeparate(face, mask)
# <command>
#            <proto>void <name>glStencilOp</name></proto>
#            <param group="StencilOp"><ptype>GLenum</ptype> <name>fail</name></param>
#            <param group="StencilOp"><ptype>GLenum</ptype> <name>zfail</name></param>
#            <param group="StencilOp"><ptype>GLenum</ptype> <name>zpass</name></param>
#            <glx opcode="163" type="render" />
#        </command>
#        
glStencilOp_impl=None
def glStencilOp (fail, zfail, zpass):
    global glStencilOp_impl
    if not glStencilOp_impl:
        fptr = pyglGetFuncAddress('glStencilOp')
        if not fptr:
            raise RuntimeError('The function glStencilOp is not available')
        glStencilOp_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glStencilOp = glStencilOp_impl
    return glStencilOp(fail, zfail, zpass)
# <command>
#            <proto>void <name>glStencilOpSeparate</name></proto>
#            <param group="StencilFaceDirection"><ptype>GLenum</ptype> <name>face</name></param>
#            <param group="StencilOp"><ptype>GLenum</ptype> <name>sfail</name></param>
#            <param group="StencilOp"><ptype>GLenum</ptype> <name>dpfail</name></param>
#            <param group="StencilOp"><ptype>GLenum</ptype> <name>dppass</name></param>
#        </command>
#        
glStencilOpSeparate_impl=None
def glStencilOpSeparate (face, sfail, dpfail, dppass):
    global glStencilOpSeparate_impl
    if not glStencilOpSeparate_impl:
        fptr = pyglGetFuncAddress('glStencilOpSeparate')
        if not fptr:
            raise RuntimeError('The function glStencilOpSeparate is not available')
        glStencilOpSeparate_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint)(fptr)
    glStencilOpSeparate = glStencilOpSeparate_impl
    return glStencilOpSeparate(face, sfail, dpfail, dppass)
# <command>
#            <proto>void <name>glTexBuffer</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glTexBuffer_impl=None
def glTexBuffer (target, internalformat, buffer):
    global glTexBuffer_impl
    if not glTexBuffer_impl:
        fptr = pyglGetFuncAddress('glTexBuffer')
        if not fptr:
            raise RuntimeError('The function glTexBuffer is not available')
        glTexBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glTexBuffer = glTexBuffer_impl
    return glTexBuffer(target, internalformat, buffer)
# <command>
#            <proto>void <name>glTexBufferRange</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#        </command>
#        
glTexBufferRange_impl=None
def glTexBufferRange (target, internalformat, buffer, offset, size):
    global glTexBufferRange_impl
    if not glTexBufferRange_impl:
        fptr = pyglGetFuncAddress('glTexBufferRange')
        if not fptr:
            raise RuntimeError('The function glTexBufferRange is not available')
        glTexBufferRange_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t, c_void_p)(fptr)
    glTexBufferRange = glTexBufferRange_impl
    return glTexBufferRange(target, internalformat, buffer, offset, size)
# <command>
#            <proto>void <name>glTexImage1D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="TextureComponentCount"><ptype>GLint</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type,width)">const void *<name>pixels</name></param>
#            <glx opcode="109" type="render" />
#            <glx comment="PBO protocol" name="glTexImage1DPBO" opcode="328" type="render" />
#        </command>
#        
glTexImage1D_impl=None
def glTexImage1D (target, level, internalformat, width, border, format, type, pixels):
    global glTexImage1D_impl
    if not glTexImage1D_impl:
        fptr = pyglGetFuncAddress('glTexImage1D')
        if not fptr:
            raise RuntimeError('The function glTexImage1D is not available')
        glTexImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTexImage1D = (lambda target,level,internalformat,width,border,format,type,pixels:glTexImage1D_impl(target,level,internalformat,width,border,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTexImage1D(target, level, internalformat, width, border, format, type, pixels)
# <command>
#            <proto>void <name>glTexImage2D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="TextureComponentCount"><ptype>GLint</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type,width,height)">const void *<name>pixels</name></param>
#            <glx opcode="110" type="render" />
#            <glx comment="PBO protocol" name="glTexImage2DPBO" opcode="329" type="render" />
#        </command>
#        
glTexImage2D_impl=None
def glTexImage2D (target, level, internalformat, width, height, border, format, type, pixels):
    global glTexImage2D_impl
    if not glTexImage2D_impl:
        fptr = pyglGetFuncAddress('glTexImage2D')
        if not fptr:
            raise RuntimeError('The function glTexImage2D is not available')
        glTexImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTexImage2D = (lambda target,level,internalformat,width,height,border,format,type,pixels:glTexImage2D_impl(target,level,internalformat,width,height,border,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)
# <command>
#            <proto>void <name>glTexImage3D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="TextureComponentCount"><ptype>GLint</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type,width,height,depth)">const void *<name>pixels</name></param>
#            <glx opcode="4114" type="render" />
#            <glx comment="PBO protocol" name="glTexImage3DPBO" opcode="330" type="render" />
#        </command>
#        
glTexImage3D_impl=None
def glTexImage3D (target, level, internalformat, width, height, depth, border, format, type, pixels):
    global glTexImage3D_impl
    if not glTexImage3D_impl:
        fptr = pyglGetFuncAddress('glTexImage3D')
        if not fptr:
            raise RuntimeError('The function glTexImage3D is not available')
        glTexImage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTexImage3D = (lambda target,level,internalformat,width,height,depth,border,format,type,pixels:glTexImage3D_impl(target,level,internalformat,width,height,depth,border,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels)
# <command>
#            <proto>void <name>glTexParameterIiv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="346" type="render" />
#        </command>
#        
glTexParameterIiv_impl=None
def glTexParameterIiv (target, pname, params):
    global glTexParameterIiv_impl
    if not glTexParameterIiv_impl:
        fptr = pyglGetFuncAddress('glTexParameterIiv')
        if not fptr:
            raise RuntimeError('The function glTexParameterIiv is not available')
        glTexParameterIiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glTexParameterIiv = (lambda target,pname,params:glTexParameterIiv_impl(target,pname,pyglGetAsConstVoidPointer( params )))
    return glTexParameterIiv(target, pname, params)
# <command>
#            <proto>void <name>glTexParameterIuiv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param len="COMPSIZE(pname)">const <ptype>GLuint</ptype> *<name>params</name></param>
#            <glx opcode="347" type="render" />
#        </command>
#        
glTexParameterIuiv_impl=None
def glTexParameterIuiv (target, pname, params):
    global glTexParameterIuiv_impl
    if not glTexParameterIuiv_impl:
        fptr = pyglGetFuncAddress('glTexParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glTexParameterIuiv is not available')
        glTexParameterIuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glTexParameterIuiv = (lambda target,pname,params:glTexParameterIuiv_impl(target,pname,pyglGetAsConstVoidPointer( params )))
    return glTexParameterIuiv(target, pname, params)
# <command>
#            <proto>void <name>glTexParameterf</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>param</name></param>
#            <glx opcode="105" type="render" />
#        </command>
#        
glTexParameterf_impl=None
def glTexParameterf (target, pname, param):
    global glTexParameterf_impl
    if not glTexParameterf_impl:
        fptr = pyglGetFuncAddress('glTexParameterf')
        if not fptr:
            raise RuntimeError('The function glTexParameterf is not available')
        glTexParameterf_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_float)(fptr)
    glTexParameterf = glTexParameterf_impl
    return glTexParameterf(target, pname, param)
# <command>
#            <proto>void <name>glTexParameterfv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="CheckedFloat32" len="COMPSIZE(pname)">const <ptype>GLfloat</ptype> *<name>params</name></param>
#            <glx opcode="106" type="render" />
#        </command>
#        
glTexParameterfv_impl=None
def glTexParameterfv (target, pname, params):
    global glTexParameterfv_impl
    if not glTexParameterfv_impl:
        fptr = pyglGetFuncAddress('glTexParameterfv')
        if not fptr:
            raise RuntimeError('The function glTexParameterfv is not available')
        glTexParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glTexParameterfv = (lambda target,pname,params:glTexParameterfv_impl(target,pname,pyglGetAsConstVoidPointer( params )))
    return glTexParameterfv(target, pname, params)
# <command>
#            <proto>void <name>glTexParameteri</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>param</name></param>
#            <glx opcode="107" type="render" />
#        </command>
#        
glTexParameteri_impl=None
def glTexParameteri (target, pname, param):
    global glTexParameteri_impl
    if not glTexParameteri_impl:
        fptr = pyglGetFuncAddress('glTexParameteri')
        if not fptr:
            raise RuntimeError('The function glTexParameteri is not available')
        glTexParameteri_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int)(fptr)
    glTexParameteri = glTexParameteri_impl
    return glTexParameteri(target, pname, param)
# <command>
#            <proto>void <name>glTexParameteriv</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
#            <param group="CheckedInt32" len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>params</name></param>
#            <glx opcode="108" type="render" />
#        </command>
#        
glTexParameteriv_impl=None
def glTexParameteriv (target, pname, params):
    global glTexParameteriv_impl
    if not glTexParameteriv_impl:
        fptr = pyglGetFuncAddress('glTexParameteriv')
        if not fptr:
            raise RuntimeError('The function glTexParameteriv is not available')
        glTexParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glTexParameteriv = (lambda target,pname,params:glTexParameteriv_impl(target,pname,pyglGetAsConstVoidPointer( params )))
    return glTexParameteriv(target, pname, params)
# <command>
#            <proto>void <name>glTexStorage1D</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizei</ptype> <name>levels</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#        </command>
#        
glTexStorage1D_impl=None
def glTexStorage1D (target, levels, internalformat, width):
    global glTexStorage1D_impl
    if not glTexStorage1D_impl:
        fptr = pyglGetFuncAddress('glTexStorage1D')
        if not fptr:
            raise RuntimeError('The function glTexStorage1D is not available')
        glTexStorage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int)(fptr)
    glTexStorage1D = glTexStorage1D_impl
    return glTexStorage1D(target, levels, internalformat, width)
# <command>
#            <proto>void <name>glTexStorage2D</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizei</ptype> <name>levels</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glTexStorage2D_impl=None
def glTexStorage2D (target, levels, internalformat, width, height):
    global glTexStorage2D_impl
    if not glTexStorage2D_impl:
        fptr = pyglGetFuncAddress('glTexStorage2D')
        if not fptr:
            raise RuntimeError('The function glTexStorage2D is not available')
        glTexStorage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int)(fptr)
    glTexStorage2D = glTexStorage2D_impl
    return glTexStorage2D(target, levels, internalformat, width, height)
# <command>
#            <proto>void <name>glTexStorage3D</name></proto>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLsizei</ptype> <name>levels</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#        </command>
#        
glTexStorage3D_impl=None
def glTexStorage3D (target, levels, internalformat, width, height, depth):
    global glTexStorage3D_impl
    if not glTexStorage3D_impl:
        fptr = pyglGetFuncAddress('glTexStorage3D')
        if not fptr:
            raise RuntimeError('The function glTexStorage3D is not available')
        glTexStorage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int, c_int)(fptr)
    glTexStorage3D = glTexStorage3D_impl
    return glTexStorage3D(target, levels, internalformat, width, height, depth)
# <command>
#            <proto>void <name>glTexSubImage1D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type,width)">const void *<name>pixels</name></param>
#            <glx opcode="4099" type="render" />
#            <glx comment="PBO protocol" name="glTexSubImage1DPBO" opcode="331" type="render" />
#        </command>
#        
glTexSubImage1D_impl=None
def glTexSubImage1D (target, level, xoffset, width, format, type, pixels):
    global glTexSubImage1D_impl
    if not glTexSubImage1D_impl:
        fptr = pyglGetFuncAddress('glTexSubImage1D')
        if not fptr:
            raise RuntimeError('The function glTexSubImage1D is not available')
        glTexSubImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTexSubImage1D = (lambda target,level,xoffset,width,format,type,pixels:glTexSubImage1D_impl(target,level,xoffset,width,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTexSubImage1D(target, level, xoffset, width, format, type, pixels)
# <command>
#            <proto>void <name>glTexSubImage2D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type,width,height)">const void *<name>pixels</name></param>
#            <glx opcode="4100" type="render" />
#            <glx comment="PBO protocol" name="glTexSubImage2DPBO" opcode="332" type="render" />
#        </command>
#        
glTexSubImage2D_impl=None
def glTexSubImage2D (target, level, xoffset, yoffset, width, height, format, type, pixels):
    global glTexSubImage2D_impl
    if not glTexSubImage2D_impl:
        fptr = pyglGetFuncAddress('glTexSubImage2D')
        if not fptr:
            raise RuntimeError('The function glTexSubImage2D is not available')
        glTexSubImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTexSubImage2D = (lambda target,level,xoffset,yoffset,width,height,format,type,pixels:glTexSubImage2D_impl(target,level,xoffset,yoffset,width,height,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)
# <command>
#            <proto>void <name>glTexSubImage3D</name></proto>
#            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param group="CheckedInt32"><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
#            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param len="COMPSIZE(format,type,width,height,depth)">const void *<name>pixels</name></param>
#            <glx opcode="4115" type="render" />
#            <glx comment="PBO protocol" name="glTexSubImage3DPBO" opcode="333" type="render" />
#        </command>
#        
glTexSubImage3D_impl=None
def glTexSubImage3D (target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
    global glTexSubImage3D_impl
    if not glTexSubImage3D_impl:
        fptr = pyglGetFuncAddress('glTexSubImage3D')
        if not fptr:
            raise RuntimeError('The function glTexSubImage3D is not available')
        glTexSubImage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTexSubImage3D = (lambda target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels:glTexSubImage3D_impl(target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)
# <command>
#            <proto>void <name>glTextureBarrier</name></proto>
#        </command>
#        
glTextureBarrier_impl=None
def glTextureBarrier ():
    global glTextureBarrier_impl
    if not glTextureBarrier_impl:
        fptr = pyglGetFuncAddress('glTextureBarrier')
        if not fptr:
            raise RuntimeError('The function glTextureBarrier is not available')
        glTextureBarrier_impl = PYGL_FUNC_TYPE( None ,)(fptr)
    glTextureBarrier = glTextureBarrier_impl
    return glTextureBarrier()
# <command>
#            <proto>void <name>glTextureBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glTextureBuffer_impl=None
def glTextureBuffer (texture, internalformat, buffer):
    global glTextureBuffer_impl
    if not glTextureBuffer_impl:
        fptr = pyglGetFuncAddress('glTextureBuffer')
        if not fptr:
            raise RuntimeError('The function glTextureBuffer is not available')
        glTextureBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glTextureBuffer = glTextureBuffer_impl
    return glTextureBuffer(texture, internalformat, buffer)
# <command>
#            <proto>void <name>glTextureBufferRange</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#        </command>
#        
glTextureBufferRange_impl=None
def glTextureBufferRange (texture, internalformat, buffer, offset, size):
    global glTextureBufferRange_impl
    if not glTextureBufferRange_impl:
        fptr = pyglGetFuncAddress('glTextureBufferRange')
        if not fptr:
            raise RuntimeError('The function glTextureBufferRange is not available')
        glTextureBufferRange_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t, c_void_p)(fptr)
    glTextureBufferRange = glTextureBufferRange_impl
    return glTextureBufferRange(texture, internalformat, buffer, offset, size)
# <command>
#            <proto>void <name>glTextureParameterIiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param>const <ptype>GLint</ptype> *<name>params</name></param>
#        </command>
#        
glTextureParameterIiv_impl=None
def glTextureParameterIiv (texture, pname, params):
    global glTextureParameterIiv_impl
    if not glTextureParameterIiv_impl:
        fptr = pyglGetFuncAddress('glTextureParameterIiv')
        if not fptr:
            raise RuntimeError('The function glTextureParameterIiv is not available')
        glTextureParameterIiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glTextureParameterIiv = (lambda texture,pname,params:glTextureParameterIiv_impl(texture,pname,pyglGetAsConstVoidPointer( params )))
    return glTextureParameterIiv(texture, pname, params)
# <command>
#            <proto>void <name>glTextureParameterIuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param>const <ptype>GLuint</ptype> *<name>params</name></param>
#        </command>
#        
glTextureParameterIuiv_impl=None
def glTextureParameterIuiv (texture, pname, params):
    global glTextureParameterIuiv_impl
    if not glTextureParameterIuiv_impl:
        fptr = pyglGetFuncAddress('glTextureParameterIuiv')
        if not fptr:
            raise RuntimeError('The function glTextureParameterIuiv is not available')
        glTextureParameterIuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glTextureParameterIuiv = (lambda texture,pname,params:glTextureParameterIuiv_impl(texture,pname,pyglGetAsConstVoidPointer( params )))
    return glTextureParameterIuiv(texture, pname, params)
# <command>
#            <proto>void <name>glTextureParameterf</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLfloat</ptype> <name>param</name></param>
#        </command>
#        
glTextureParameterf_impl=None
def glTextureParameterf (texture, pname, param):
    global glTextureParameterf_impl
    if not glTextureParameterf_impl:
        fptr = pyglGetFuncAddress('glTextureParameterf')
        if not fptr:
            raise RuntimeError('The function glTextureParameterf is not available')
        glTextureParameterf_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_float)(fptr)
    glTextureParameterf = glTextureParameterf_impl
    return glTextureParameterf(texture, pname, param)
# <command>
#            <proto>void <name>glTextureParameterfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param>const <ptype>GLfloat</ptype> *<name>param</name></param>
#        </command>
#        
glTextureParameterfv_impl=None
def glTextureParameterfv (texture, pname, param):
    global glTextureParameterfv_impl
    if not glTextureParameterfv_impl:
        fptr = pyglGetFuncAddress('glTextureParameterfv')
        if not fptr:
            raise RuntimeError('The function glTextureParameterfv is not available')
        glTextureParameterfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glTextureParameterfv = (lambda texture,pname,param:glTextureParameterfv_impl(texture,pname,pyglGetAsConstVoidPointer( param )))
    return glTextureParameterfv(texture, pname, param)
# <command>
#            <proto>void <name>glTextureParameteri</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param><ptype>GLint</ptype> <name>param</name></param>
#        </command>
#        
glTextureParameteri_impl=None
def glTextureParameteri (texture, pname, param):
    global glTextureParameteri_impl
    if not glTextureParameteri_impl:
        fptr = pyglGetFuncAddress('glTextureParameteri')
        if not fptr:
            raise RuntimeError('The function glTextureParameteri is not available')
        glTextureParameteri_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int)(fptr)
    glTextureParameteri = glTextureParameteri_impl
    return glTextureParameteri(texture, pname, param)
# <command>
#            <proto>void <name>glTextureParameteriv</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>pname</name></param>
#            <param>const <ptype>GLint</ptype> *<name>param</name></param>
#        </command>
#        
glTextureParameteriv_impl=None
def glTextureParameteriv (texture, pname, param):
    global glTextureParameteriv_impl
    if not glTextureParameteriv_impl:
        fptr = pyglGetFuncAddress('glTextureParameteriv')
        if not fptr:
            raise RuntimeError('The function glTextureParameteriv is not available')
        glTextureParameteriv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_void_p)(fptr)
    glTextureParameteriv = (lambda texture,pname,param:glTextureParameteriv_impl(texture,pname,pyglGetAsConstVoidPointer( param )))
    return glTextureParameteriv(texture, pname, param)
# <command>
#            <proto>void <name>glTextureStorage1D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLsizei</ptype> <name>levels</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#        </command>
#        
glTextureStorage1D_impl=None
def glTextureStorage1D (texture, levels, internalformat, width):
    global glTextureStorage1D_impl
    if not glTextureStorage1D_impl:
        fptr = pyglGetFuncAddress('glTextureStorage1D')
        if not fptr:
            raise RuntimeError('The function glTextureStorage1D is not available')
        glTextureStorage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int)(fptr)
    glTextureStorage1D = glTextureStorage1D_impl
    return glTextureStorage1D(texture, levels, internalformat, width)
# <command>
#            <proto>void <name>glTextureStorage2D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLsizei</ptype> <name>levels</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#        </command>
#        
glTextureStorage2D_impl=None
def glTextureStorage2D (texture, levels, internalformat, width, height):
    global glTextureStorage2D_impl
    if not glTextureStorage2D_impl:
        fptr = pyglGetFuncAddress('glTextureStorage2D')
        if not fptr:
            raise RuntimeError('The function glTextureStorage2D is not available')
        glTextureStorage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int)(fptr)
    glTextureStorage2D = glTextureStorage2D_impl
    return glTextureStorage2D(texture, levels, internalformat, width, height)
# <command>
#            <proto>void <name>glTextureStorage3D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLsizei</ptype> <name>levels</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#        </command>
#        
glTextureStorage3D_impl=None
def glTextureStorage3D (texture, levels, internalformat, width, height, depth):
    global glTextureStorage3D_impl
    if not glTextureStorage3D_impl:
        fptr = pyglGetFuncAddress('glTextureStorage3D')
        if not fptr:
            raise RuntimeError('The function glTextureStorage3D is not available')
        glTextureStorage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_int, c_int, c_int)(fptr)
    glTextureStorage3D = glTextureStorage3D_impl
    return glTextureStorage3D(texture, levels, internalformat, width, height, depth)
# <command>
#            <proto>void <name>glTextureSubImage1D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param>const void *<name>pixels</name></param>
#        </command>
#        
glTextureSubImage1D_impl=None
def glTextureSubImage1D (texture, level, xoffset, width, format, type, pixels):
    global glTextureSubImage1D_impl
    if not glTextureSubImage1D_impl:
        fptr = pyglGetFuncAddress('glTextureSubImage1D')
        if not fptr:
            raise RuntimeError('The function glTextureSubImage1D is not available')
        glTextureSubImage1D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTextureSubImage1D = (lambda texture,level,xoffset,width,format,type,pixels:glTextureSubImage1D_impl(texture,level,xoffset,width,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTextureSubImage1D(texture, level, xoffset, width, format, type, pixels)
# <command>
#            <proto>void <name>glTextureSubImage2D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param>const void *<name>pixels</name></param>
#        </command>
#        
glTextureSubImage2D_impl=None
def glTextureSubImage2D (texture, level, xoffset, yoffset, width, height, format, type, pixels):
    global glTextureSubImage2D_impl
    if not glTextureSubImage2D_impl:
        fptr = pyglGetFuncAddress('glTextureSubImage2D')
        if not fptr:
            raise RuntimeError('The function glTextureSubImage2D is not available')
        glTextureSubImage2D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTextureSubImage2D = (lambda texture,level,xoffset,yoffset,width,height,format,type,pixels:glTextureSubImage2D_impl(texture,level,xoffset,yoffset,width,height,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels)
# <command>
#            <proto>void <name>glTextureSubImage3D</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLint</ptype> <name>level</name></param>
#            <param><ptype>GLint</ptype> <name>xoffset</name></param>
#            <param><ptype>GLint</ptype> <name>yoffset</name></param>
#            <param><ptype>GLint</ptype> <name>zoffset</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <param><ptype>GLsizei</ptype> <name>depth</name></param>
#            <param><ptype>GLenum</ptype> <name>format</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param>const void *<name>pixels</name></param>
#        </command>
#        
glTextureSubImage3D_impl=None
def glTextureSubImage3D (texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels):
    global glTextureSubImage3D_impl
    if not glTextureSubImage3D_impl:
        fptr = pyglGetFuncAddress('glTextureSubImage3D')
        if not fptr:
            raise RuntimeError('The function glTextureSubImage3D is not available')
        glTextureSubImage3D_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_uint, c_uint, c_void_p)(fptr)
    glTextureSubImage3D = (lambda texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels:glTextureSubImage3D_impl(texture,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pyglGetAsConstVoidPointer( pixels )))
    return glTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)
# <command>
#            <proto>void <name>glTextureView</name></proto>
#            <param><ptype>GLuint</ptype> <name>texture</name></param>
#            <param><ptype>GLenum</ptype> <name>target</name></param>
#            <param><ptype>GLuint</ptype> <name>origtexture</name></param>
#            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
#            <param><ptype>GLuint</ptype> <name>minlevel</name></param>
#            <param><ptype>GLuint</ptype> <name>numlevels</name></param>
#            <param><ptype>GLuint</ptype> <name>minlayer</name></param>
#            <param><ptype>GLuint</ptype> <name>numlayers</name></param>
#        </command>
#        
glTextureView_impl=None
def glTextureView (texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers):
    global glTextureView_impl
    if not glTextureView_impl:
        fptr = pyglGetFuncAddress('glTextureView')
        if not fptr:
            raise RuntimeError('The function glTextureView is not available')
        glTextureView_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_uint, c_uint, c_uint, c_uint)(fptr)
    glTextureView = glTextureView_impl
    return glTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers)
# <command>
#            <proto>void <name>glTransformFeedbackBufferBase</name></proto>
#            <param><ptype>GLuint</ptype> <name>xfb</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glTransformFeedbackBufferBase_impl=None
def glTransformFeedbackBufferBase (xfb, index, buffer):
    global glTransformFeedbackBufferBase_impl
    if not glTransformFeedbackBufferBase_impl:
        fptr = pyglGetFuncAddress('glTransformFeedbackBufferBase')
        if not fptr:
            raise RuntimeError('The function glTransformFeedbackBufferBase is not available')
        glTransformFeedbackBufferBase_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glTransformFeedbackBufferBase = glTransformFeedbackBufferBase_impl
    return glTransformFeedbackBufferBase(xfb, index, buffer)
# <command>
#            <proto>void <name>glTransformFeedbackBufferRange</name></proto>
#            <param><ptype>GLuint</ptype> <name>xfb</name></param>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
#        </command>
#        
glTransformFeedbackBufferRange_impl=None
def glTransformFeedbackBufferRange (xfb, index, buffer, offset, size):
    global glTransformFeedbackBufferRange_impl
    if not glTransformFeedbackBufferRange_impl:
        fptr = pyglGetFuncAddress('glTransformFeedbackBufferRange')
        if not fptr:
            raise RuntimeError('The function glTransformFeedbackBufferRange is not available')
        glTransformFeedbackBufferRange_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t, c_void_p)(fptr)
    glTransformFeedbackBufferRange = glTransformFeedbackBufferRange_impl
    return glTransformFeedbackBufferRange(xfb, index, buffer, offset, size)
# <command>
#            <proto>void <name>glTransformFeedbackVaryings</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLchar</ptype> *const*<name>varyings</name></param>
#            <param><ptype>GLenum</ptype> <name>bufferMode</name></param>
#        </command>
#        
glTransformFeedbackVaryings_impl=None
def glTransformFeedbackVaryings (program, count, varyings, bufferMode):
    global glTransformFeedbackVaryings_impl
    if not glTransformFeedbackVaryings_impl:
        fptr = pyglGetFuncAddress('glTransformFeedbackVaryings')
        if not fptr:
            raise RuntimeError('The function glTransformFeedbackVaryings is not available')
        glTransformFeedbackVaryings_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p, c_uint)(fptr)
    glTransformFeedbackVaryings = (lambda program,count,varyings,bufferMode:glTransformFeedbackVaryings_impl(program,count,c_char_p( varyings .encode() ),bufferMode))
    return glTransformFeedbackVaryings(program, count, varyings, bufferMode)
# <command>
#            <proto>void <name>glUniform1d</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#        </command>
#        
glUniform1d_impl=None
def glUniform1d (location, x):
    global glUniform1d_impl
    if not glUniform1d_impl:
        fptr = pyglGetFuncAddress('glUniform1d')
        if not fptr:
            raise RuntimeError('The function glUniform1d is not available')
        glUniform1d_impl = PYGL_FUNC_TYPE( None ,c_int, c_double)(fptr)
    glUniform1d = glUniform1d_impl
    return glUniform1d(location, x)
# <command>
#            <proto>void <name>glUniform1dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*1">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniform1dv_impl=None
def glUniform1dv (location, count, value):
    global glUniform1dv_impl
    if not glUniform1dv_impl:
        fptr = pyglGetFuncAddress('glUniform1dv')
        if not fptr:
            raise RuntimeError('The function glUniform1dv is not available')
        glUniform1dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform1dv = (lambda location,count,value:glUniform1dv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform1dv(location, count, value)
# <command>
#            <proto>void <name>glUniform1f</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLfloat</ptype> <name>v0</name></param>
#        </command>
#        
glUniform1f_impl=None
def glUniform1f (location, v0):
    global glUniform1f_impl
    if not glUniform1f_impl:
        fptr = pyglGetFuncAddress('glUniform1f')
        if not fptr:
            raise RuntimeError('The function glUniform1f is not available')
        glUniform1f_impl = PYGL_FUNC_TYPE( None ,c_int, c_float)(fptr)
    glUniform1f = glUniform1f_impl
    return glUniform1f(location, v0)
# <command>
#            <proto>void <name>glUniform1fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*1">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glUniform1fv_impl=None
def glUniform1fv (location, count, value):
    global glUniform1fv_impl
    if not glUniform1fv_impl:
        fptr = pyglGetFuncAddress('glUniform1fv')
        if not fptr:
            raise RuntimeError('The function glUniform1fv is not available')
        glUniform1fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform1fv = (lambda location,count,value:glUniform1fv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform1fv(location, count, value)
# <command>
#            <proto>void <name>glUniform1i</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLint</ptype> <name>v0</name></param>
#        </command>
#        
glUniform1i_impl=None
def glUniform1i (location, v0):
    global glUniform1i_impl
    if not glUniform1i_impl:
        fptr = pyglGetFuncAddress('glUniform1i')
        if not fptr:
            raise RuntimeError('The function glUniform1i is not available')
        glUniform1i_impl = PYGL_FUNC_TYPE( None ,c_int, c_int)(fptr)
    glUniform1i = glUniform1i_impl
    return glUniform1i(location, v0)
# <command>
#            <proto>void <name>glUniform1iv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*1">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glUniform1iv_impl=None
def glUniform1iv (location, count, value):
    global glUniform1iv_impl
    if not glUniform1iv_impl:
        fptr = pyglGetFuncAddress('glUniform1iv')
        if not fptr:
            raise RuntimeError('The function glUniform1iv is not available')
        glUniform1iv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform1iv = (lambda location,count,value:glUniform1iv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform1iv(location, count, value)
# <command>
#            <proto>void <name>glUniform1ui</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLuint</ptype> <name>v0</name></param>
#        </command>
#        
glUniform1ui_impl=None
def glUniform1ui (location, v0):
    global glUniform1ui_impl
    if not glUniform1ui_impl:
        fptr = pyglGetFuncAddress('glUniform1ui')
        if not fptr:
            raise RuntimeError('The function glUniform1ui is not available')
        glUniform1ui_impl = PYGL_FUNC_TYPE( None ,c_int, c_uint)(fptr)
    glUniform1ui = glUniform1ui_impl
    return glUniform1ui(location, v0)
# <command>
#            <proto>void <name>glUniform1uiv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*1">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glUniform1uiv_impl=None
def glUniform1uiv (location, count, value):
    global glUniform1uiv_impl
    if not glUniform1uiv_impl:
        fptr = pyglGetFuncAddress('glUniform1uiv')
        if not fptr:
            raise RuntimeError('The function glUniform1uiv is not available')
        glUniform1uiv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform1uiv = (lambda location,count,value:glUniform1uiv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform1uiv(location, count, value)
# <command>
#            <proto>void <name>glUniform2d</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#        </command>
#        
glUniform2d_impl=None
def glUniform2d (location, x, y):
    global glUniform2d_impl
    if not glUniform2d_impl:
        fptr = pyglGetFuncAddress('glUniform2d')
        if not fptr:
            raise RuntimeError('The function glUniform2d is not available')
        glUniform2d_impl = PYGL_FUNC_TYPE( None ,c_int, c_double, c_double)(fptr)
    glUniform2d = glUniform2d_impl
    return glUniform2d(location, x, y)
# <command>
#            <proto>void <name>glUniform2dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*2">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniform2dv_impl=None
def glUniform2dv (location, count, value):
    global glUniform2dv_impl
    if not glUniform2dv_impl:
        fptr = pyglGetFuncAddress('glUniform2dv')
        if not fptr:
            raise RuntimeError('The function glUniform2dv is not available')
        glUniform2dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform2dv = (lambda location,count,value:glUniform2dv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform2dv(location, count, value)
# <command>
#            <proto>void <name>glUniform2f</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLfloat</ptype> <name>v0</name></param>
#            <param><ptype>GLfloat</ptype> <name>v1</name></param>
#        </command>
#        
glUniform2f_impl=None
def glUniform2f (location, v0, v1):
    global glUniform2f_impl
    if not glUniform2f_impl:
        fptr = pyglGetFuncAddress('glUniform2f')
        if not fptr:
            raise RuntimeError('The function glUniform2f is not available')
        glUniform2f_impl = PYGL_FUNC_TYPE( None ,c_int, c_float, c_float)(fptr)
    glUniform2f = glUniform2f_impl
    return glUniform2f(location, v0, v1)
# <command>
#            <proto>void <name>glUniform2fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*2">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glUniform2fv_impl=None
def glUniform2fv (location, count, value):
    global glUniform2fv_impl
    if not glUniform2fv_impl:
        fptr = pyglGetFuncAddress('glUniform2fv')
        if not fptr:
            raise RuntimeError('The function glUniform2fv is not available')
        glUniform2fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform2fv = (lambda location,count,value:glUniform2fv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform2fv(location, count, value)
# <command>
#            <proto>void <name>glUniform2i</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLint</ptype> <name>v0</name></param>
#            <param><ptype>GLint</ptype> <name>v1</name></param>
#        </command>
#        
glUniform2i_impl=None
def glUniform2i (location, v0, v1):
    global glUniform2i_impl
    if not glUniform2i_impl:
        fptr = pyglGetFuncAddress('glUniform2i')
        if not fptr:
            raise RuntimeError('The function glUniform2i is not available')
        glUniform2i_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_int)(fptr)
    glUniform2i = glUniform2i_impl
    return glUniform2i(location, v0, v1)
# <command>
#            <proto>void <name>glUniform2iv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*2">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glUniform2iv_impl=None
def glUniform2iv (location, count, value):
    global glUniform2iv_impl
    if not glUniform2iv_impl:
        fptr = pyglGetFuncAddress('glUniform2iv')
        if not fptr:
            raise RuntimeError('The function glUniform2iv is not available')
        glUniform2iv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform2iv = (lambda location,count,value:glUniform2iv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform2iv(location, count, value)
# <command>
#            <proto>void <name>glUniform2ui</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLuint</ptype> <name>v0</name></param>
#            <param><ptype>GLuint</ptype> <name>v1</name></param>
#        </command>
#        
glUniform2ui_impl=None
def glUniform2ui (location, v0, v1):
    global glUniform2ui_impl
    if not glUniform2ui_impl:
        fptr = pyglGetFuncAddress('glUniform2ui')
        if not fptr:
            raise RuntimeError('The function glUniform2ui is not available')
        glUniform2ui_impl = PYGL_FUNC_TYPE( None ,c_int, c_uint, c_uint)(fptr)
    glUniform2ui = glUniform2ui_impl
    return glUniform2ui(location, v0, v1)
# <command>
#            <proto>void <name>glUniform2uiv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*2">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glUniform2uiv_impl=None
def glUniform2uiv (location, count, value):
    global glUniform2uiv_impl
    if not glUniform2uiv_impl:
        fptr = pyglGetFuncAddress('glUniform2uiv')
        if not fptr:
            raise RuntimeError('The function glUniform2uiv is not available')
        glUniform2uiv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform2uiv = (lambda location,count,value:glUniform2uiv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform2uiv(location, count, value)
# <command>
#            <proto>void <name>glUniform3d</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#            <param><ptype>GLdouble</ptype> <name>z</name></param>
#        </command>
#        
glUniform3d_impl=None
def glUniform3d (location, x, y, z):
    global glUniform3d_impl
    if not glUniform3d_impl:
        fptr = pyglGetFuncAddress('glUniform3d')
        if not fptr:
            raise RuntimeError('The function glUniform3d is not available')
        glUniform3d_impl = PYGL_FUNC_TYPE( None ,c_int, c_double, c_double, c_double)(fptr)
    glUniform3d = glUniform3d_impl
    return glUniform3d(location, x, y, z)
# <command>
#            <proto>void <name>glUniform3dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*3">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniform3dv_impl=None
def glUniform3dv (location, count, value):
    global glUniform3dv_impl
    if not glUniform3dv_impl:
        fptr = pyglGetFuncAddress('glUniform3dv')
        if not fptr:
            raise RuntimeError('The function glUniform3dv is not available')
        glUniform3dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform3dv = (lambda location,count,value:glUniform3dv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform3dv(location, count, value)
# <command>
#            <proto>void <name>glUniform3f</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLfloat</ptype> <name>v0</name></param>
#            <param><ptype>GLfloat</ptype> <name>v1</name></param>
#            <param><ptype>GLfloat</ptype> <name>v2</name></param>
#        </command>
#        
glUniform3f_impl=None
def glUniform3f (location, v0, v1, v2):
    global glUniform3f_impl
    if not glUniform3f_impl:
        fptr = pyglGetFuncAddress('glUniform3f')
        if not fptr:
            raise RuntimeError('The function glUniform3f is not available')
        glUniform3f_impl = PYGL_FUNC_TYPE( None ,c_int, c_float, c_float, c_float)(fptr)
    glUniform3f = glUniform3f_impl
    return glUniform3f(location, v0, v1, v2)
# <command>
#            <proto>void <name>glUniform3fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*3">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glUniform3fv_impl=None
def glUniform3fv (location, count, value):
    global glUniform3fv_impl
    if not glUniform3fv_impl:
        fptr = pyglGetFuncAddress('glUniform3fv')
        if not fptr:
            raise RuntimeError('The function glUniform3fv is not available')
        glUniform3fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform3fv = (lambda location,count,value:glUniform3fv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform3fv(location, count, value)
# <command>
#            <proto>void <name>glUniform3i</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLint</ptype> <name>v0</name></param>
#            <param><ptype>GLint</ptype> <name>v1</name></param>
#            <param><ptype>GLint</ptype> <name>v2</name></param>
#        </command>
#        
glUniform3i_impl=None
def glUniform3i (location, v0, v1, v2):
    global glUniform3i_impl
    if not glUniform3i_impl:
        fptr = pyglGetFuncAddress('glUniform3i')
        if not fptr:
            raise RuntimeError('The function glUniform3i is not available')
        glUniform3i_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_int, c_int)(fptr)
    glUniform3i = glUniform3i_impl
    return glUniform3i(location, v0, v1, v2)
# <command>
#            <proto>void <name>glUniform3iv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*3">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glUniform3iv_impl=None
def glUniform3iv (location, count, value):
    global glUniform3iv_impl
    if not glUniform3iv_impl:
        fptr = pyglGetFuncAddress('glUniform3iv')
        if not fptr:
            raise RuntimeError('The function glUniform3iv is not available')
        glUniform3iv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform3iv = (lambda location,count,value:glUniform3iv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform3iv(location, count, value)
# <command>
#            <proto>void <name>glUniform3ui</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLuint</ptype> <name>v0</name></param>
#            <param><ptype>GLuint</ptype> <name>v1</name></param>
#            <param><ptype>GLuint</ptype> <name>v2</name></param>
#        </command>
#        
glUniform3ui_impl=None
def glUniform3ui (location, v0, v1, v2):
    global glUniform3ui_impl
    if not glUniform3ui_impl:
        fptr = pyglGetFuncAddress('glUniform3ui')
        if not fptr:
            raise RuntimeError('The function glUniform3ui is not available')
        glUniform3ui_impl = PYGL_FUNC_TYPE( None ,c_int, c_uint, c_uint, c_uint)(fptr)
    glUniform3ui = glUniform3ui_impl
    return glUniform3ui(location, v0, v1, v2)
# <command>
#            <proto>void <name>glUniform3uiv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*3">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glUniform3uiv_impl=None
def glUniform3uiv (location, count, value):
    global glUniform3uiv_impl
    if not glUniform3uiv_impl:
        fptr = pyglGetFuncAddress('glUniform3uiv')
        if not fptr:
            raise RuntimeError('The function glUniform3uiv is not available')
        glUniform3uiv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform3uiv = (lambda location,count,value:glUniform3uiv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform3uiv(location, count, value)
# <command>
#            <proto>void <name>glUniform4d</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#            <param><ptype>GLdouble</ptype> <name>z</name></param>
#            <param><ptype>GLdouble</ptype> <name>w</name></param>
#        </command>
#        
glUniform4d_impl=None
def glUniform4d (location, x, y, z, w):
    global glUniform4d_impl
    if not glUniform4d_impl:
        fptr = pyglGetFuncAddress('glUniform4d')
        if not fptr:
            raise RuntimeError('The function glUniform4d is not available')
        glUniform4d_impl = PYGL_FUNC_TYPE( None ,c_int, c_double, c_double, c_double, c_double)(fptr)
    glUniform4d = glUniform4d_impl
    return glUniform4d(location, x, y, z, w)
# <command>
#            <proto>void <name>glUniform4dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*4">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniform4dv_impl=None
def glUniform4dv (location, count, value):
    global glUniform4dv_impl
    if not glUniform4dv_impl:
        fptr = pyglGetFuncAddress('glUniform4dv')
        if not fptr:
            raise RuntimeError('The function glUniform4dv is not available')
        glUniform4dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform4dv = (lambda location,count,value:glUniform4dv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform4dv(location, count, value)
# <command>
#            <proto>void <name>glUniform4f</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLfloat</ptype> <name>v0</name></param>
#            <param><ptype>GLfloat</ptype> <name>v1</name></param>
#            <param><ptype>GLfloat</ptype> <name>v2</name></param>
#            <param><ptype>GLfloat</ptype> <name>v3</name></param>
#        </command>
#        
glUniform4f_impl=None
def glUniform4f (location, v0, v1, v2, v3):
    global glUniform4f_impl
    if not glUniform4f_impl:
        fptr = pyglGetFuncAddress('glUniform4f')
        if not fptr:
            raise RuntimeError('The function glUniform4f is not available')
        glUniform4f_impl = PYGL_FUNC_TYPE( None ,c_int, c_float, c_float, c_float, c_float)(fptr)
    glUniform4f = glUniform4f_impl
    return glUniform4f(location, v0, v1, v2, v3)
# <command>
#            <proto>void <name>glUniform4fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*4">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glUniform4fv_impl=None
def glUniform4fv (location, count, value):
    global glUniform4fv_impl
    if not glUniform4fv_impl:
        fptr = pyglGetFuncAddress('glUniform4fv')
        if not fptr:
            raise RuntimeError('The function glUniform4fv is not available')
        glUniform4fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform4fv = (lambda location,count,value:glUniform4fv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform4fv(location, count, value)
# <command>
#            <proto>void <name>glUniform4i</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLint</ptype> <name>v0</name></param>
#            <param><ptype>GLint</ptype> <name>v1</name></param>
#            <param><ptype>GLint</ptype> <name>v2</name></param>
#            <param><ptype>GLint</ptype> <name>v3</name></param>
#        </command>
#        
glUniform4i_impl=None
def glUniform4i (location, v0, v1, v2, v3):
    global glUniform4i_impl
    if not glUniform4i_impl:
        fptr = pyglGetFuncAddress('glUniform4i')
        if not fptr:
            raise RuntimeError('The function glUniform4i is not available')
        glUniform4i_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_int, c_int, c_int)(fptr)
    glUniform4i = glUniform4i_impl
    return glUniform4i(location, v0, v1, v2, v3)
# <command>
#            <proto>void <name>glUniform4iv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*4">const <ptype>GLint</ptype> *<name>value</name></param>
#        </command>
#        
glUniform4iv_impl=None
def glUniform4iv (location, count, value):
    global glUniform4iv_impl
    if not glUniform4iv_impl:
        fptr = pyglGetFuncAddress('glUniform4iv')
        if not fptr:
            raise RuntimeError('The function glUniform4iv is not available')
        glUniform4iv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform4iv = (lambda location,count,value:glUniform4iv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform4iv(location, count, value)
# <command>
#            <proto>void <name>glUniform4ui</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLuint</ptype> <name>v0</name></param>
#            <param><ptype>GLuint</ptype> <name>v1</name></param>
#            <param><ptype>GLuint</ptype> <name>v2</name></param>
#            <param><ptype>GLuint</ptype> <name>v3</name></param>
#        </command>
#        
glUniform4ui_impl=None
def glUniform4ui (location, v0, v1, v2, v3):
    global glUniform4ui_impl
    if not glUniform4ui_impl:
        fptr = pyglGetFuncAddress('glUniform4ui')
        if not fptr:
            raise RuntimeError('The function glUniform4ui is not available')
        glUniform4ui_impl = PYGL_FUNC_TYPE( None ,c_int, c_uint, c_uint, c_uint, c_uint)(fptr)
    glUniform4ui = glUniform4ui_impl
    return glUniform4ui(location, v0, v1, v2, v3)
# <command>
#            <proto>void <name>glUniform4uiv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count*4">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glUniform4uiv_impl=None
def glUniform4uiv (location, count, value):
    global glUniform4uiv_impl
    if not glUniform4uiv_impl:
        fptr = pyglGetFuncAddress('glUniform4uiv')
        if not fptr:
            raise RuntimeError('The function glUniform4uiv is not available')
        glUniform4uiv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_void_p)(fptr)
    glUniform4uiv = (lambda location,count,value:glUniform4uiv_impl(location,count,pyglGetAsConstVoidPointer( value )))
    return glUniform4uiv(location, count, value)
# <command>
#            <proto>void <name>glUniformBlockBinding</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#            <param><ptype>GLuint</ptype> <name>uniformBlockIndex</name></param>
#            <param><ptype>GLuint</ptype> <name>uniformBlockBinding</name></param>
#        </command>
#        
glUniformBlockBinding_impl=None
def glUniformBlockBinding (program, uniformBlockIndex, uniformBlockBinding):
    global glUniformBlockBinding_impl
    if not glUniformBlockBinding_impl:
        fptr = pyglGetFuncAddress('glUniformBlockBinding')
        if not fptr:
            raise RuntimeError('The function glUniformBlockBinding is not available')
        glUniformBlockBinding_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glUniformBlockBinding = glUniformBlockBinding_impl
    return glUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding)
# <command>
#            <proto>void <name>glUniformMatrix2dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*4">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix2dv_impl=None
def glUniformMatrix2dv (location, count, transpose, value):
    global glUniformMatrix2dv_impl
    if not glUniformMatrix2dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix2dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2dv is not available')
        glUniformMatrix2dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix2dv = (lambda location,count,transpose,value:glUniformMatrix2dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix2dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix2fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*4">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix2fv_impl=None
def glUniformMatrix2fv (location, count, transpose, value):
    global glUniformMatrix2fv_impl
    if not glUniformMatrix2fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix2fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2fv is not available')
        glUniformMatrix2fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix2fv = (lambda location,count,transpose,value:glUniformMatrix2fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix2fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix2x3dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*6">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix2x3dv_impl=None
def glUniformMatrix2x3dv (location, count, transpose, value):
    global glUniformMatrix2x3dv_impl
    if not glUniformMatrix2x3dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix2x3dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2x3dv is not available')
        glUniformMatrix2x3dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix2x3dv = (lambda location,count,transpose,value:glUniformMatrix2x3dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix2x3dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix2x3fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*6">const <ptype>GLfloat</ptype> *<name>value</name></param>
#            <glx opcode="305" type="render" />
#        </command>
#        
glUniformMatrix2x3fv_impl=None
def glUniformMatrix2x3fv (location, count, transpose, value):
    global glUniformMatrix2x3fv_impl
    if not glUniformMatrix2x3fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix2x3fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2x3fv is not available')
        glUniformMatrix2x3fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix2x3fv = (lambda location,count,transpose,value:glUniformMatrix2x3fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix2x3fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix2x4dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*8">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix2x4dv_impl=None
def glUniformMatrix2x4dv (location, count, transpose, value):
    global glUniformMatrix2x4dv_impl
    if not glUniformMatrix2x4dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix2x4dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2x4dv is not available')
        glUniformMatrix2x4dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix2x4dv = (lambda location,count,transpose,value:glUniformMatrix2x4dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix2x4dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix2x4fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*8">const <ptype>GLfloat</ptype> *<name>value</name></param>
#            <glx opcode="307" type="render" />
#        </command>
#        
glUniformMatrix2x4fv_impl=None
def glUniformMatrix2x4fv (location, count, transpose, value):
    global glUniformMatrix2x4fv_impl
    if not glUniformMatrix2x4fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix2x4fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix2x4fv is not available')
        glUniformMatrix2x4fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix2x4fv = (lambda location,count,transpose,value:glUniformMatrix2x4fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix2x4fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix3dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*9">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix3dv_impl=None
def glUniformMatrix3dv (location, count, transpose, value):
    global glUniformMatrix3dv_impl
    if not glUniformMatrix3dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix3dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3dv is not available')
        glUniformMatrix3dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix3dv = (lambda location,count,transpose,value:glUniformMatrix3dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix3dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix3fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*9">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix3fv_impl=None
def glUniformMatrix3fv (location, count, transpose, value):
    global glUniformMatrix3fv_impl
    if not glUniformMatrix3fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix3fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3fv is not available')
        glUniformMatrix3fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix3fv = (lambda location,count,transpose,value:glUniformMatrix3fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix3fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix3x2dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*6">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix3x2dv_impl=None
def glUniformMatrix3x2dv (location, count, transpose, value):
    global glUniformMatrix3x2dv_impl
    if not glUniformMatrix3x2dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix3x2dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3x2dv is not available')
        glUniformMatrix3x2dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix3x2dv = (lambda location,count,transpose,value:glUniformMatrix3x2dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix3x2dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix3x2fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*6">const <ptype>GLfloat</ptype> *<name>value</name></param>
#            <glx opcode="306" type="render" />
#        </command>
#        
glUniformMatrix3x2fv_impl=None
def glUniformMatrix3x2fv (location, count, transpose, value):
    global glUniformMatrix3x2fv_impl
    if not glUniformMatrix3x2fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix3x2fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3x2fv is not available')
        glUniformMatrix3x2fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix3x2fv = (lambda location,count,transpose,value:glUniformMatrix3x2fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix3x2fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix3x4dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*12">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix3x4dv_impl=None
def glUniformMatrix3x4dv (location, count, transpose, value):
    global glUniformMatrix3x4dv_impl
    if not glUniformMatrix3x4dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix3x4dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3x4dv is not available')
        glUniformMatrix3x4dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix3x4dv = (lambda location,count,transpose,value:glUniformMatrix3x4dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix3x4dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix3x4fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*12">const <ptype>GLfloat</ptype> *<name>value</name></param>
#            <glx opcode="309" type="render" />
#        </command>
#        
glUniformMatrix3x4fv_impl=None
def glUniformMatrix3x4fv (location, count, transpose, value):
    global glUniformMatrix3x4fv_impl
    if not glUniformMatrix3x4fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix3x4fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix3x4fv is not available')
        glUniformMatrix3x4fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix3x4fv = (lambda location,count,transpose,value:glUniformMatrix3x4fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix3x4fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix4dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*16">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix4dv_impl=None
def glUniformMatrix4dv (location, count, transpose, value):
    global glUniformMatrix4dv_impl
    if not glUniformMatrix4dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix4dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4dv is not available')
        glUniformMatrix4dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix4dv = (lambda location,count,transpose,value:glUniformMatrix4dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix4dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix4fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*16">const <ptype>GLfloat</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix4fv_impl=None
def glUniformMatrix4fv (location, count, transpose, value):
    global glUniformMatrix4fv_impl
    if not glUniformMatrix4fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix4fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4fv is not available')
        glUniformMatrix4fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix4fv = (lambda location,count,transpose,value:glUniformMatrix4fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix4fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix4x2dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*8">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix4x2dv_impl=None
def glUniformMatrix4x2dv (location, count, transpose, value):
    global glUniformMatrix4x2dv_impl
    if not glUniformMatrix4x2dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix4x2dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4x2dv is not available')
        glUniformMatrix4x2dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix4x2dv = (lambda location,count,transpose,value:glUniformMatrix4x2dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix4x2dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix4x2fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*8">const <ptype>GLfloat</ptype> *<name>value</name></param>
#            <glx opcode="308" type="render" />
#        </command>
#        
glUniformMatrix4x2fv_impl=None
def glUniformMatrix4x2fv (location, count, transpose, value):
    global glUniformMatrix4x2fv_impl
    if not glUniformMatrix4x2fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix4x2fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4x2fv is not available')
        glUniformMatrix4x2fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix4x2fv = (lambda location,count,transpose,value:glUniformMatrix4x2fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix4x2fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix4x3dv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*12">const <ptype>GLdouble</ptype> *<name>value</name></param>
#        </command>
#        
glUniformMatrix4x3dv_impl=None
def glUniformMatrix4x3dv (location, count, transpose, value):
    global glUniformMatrix4x3dv_impl
    if not glUniformMatrix4x3dv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix4x3dv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4x3dv is not available')
        glUniformMatrix4x3dv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix4x3dv = (lambda location,count,transpose,value:glUniformMatrix4x3dv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix4x3dv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformMatrix4x3fv</name></proto>
#            <param><ptype>GLint</ptype> <name>location</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
#            <param len="count*12">const <ptype>GLfloat</ptype> *<name>value</name></param>
#            <glx opcode="310" type="render" />
#        </command>
#        
glUniformMatrix4x3fv_impl=None
def glUniformMatrix4x3fv (location, count, transpose, value):
    global glUniformMatrix4x3fv_impl
    if not glUniformMatrix4x3fv_impl:
        fptr = pyglGetFuncAddress('glUniformMatrix4x3fv')
        if not fptr:
            raise RuntimeError('The function glUniformMatrix4x3fv is not available')
        glUniformMatrix4x3fv_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_char, c_void_p)(fptr)
    glUniformMatrix4x3fv = (lambda location,count,transpose,value:glUniformMatrix4x3fv_impl(location,count,transpose,pyglGetAsConstVoidPointer( value )))
    return glUniformMatrix4x3fv(location, count, transpose, value)
# <command>
#            <proto>void <name>glUniformSubroutinesuiv</name></proto>
#            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="count">const <ptype>GLuint</ptype> *<name>indices</name></param>
#        </command>
#        
glUniformSubroutinesuiv_impl=None
def glUniformSubroutinesuiv (shadertype, count, indices):
    global glUniformSubroutinesuiv_impl
    if not glUniformSubroutinesuiv_impl:
        fptr = pyglGetFuncAddress('glUniformSubroutinesuiv')
        if not fptr:
            raise RuntimeError('The function glUniformSubroutinesuiv is not available')
        glUniformSubroutinesuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glUniformSubroutinesuiv = (lambda shadertype,count,indices:glUniformSubroutinesuiv_impl(shadertype,count,pyglGetAsConstVoidPointer( indices )))
    return glUniformSubroutinesuiv(shadertype, count, indices)
# <command>
#            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glUnmapBuffer</name></proto>
#            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
#        </command>
#        
glUnmapBuffer_impl=None
def glUnmapBuffer (target):
    global glUnmapBuffer_impl
    if not glUnmapBuffer_impl:
        fptr = pyglGetFuncAddress('glUnmapBuffer')
        if not fptr:
            raise RuntimeError('The function glUnmapBuffer is not available')
        glUnmapBuffer_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glUnmapBuffer = glUnmapBuffer_impl
    return glUnmapBuffer(target)
# <command>
#            <proto><ptype>GLboolean</ptype> <name>glUnmapNamedBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glUnmapNamedBuffer_impl=None
def glUnmapNamedBuffer (buffer):
    global glUnmapNamedBuffer_impl
    if not glUnmapNamedBuffer_impl:
        fptr = pyglGetFuncAddress('glUnmapNamedBuffer')
        if not fptr:
            raise RuntimeError('The function glUnmapNamedBuffer is not available')
        glUnmapNamedBuffer_impl = PYGL_FUNC_TYPE( c_char ,c_uint)(fptr)
    glUnmapNamedBuffer = glUnmapNamedBuffer_impl
    return glUnmapNamedBuffer(buffer)
# <command>
#            <proto>void <name>glUseProgram</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#        </command>
#        
glUseProgram_impl=None
def glUseProgram (program):
    global glUseProgram_impl
    if not glUseProgram_impl:
        fptr = pyglGetFuncAddress('glUseProgram')
        if not fptr:
            raise RuntimeError('The function glUseProgram is not available')
        glUseProgram_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glUseProgram = glUseProgram_impl
    return glUseProgram(program)
# <command>
#            <proto>void <name>glUseProgramStages</name></proto>
#            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
#            <param><ptype>GLbitfield</ptype> <name>stages</name></param>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#        </command>
#        
glUseProgramStages_impl=None
def glUseProgramStages (pipeline, stages, program):
    global glUseProgramStages_impl
    if not glUseProgramStages_impl:
        fptr = pyglGetFuncAddress('glUseProgramStages')
        if not fptr:
            raise RuntimeError('The function glUseProgramStages is not available')
        glUseProgramStages_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glUseProgramStages = glUseProgramStages_impl
    return glUseProgramStages(pipeline, stages, program)
# <command>
#            <proto>void <name>glValidateProgram</name></proto>
#            <param><ptype>GLuint</ptype> <name>program</name></param>
#        </command>
#        
glValidateProgram_impl=None
def glValidateProgram (program):
    global glValidateProgram_impl
    if not glValidateProgram_impl:
        fptr = pyglGetFuncAddress('glValidateProgram')
        if not fptr:
            raise RuntimeError('The function glValidateProgram is not available')
        glValidateProgram_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glValidateProgram = glValidateProgram_impl
    return glValidateProgram(program)
# <command>
#            <proto>void <name>glValidateProgramPipeline</name></proto>
#            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
#        </command>
#        
glValidateProgramPipeline_impl=None
def glValidateProgramPipeline (pipeline):
    global glValidateProgramPipeline_impl
    if not glValidateProgramPipeline_impl:
        fptr = pyglGetFuncAddress('glValidateProgramPipeline')
        if not fptr:
            raise RuntimeError('The function glValidateProgramPipeline is not available')
        glValidateProgramPipeline_impl = PYGL_FUNC_TYPE( None ,c_uint)(fptr)
    glValidateProgramPipeline = glValidateProgramPipeline_impl
    return glValidateProgramPipeline(pipeline)
# <command>
#            <proto>void <name>glVertexArrayAttribBinding</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>attribindex</name></param>
#            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
#        </command>
#        
glVertexArrayAttribBinding_impl=None
def glVertexArrayAttribBinding (vaobj, attribindex, bindingindex):
    global glVertexArrayAttribBinding_impl
    if not glVertexArrayAttribBinding_impl:
        fptr = pyglGetFuncAddress('glVertexArrayAttribBinding')
        if not fptr:
            raise RuntimeError('The function glVertexArrayAttribBinding is not available')
        glVertexArrayAttribBinding_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glVertexArrayAttribBinding = glVertexArrayAttribBinding_impl
    return glVertexArrayAttribBinding(vaobj, attribindex, bindingindex)
# <command>
#            <proto>void <name>glVertexArrayAttribFormat</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>attribindex</name></param>
#            <param><ptype>GLint</ptype> <name>size</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param><ptype>GLuint</ptype> <name>relativeoffset</name></param>
#        </command>
#        
glVertexArrayAttribFormat_impl=None
def glVertexArrayAttribFormat (vaobj, attribindex, size, type, normalized, relativeoffset):
    global glVertexArrayAttribFormat_impl
    if not glVertexArrayAttribFormat_impl:
        fptr = pyglGetFuncAddress('glVertexArrayAttribFormat')
        if not fptr:
            raise RuntimeError('The function glVertexArrayAttribFormat is not available')
        glVertexArrayAttribFormat_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_uint, c_char, c_uint)(fptr)
    glVertexArrayAttribFormat = glVertexArrayAttribFormat_impl
    return glVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset)
# <command>
#            <proto>void <name>glVertexArrayBindingDivisor</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
#            <param><ptype>GLuint</ptype> <name>divisor</name></param>
#        </command>
#        
glVertexArrayBindingDivisor_impl=None
def glVertexArrayBindingDivisor (vaobj, bindingindex, divisor):
    global glVertexArrayBindingDivisor_impl
    if not glVertexArrayBindingDivisor_impl:
        fptr = pyglGetFuncAddress('glVertexArrayBindingDivisor')
        if not fptr:
            raise RuntimeError('The function glVertexArrayBindingDivisor is not available')
        glVertexArrayBindingDivisor_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glVertexArrayBindingDivisor = glVertexArrayBindingDivisor_impl
    return glVertexArrayBindingDivisor(vaobj, bindingindex, divisor)
# <command>
#            <proto>void <name>glVertexArrayElementBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#        </command>
#        
glVertexArrayElementBuffer_impl=None
def glVertexArrayElementBuffer (vaobj, buffer):
    global glVertexArrayElementBuffer_impl
    if not glVertexArrayElementBuffer_impl:
        fptr = pyglGetFuncAddress('glVertexArrayElementBuffer')
        if not fptr:
            raise RuntimeError('The function glVertexArrayElementBuffer is not available')
        glVertexArrayElementBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glVertexArrayElementBuffer = glVertexArrayElementBuffer_impl
    return glVertexArrayElementBuffer(vaobj, buffer)
# <command>
#            <proto>void <name>glVertexArrayVertexBuffer</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
#            <param><ptype>GLuint</ptype> <name>buffer</name></param>
#            <param><ptype>GLintptr</ptype> <name>offset</name></param>
#            <param><ptype>GLsizei</ptype> <name>stride</name></param>
#        </command>
#        
glVertexArrayVertexBuffer_impl=None
def glVertexArrayVertexBuffer (vaobj, bindingindex, buffer, offset, stride):
    global glVertexArrayVertexBuffer_impl
    if not glVertexArrayVertexBuffer_impl:
        fptr = pyglGetFuncAddress('glVertexArrayVertexBuffer')
        if not fptr:
            raise RuntimeError('The function glVertexArrayVertexBuffer is not available')
        glVertexArrayVertexBuffer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_size_t, c_int)(fptr)
    glVertexArrayVertexBuffer = glVertexArrayVertexBuffer_impl
    return glVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride)
# <command>
#            <proto>void <name>glVertexArrayVertexBuffers</name></proto>
#            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param>const <ptype>GLuint</ptype> *<name>buffers</name></param>
#            <param>const <ptype>GLintptr</ptype> *<name>offsets</name></param>
#            <param>const <ptype>GLsizei</ptype> *<name>strides</name></param>
#        </command>
#        
glVertexArrayVertexBuffers_impl=None
def glVertexArrayVertexBuffers (vaobj, first, count, buffers, offsets, strides):
    global glVertexArrayVertexBuffers_impl
    if not glVertexArrayVertexBuffers_impl:
        fptr = pyglGetFuncAddress('glVertexArrayVertexBuffers')
        if not fptr:
            raise RuntimeError('The function glVertexArrayVertexBuffers is not available')
        glVertexArrayVertexBuffers_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_int, c_void_p, c_void_p, c_void_p)(fptr)
    glVertexArrayVertexBuffers = (lambda vaobj,first,count,buffers,offsets,strides:glVertexArrayVertexBuffers_impl(vaobj,first,count,pyglGetAsConstVoidPointer( buffers ),pyglGetAsConstVoidPointer( offsets ),pyglGetAsConstVoidPointer( strides )))
    return glVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides)
# <command>
#            <proto>void <name>glVertexAttrib1d</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <vecequiv name="glVertexAttrib1dv" />
#        </command>
#        
glVertexAttrib1d_impl=None
def glVertexAttrib1d (index, x):
    global glVertexAttrib1d_impl
    if not glVertexAttrib1d_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib1d')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1d is not available')
        glVertexAttrib1d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double)(fptr)
    glVertexAttrib1d = glVertexAttrib1d_impl
    return glVertexAttrib1d(index, x)
# <command>
#            <proto>void <name>glVertexAttrib1dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="1">const <ptype>GLdouble</ptype> *<name>v</name></param>
#            <glx opcode="4197" type="render" />
#        </command>
#        
glVertexAttrib1dv_impl=None
def glVertexAttrib1dv (index, v):
    global glVertexAttrib1dv_impl
    if not glVertexAttrib1dv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib1dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1dv is not available')
        glVertexAttrib1dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib1dv = (lambda index,v:glVertexAttrib1dv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib1dv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib1f</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLfloat</ptype> <name>x</name></param>
#            <vecequiv name="glVertexAttrib1fv" />
#        </command>
#        
glVertexAttrib1f_impl=None
def glVertexAttrib1f (index, x):
    global glVertexAttrib1f_impl
    if not glVertexAttrib1f_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib1f')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1f is not available')
        glVertexAttrib1f_impl = PYGL_FUNC_TYPE( None ,c_uint, c_float)(fptr)
    glVertexAttrib1f = glVertexAttrib1f_impl
    return glVertexAttrib1f(index, x)
# <command>
#            <proto>void <name>glVertexAttrib1fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="1">const <ptype>GLfloat</ptype> *<name>v</name></param>
#            <glx opcode="4193" type="render" />
#        </command>
#        
glVertexAttrib1fv_impl=None
def glVertexAttrib1fv (index, v):
    global glVertexAttrib1fv_impl
    if not glVertexAttrib1fv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib1fv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1fv is not available')
        glVertexAttrib1fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib1fv = (lambda index,v:glVertexAttrib1fv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib1fv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib1s</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLshort</ptype> <name>x</name></param>
#            <vecequiv name="glVertexAttrib1sv" />
#        </command>
#        
glVertexAttrib1s_impl=None
def glVertexAttrib1s (index, x):
    global glVertexAttrib1s_impl
    if not glVertexAttrib1s_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib1s')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1s is not available')
        glVertexAttrib1s_impl = PYGL_FUNC_TYPE( None ,c_uint, c_short)(fptr)
    glVertexAttrib1s = glVertexAttrib1s_impl
    return glVertexAttrib1s(index, x)
# <command>
#            <proto>void <name>glVertexAttrib1sv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="1">const <ptype>GLshort</ptype> *<name>v</name></param>
#            <glx opcode="4189" type="render" />
#        </command>
#        
glVertexAttrib1sv_impl=None
def glVertexAttrib1sv (index, v):
    global glVertexAttrib1sv_impl
    if not glVertexAttrib1sv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib1sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib1sv is not available')
        glVertexAttrib1sv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib1sv = (lambda index,v:glVertexAttrib1sv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib1sv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib2d</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#            <vecequiv name="glVertexAttrib2dv" />
#        </command>
#        
glVertexAttrib2d_impl=None
def glVertexAttrib2d (index, x, y):
    global glVertexAttrib2d_impl
    if not glVertexAttrib2d_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib2d')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2d is not available')
        glVertexAttrib2d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double, c_double)(fptr)
    glVertexAttrib2d = glVertexAttrib2d_impl
    return glVertexAttrib2d(index, x, y)
# <command>
#            <proto>void <name>glVertexAttrib2dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="2">const <ptype>GLdouble</ptype> *<name>v</name></param>
#            <glx opcode="4198" type="render" />
#        </command>
#        
glVertexAttrib2dv_impl=None
def glVertexAttrib2dv (index, v):
    global glVertexAttrib2dv_impl
    if not glVertexAttrib2dv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib2dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2dv is not available')
        glVertexAttrib2dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib2dv = (lambda index,v:glVertexAttrib2dv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib2dv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib2f</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLfloat</ptype> <name>x</name></param>
#            <param><ptype>GLfloat</ptype> <name>y</name></param>
#            <vecequiv name="glVertexAttrib2fv" />
#        </command>
#        
glVertexAttrib2f_impl=None
def glVertexAttrib2f (index, x, y):
    global glVertexAttrib2f_impl
    if not glVertexAttrib2f_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib2f')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2f is not available')
        glVertexAttrib2f_impl = PYGL_FUNC_TYPE( None ,c_uint, c_float, c_float)(fptr)
    glVertexAttrib2f = glVertexAttrib2f_impl
    return glVertexAttrib2f(index, x, y)
# <command>
#            <proto>void <name>glVertexAttrib2fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="2">const <ptype>GLfloat</ptype> *<name>v</name></param>
#            <glx opcode="4194" type="render" />
#        </command>
#        
glVertexAttrib2fv_impl=None
def glVertexAttrib2fv (index, v):
    global glVertexAttrib2fv_impl
    if not glVertexAttrib2fv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib2fv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2fv is not available')
        glVertexAttrib2fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib2fv = (lambda index,v:glVertexAttrib2fv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib2fv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib2s</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLshort</ptype> <name>x</name></param>
#            <param><ptype>GLshort</ptype> <name>y</name></param>
#            <vecequiv name="glVertexAttrib2sv" />
#        </command>
#        
glVertexAttrib2s_impl=None
def glVertexAttrib2s (index, x, y):
    global glVertexAttrib2s_impl
    if not glVertexAttrib2s_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib2s')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2s is not available')
        glVertexAttrib2s_impl = PYGL_FUNC_TYPE( None ,c_uint, c_short, c_short)(fptr)
    glVertexAttrib2s = glVertexAttrib2s_impl
    return glVertexAttrib2s(index, x, y)
# <command>
#            <proto>void <name>glVertexAttrib2sv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="2">const <ptype>GLshort</ptype> *<name>v</name></param>
#            <glx opcode="4190" type="render" />
#        </command>
#        
glVertexAttrib2sv_impl=None
def glVertexAttrib2sv (index, v):
    global glVertexAttrib2sv_impl
    if not glVertexAttrib2sv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib2sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib2sv is not available')
        glVertexAttrib2sv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib2sv = (lambda index,v:glVertexAttrib2sv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib2sv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib3d</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#            <param><ptype>GLdouble</ptype> <name>z</name></param>
#            <vecequiv name="glVertexAttrib3dv" />
#        </command>
#        
glVertexAttrib3d_impl=None
def glVertexAttrib3d (index, x, y, z):
    global glVertexAttrib3d_impl
    if not glVertexAttrib3d_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib3d')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3d is not available')
        glVertexAttrib3d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double, c_double, c_double)(fptr)
    glVertexAttrib3d = glVertexAttrib3d_impl
    return glVertexAttrib3d(index, x, y, z)
# <command>
#            <proto>void <name>glVertexAttrib3dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="3">const <ptype>GLdouble</ptype> *<name>v</name></param>
#            <glx opcode="4199" type="render" />
#        </command>
#        
glVertexAttrib3dv_impl=None
def glVertexAttrib3dv (index, v):
    global glVertexAttrib3dv_impl
    if not glVertexAttrib3dv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib3dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3dv is not available')
        glVertexAttrib3dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib3dv = (lambda index,v:glVertexAttrib3dv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib3dv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib3f</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLfloat</ptype> <name>x</name></param>
#            <param><ptype>GLfloat</ptype> <name>y</name></param>
#            <param><ptype>GLfloat</ptype> <name>z</name></param>
#            <vecequiv name="glVertexAttrib3fv" />
#        </command>
#        
glVertexAttrib3f_impl=None
def glVertexAttrib3f (index, x, y, z):
    global glVertexAttrib3f_impl
    if not glVertexAttrib3f_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib3f')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3f is not available')
        glVertexAttrib3f_impl = PYGL_FUNC_TYPE( None ,c_uint, c_float, c_float, c_float)(fptr)
    glVertexAttrib3f = glVertexAttrib3f_impl
    return glVertexAttrib3f(index, x, y, z)
# <command>
#            <proto>void <name>glVertexAttrib3fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="3">const <ptype>GLfloat</ptype> *<name>v</name></param>
#            <glx opcode="4195" type="render" />
#        </command>
#        
glVertexAttrib3fv_impl=None
def glVertexAttrib3fv (index, v):
    global glVertexAttrib3fv_impl
    if not glVertexAttrib3fv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib3fv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3fv is not available')
        glVertexAttrib3fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib3fv = (lambda index,v:glVertexAttrib3fv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib3fv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib3s</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLshort</ptype> <name>x</name></param>
#            <param><ptype>GLshort</ptype> <name>y</name></param>
#            <param><ptype>GLshort</ptype> <name>z</name></param>
#            <vecequiv name="glVertexAttrib3sv" />
#        </command>
#        
glVertexAttrib3s_impl=None
def glVertexAttrib3s (index, x, y, z):
    global glVertexAttrib3s_impl
    if not glVertexAttrib3s_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib3s')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3s is not available')
        glVertexAttrib3s_impl = PYGL_FUNC_TYPE( None ,c_uint, c_short, c_short, c_short)(fptr)
    glVertexAttrib3s = glVertexAttrib3s_impl
    return glVertexAttrib3s(index, x, y, z)
# <command>
#            <proto>void <name>glVertexAttrib3sv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="3">const <ptype>GLshort</ptype> *<name>v</name></param>
#            <glx opcode="4191" type="render" />
#        </command>
#        
glVertexAttrib3sv_impl=None
def glVertexAttrib3sv (index, v):
    global glVertexAttrib3sv_impl
    if not glVertexAttrib3sv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib3sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib3sv is not available')
        glVertexAttrib3sv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib3sv = (lambda index,v:glVertexAttrib3sv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib3sv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4Nbv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLbyte</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4Nbv_impl=None
def glVertexAttrib4Nbv (index, v):
    global glVertexAttrib4Nbv_impl
    if not glVertexAttrib4Nbv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4Nbv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nbv is not available')
        glVertexAttrib4Nbv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4Nbv = (lambda index,v:glVertexAttrib4Nbv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4Nbv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4Niv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4Niv_impl=None
def glVertexAttrib4Niv (index, v):
    global glVertexAttrib4Niv_impl
    if not glVertexAttrib4Niv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4Niv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Niv is not available')
        glVertexAttrib4Niv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4Niv = (lambda index,v:glVertexAttrib4Niv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4Niv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4Nsv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLshort</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4Nsv_impl=None
def glVertexAttrib4Nsv (index, v):
    global glVertexAttrib4Nsv_impl
    if not glVertexAttrib4Nsv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4Nsv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nsv is not available')
        glVertexAttrib4Nsv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4Nsv = (lambda index,v:glVertexAttrib4Nsv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4Nsv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4Nub</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLubyte</ptype> <name>x</name></param>
#            <param><ptype>GLubyte</ptype> <name>y</name></param>
#            <param><ptype>GLubyte</ptype> <name>z</name></param>
#            <param><ptype>GLubyte</ptype> <name>w</name></param>
#        </command>
#        
glVertexAttrib4Nub_impl=None
def glVertexAttrib4Nub (index, x, y, z, w):
    global glVertexAttrib4Nub_impl
    if not glVertexAttrib4Nub_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4Nub')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nub is not available')
        glVertexAttrib4Nub_impl = PYGL_FUNC_TYPE( None ,c_uint, c_ubyte, c_ubyte, c_ubyte, c_ubyte)(fptr)
    glVertexAttrib4Nub = glVertexAttrib4Nub_impl
    return glVertexAttrib4Nub(index, x, y, z, w)
# <command>
#            <proto>void <name>glVertexAttrib4Nubv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLubyte</ptype> *<name>v</name></param>
#            <glx opcode="4201" type="render" />
#        </command>
#        
glVertexAttrib4Nubv_impl=None
def glVertexAttrib4Nubv (index, v):
    global glVertexAttrib4Nubv_impl
    if not glVertexAttrib4Nubv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4Nubv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nubv is not available')
        glVertexAttrib4Nubv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_char_p)(fptr)
    glVertexAttrib4Nubv = (lambda index,v:glVertexAttrib4Nubv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4Nubv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4Nuiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLuint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4Nuiv_impl=None
def glVertexAttrib4Nuiv (index, v):
    global glVertexAttrib4Nuiv_impl
    if not glVertexAttrib4Nuiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4Nuiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nuiv is not available')
        glVertexAttrib4Nuiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4Nuiv = (lambda index,v:glVertexAttrib4Nuiv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4Nuiv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4Nusv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLushort</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4Nusv_impl=None
def glVertexAttrib4Nusv (index, v):
    global glVertexAttrib4Nusv_impl
    if not glVertexAttrib4Nusv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4Nusv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4Nusv is not available')
        glVertexAttrib4Nusv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4Nusv = (lambda index,v:glVertexAttrib4Nusv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4Nusv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4bv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLbyte</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4bv_impl=None
def glVertexAttrib4bv (index, v):
    global glVertexAttrib4bv_impl
    if not glVertexAttrib4bv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4bv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4bv is not available')
        glVertexAttrib4bv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4bv = (lambda index,v:glVertexAttrib4bv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4bv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4d</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#            <param><ptype>GLdouble</ptype> <name>z</name></param>
#            <param><ptype>GLdouble</ptype> <name>w</name></param>
#            <vecequiv name="glVertexAttrib4dv" />
#        </command>
#        
glVertexAttrib4d_impl=None
def glVertexAttrib4d (index, x, y, z, w):
    global glVertexAttrib4d_impl
    if not glVertexAttrib4d_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4d')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4d is not available')
        glVertexAttrib4d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double, c_double, c_double, c_double)(fptr)
    glVertexAttrib4d = glVertexAttrib4d_impl
    return glVertexAttrib4d(index, x, y, z, w)
# <command>
#            <proto>void <name>glVertexAttrib4dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLdouble</ptype> *<name>v</name></param>
#            <glx opcode="4200" type="render" />
#        </command>
#        
glVertexAttrib4dv_impl=None
def glVertexAttrib4dv (index, v):
    global glVertexAttrib4dv_impl
    if not glVertexAttrib4dv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4dv is not available')
        glVertexAttrib4dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4dv = (lambda index,v:glVertexAttrib4dv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4dv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4f</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLfloat</ptype> <name>x</name></param>
#            <param><ptype>GLfloat</ptype> <name>y</name></param>
#            <param><ptype>GLfloat</ptype> <name>z</name></param>
#            <param><ptype>GLfloat</ptype> <name>w</name></param>
#            <vecequiv name="glVertexAttrib4fv" />
#        </command>
#        
glVertexAttrib4f_impl=None
def glVertexAttrib4f (index, x, y, z, w):
    global glVertexAttrib4f_impl
    if not glVertexAttrib4f_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4f')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4f is not available')
        glVertexAttrib4f_impl = PYGL_FUNC_TYPE( None ,c_uint, c_float, c_float, c_float, c_float)(fptr)
    glVertexAttrib4f = glVertexAttrib4f_impl
    return glVertexAttrib4f(index, x, y, z, w)
# <command>
#            <proto>void <name>glVertexAttrib4fv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLfloat</ptype> *<name>v</name></param>
#            <glx opcode="4196" type="render" />
#        </command>
#        
glVertexAttrib4fv_impl=None
def glVertexAttrib4fv (index, v):
    global glVertexAttrib4fv_impl
    if not glVertexAttrib4fv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4fv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4fv is not available')
        glVertexAttrib4fv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4fv = (lambda index,v:glVertexAttrib4fv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4fv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4iv_impl=None
def glVertexAttrib4iv (index, v):
    global glVertexAttrib4iv_impl
    if not glVertexAttrib4iv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4iv is not available')
        glVertexAttrib4iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4iv = (lambda index,v:glVertexAttrib4iv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4iv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4s</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLshort</ptype> <name>x</name></param>
#            <param><ptype>GLshort</ptype> <name>y</name></param>
#            <param><ptype>GLshort</ptype> <name>z</name></param>
#            <param><ptype>GLshort</ptype> <name>w</name></param>
#            <vecequiv name="glVertexAttrib4sv" />
#        </command>
#        
glVertexAttrib4s_impl=None
def glVertexAttrib4s (index, x, y, z, w):
    global glVertexAttrib4s_impl
    if not glVertexAttrib4s_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4s')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4s is not available')
        glVertexAttrib4s_impl = PYGL_FUNC_TYPE( None ,c_uint, c_short, c_short, c_short, c_short)(fptr)
    glVertexAttrib4s = glVertexAttrib4s_impl
    return glVertexAttrib4s(index, x, y, z, w)
# <command>
#            <proto>void <name>glVertexAttrib4sv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLshort</ptype> *<name>v</name></param>
#            <glx opcode="4192" type="render" />
#        </command>
#        
glVertexAttrib4sv_impl=None
def glVertexAttrib4sv (index, v):
    global glVertexAttrib4sv_impl
    if not glVertexAttrib4sv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4sv is not available')
        glVertexAttrib4sv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4sv = (lambda index,v:glVertexAttrib4sv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4sv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4ubv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLubyte</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4ubv_impl=None
def glVertexAttrib4ubv (index, v):
    global glVertexAttrib4ubv_impl
    if not glVertexAttrib4ubv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4ubv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4ubv is not available')
        glVertexAttrib4ubv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_char_p)(fptr)
    glVertexAttrib4ubv = (lambda index,v:glVertexAttrib4ubv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4ubv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLuint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4uiv_impl=None
def glVertexAttrib4uiv (index, v):
    global glVertexAttrib4uiv_impl
    if not glVertexAttrib4uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4uiv is not available')
        glVertexAttrib4uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4uiv = (lambda index,v:glVertexAttrib4uiv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4uiv(index, v)
# <command>
#            <proto>void <name>glVertexAttrib4usv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLushort</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttrib4usv_impl=None
def glVertexAttrib4usv (index, v):
    global glVertexAttrib4usv_impl
    if not glVertexAttrib4usv_impl:
        fptr = pyglGetFuncAddress('glVertexAttrib4usv')
        if not fptr:
            raise RuntimeError('The function glVertexAttrib4usv is not available')
        glVertexAttrib4usv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttrib4usv = (lambda index,v:glVertexAttrib4usv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttrib4usv(index, v)
# <command>
#            <proto>void <name>glVertexAttribBinding</name></proto>
#            <param><ptype>GLuint</ptype> <name>attribindex</name></param>
#            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
#        </command>
#        
glVertexAttribBinding_impl=None
def glVertexAttribBinding (attribindex, bindingindex):
    global glVertexAttribBinding_impl
    if not glVertexAttribBinding_impl:
        fptr = pyglGetFuncAddress('glVertexAttribBinding')
        if not fptr:
            raise RuntimeError('The function glVertexAttribBinding is not available')
        glVertexAttribBinding_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glVertexAttribBinding = glVertexAttribBinding_impl
    return glVertexAttribBinding(attribindex, bindingindex)
# <command>
#            <proto>void <name>glVertexAttribDivisor</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>divisor</name></param>
#        </command>
#        
glVertexAttribDivisor_impl=None
def glVertexAttribDivisor (index, divisor):
    global glVertexAttribDivisor_impl
    if not glVertexAttribDivisor_impl:
        fptr = pyglGetFuncAddress('glVertexAttribDivisor')
        if not fptr:
            raise RuntimeError('The function glVertexAttribDivisor is not available')
        glVertexAttribDivisor_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glVertexAttribDivisor = glVertexAttribDivisor_impl
    return glVertexAttribDivisor(index, divisor)
# <command>
#            <proto>void <name>glVertexAttribFormat</name></proto>
#            <param><ptype>GLuint</ptype> <name>attribindex</name></param>
#            <param><ptype>GLint</ptype> <name>size</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param><ptype>GLuint</ptype> <name>relativeoffset</name></param>
#        </command>
#        
glVertexAttribFormat_impl=None
def glVertexAttribFormat (attribindex, size, type, normalized, relativeoffset):
    global glVertexAttribFormat_impl
    if not glVertexAttribFormat_impl:
        fptr = pyglGetFuncAddress('glVertexAttribFormat')
        if not fptr:
            raise RuntimeError('The function glVertexAttribFormat is not available')
        glVertexAttribFormat_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_char, c_uint)(fptr)
    glVertexAttribFormat = glVertexAttribFormat_impl
    return glVertexAttribFormat(attribindex, size, type, normalized, relativeoffset)
# <command>
#            <proto>void <name>glVertexAttribI1i</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <vecequiv name="glVertexAttribI1iv" />
#        </command>
#        
glVertexAttribI1i_impl=None
def glVertexAttribI1i (index, x):
    global glVertexAttribI1i_impl
    if not glVertexAttribI1i_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI1i')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI1i is not available')
        glVertexAttribI1i_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int)(fptr)
    glVertexAttribI1i = glVertexAttribI1i_impl
    return glVertexAttribI1i(index, x)
# <command>
#            <proto>void <name>glVertexAttribI1iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="1">const <ptype>GLint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI1iv_impl=None
def glVertexAttribI1iv (index, v):
    global glVertexAttribI1iv_impl
    if not glVertexAttribI1iv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI1iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI1iv is not available')
        glVertexAttribI1iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI1iv = (lambda index,v:glVertexAttribI1iv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI1iv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI1ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>x</name></param>
#            <vecequiv name="glVertexAttribI1uiv" />
#        </command>
#        
glVertexAttribI1ui_impl=None
def glVertexAttribI1ui (index, x):
    global glVertexAttribI1ui_impl
    if not glVertexAttribI1ui_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI1ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI1ui is not available')
        glVertexAttribI1ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glVertexAttribI1ui = glVertexAttribI1ui_impl
    return glVertexAttribI1ui(index, x)
# <command>
#            <proto>void <name>glVertexAttribI1uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="1">const <ptype>GLuint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI1uiv_impl=None
def glVertexAttribI1uiv (index, v):
    global glVertexAttribI1uiv_impl
    if not glVertexAttribI1uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI1uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI1uiv is not available')
        glVertexAttribI1uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI1uiv = (lambda index,v:glVertexAttribI1uiv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI1uiv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI2i</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <vecequiv name="glVertexAttribI2iv" />
#        </command>
#        
glVertexAttribI2i_impl=None
def glVertexAttribI2i (index, x, y):
    global glVertexAttribI2i_impl
    if not glVertexAttribI2i_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI2i')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI2i is not available')
        glVertexAttribI2i_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int)(fptr)
    glVertexAttribI2i = glVertexAttribI2i_impl
    return glVertexAttribI2i(index, x, y)
# <command>
#            <proto>void <name>glVertexAttribI2iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="2">const <ptype>GLint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI2iv_impl=None
def glVertexAttribI2iv (index, v):
    global glVertexAttribI2iv_impl
    if not glVertexAttribI2iv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI2iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI2iv is not available')
        glVertexAttribI2iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI2iv = (lambda index,v:glVertexAttribI2iv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI2iv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI2ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>x</name></param>
#            <param><ptype>GLuint</ptype> <name>y</name></param>
#            <vecequiv name="glVertexAttribI2uiv" />
#        </command>
#        
glVertexAttribI2ui_impl=None
def glVertexAttribI2ui (index, x, y):
    global glVertexAttribI2ui_impl
    if not glVertexAttribI2ui_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI2ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI2ui is not available')
        glVertexAttribI2ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint)(fptr)
    glVertexAttribI2ui = glVertexAttribI2ui_impl
    return glVertexAttribI2ui(index, x, y)
# <command>
#            <proto>void <name>glVertexAttribI2uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="2">const <ptype>GLuint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI2uiv_impl=None
def glVertexAttribI2uiv (index, v):
    global glVertexAttribI2uiv_impl
    if not glVertexAttribI2uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI2uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI2uiv is not available')
        glVertexAttribI2uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI2uiv = (lambda index,v:glVertexAttribI2uiv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI2uiv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI3i</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLint</ptype> <name>z</name></param>
#            <vecequiv name="glVertexAttribI3iv" />
#        </command>
#        
glVertexAttribI3i_impl=None
def glVertexAttribI3i (index, x, y, z):
    global glVertexAttribI3i_impl
    if not glVertexAttribI3i_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI3i')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI3i is not available')
        glVertexAttribI3i_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int)(fptr)
    glVertexAttribI3i = glVertexAttribI3i_impl
    return glVertexAttribI3i(index, x, y, z)
# <command>
#            <proto>void <name>glVertexAttribI3iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="3">const <ptype>GLint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI3iv_impl=None
def glVertexAttribI3iv (index, v):
    global glVertexAttribI3iv_impl
    if not glVertexAttribI3iv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI3iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI3iv is not available')
        glVertexAttribI3iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI3iv = (lambda index,v:glVertexAttribI3iv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI3iv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI3ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>x</name></param>
#            <param><ptype>GLuint</ptype> <name>y</name></param>
#            <param><ptype>GLuint</ptype> <name>z</name></param>
#            <vecequiv name="glVertexAttribI3uiv" />
#        </command>
#        
glVertexAttribI3ui_impl=None
def glVertexAttribI3ui (index, x, y, z):
    global glVertexAttribI3ui_impl
    if not glVertexAttribI3ui_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI3ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI3ui is not available')
        glVertexAttribI3ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint)(fptr)
    glVertexAttribI3ui = glVertexAttribI3ui_impl
    return glVertexAttribI3ui(index, x, y, z)
# <command>
#            <proto>void <name>glVertexAttribI3uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="3">const <ptype>GLuint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI3uiv_impl=None
def glVertexAttribI3uiv (index, v):
    global glVertexAttribI3uiv_impl
    if not glVertexAttribI3uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI3uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI3uiv is not available')
        glVertexAttribI3uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI3uiv = (lambda index,v:glVertexAttribI3uiv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI3uiv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI4bv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLbyte</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI4bv_impl=None
def glVertexAttribI4bv (index, v):
    global glVertexAttribI4bv_impl
    if not glVertexAttribI4bv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI4bv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4bv is not available')
        glVertexAttribI4bv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI4bv = (lambda index,v:glVertexAttribI4bv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI4bv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI4i</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLint</ptype> <name>x</name></param>
#            <param><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLint</ptype> <name>z</name></param>
#            <param><ptype>GLint</ptype> <name>w</name></param>
#            <vecequiv name="glVertexAttribI4iv" />
#        </command>
#        
glVertexAttribI4i_impl=None
def glVertexAttribI4i (index, x, y, z, w):
    global glVertexAttribI4i_impl
    if not glVertexAttribI4i_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI4i')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4i is not available')
        glVertexAttribI4i_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_int, c_int, c_int)(fptr)
    glVertexAttribI4i = glVertexAttribI4i_impl
    return glVertexAttribI4i(index, x, y, z, w)
# <command>
#            <proto>void <name>glVertexAttribI4iv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI4iv_impl=None
def glVertexAttribI4iv (index, v):
    global glVertexAttribI4iv_impl
    if not glVertexAttribI4iv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI4iv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4iv is not available')
        glVertexAttribI4iv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI4iv = (lambda index,v:glVertexAttribI4iv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI4iv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI4sv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLshort</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI4sv_impl=None
def glVertexAttribI4sv (index, v):
    global glVertexAttribI4sv_impl
    if not glVertexAttribI4sv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI4sv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4sv is not available')
        glVertexAttribI4sv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI4sv = (lambda index,v:glVertexAttribI4sv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI4sv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI4ubv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLubyte</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI4ubv_impl=None
def glVertexAttribI4ubv (index, v):
    global glVertexAttribI4ubv_impl
    if not glVertexAttribI4ubv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI4ubv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4ubv is not available')
        glVertexAttribI4ubv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_char_p)(fptr)
    glVertexAttribI4ubv = (lambda index,v:glVertexAttribI4ubv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI4ubv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI4ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLuint</ptype> <name>x</name></param>
#            <param><ptype>GLuint</ptype> <name>y</name></param>
#            <param><ptype>GLuint</ptype> <name>z</name></param>
#            <param><ptype>GLuint</ptype> <name>w</name></param>
#            <vecequiv name="glVertexAttribI4uiv" />
#        </command>
#        
glVertexAttribI4ui_impl=None
def glVertexAttribI4ui (index, x, y, z, w):
    global glVertexAttribI4ui_impl
    if not glVertexAttribI4ui_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI4ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4ui is not available')
        glVertexAttribI4ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_uint, c_uint, c_uint)(fptr)
    glVertexAttribI4ui = glVertexAttribI4ui_impl
    return glVertexAttribI4ui(index, x, y, z, w)
# <command>
#            <proto>void <name>glVertexAttribI4uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLuint</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI4uiv_impl=None
def glVertexAttribI4uiv (index, v):
    global glVertexAttribI4uiv_impl
    if not glVertexAttribI4uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI4uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4uiv is not available')
        glVertexAttribI4uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI4uiv = (lambda index,v:glVertexAttribI4uiv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI4uiv(index, v)
# <command>
#            <proto>void <name>glVertexAttribI4usv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLushort</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribI4usv_impl=None
def glVertexAttribI4usv (index, v):
    global glVertexAttribI4usv_impl
    if not glVertexAttribI4usv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribI4usv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribI4usv is not available')
        glVertexAttribI4usv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribI4usv = (lambda index,v:glVertexAttribI4usv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribI4usv(index, v)
# <command>
#            <proto>void <name>glVertexAttribL1d</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#        </command>
#        
glVertexAttribL1d_impl=None
def glVertexAttribL1d (index, x):
    global glVertexAttribL1d_impl
    if not glVertexAttribL1d_impl:
        fptr = pyglGetFuncAddress('glVertexAttribL1d')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL1d is not available')
        glVertexAttribL1d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double)(fptr)
    glVertexAttribL1d = glVertexAttribL1d_impl
    return glVertexAttribL1d(index, x)
# <command>
#            <proto>void <name>glVertexAttribL1dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="1">const <ptype>GLdouble</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribL1dv_impl=None
def glVertexAttribL1dv (index, v):
    global glVertexAttribL1dv_impl
    if not glVertexAttribL1dv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribL1dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL1dv is not available')
        glVertexAttribL1dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribL1dv = (lambda index,v:glVertexAttribL1dv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribL1dv(index, v)
# <command>
#            <proto>void <name>glVertexAttribL2d</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#        </command>
#        
glVertexAttribL2d_impl=None
def glVertexAttribL2d (index, x, y):
    global glVertexAttribL2d_impl
    if not glVertexAttribL2d_impl:
        fptr = pyglGetFuncAddress('glVertexAttribL2d')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL2d is not available')
        glVertexAttribL2d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double, c_double)(fptr)
    glVertexAttribL2d = glVertexAttribL2d_impl
    return glVertexAttribL2d(index, x, y)
# <command>
#            <proto>void <name>glVertexAttribL2dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="2">const <ptype>GLdouble</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribL2dv_impl=None
def glVertexAttribL2dv (index, v):
    global glVertexAttribL2dv_impl
    if not glVertexAttribL2dv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribL2dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL2dv is not available')
        glVertexAttribL2dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribL2dv = (lambda index,v:glVertexAttribL2dv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribL2dv(index, v)
# <command>
#            <proto>void <name>glVertexAttribL3d</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#            <param><ptype>GLdouble</ptype> <name>z</name></param>
#        </command>
#        
glVertexAttribL3d_impl=None
def glVertexAttribL3d (index, x, y, z):
    global glVertexAttribL3d_impl
    if not glVertexAttribL3d_impl:
        fptr = pyglGetFuncAddress('glVertexAttribL3d')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL3d is not available')
        glVertexAttribL3d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double, c_double, c_double)(fptr)
    glVertexAttribL3d = glVertexAttribL3d_impl
    return glVertexAttribL3d(index, x, y, z)
# <command>
#            <proto>void <name>glVertexAttribL3dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="3">const <ptype>GLdouble</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribL3dv_impl=None
def glVertexAttribL3dv (index, v):
    global glVertexAttribL3dv_impl
    if not glVertexAttribL3dv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribL3dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL3dv is not available')
        glVertexAttribL3dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribL3dv = (lambda index,v:glVertexAttribL3dv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribL3dv(index, v)
# <command>
#            <proto>void <name>glVertexAttribL4d</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLdouble</ptype> <name>x</name></param>
#            <param><ptype>GLdouble</ptype> <name>y</name></param>
#            <param><ptype>GLdouble</ptype> <name>z</name></param>
#            <param><ptype>GLdouble</ptype> <name>w</name></param>
#        </command>
#        
glVertexAttribL4d_impl=None
def glVertexAttribL4d (index, x, y, z, w):
    global glVertexAttribL4d_impl
    if not glVertexAttribL4d_impl:
        fptr = pyglGetFuncAddress('glVertexAttribL4d')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL4d is not available')
        glVertexAttribL4d_impl = PYGL_FUNC_TYPE( None ,c_uint, c_double, c_double, c_double, c_double)(fptr)
    glVertexAttribL4d = glVertexAttribL4d_impl
    return glVertexAttribL4d(index, x, y, z, w)
# <command>
#            <proto>void <name>glVertexAttribL4dv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLdouble</ptype> *<name>v</name></param>
#        </command>
#        
glVertexAttribL4dv_impl=None
def glVertexAttribL4dv (index, v):
    global glVertexAttribL4dv_impl
    if not glVertexAttribL4dv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribL4dv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribL4dv is not available')
        glVertexAttribL4dv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glVertexAttribL4dv = (lambda index,v:glVertexAttribL4dv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glVertexAttribL4dv(index, v)
# <command>
#            <proto>void <name>glVertexAttribP1ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param><ptype>GLuint</ptype> <name>value</name></param>
#        </command>
#        
glVertexAttribP1ui_impl=None
def glVertexAttribP1ui (index, type, normalized, value):
    global glVertexAttribP1ui_impl
    if not glVertexAttribP1ui_impl:
        fptr = pyglGetFuncAddress('glVertexAttribP1ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP1ui is not available')
        glVertexAttribP1ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_char, c_uint)(fptr)
    glVertexAttribP1ui = glVertexAttribP1ui_impl
    return glVertexAttribP1ui(index, type, normalized, value)
# <command>
#            <proto>void <name>glVertexAttribP1uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glVertexAttribP1uiv_impl=None
def glVertexAttribP1uiv (index, type, normalized, value):
    global glVertexAttribP1uiv_impl
    if not glVertexAttribP1uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribP1uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP1uiv is not available')
        glVertexAttribP1uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_char, c_void_p)(fptr)
    glVertexAttribP1uiv = (lambda index,type,normalized,value:glVertexAttribP1uiv_impl(index,type,normalized,pyglGetAsConstVoidPointer( value )))
    return glVertexAttribP1uiv(index, type, normalized, value)
# <command>
#            <proto>void <name>glVertexAttribP2ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param><ptype>GLuint</ptype> <name>value</name></param>
#        </command>
#        
glVertexAttribP2ui_impl=None
def glVertexAttribP2ui (index, type, normalized, value):
    global glVertexAttribP2ui_impl
    if not glVertexAttribP2ui_impl:
        fptr = pyglGetFuncAddress('glVertexAttribP2ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP2ui is not available')
        glVertexAttribP2ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_char, c_uint)(fptr)
    glVertexAttribP2ui = glVertexAttribP2ui_impl
    return glVertexAttribP2ui(index, type, normalized, value)
# <command>
#            <proto>void <name>glVertexAttribP2uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glVertexAttribP2uiv_impl=None
def glVertexAttribP2uiv (index, type, normalized, value):
    global glVertexAttribP2uiv_impl
    if not glVertexAttribP2uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribP2uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP2uiv is not available')
        glVertexAttribP2uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_char, c_void_p)(fptr)
    glVertexAttribP2uiv = (lambda index,type,normalized,value:glVertexAttribP2uiv_impl(index,type,normalized,pyglGetAsConstVoidPointer( value )))
    return glVertexAttribP2uiv(index, type, normalized, value)
# <command>
#            <proto>void <name>glVertexAttribP3ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param><ptype>GLuint</ptype> <name>value</name></param>
#        </command>
#        
glVertexAttribP3ui_impl=None
def glVertexAttribP3ui (index, type, normalized, value):
    global glVertexAttribP3ui_impl
    if not glVertexAttribP3ui_impl:
        fptr = pyglGetFuncAddress('glVertexAttribP3ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP3ui is not available')
        glVertexAttribP3ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_char, c_uint)(fptr)
    glVertexAttribP3ui = glVertexAttribP3ui_impl
    return glVertexAttribP3ui(index, type, normalized, value)
# <command>
#            <proto>void <name>glVertexAttribP3uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glVertexAttribP3uiv_impl=None
def glVertexAttribP3uiv (index, type, normalized, value):
    global glVertexAttribP3uiv_impl
    if not glVertexAttribP3uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribP3uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP3uiv is not available')
        glVertexAttribP3uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_char, c_void_p)(fptr)
    glVertexAttribP3uiv = (lambda index,type,normalized,value:glVertexAttribP3uiv_impl(index,type,normalized,pyglGetAsConstVoidPointer( value )))
    return glVertexAttribP3uiv(index, type, normalized, value)
# <command>
#            <proto>void <name>glVertexAttribP4ui</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param><ptype>GLuint</ptype> <name>value</name></param>
#        </command>
#        
glVertexAttribP4ui_impl=None
def glVertexAttribP4ui (index, type, normalized, value):
    global glVertexAttribP4ui_impl
    if not glVertexAttribP4ui_impl:
        fptr = pyglGetFuncAddress('glVertexAttribP4ui')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP4ui is not available')
        glVertexAttribP4ui_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_char, c_uint)(fptr)
    glVertexAttribP4ui = glVertexAttribP4ui_impl
    return glVertexAttribP4ui(index, type, normalized, value)
# <command>
#            <proto>void <name>glVertexAttribP4uiv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
#        </command>
#        
glVertexAttribP4uiv_impl=None
def glVertexAttribP4uiv (index, type, normalized, value):
    global glVertexAttribP4uiv_impl
    if not glVertexAttribP4uiv_impl:
        fptr = pyglGetFuncAddress('glVertexAttribP4uiv')
        if not fptr:
            raise RuntimeError('The function glVertexAttribP4uiv is not available')
        glVertexAttribP4uiv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint, c_char, c_void_p)(fptr)
    glVertexAttribP4uiv = (lambda index,type,normalized,value:glVertexAttribP4uiv_impl(index,type,normalized,pyglGetAsConstVoidPointer( value )))
    return glVertexAttribP4uiv(index, type, normalized, value)
# <command>
#            <proto>void <name>glVertexAttribPointer</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLint</ptype> <name>size</name></param>
#            <param group="VertexAttribPointerType"><ptype>GLenum</ptype> <name>type</name></param>
#            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
#            <param><ptype>GLsizei</ptype> <name>stride</name></param>
#            <param len="COMPSIZE(size,type,stride)">const void *<name>pointer</name></param>
#        </command>
#        
glVertexAttribPointer_impl=None
def glVertexAttribPointer (index, size, type, normalized, stride, pointer):
    global glVertexAttribPointer_impl
    if not glVertexAttribPointer_impl:
        fptr = pyglGetFuncAddress('glVertexAttribPointer')
        if not fptr:
            raise RuntimeError('The function glVertexAttribPointer is not available')
        glVertexAttribPointer_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_uint, c_char, c_int, c_void_p)(fptr)
    glVertexAttribPointer = glVertexAttribPointer_impl
    return glVertexAttribPointer(index, size, type, normalized, stride, pointer)
# <command>
#            <proto>void <name>glVertexBindingDivisor</name></proto>
#            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
#            <param><ptype>GLuint</ptype> <name>divisor</name></param>
#        </command>
#        
glVertexBindingDivisor_impl=None
def glVertexBindingDivisor (bindingindex, divisor):
    global glVertexBindingDivisor_impl
    if not glVertexBindingDivisor_impl:
        fptr = pyglGetFuncAddress('glVertexBindingDivisor')
        if not fptr:
            raise RuntimeError('The function glVertexBindingDivisor is not available')
        glVertexBindingDivisor_impl = PYGL_FUNC_TYPE( None ,c_uint, c_uint)(fptr)
    glVertexBindingDivisor = glVertexBindingDivisor_impl
    return glVertexBindingDivisor(bindingindex, divisor)
# <command>
#            <proto>void <name>glViewport</name></proto>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
#            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
#            <param><ptype>GLsizei</ptype> <name>width</name></param>
#            <param><ptype>GLsizei</ptype> <name>height</name></param>
#            <glx opcode="191" type="render" />
#        </command>
#        
glViewport_impl=None
def glViewport (x, y, width, height):
    global glViewport_impl
    if not glViewport_impl:
        fptr = pyglGetFuncAddress('glViewport')
        if not fptr:
            raise RuntimeError('The function glViewport is not available')
        glViewport_impl = PYGL_FUNC_TYPE( None ,c_int, c_int, c_int, c_int)(fptr)
    glViewport = glViewport_impl
    return glViewport(x, y, width, height)
# <command>
#            <proto>void <name>glViewportArrayv</name></proto>
#            <param><ptype>GLuint</ptype> <name>first</name></param>
#            <param><ptype>GLsizei</ptype> <name>count</name></param>
#            <param len="COMPSIZE(count)">const <ptype>GLfloat</ptype> *<name>v</name></param>
#        </command>
#        
glViewportArrayv_impl=None
def glViewportArrayv (first, count, v):
    global glViewportArrayv_impl
    if not glViewportArrayv_impl:
        fptr = pyglGetFuncAddress('glViewportArrayv')
        if not fptr:
            raise RuntimeError('The function glViewportArrayv is not available')
        glViewportArrayv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_int, c_void_p)(fptr)
    glViewportArrayv = (lambda first,count,v:glViewportArrayv_impl(first,count,pyglGetAsConstVoidPointer( v )))
    return glViewportArrayv(first, count, v)
# <command>
#            <proto>void <name>glViewportIndexedf</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param><ptype>GLfloat</ptype> <name>x</name></param>
#            <param><ptype>GLfloat</ptype> <name>y</name></param>
#            <param><ptype>GLfloat</ptype> <name>w</name></param>
#            <param><ptype>GLfloat</ptype> <name>h</name></param>
#        </command>
#        
glViewportIndexedf_impl=None
def glViewportIndexedf (index, x, y, w, h):
    global glViewportIndexedf_impl
    if not glViewportIndexedf_impl:
        fptr = pyglGetFuncAddress('glViewportIndexedf')
        if not fptr:
            raise RuntimeError('The function glViewportIndexedf is not available')
        glViewportIndexedf_impl = PYGL_FUNC_TYPE( None ,c_uint, c_float, c_float, c_float, c_float)(fptr)
    glViewportIndexedf = glViewportIndexedf_impl
    return glViewportIndexedf(index, x, y, w, h)
# <command>
#            <proto>void <name>glViewportIndexedfv</name></proto>
#            <param><ptype>GLuint</ptype> <name>index</name></param>
#            <param len="4">const <ptype>GLfloat</ptype> *<name>v</name></param>
#        </command>
#        
glViewportIndexedfv_impl=None
def glViewportIndexedfv (index, v):
    global glViewportIndexedfv_impl
    if not glViewportIndexedfv_impl:
        fptr = pyglGetFuncAddress('glViewportIndexedfv')
        if not fptr:
            raise RuntimeError('The function glViewportIndexedfv is not available')
        glViewportIndexedfv_impl = PYGL_FUNC_TYPE( None ,c_uint, c_void_p)(fptr)
    glViewportIndexedfv = (lambda index,v:glViewportIndexedfv_impl(index,pyglGetAsConstVoidPointer( v )))
    return glViewportIndexedfv(index, v)
# <command>
#            <proto>void <name>glWaitSync</name></proto>
#            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
#            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
#            <param><ptype>GLuint64</ptype> <name>timeout</name></param>
#        </command>
#        
glWaitSync_impl=None
def glWaitSync (sync, flags, timeout):
    global glWaitSync_impl
    if not glWaitSync_impl:
        fptr = pyglGetFuncAddress('glWaitSync')
        if not fptr:
            raise RuntimeError('The function glWaitSync is not available')
        glWaitSync_impl = PYGL_FUNC_TYPE( None ,c_void_p, c_uint, c_ulonglong)(fptr)
    glWaitSync = glWaitSync_impl
    return glWaitSync(sync, flags, timeout)

def glShaderSource(shader,count,list_of_strings,list_of_lengths):
    if "impl" not in glShaderSource.__dict__:
        glShaderSource.impl = PYGL_FUNC_TYPE(None,c_uint,c_size_t,POINTER(c_char_p),
            POINTER(c_uint))(pyglGetFuncAddress("glShaderSource"))
    
    if list_of_lengths == None:
        list_of_lengths = [len(q) for q in list_of_strings]
        
    if len(list_of_strings) != len(list_of_lengths):
        raise RuntimeError("List length mismatch")
        
    sarray = (c_char_p * len(list_of_strings))()
    iarray = (c_uint * len(list_of_lengths))()

    for i in range(len(list_of_strings)):
        sarray[i] = list_of_strings[i].encode()
        iarray[i] = list_of_lengths[i]
        
    glShaderSource.impl( shader, count, sarray, iarray )

pyglDebugMessageCallbackFunc=None
pyglDebugMessageCallbackArg=None
def pyglDebugMessageCallback(src,typ,id_,sev,le,msg,p):
    if pyglDebugMessageCallbackFunc:
        pyglDebugMessageCallbackFunc( src,typ,id_,sev,le,msg.decode(),pyglDebugMessageCallbackArg)
        
def glDebugMessageCallback(func,parm):
    global pyglDebugMessageCallbackFunc
    global pyglDebugMessageCallbackArg
    #source,type,id,severity,length,mesg,parm)
    if sys.platform.lower().find("win32") != -1:
        FT = WINFUNCTYPE
    else:
        FT = CFUNCTYPE
        
    pyglDebugMessageCallbackFunc = func
    pyglDebugMessageCallbackArg = parm
    
    tmp = FT(None,c_uint,c_uint,c_uint,c_uint,c_uint,c_char_p,c_void_p)
    tmp2 = tmp(pyglDebugMessageCallback)
    
    #need to hold a reference to the variable
    glDebugMessageCallback.tmp2 = tmp2
    
    if "impl" not in glDebugMessageCallback.__dict__:
        glDebugMessageCallback.impl = PYGL_FUNC_TYPE(None,c_void_p,c_void_p)(
            pyglGetFuncAddress("glDebugMessageCallback")
        )
    glDebugMessageCallback.impl( tmp2, None )
    
