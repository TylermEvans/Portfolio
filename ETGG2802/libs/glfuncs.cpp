/*Data from gl.xml, which has this copyright:

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
*/
#include "glfuncs.h"

#ifdef WIN32
#include <windows.h>
#else
#include <dlfcn.h>
#endif
#include "glcorearb.h"
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdexcept>
#include <cstdio>

using namespace std;

static void* mygetprocaddr(const char* funcname){
    void* x = 0;
    
#ifdef WIN32
    static HMODULE gllib = 0;
    if (!gllib) {
        gllib = LoadLibraryA("opengl32.dll");
        if (!gllib)
            throw runtime_error("Cannot load GL library");
    }
    typedef void* (__stdcall *GLT)(LPCSTR);
    static GLT wglgpa;    
    if( !wglgpa ){
        wglgpa = (GLT) GetProcAddress(gllib,"wglGetProcAddress");
        if(!wglgpa)
            throw runtime_error("Cannot find wglGetProcAddress");
    }
    
    x = (void*) wglgpa(funcname);
    
    if (!x || x == (void*)1 || x == (void*)2 || x == (void*)3 || x == (void*)-1)
        x = 0;
        
    if(!x)
        x = (void*)GetProcAddress(gllib, funcname);
        
#else   
    static void* gllib = 0;
    if(!gllib){
        gllib = dlopen("libGL.so", RTLD_NOW);
        if (!gllib)
            throw runtime_error("Cannot load GL library");
    }
    x = dlsym(gllib, funcname);
#endif

    if (!x)
        throw runtime_error(string("Could not load function ")+funcname);
        
    return x;
  
}


void glActiveShaderProgram (GLuint pipeline_ , GLuint program_ ){
    /* <command>
            <proto>void <name>glActiveShaderProgram</name></proto>
            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
            <param><ptype>GLuint</ptype> <name>program</name></param>
        </command>
         */
    static PFNGLACTIVESHADERPROGRAMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLACTIVESHADERPROGRAMPROC ) mygetprocaddr("glActiveShaderProgram");
    glfunc(pipeline_, program_);
    return;
}
void glActiveTexture (GLenum texture_ ){
    /* <command>
            <proto>void <name>glActiveTexture</name></proto>
            <param group="TextureUnit"><ptype>GLenum</ptype> <name>texture</name></param>
            <glx opcode="197" type="render" />
        </command>
         */
    static PFNGLACTIVETEXTUREPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLACTIVETEXTUREPROC ) mygetprocaddr("glActiveTexture");
    glfunc(texture_);
    return;
}
void glAttachShader (GLuint program_ , GLuint shader_ ){
    /* <command>
            <proto>void <name>glAttachShader</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
        </command>
         */
    static PFNGLATTACHSHADERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLATTACHSHADERPROC ) mygetprocaddr("glAttachShader");
    glfunc(program_, shader_);
    return;
}
void glBeginConditionalRender (GLuint id_ , GLenum mode_ ){
    /* <command>
            <proto>void <name>glBeginConditionalRender</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param group="TypeEnum"><ptype>GLenum</ptype> <name>mode</name></param>
        </command>
         */
    static PFNGLBEGINCONDITIONALRENDERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBEGINCONDITIONALRENDERPROC ) mygetprocaddr("glBeginConditionalRender");
    glfunc(id_, mode_);
    return;
}
void glBeginQuery (GLenum target_ , GLuint id_ ){
    /* <command>
            <proto>void <name>glBeginQuery</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <glx opcode="231" type="render" />
        </command>
         */
    static PFNGLBEGINQUERYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBEGINQUERYPROC ) mygetprocaddr("glBeginQuery");
    glfunc(target_, id_);
    return;
}
void glBeginQueryIndexed (GLenum target_ , GLuint index_ , GLuint id_ ){
    /* <command>
            <proto>void <name>glBeginQueryIndexed</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
        </command>
         */
    static PFNGLBEGINQUERYINDEXEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBEGINQUERYINDEXEDPROC ) mygetprocaddr("glBeginQueryIndexed");
    glfunc(target_, index_, id_);
    return;
}
void glBeginTransformFeedback (GLenum primitiveMode_ ){
    /* <command>
            <proto>void <name>glBeginTransformFeedback</name></proto>
            <param><ptype>GLenum</ptype> <name>primitiveMode</name></param>
        </command>
         */
    static PFNGLBEGINTRANSFORMFEEDBACKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBEGINTRANSFORMFEEDBACKPROC ) mygetprocaddr("glBeginTransformFeedback");
    glfunc(primitiveMode_);
    return;
}
void glBindAttribLocation (GLuint program_ , GLuint index_ , const GLchar * name_ ){
    /* <command>
            <proto>void <name>glBindAttribLocation</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLBINDATTRIBLOCATIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDATTRIBLOCATIONPROC ) mygetprocaddr("glBindAttribLocation");
    glfunc(program_, index_, name_);
    return;
}
void glBindBuffer (GLenum target_ , GLuint buffer_ ){
    /* <command>
            <proto>void <name>glBindBuffer</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLBINDBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDBUFFERPROC ) mygetprocaddr("glBindBuffer");
    glfunc(target_, buffer_);
    return;
}
void glBindBufferBase (GLenum target_ , GLuint index_ , GLuint buffer_ ){
    /* <command>
            <proto>void <name>glBindBufferBase</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLBINDBUFFERBASEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDBUFFERBASEPROC ) mygetprocaddr("glBindBufferBase");
    glfunc(target_, index_, buffer_);
    return;
}
void glBindBufferRange (GLenum target_ , GLuint index_ , GLuint buffer_ , GLintptr offset_ , GLsizeiptr size_ ){
    /* <command>
            <proto>void <name>glBindBufferRange</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
        </command>
         */
    static PFNGLBINDBUFFERRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDBUFFERRANGEPROC ) mygetprocaddr("glBindBufferRange");
    glfunc(target_, index_, buffer_, offset_, size_);
    return;
}
void glBindBuffersBase (GLenum target_ , GLuint first_ , GLsizei count_ , const GLuint * buffers_ ){
    /* <command>
            <proto>void <name>glBindBuffersBase</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>buffers</name></param>
        </command>
         */
    static PFNGLBINDBUFFERSBASEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDBUFFERSBASEPROC ) mygetprocaddr("glBindBuffersBase");
    glfunc(target_, first_, count_, buffers_);
    return;
}
void glBindBuffersRange (GLenum target_ , GLuint first_ , GLsizei count_ , const GLuint * buffers_ , const GLintptr * offsets_ , const GLsizeiptr * sizes_ ){
    /* <command>
            <proto>void <name>glBindBuffersRange</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>buffers</name></param>
            <param len="count">const <ptype>GLintptr</ptype> *<name>offsets</name></param>
            <param len="count">const <ptype>GLsizeiptr</ptype> *<name>sizes</name></param>
        </command>
         */
    static PFNGLBINDBUFFERSRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDBUFFERSRANGEPROC ) mygetprocaddr("glBindBuffersRange");
    glfunc(target_, first_, count_, buffers_, offsets_, sizes_);
    return;
}
void glBindFragDataLocation (GLuint program_ , GLuint color_ , const GLchar * name_ ){
    /* <command>
            <proto>void <name>glBindFragDataLocation</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>color</name></param>
            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLBINDFRAGDATALOCATIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDFRAGDATALOCATIONPROC ) mygetprocaddr("glBindFragDataLocation");
    glfunc(program_, color_, name_);
    return;
}
void glBindFragDataLocationIndexed (GLuint program_ , GLuint colorNumber_ , GLuint index_ , const GLchar * name_ ){
    /* <command>
            <proto>void <name>glBindFragDataLocationIndexed</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>colorNumber</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLBINDFRAGDATALOCATIONINDEXEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDFRAGDATALOCATIONINDEXEDPROC ) mygetprocaddr("glBindFragDataLocationIndexed");
    glfunc(program_, colorNumber_, index_, name_);
    return;
}
void glBindFramebuffer (GLenum target_ , GLuint framebuffer_ ){
    /* <command>
            <proto>void <name>glBindFramebuffer</name></proto>
            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <glx opcode="236" type="render" />
        </command>
         */
    static PFNGLBINDFRAMEBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDFRAMEBUFFERPROC ) mygetprocaddr("glBindFramebuffer");
    glfunc(target_, framebuffer_);
    return;
}
void glBindImageTexture (GLuint unit_ , GLuint texture_ , GLint level_ , GLboolean layered_ , GLint layer_ , GLenum access_ , GLenum format_ ){
    /* <command>
            <proto>void <name>glBindImageTexture</name></proto>
            <param><ptype>GLuint</ptype> <name>unit</name></param>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>layered</name></param>
            <param><ptype>GLint</ptype> <name>layer</name></param>
            <param><ptype>GLenum</ptype> <name>access</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
        </command>
         */
    static PFNGLBINDIMAGETEXTUREPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDIMAGETEXTUREPROC ) mygetprocaddr("glBindImageTexture");
    glfunc(unit_, texture_, level_, layered_, layer_, access_, format_);
    return;
}
void glBindImageTextures (GLuint first_ , GLsizei count_ , const GLuint * textures_ ){
    /* <command>
            <proto>void <name>glBindImageTextures</name></proto>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>textures</name></param>
        </command>
         */
    static PFNGLBINDIMAGETEXTURESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDIMAGETEXTURESPROC ) mygetprocaddr("glBindImageTextures");
    glfunc(first_, count_, textures_);
    return;
}
void glBindProgramPipeline (GLuint pipeline_ ){
    /* <command>
            <proto>void <name>glBindProgramPipeline</name></proto>
            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
        </command>
         */
    static PFNGLBINDPROGRAMPIPELINEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDPROGRAMPIPELINEPROC ) mygetprocaddr("glBindProgramPipeline");
    glfunc(pipeline_);
    return;
}
void glBindRenderbuffer (GLenum target_ , GLuint renderbuffer_ ){
    /* <command>
            <proto>void <name>glBindRenderbuffer</name></proto>
            <param group="RenderbufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
            <glx opcode="235" type="render" />
        </command>
         */
    static PFNGLBINDRENDERBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDRENDERBUFFERPROC ) mygetprocaddr("glBindRenderbuffer");
    glfunc(target_, renderbuffer_);
    return;
}
void glBindSampler (GLuint unit_ , GLuint sampler_ ){
    /* <command>
            <proto>void <name>glBindSampler</name></proto>
            <param><ptype>GLuint</ptype> <name>unit</name></param>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
        </command>
         */
    static PFNGLBINDSAMPLERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDSAMPLERPROC ) mygetprocaddr("glBindSampler");
    glfunc(unit_, sampler_);
    return;
}
void glBindSamplers (GLuint first_ , GLsizei count_ , const GLuint * samplers_ ){
    /* <command>
            <proto>void <name>glBindSamplers</name></proto>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>samplers</name></param>
        </command>
         */
    static PFNGLBINDSAMPLERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDSAMPLERSPROC ) mygetprocaddr("glBindSamplers");
    glfunc(first_, count_, samplers_);
    return;
}
void glBindTexture (GLenum target_ , GLuint texture_ ){
    /* <command>
            <proto>void <name>glBindTexture</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="Texture"><ptype>GLuint</ptype> <name>texture</name></param>
            <glx opcode="4117" type="render" />
        </command>
         */
    static PFNGLBINDTEXTUREPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDTEXTUREPROC ) mygetprocaddr("glBindTexture");
    glfunc(target_, texture_);
    return;
}
void glBindTextureUnit (GLuint unit_ , GLuint texture_ ){
    /* <command>
            <proto>void <name>glBindTextureUnit</name></proto>
            <param><ptype>GLuint</ptype> <name>unit</name></param>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
        </command>
         */
    static PFNGLBINDTEXTUREUNITPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDTEXTUREUNITPROC ) mygetprocaddr("glBindTextureUnit");
    glfunc(unit_, texture_);
    return;
}
void glBindTextures (GLuint first_ , GLsizei count_ , const GLuint * textures_ ){
    /* <command>
            <proto>void <name>glBindTextures</name></proto>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>textures</name></param>
        </command>
         */
    static PFNGLBINDTEXTURESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDTEXTURESPROC ) mygetprocaddr("glBindTextures");
    glfunc(first_, count_, textures_);
    return;
}
void glBindTransformFeedback (GLenum target_ , GLuint id_ ){
    /* <command>
            <proto>void <name>glBindTransformFeedback</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
        </command>
         */
    static PFNGLBINDTRANSFORMFEEDBACKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDTRANSFORMFEEDBACKPROC ) mygetprocaddr("glBindTransformFeedback");
    glfunc(target_, id_);
    return;
}
void glBindVertexArray (GLuint array_ ){
    /* <command>
            <proto>void <name>glBindVertexArray</name></proto>
            <param><ptype>GLuint</ptype> <name>array</name></param>
            <glx opcode="350" type="render" />
        </command>
         */
    static PFNGLBINDVERTEXARRAYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDVERTEXARRAYPROC ) mygetprocaddr("glBindVertexArray");
    glfunc(array_);
    return;
}
void glBindVertexBuffer (GLuint bindingindex_ , GLuint buffer_ , GLintptr offset_ , GLsizei stride_ ){
    /* <command>
            <proto>void <name>glBindVertexBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param><ptype>GLsizei</ptype> <name>stride</name></param>
        </command>
         */
    static PFNGLBINDVERTEXBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDVERTEXBUFFERPROC ) mygetprocaddr("glBindVertexBuffer");
    glfunc(bindingindex_, buffer_, offset_, stride_);
    return;
}
void glBindVertexBuffers (GLuint first_ , GLsizei count_ , const GLuint * buffers_ , const GLintptr * offsets_ , const GLsizei * strides_ ){
    /* <command>
            <proto>void <name>glBindVertexBuffers</name></proto>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>buffers</name></param>
            <param len="count">const <ptype>GLintptr</ptype> *<name>offsets</name></param>
            <param len="count">const <ptype>GLsizei</ptype> *<name>strides</name></param>
        </command>
         */
    static PFNGLBINDVERTEXBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBINDVERTEXBUFFERSPROC ) mygetprocaddr("glBindVertexBuffers");
    glfunc(first_, count_, buffers_, offsets_, strides_);
    return;
}
void glBlendColor (GLfloat red_ , GLfloat green_ , GLfloat blue_ , GLfloat alpha_ ){
    /* <command>
            <proto>void <name>glBlendColor</name></proto>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>red</name></param>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>green</name></param>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>blue</name></param>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>alpha</name></param>
            <glx opcode="4096" type="render" />
        </command>
         */
    static PFNGLBLENDCOLORPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDCOLORPROC ) mygetprocaddr("glBlendColor");
    glfunc(red_, green_, blue_, alpha_);
    return;
}
void glBlendEquation (GLenum mode_ ){
    /* <command>
            <proto>void <name>glBlendEquation</name></proto>
            <param group="BlendEquationMode"><ptype>GLenum</ptype> <name>mode</name></param>
            <glx opcode="4097" type="render" />
        </command>
         */
    static PFNGLBLENDEQUATIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDEQUATIONPROC ) mygetprocaddr("glBlendEquation");
    glfunc(mode_);
    return;
}
void glBlendEquationSeparate (GLenum modeRGB_ , GLenum modeAlpha_ ){
    /* <command>
            <proto>void <name>glBlendEquationSeparate</name></proto>
            <param group="BlendEquationModeEXT"><ptype>GLenum</ptype> <name>modeRGB</name></param>
            <param group="BlendEquationModeEXT"><ptype>GLenum</ptype> <name>modeAlpha</name></param>
            <glx opcode="4228" type="render" />
        </command>
         */
    static PFNGLBLENDEQUATIONSEPARATEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDEQUATIONSEPARATEPROC ) mygetprocaddr("glBlendEquationSeparate");
    glfunc(modeRGB_, modeAlpha_);
    return;
}
void glBlendEquationSeparatei (GLuint buf_ , GLenum modeRGB_ , GLenum modeAlpha_ ){
    /* <command>
            <proto>void <name>glBlendEquationSeparatei</name></proto>
            <param><ptype>GLuint</ptype> <name>buf</name></param>
            <param><ptype>GLenum</ptype> <name>modeRGB</name></param>
            <param><ptype>GLenum</ptype> <name>modeAlpha</name></param>
        </command>
         */
    static PFNGLBLENDEQUATIONSEPARATEIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDEQUATIONSEPARATEIPROC ) mygetprocaddr("glBlendEquationSeparatei");
    glfunc(buf_, modeRGB_, modeAlpha_);
    return;
}
void glBlendEquationi (GLuint buf_ , GLenum mode_ ){
    /* <command>
            <proto>void <name>glBlendEquationi</name></proto>
            <param><ptype>GLuint</ptype> <name>buf</name></param>
            <param><ptype>GLenum</ptype> <name>mode</name></param>
        </command>
         */
    static PFNGLBLENDEQUATIONIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDEQUATIONIPROC ) mygetprocaddr("glBlendEquationi");
    glfunc(buf_, mode_);
    return;
}
void glBlendFunc (GLenum sfactor_ , GLenum dfactor_ ){
    /* <command>
            <proto>void <name>glBlendFunc</name></proto>
            <param group="BlendingFactorSrc"><ptype>GLenum</ptype> <name>sfactor</name></param>
            <param group="BlendingFactorDest"><ptype>GLenum</ptype> <name>dfactor</name></param>
            <glx opcode="160" type="render" />
        </command>
         */
    static PFNGLBLENDFUNCPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDFUNCPROC ) mygetprocaddr("glBlendFunc");
    glfunc(sfactor_, dfactor_);
    return;
}
void glBlendFuncSeparate (GLenum sfactorRGB_ , GLenum dfactorRGB_ , GLenum sfactorAlpha_ , GLenum dfactorAlpha_ ){
    /* <command>
            <proto>void <name>glBlendFuncSeparate</name></proto>
            <param group="BlendFuncSeparateParameterEXT"><ptype>GLenum</ptype> <name>sfactorRGB</name></param>
            <param group="BlendFuncSeparateParameterEXT"><ptype>GLenum</ptype> <name>dfactorRGB</name></param>
            <param group="BlendFuncSeparateParameterEXT"><ptype>GLenum</ptype> <name>sfactorAlpha</name></param>
            <param group="BlendFuncSeparateParameterEXT"><ptype>GLenum</ptype> <name>dfactorAlpha</name></param>
            <glx opcode="4134" type="render" />
        </command>
         */
    static PFNGLBLENDFUNCSEPARATEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDFUNCSEPARATEPROC ) mygetprocaddr("glBlendFuncSeparate");
    glfunc(sfactorRGB_, dfactorRGB_, sfactorAlpha_, dfactorAlpha_);
    return;
}
void glBlendFuncSeparatei (GLuint buf_ , GLenum srcRGB_ , GLenum dstRGB_ , GLenum srcAlpha_ , GLenum dstAlpha_ ){
    /* <command>
            <proto>void <name>glBlendFuncSeparatei</name></proto>
            <param><ptype>GLuint</ptype> <name>buf</name></param>
            <param><ptype>GLenum</ptype> <name>srcRGB</name></param>
            <param><ptype>GLenum</ptype> <name>dstRGB</name></param>
            <param><ptype>GLenum</ptype> <name>srcAlpha</name></param>
            <param><ptype>GLenum</ptype> <name>dstAlpha</name></param>
        </command>
         */
    static PFNGLBLENDFUNCSEPARATEIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDFUNCSEPARATEIPROC ) mygetprocaddr("glBlendFuncSeparatei");
    glfunc(buf_, srcRGB_, dstRGB_, srcAlpha_, dstAlpha_);
    return;
}
void glBlendFunci (GLuint buf_ , GLenum src_ , GLenum dst_ ){
    /* <command>
            <proto>void <name>glBlendFunci</name></proto>
            <param><ptype>GLuint</ptype> <name>buf</name></param>
            <param><ptype>GLenum</ptype> <name>src</name></param>
            <param><ptype>GLenum</ptype> <name>dst</name></param>
        </command>
         */
    static PFNGLBLENDFUNCIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLENDFUNCIPROC ) mygetprocaddr("glBlendFunci");
    glfunc(buf_, src_, dst_);
    return;
}
void glBlitFramebuffer (GLint srcX0_ , GLint srcY0_ , GLint srcX1_ , GLint srcY1_ , GLint dstX0_ , GLint dstY0_ , GLint dstX1_ , GLint dstY1_ , GLbitfield mask_ , GLenum filter_ ){
    /* <command>
            <proto>void <name>glBlitFramebuffer</name></proto>
            <param><ptype>GLint</ptype> <name>srcX0</name></param>
            <param><ptype>GLint</ptype> <name>srcY0</name></param>
            <param><ptype>GLint</ptype> <name>srcX1</name></param>
            <param><ptype>GLint</ptype> <name>srcY1</name></param>
            <param><ptype>GLint</ptype> <name>dstX0</name></param>
            <param><ptype>GLint</ptype> <name>dstY0</name></param>
            <param><ptype>GLint</ptype> <name>dstX1</name></param>
            <param><ptype>GLint</ptype> <name>dstY1</name></param>
            <param group="ClearBufferMask"><ptype>GLbitfield</ptype> <name>mask</name></param>
            <param><ptype>GLenum</ptype> <name>filter</name></param>
            <glx opcode="4330" type="render" />
        </command>
         */
    static PFNGLBLITFRAMEBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLITFRAMEBUFFERPROC ) mygetprocaddr("glBlitFramebuffer");
    glfunc(srcX0_, srcY0_, srcX1_, srcY1_, dstX0_, dstY0_, dstX1_, dstY1_, mask_, filter_);
    return;
}
void glBlitNamedFramebuffer (GLuint readFramebuffer_ , GLuint drawFramebuffer_ , GLint srcX0_ , GLint srcY0_ , GLint srcX1_ , GLint srcY1_ , GLint dstX0_ , GLint dstY0_ , GLint dstX1_ , GLint dstY1_ , GLbitfield mask_ , GLenum filter_ ){
    /* <command>
            <proto>void <name>glBlitNamedFramebuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>readFramebuffer</name></param>
            <param><ptype>GLuint</ptype> <name>drawFramebuffer</name></param>
            <param><ptype>GLint</ptype> <name>srcX0</name></param>
            <param><ptype>GLint</ptype> <name>srcY0</name></param>
            <param><ptype>GLint</ptype> <name>srcX1</name></param>
            <param><ptype>GLint</ptype> <name>srcY1</name></param>
            <param><ptype>GLint</ptype> <name>dstX0</name></param>
            <param><ptype>GLint</ptype> <name>dstY0</name></param>
            <param><ptype>GLint</ptype> <name>dstX1</name></param>
            <param><ptype>GLint</ptype> <name>dstY1</name></param>
            <param><ptype>GLbitfield</ptype> <name>mask</name></param>
            <param><ptype>GLenum</ptype> <name>filter</name></param>
        </command>
         */
    static PFNGLBLITNAMEDFRAMEBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBLITNAMEDFRAMEBUFFERPROC ) mygetprocaddr("glBlitNamedFramebuffer");
    glfunc(readFramebuffer_, drawFramebuffer_, srcX0_, srcY0_, srcX1_, srcY1_, dstX0_, dstY0_, dstX1_, dstY1_, mask_, filter_);
    return;
}
void glBufferData (GLenum target_ , GLsizeiptr size_ , const void * data_ , GLenum usage_ ){
    /* <command>
            <proto>void <name>glBufferData</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param len="size">const void *<name>data</name></param>
            <param group="BufferUsageARB"><ptype>GLenum</ptype> <name>usage</name></param>
        </command>
         */
    static PFNGLBUFFERDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBUFFERDATAPROC ) mygetprocaddr("glBufferData");
    glfunc(target_, size_, data_, usage_);
    return;
}
void glBufferStorage (GLenum target_ , GLsizeiptr size_ , const void * data_ , GLbitfield flags_ ){
    /* <command>
            <proto>void <name>glBufferStorage</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param len="size">const void *<name>data</name></param>
            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
        </command>
         */
    static PFNGLBUFFERSTORAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBUFFERSTORAGEPROC ) mygetprocaddr("glBufferStorage");
    glfunc(target_, size_, data_, flags_);
    return;
}
void glBufferSubData (GLenum target_ , GLintptr offset_ , GLsizeiptr size_ , const void * data_ ){
    /* <command>
            <proto>void <name>glBufferSubData</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param len="size">const void *<name>data</name></param>
        </command>
         */
    static PFNGLBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLBUFFERSUBDATAPROC ) mygetprocaddr("glBufferSubData");
    glfunc(target_, offset_, size_, data_);
    return;
}
GLenum glCheckFramebufferStatus (GLenum target_ ){
    /* <command>
            <proto><ptype>GLenum</ptype> <name>glCheckFramebufferStatus</name></proto>
            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <glx opcode="1427" type="vendor" />
        </command>
         */
    static PFNGLCHECKFRAMEBUFFERSTATUSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCHECKFRAMEBUFFERSTATUSPROC ) mygetprocaddr("glCheckFramebufferStatus");
    GLenum retval = glfunc(target_);
    return retval;
}
GLenum glCheckNamedFramebufferStatus (GLuint framebuffer_ , GLenum target_ ){
    /* <command>
            <proto><ptype>GLenum</ptype> <name>glCheckNamedFramebufferStatus</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>target</name></param>
        </command>
         */
    static PFNGLCHECKNAMEDFRAMEBUFFERSTATUSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCHECKNAMEDFRAMEBUFFERSTATUSPROC ) mygetprocaddr("glCheckNamedFramebufferStatus");
    GLenum retval = glfunc(framebuffer_, target_);
    return retval;
}
void glClampColor (GLenum target_ , GLenum clamp_ ){
    /* <command>
            <proto>void <name>glClampColor</name></proto>
            <param group="ClampColorTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="ClampColorModeARB"><ptype>GLenum</ptype> <name>clamp</name></param>
            <glx opcode="234" type="render" />
        </command>
         */
    static PFNGLCLAMPCOLORPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLAMPCOLORPROC ) mygetprocaddr("glClampColor");
    glfunc(target_, clamp_);
    return;
}
void glClear (GLbitfield mask_ ){
    /* <command>
            <proto>void <name>glClear</name></proto>
            <param group="ClearBufferMask"><ptype>GLbitfield</ptype> <name>mask</name></param>
            <glx opcode="127" type="render" />
        </command>
         */
    static PFNGLCLEARPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARPROC ) mygetprocaddr("glClear");
    glfunc(mask_);
    return;
}
void glClearBufferData (GLenum target_ , GLenum internalformat_ , GLenum format_ , GLenum type_ , const void * data_ ){
    /* <command>
            <proto>void <name>glClearBufferData</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type)">const void *<name>data</name></param>
        </command>
         */
    static PFNGLCLEARBUFFERDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARBUFFERDATAPROC ) mygetprocaddr("glClearBufferData");
    glfunc(target_, internalformat_, format_, type_, data_);
    return;
}
void glClearBufferSubData (GLenum target_ , GLenum internalformat_ , GLintptr offset_ , GLsizeiptr size_ , GLenum format_ , GLenum type_ , const void * data_ ){
    /* <command>
            <proto>void <name>glClearBufferSubData</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type)">const void *<name>data</name></param>
        </command>
         */
    static PFNGLCLEARBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARBUFFERSUBDATAPROC ) mygetprocaddr("glClearBufferSubData");
    glfunc(target_, internalformat_, offset_, size_, format_, type_, data_);
    return;
}
void glClearBufferfi (GLenum buffer_ , GLint drawbuffer_ , GLfloat depth_ , GLint stencil_ ){
    /* <command>
            <proto>void <name>glClearBufferfi</name></proto>
            <param><ptype>GLenum</ptype> <name>buffer</name></param>
            <param group="DrawBufferName"><ptype>GLint</ptype> <name>drawbuffer</name></param>
            <param><ptype>GLfloat</ptype> <name>depth</name></param>
            <param><ptype>GLint</ptype> <name>stencil</name></param>
        </command>
         */
    static PFNGLCLEARBUFFERFIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARBUFFERFIPROC ) mygetprocaddr("glClearBufferfi");
    glfunc(buffer_, drawbuffer_, depth_, stencil_);
    return;
}
void glClearBufferfv (GLenum buffer_ , GLint drawbuffer_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glClearBufferfv</name></proto>
            <param><ptype>GLenum</ptype> <name>buffer</name></param>
            <param group="DrawBufferName"><ptype>GLint</ptype> <name>drawbuffer</name></param>
            <param len="COMPSIZE(buffer)">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLCLEARBUFFERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARBUFFERFVPROC ) mygetprocaddr("glClearBufferfv");
    glfunc(buffer_, drawbuffer_, value_);
    return;
}
void glClearBufferiv (GLenum buffer_ , GLint drawbuffer_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glClearBufferiv</name></proto>
            <param><ptype>GLenum</ptype> <name>buffer</name></param>
            <param group="DrawBufferName"><ptype>GLint</ptype> <name>drawbuffer</name></param>
            <param len="COMPSIZE(buffer)">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLCLEARBUFFERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARBUFFERIVPROC ) mygetprocaddr("glClearBufferiv");
    glfunc(buffer_, drawbuffer_, value_);
    return;
}
void glClearBufferuiv (GLenum buffer_ , GLint drawbuffer_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glClearBufferuiv</name></proto>
            <param><ptype>GLenum</ptype> <name>buffer</name></param>
            <param group="DrawBufferName"><ptype>GLint</ptype> <name>drawbuffer</name></param>
            <param len="COMPSIZE(buffer)">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLCLEARBUFFERUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARBUFFERUIVPROC ) mygetprocaddr("glClearBufferuiv");
    glfunc(buffer_, drawbuffer_, value_);
    return;
}
void glClearColor (GLfloat red_ , GLfloat green_ , GLfloat blue_ , GLfloat alpha_ ){
    /* <command>
            <proto>void <name>glClearColor</name></proto>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>red</name></param>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>green</name></param>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>blue</name></param>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>alpha</name></param>
            <glx opcode="130" type="render" />
        </command>
         */
    static PFNGLCLEARCOLORPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARCOLORPROC ) mygetprocaddr("glClearColor");
    glfunc(red_, green_, blue_, alpha_);
    return;
}
void glClearDepth (GLdouble depth_ ){
    /* <command>
            <proto>void <name>glClearDepth</name></proto>
            <param><ptype>GLdouble</ptype> <name>depth</name></param>
            <glx opcode="132" type="render" />
        </command>
         */
    static PFNGLCLEARDEPTHPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARDEPTHPROC ) mygetprocaddr("glClearDepth");
    glfunc(depth_);
    return;
}
void glClearDepthf (GLfloat d_ ){
    /* <command>
            <proto>void <name>glClearDepthf</name></proto>
            <param><ptype>GLfloat</ptype> <name>d</name></param>
        </command>
         */
    static PFNGLCLEARDEPTHFPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARDEPTHFPROC ) mygetprocaddr("glClearDepthf");
    glfunc(d_);
    return;
}
void glClearNamedBufferData (GLuint buffer_ , GLenum internalformat_ , GLenum format_ , GLenum type_ , const void * data_ ){
    /* <command>
            <proto>void <name>glClearNamedBufferData</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param>const void *<name>data</name></param>
        </command>
         */
    static PFNGLCLEARNAMEDBUFFERDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARNAMEDBUFFERDATAPROC ) mygetprocaddr("glClearNamedBufferData");
    glfunc(buffer_, internalformat_, format_, type_, data_);
    return;
}
void glClearNamedBufferSubData (GLuint buffer_ , GLenum internalformat_ , GLintptr offset_ , GLsizeiptr size_ , GLenum format_ , GLenum type_ , const void * data_ ){
    /* <command>
            <proto>void <name>glClearNamedBufferSubData</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param>const void *<name>data</name></param>
        </command>
         */
    static PFNGLCLEARNAMEDBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARNAMEDBUFFERSUBDATAPROC ) mygetprocaddr("glClearNamedBufferSubData");
    glfunc(buffer_, internalformat_, offset_, size_, format_, type_, data_);
    return;
}
void glClearNamedFramebufferfi (GLuint framebuffer_ , GLenum buffer_ , GLint drawbuffer_ , GLfloat depth_ , GLint stencil_ ){
    /* <command>
            <proto>void <name>glClearNamedFramebufferfi</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>buffer</name></param>
            <param><ptype>GLint</ptype> <name>drawbuffer</name></param>
            <param><ptype>GLfloat</ptype> <name>depth</name></param>
            <param><ptype>GLint</ptype> <name>stencil</name></param>
        </command>
         */
    static PFNGLCLEARNAMEDFRAMEBUFFERFIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARNAMEDFRAMEBUFFERFIPROC ) mygetprocaddr("glClearNamedFramebufferfi");
    glfunc(framebuffer_, buffer_, drawbuffer_, depth_, stencil_);
    return;
}
void glClearNamedFramebufferfv (GLuint framebuffer_ , GLenum buffer_ , GLint drawbuffer_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glClearNamedFramebufferfv</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>buffer</name></param>
            <param><ptype>GLint</ptype> <name>drawbuffer</name></param>
            <param>const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLCLEARNAMEDFRAMEBUFFERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARNAMEDFRAMEBUFFERFVPROC ) mygetprocaddr("glClearNamedFramebufferfv");
    glfunc(framebuffer_, buffer_, drawbuffer_, value_);
    return;
}
void glClearNamedFramebufferiv (GLuint framebuffer_ , GLenum buffer_ , GLint drawbuffer_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glClearNamedFramebufferiv</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>buffer</name></param>
            <param><ptype>GLint</ptype> <name>drawbuffer</name></param>
            <param>const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLCLEARNAMEDFRAMEBUFFERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARNAMEDFRAMEBUFFERIVPROC ) mygetprocaddr("glClearNamedFramebufferiv");
    glfunc(framebuffer_, buffer_, drawbuffer_, value_);
    return;
}
void glClearNamedFramebufferuiv (GLuint framebuffer_ , GLenum buffer_ , GLint drawbuffer_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glClearNamedFramebufferuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>buffer</name></param>
            <param><ptype>GLint</ptype> <name>drawbuffer</name></param>
            <param>const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLCLEARNAMEDFRAMEBUFFERUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARNAMEDFRAMEBUFFERUIVPROC ) mygetprocaddr("glClearNamedFramebufferuiv");
    glfunc(framebuffer_, buffer_, drawbuffer_, value_);
    return;
}
void glClearStencil (GLint s_ ){
    /* <command>
            <proto>void <name>glClearStencil</name></proto>
            <param group="StencilValue"><ptype>GLint</ptype> <name>s</name></param>
            <glx opcode="131" type="render" />
        </command>
         */
    static PFNGLCLEARSTENCILPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARSTENCILPROC ) mygetprocaddr("glClearStencil");
    glfunc(s_);
    return;
}
void glClearTexImage (GLuint texture_ , GLint level_ , GLenum format_ , GLenum type_ , const void * data_ ){
    /* <command>
            <proto>void <name>glClearTexImage</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type)">const void *<name>data</name></param>
        </command>
         */
    static PFNGLCLEARTEXIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARTEXIMAGEPROC ) mygetprocaddr("glClearTexImage");
    glfunc(texture_, level_, format_, type_, data_);
    return;
}
void glClearTexSubImage (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLenum format_ , GLenum type_ , const void * data_ ){
    /* <command>
            <proto>void <name>glClearTexSubImage</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type)">const void *<name>data</name></param>
        </command>
         */
    static PFNGLCLEARTEXSUBIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLEARTEXSUBIMAGEPROC ) mygetprocaddr("glClearTexSubImage");
    glfunc(texture_, level_, xoffset_, yoffset_, zoffset_, width_, height_, depth_, format_, type_, data_);
    return;
}
GLenum glClientWaitSync (GLsync sync_ , GLbitfield flags_ , GLuint64 timeout_ ){
    /* <command>
            <proto><ptype>GLenum</ptype> <name>glClientWaitSync</name></proto>
            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
            <param><ptype>GLuint64</ptype> <name>timeout</name></param>
        </command>
         */
    static PFNGLCLIENTWAITSYNCPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLIENTWAITSYNCPROC ) mygetprocaddr("glClientWaitSync");
    GLenum retval = glfunc(sync_, flags_, timeout_);
    return retval;
}
void glClipControl (GLenum origin_ , GLenum depth_ ){
    /* <command>
            <proto>void <name>glClipControl</name></proto>
            <param><ptype>GLenum</ptype> <name>origin</name></param>
            <param><ptype>GLenum</ptype> <name>depth</name></param>
        </command>
         */
    static PFNGLCLIPCONTROLPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCLIPCONTROLPROC ) mygetprocaddr("glClipControl");
    glfunc(origin_, depth_);
    return;
}
void glColorMask (GLboolean red_ , GLboolean green_ , GLboolean blue_ , GLboolean alpha_ ){
    /* <command>
            <proto>void <name>glColorMask</name></proto>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>red</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>green</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>blue</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>alpha</name></param>
            <glx opcode="134" type="render" />
        </command>
         */
    static PFNGLCOLORMASKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOLORMASKPROC ) mygetprocaddr("glColorMask");
    glfunc(red_, green_, blue_, alpha_);
    return;
}
void glColorMaski (GLuint index_ , GLboolean r_ , GLboolean g_ , GLboolean b_ , GLboolean a_ ){
    /* <command>
            <proto>void <name>glColorMaski</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>r</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>g</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>b</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>a</name></param>
        </command>
         */
    static PFNGLCOLORMASKIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOLORMASKIPROC ) mygetprocaddr("glColorMaski");
    glfunc(index_, r_, g_, b_, a_);
    return;
}
void glCompileShader (GLuint shader_ ){
    /* <command>
            <proto>void <name>glCompileShader</name></proto>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
        </command>
         */
    static PFNGLCOMPILESHADERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPILESHADERPROC ) mygetprocaddr("glCompileShader");
    glfunc(shader_);
    return;
}
void glCompressedTexImage1D (GLenum target_ , GLint level_ , GLenum internalformat_ , GLsizei width_ , GLint border_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTexImage1D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
            <glx opcode="214" type="render" />
            <glx comment="PBO protocol" name="glCompressedTexImage1DPBO" opcode="314" type="render" />
        </command>
         */
    static PFNGLCOMPRESSEDTEXIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXIMAGE1DPROC ) mygetprocaddr("glCompressedTexImage1D");
    glfunc(target_, level_, internalformat_, width_, border_, imageSize_, data_);
    return;
}
void glCompressedTexImage2D (GLenum target_ , GLint level_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ , GLint border_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTexImage2D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
            <glx opcode="215" type="render" />
            <glx comment="PBO protocol" name="glCompressedTexImage2DPBO" opcode="315" type="render" />
        </command>
         */
    static PFNGLCOMPRESSEDTEXIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXIMAGE2DPROC ) mygetprocaddr("glCompressedTexImage2D");
    glfunc(target_, level_, internalformat_, width_, height_, border_, imageSize_, data_);
    return;
}
void glCompressedTexImage3D (GLenum target_ , GLint level_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLint border_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTexImage3D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
            <glx opcode="216" type="render" />
            <glx comment="PBO protocol" name="glCompressedTexImage3DPBO" opcode="316" type="render" />
        </command>
         */
    static PFNGLCOMPRESSEDTEXIMAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXIMAGE3DPROC ) mygetprocaddr("glCompressedTexImage3D");
    glfunc(target_, level_, internalformat_, width_, height_, depth_, border_, imageSize_, data_);
    return;
}
void glCompressedTexSubImage1D (GLenum target_ , GLint level_ , GLint xoffset_ , GLsizei width_ , GLenum format_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTexSubImage1D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
            <glx opcode="217" type="render" />
            <glx comment="PBO protocol" name="glCompressedTexSubImage1DPBO" opcode="317" type="render" />
        </command>
         */
    static PFNGLCOMPRESSEDTEXSUBIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXSUBIMAGE1DPROC ) mygetprocaddr("glCompressedTexSubImage1D");
    glfunc(target_, level_, xoffset_, width_, format_, imageSize_, data_);
    return;
}
void glCompressedTexSubImage2D (GLenum target_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLsizei width_ , GLsizei height_ , GLenum format_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTexSubImage2D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
            <glx opcode="218" type="render" />
            <glx comment="PBO protocol" name="glCompressedTexSubImage2DPBO" opcode="318" type="render" />
        </command>
         */
    static PFNGLCOMPRESSEDTEXSUBIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXSUBIMAGE2DPROC ) mygetprocaddr("glCompressedTexSubImage2D");
    glfunc(target_, level_, xoffset_, yoffset_, width_, height_, format_, imageSize_, data_);
    return;
}
void glCompressedTexSubImage3D (GLenum target_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLenum format_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTexSubImage3D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param group="CompressedTextureARB" len="imageSize">const void *<name>data</name></param>
            <glx opcode="219" type="render" />
            <glx comment="PBO protocol" name="glCompressedTexSubImage3DPBO" opcode="319" type="render" />
        </command>
         */
    static PFNGLCOMPRESSEDTEXSUBIMAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXSUBIMAGE3DPROC ) mygetprocaddr("glCompressedTexSubImage3D");
    glfunc(target_, level_, xoffset_, yoffset_, zoffset_, width_, height_, depth_, format_, imageSize_, data_);
    return;
}
void glCompressedTextureSubImage1D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLsizei width_ , GLenum format_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTextureSubImage1D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param>const void *<name>data</name></param>
        </command>
         */
    static PFNGLCOMPRESSEDTEXTURESUBIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXTURESUBIMAGE1DPROC ) mygetprocaddr("glCompressedTextureSubImage1D");
    glfunc(texture_, level_, xoffset_, width_, format_, imageSize_, data_);
    return;
}
void glCompressedTextureSubImage2D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLsizei width_ , GLsizei height_ , GLenum format_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTextureSubImage2D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param>const void *<name>data</name></param>
        </command>
         */
    static PFNGLCOMPRESSEDTEXTURESUBIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXTURESUBIMAGE2DPROC ) mygetprocaddr("glCompressedTextureSubImage2D");
    glfunc(texture_, level_, xoffset_, yoffset_, width_, height_, format_, imageSize_, data_);
    return;
}
void glCompressedTextureSubImage3D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLenum format_ , GLsizei imageSize_ , const void * data_ ){
    /* <command>
            <proto>void <name>glCompressedTextureSubImage3D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLsizei</ptype> <name>imageSize</name></param>
            <param>const void *<name>data</name></param>
        </command>
         */
    static PFNGLCOMPRESSEDTEXTURESUBIMAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOMPRESSEDTEXTURESUBIMAGE3DPROC ) mygetprocaddr("glCompressedTextureSubImage3D");
    glfunc(texture_, level_, xoffset_, yoffset_, zoffset_, width_, height_, depth_, format_, imageSize_, data_);
    return;
}
void glCopyBufferSubData (GLenum readTarget_ , GLenum writeTarget_ , GLintptr readOffset_ , GLintptr writeOffset_ , GLsizeiptr size_ ){
    /* <command>
            <proto>void <name>glCopyBufferSubData</name></proto>
            <param><ptype>GLenum</ptype> <name>readTarget</name></param>
            <param><ptype>GLenum</ptype> <name>writeTarget</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>readOffset</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>writeOffset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
        </command>
         */
    static PFNGLCOPYBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYBUFFERSUBDATAPROC ) mygetprocaddr("glCopyBufferSubData");
    glfunc(readTarget_, writeTarget_, readOffset_, writeOffset_, size_);
    return;
}
void glCopyImageSubData (GLuint srcName_ , GLenum srcTarget_ , GLint srcLevel_ , GLint srcX_ , GLint srcY_ , GLint srcZ_ , GLuint dstName_ , GLenum dstTarget_ , GLint dstLevel_ , GLint dstX_ , GLint dstY_ , GLint dstZ_ , GLsizei srcWidth_ , GLsizei srcHeight_ , GLsizei srcDepth_ ){
    /* <command>
            <proto>void <name>glCopyImageSubData</name></proto>
            <param><ptype>GLuint</ptype> <name>srcName</name></param>
            <param><ptype>GLenum</ptype> <name>srcTarget</name></param>
            <param><ptype>GLint</ptype> <name>srcLevel</name></param>
            <param><ptype>GLint</ptype> <name>srcX</name></param>
            <param><ptype>GLint</ptype> <name>srcY</name></param>
            <param><ptype>GLint</ptype> <name>srcZ</name></param>
            <param><ptype>GLuint</ptype> <name>dstName</name></param>
            <param><ptype>GLenum</ptype> <name>dstTarget</name></param>
            <param><ptype>GLint</ptype> <name>dstLevel</name></param>
            <param><ptype>GLint</ptype> <name>dstX</name></param>
            <param><ptype>GLint</ptype> <name>dstY</name></param>
            <param><ptype>GLint</ptype> <name>dstZ</name></param>
            <param><ptype>GLsizei</ptype> <name>srcWidth</name></param>
            <param><ptype>GLsizei</ptype> <name>srcHeight</name></param>
            <param><ptype>GLsizei</ptype> <name>srcDepth</name></param>
        </command>
         */
    static PFNGLCOPYIMAGESUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYIMAGESUBDATAPROC ) mygetprocaddr("glCopyImageSubData");
    glfunc(srcName_, srcTarget_, srcLevel_, srcX_, srcY_, srcZ_, dstName_, dstTarget_, dstLevel_, dstX_, dstY_, dstZ_, srcWidth_, srcHeight_, srcDepth_);
    return;
}
void glCopyNamedBufferSubData (GLuint readBuffer_ , GLuint writeBuffer_ , GLintptr readOffset_ , GLintptr writeOffset_ , GLsizeiptr size_ ){
    /* <command>
            <proto>void <name>glCopyNamedBufferSubData</name></proto>
            <param><ptype>GLuint</ptype> <name>readBuffer</name></param>
            <param><ptype>GLuint</ptype> <name>writeBuffer</name></param>
            <param><ptype>GLintptr</ptype> <name>readOffset</name></param>
            <param><ptype>GLintptr</ptype> <name>writeOffset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
        </command>
         */
    static PFNGLCOPYNAMEDBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYNAMEDBUFFERSUBDATAPROC ) mygetprocaddr("glCopyNamedBufferSubData");
    glfunc(readBuffer_, writeBuffer_, readOffset_, writeOffset_, size_);
    return;
}
void glCopyTexImage1D (GLenum target_ , GLint level_ , GLenum internalformat_ , GLint x_ , GLint y_ , GLsizei width_ , GLint border_ ){
    /* <command>
            <proto>void <name>glCopyTexImage1D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
            <glx opcode="4119" type="render" />
        </command>
         */
    static PFNGLCOPYTEXIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYTEXIMAGE1DPROC ) mygetprocaddr("glCopyTexImage1D");
    glfunc(target_, level_, internalformat_, x_, y_, width_, border_);
    return;
}
void glCopyTexImage2D (GLenum target_ , GLint level_ , GLenum internalformat_ , GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ , GLint border_ ){
    /* <command>
            <proto>void <name>glCopyTexImage2D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="PixelInternalFormat"><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
            <glx opcode="4120" type="render" />
        </command>
         */
    static PFNGLCOPYTEXIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYTEXIMAGE2DPROC ) mygetprocaddr("glCopyTexImage2D");
    glfunc(target_, level_, internalformat_, x_, y_, width_, height_, border_);
    return;
}
void glCopyTexSubImage1D (GLenum target_ , GLint level_ , GLint xoffset_ , GLint x_ , GLint y_ , GLsizei width_ ){
    /* <command>
            <proto>void <name>glCopyTexSubImage1D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <glx opcode="4121" type="render" />
        </command>
         */
    static PFNGLCOPYTEXSUBIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYTEXSUBIMAGE1DPROC ) mygetprocaddr("glCopyTexSubImage1D");
    glfunc(target_, level_, xoffset_, x_, y_, width_);
    return;
}
void glCopyTexSubImage2D (GLenum target_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glCopyTexSubImage2D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <glx opcode="4122" type="render" />
        </command>
         */
    static PFNGLCOPYTEXSUBIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYTEXSUBIMAGE2DPROC ) mygetprocaddr("glCopyTexSubImage2D");
    glfunc(target_, level_, xoffset_, yoffset_, x_, y_, width_, height_);
    return;
}
void glCopyTexSubImage3D (GLenum target_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glCopyTexSubImage3D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>zoffset</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <glx opcode="4123" type="render" />
        </command>
         */
    static PFNGLCOPYTEXSUBIMAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYTEXSUBIMAGE3DPROC ) mygetprocaddr("glCopyTexSubImage3D");
    glfunc(target_, level_, xoffset_, yoffset_, zoffset_, x_, y_, width_, height_);
    return;
}
void glCopyTextureSubImage1D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint x_ , GLint y_ , GLsizei width_ ){
    /* <command>
            <proto>void <name>glCopyTextureSubImage1D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
        </command>
         */
    static PFNGLCOPYTEXTURESUBIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYTEXTURESUBIMAGE1DPROC ) mygetprocaddr("glCopyTextureSubImage1D");
    glfunc(texture_, level_, xoffset_, x_, y_, width_);
    return;
}
void glCopyTextureSubImage2D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glCopyTextureSubImage2D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLCOPYTEXTURESUBIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYTEXTURESUBIMAGE2DPROC ) mygetprocaddr("glCopyTextureSubImage2D");
    glfunc(texture_, level_, xoffset_, yoffset_, x_, y_, width_, height_);
    return;
}
void glCopyTextureSubImage3D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glCopyTextureSubImage3D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLCOPYTEXTURESUBIMAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCOPYTEXTURESUBIMAGE3DPROC ) mygetprocaddr("glCopyTextureSubImage3D");
    glfunc(texture_, level_, xoffset_, yoffset_, zoffset_, x_, y_, width_, height_);
    return;
}
void glCreateBuffers (GLsizei n_ , GLuint * buffers_ ){
    /* <command>
            <proto>void <name>glCreateBuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>buffers</name></param>
        </command>
         */
    static PFNGLCREATEBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATEBUFFERSPROC ) mygetprocaddr("glCreateBuffers");
    glfunc(n_, buffers_);
    return;
}
void glCreateFramebuffers (GLsizei n_ , GLuint * framebuffers_ ){
    /* <command>
            <proto>void <name>glCreateFramebuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>framebuffers</name></param>
        </command>
         */
    static PFNGLCREATEFRAMEBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATEFRAMEBUFFERSPROC ) mygetprocaddr("glCreateFramebuffers");
    glfunc(n_, framebuffers_);
    return;
}
GLuint glCreateProgram (){
    /* <command>
            <proto><ptype>GLuint</ptype> <name>glCreateProgram</name></proto>
        </command>
         */
    static PFNGLCREATEPROGRAMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATEPROGRAMPROC ) mygetprocaddr("glCreateProgram");
    GLuint retval = glfunc();
    return retval;
}
void glCreateProgramPipelines (GLsizei n_ , GLuint * pipelines_ ){
    /* <command>
            <proto>void <name>glCreateProgramPipelines</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>pipelines</name></param>
        </command>
         */
    static PFNGLCREATEPROGRAMPIPELINESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATEPROGRAMPIPELINESPROC ) mygetprocaddr("glCreateProgramPipelines");
    glfunc(n_, pipelines_);
    return;
}
void glCreateQueries (GLenum target_ , GLsizei n_ , GLuint * ids_ ){
    /* <command>
            <proto>void <name>glCreateQueries</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>ids</name></param>
        </command>
         */
    static PFNGLCREATEQUERIESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATEQUERIESPROC ) mygetprocaddr("glCreateQueries");
    glfunc(target_, n_, ids_);
    return;
}
void glCreateRenderbuffers (GLsizei n_ , GLuint * renderbuffers_ ){
    /* <command>
            <proto>void <name>glCreateRenderbuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>renderbuffers</name></param>
        </command>
         */
    static PFNGLCREATERENDERBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATERENDERBUFFERSPROC ) mygetprocaddr("glCreateRenderbuffers");
    glfunc(n_, renderbuffers_);
    return;
}
void glCreateSamplers (GLsizei n_ , GLuint * samplers_ ){
    /* <command>
            <proto>void <name>glCreateSamplers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>samplers</name></param>
        </command>
         */
    static PFNGLCREATESAMPLERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATESAMPLERSPROC ) mygetprocaddr("glCreateSamplers");
    glfunc(n_, samplers_);
    return;
}
GLuint glCreateShader (GLenum type_ ){
    /* <command>
            <proto><ptype>GLuint</ptype> <name>glCreateShader</name></proto>
            <param><ptype>GLenum</ptype> <name>type</name></param>
        </command>
         */
    static PFNGLCREATESHADERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATESHADERPROC ) mygetprocaddr("glCreateShader");
    GLuint retval = glfunc(type_);
    return retval;
}
GLuint glCreateShaderProgramv (GLenum type_ , GLsizei count_ , const GLchar ** strings_ ){
    /* <command>
            <proto><ptype>GLuint</ptype> <name>glCreateShaderProgramv</name></proto>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLchar</ptype> *const*<name>strings</name></param>
        </command>
         */
    static PFNGLCREATESHADERPROGRAMVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATESHADERPROGRAMVPROC ) mygetprocaddr("glCreateShaderProgramv");
    GLuint retval = glfunc(type_, count_, strings_);
    return retval;
}
void glCreateTextures (GLenum target_ , GLsizei n_ , GLuint * textures_ ){
    /* <command>
            <proto>void <name>glCreateTextures</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>textures</name></param>
        </command>
         */
    static PFNGLCREATETEXTURESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATETEXTURESPROC ) mygetprocaddr("glCreateTextures");
    glfunc(target_, n_, textures_);
    return;
}
void glCreateTransformFeedbacks (GLsizei n_ , GLuint * ids_ ){
    /* <command>
            <proto>void <name>glCreateTransformFeedbacks</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>ids</name></param>
        </command>
         */
    static PFNGLCREATETRANSFORMFEEDBACKSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATETRANSFORMFEEDBACKSPROC ) mygetprocaddr("glCreateTransformFeedbacks");
    glfunc(n_, ids_);
    return;
}
void glCreateVertexArrays (GLsizei n_ , GLuint * arrays_ ){
    /* <command>
            <proto>void <name>glCreateVertexArrays</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param><ptype>GLuint</ptype> *<name>arrays</name></param>
        </command>
         */
    static PFNGLCREATEVERTEXARRAYSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCREATEVERTEXARRAYSPROC ) mygetprocaddr("glCreateVertexArrays");
    glfunc(n_, arrays_);
    return;
}
void glCullFace (GLenum mode_ ){
    /* <command>
            <proto>void <name>glCullFace</name></proto>
            <param group="CullFaceMode"><ptype>GLenum</ptype> <name>mode</name></param>
            <glx opcode="79" type="render" />
        </command>
         */
    static PFNGLCULLFACEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLCULLFACEPROC ) mygetprocaddr("glCullFace");
    glfunc(mode_);
    return;
}
void glDebugMessageCallback (GLDEBUGPROC callback_ , const void * userParam_ ){
    /* <command>
            <proto>void <name>glDebugMessageCallback</name></proto>
            <param><ptype>GLDEBUGPROC</ptype> <name>callback</name></param>
            <param>const void *<name>userParam</name></param>
        </command>
         */
    static PFNGLDEBUGMESSAGECALLBACKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEBUGMESSAGECALLBACKPROC ) mygetprocaddr("glDebugMessageCallback");
    glfunc(callback_, userParam_);
    return;
}
void glDebugMessageControl (GLenum source_ , GLenum type_ , GLenum severity_ , GLsizei count_ , const GLuint * ids_ , GLboolean enabled_ ){
    /* <command>
            <proto>void <name>glDebugMessageControl</name></proto>
            <param><ptype>GLenum</ptype> <name>source</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param><ptype>GLenum</ptype> <name>severity</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>ids</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>enabled</name></param>
        </command>
         */
    static PFNGLDEBUGMESSAGECONTROLPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEBUGMESSAGECONTROLPROC ) mygetprocaddr("glDebugMessageControl");
    glfunc(source_, type_, severity_, count_, ids_, enabled_);
    return;
}
void glDebugMessageInsert (GLenum source_ , GLenum type_ , GLuint id_ , GLenum severity_ , GLsizei length_ , const GLchar * buf_ ){
    /* <command>
            <proto>void <name>glDebugMessageInsert</name></proto>
            <param><ptype>GLenum</ptype> <name>source</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLenum</ptype> <name>severity</name></param>
            <param><ptype>GLsizei</ptype> <name>length</name></param>
            <param len="COMPSIZE(buf,length)">const <ptype>GLchar</ptype> *<name>buf</name></param>
        </command>
         */
    static PFNGLDEBUGMESSAGEINSERTPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEBUGMESSAGEINSERTPROC ) mygetprocaddr("glDebugMessageInsert");
    glfunc(source_, type_, id_, severity_, length_, buf_);
    return;
}
void glDeleteBuffers (GLsizei n_ , const GLuint * buffers_ ){
    /* <command>
            <proto>void <name>glDeleteBuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n">const <ptype>GLuint</ptype> *<name>buffers</name></param>
        </command>
         */
    static PFNGLDELETEBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETEBUFFERSPROC ) mygetprocaddr("glDeleteBuffers");
    glfunc(n_, buffers_);
    return;
}
void glDeleteFramebuffers (GLsizei n_ , const GLuint * framebuffers_ ){
    /* <command>
            <proto>void <name>glDeleteFramebuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n">const <ptype>GLuint</ptype> *<name>framebuffers</name></param>
            <glx opcode="4320" type="render" />
        </command>
         */
    static PFNGLDELETEFRAMEBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETEFRAMEBUFFERSPROC ) mygetprocaddr("glDeleteFramebuffers");
    glfunc(n_, framebuffers_);
    return;
}
void glDeleteProgram (GLuint program_ ){
    /* <command>
            <proto>void <name>glDeleteProgram</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <glx opcode="202" type="single" />
        </command>
         */
    static PFNGLDELETEPROGRAMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETEPROGRAMPROC ) mygetprocaddr("glDeleteProgram");
    glfunc(program_);
    return;
}
void glDeleteProgramPipelines (GLsizei n_ , const GLuint * pipelines_ ){
    /* <command>
            <proto>void <name>glDeleteProgramPipelines</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n">const <ptype>GLuint</ptype> *<name>pipelines</name></param>
        </command>
         */
    static PFNGLDELETEPROGRAMPIPELINESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETEPROGRAMPIPELINESPROC ) mygetprocaddr("glDeleteProgramPipelines");
    glfunc(n_, pipelines_);
    return;
}
void glDeleteQueries (GLsizei n_ , const GLuint * ids_ ){
    /* <command>
            <proto>void <name>glDeleteQueries</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n">const <ptype>GLuint</ptype> *<name>ids</name></param>
            <glx opcode="161" type="single" />
        </command>
         */
    static PFNGLDELETEQUERIESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETEQUERIESPROC ) mygetprocaddr("glDeleteQueries");
    glfunc(n_, ids_);
    return;
}
void glDeleteRenderbuffers (GLsizei n_ , const GLuint * renderbuffers_ ){
    /* <command>
            <proto>void <name>glDeleteRenderbuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n">const <ptype>GLuint</ptype> *<name>renderbuffers</name></param>
            <glx opcode="4317" type="render" />
        </command>
         */
    static PFNGLDELETERENDERBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETERENDERBUFFERSPROC ) mygetprocaddr("glDeleteRenderbuffers");
    glfunc(n_, renderbuffers_);
    return;
}
void glDeleteSamplers (GLsizei count_ , const GLuint * samplers_ ){
    /* <command>
            <proto>void <name>glDeleteSamplers</name></proto>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>samplers</name></param>
        </command>
         */
    static PFNGLDELETESAMPLERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETESAMPLERSPROC ) mygetprocaddr("glDeleteSamplers");
    glfunc(count_, samplers_);
    return;
}
void glDeleteShader (GLuint shader_ ){
    /* <command>
            <proto>void <name>glDeleteShader</name></proto>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
            <glx opcode="195" type="single" />
        </command>
         */
    static PFNGLDELETESHADERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETESHADERPROC ) mygetprocaddr("glDeleteShader");
    glfunc(shader_);
    return;
}
void glDeleteSync (GLsync sync_ ){
    /* <command>
            <proto>void <name>glDeleteSync</name></proto>
            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
        </command>
         */
    static PFNGLDELETESYNCPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETESYNCPROC ) mygetprocaddr("glDeleteSync");
    glfunc(sync_);
    return;
}
void glDeleteTextures (GLsizei n_ , const GLuint * textures_ ){
    /* <command>
            <proto>void <name>glDeleteTextures</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param group="Texture" len="n">const <ptype>GLuint</ptype> *<name>textures</name></param>
            <glx opcode="144" type="single" />
        </command>
         */
    static PFNGLDELETETEXTURESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETETEXTURESPROC ) mygetprocaddr("glDeleteTextures");
    glfunc(n_, textures_);
    return;
}
void glDeleteTransformFeedbacks (GLsizei n_ , const GLuint * ids_ ){
    /* <command>
            <proto>void <name>glDeleteTransformFeedbacks</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n">const <ptype>GLuint</ptype> *<name>ids</name></param>
        </command>
         */
    static PFNGLDELETETRANSFORMFEEDBACKSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETETRANSFORMFEEDBACKSPROC ) mygetprocaddr("glDeleteTransformFeedbacks");
    glfunc(n_, ids_);
    return;
}
void glDeleteVertexArrays (GLsizei n_ , const GLuint * arrays_ ){
    /* <command>
            <proto>void <name>glDeleteVertexArrays</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n">const <ptype>GLuint</ptype> *<name>arrays</name></param>
            <glx opcode="351" type="render" />
        </command>
         */
    static PFNGLDELETEVERTEXARRAYSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDELETEVERTEXARRAYSPROC ) mygetprocaddr("glDeleteVertexArrays");
    glfunc(n_, arrays_);
    return;
}
void glDepthFunc (GLenum func_ ){
    /* <command>
            <proto>void <name>glDepthFunc</name></proto>
            <param group="DepthFunction"><ptype>GLenum</ptype> <name>func</name></param>
            <glx opcode="164" type="render" />
        </command>
         */
    static PFNGLDEPTHFUNCPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEPTHFUNCPROC ) mygetprocaddr("glDepthFunc");
    glfunc(func_);
    return;
}
void glDepthMask (GLboolean flag_ ){
    /* <command>
            <proto>void <name>glDepthMask</name></proto>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>flag</name></param>
            <glx opcode="135" type="render" />
        </command>
         */
    static PFNGLDEPTHMASKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEPTHMASKPROC ) mygetprocaddr("glDepthMask");
    glfunc(flag_);
    return;
}
void glDepthRange (GLdouble near_ , GLdouble far_ ){
    /* <command>
            <proto>void <name>glDepthRange</name></proto>
            <param><ptype>GLdouble</ptype> <name>near</name></param>
            <param><ptype>GLdouble</ptype> <name>far</name></param>
            <glx opcode="174" type="render" />
        </command>
         */
    static PFNGLDEPTHRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEPTHRANGEPROC ) mygetprocaddr("glDepthRange");
    glfunc(near_, far_);
    return;
}
void glDepthRangeArrayv (GLuint first_ , GLsizei count_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glDepthRangeArrayv</name></proto>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="COMPSIZE(count)">const <ptype>GLdouble</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLDEPTHRANGEARRAYVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEPTHRANGEARRAYVPROC ) mygetprocaddr("glDepthRangeArrayv");
    glfunc(first_, count_, v_);
    return;
}
void glDepthRangeIndexed (GLuint index_ , GLdouble n_ , GLdouble f_ ){
    /* <command>
            <proto>void <name>glDepthRangeIndexed</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>n</name></param>
            <param><ptype>GLdouble</ptype> <name>f</name></param>
        </command>
         */
    static PFNGLDEPTHRANGEINDEXEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEPTHRANGEINDEXEDPROC ) mygetprocaddr("glDepthRangeIndexed");
    glfunc(index_, n_, f_);
    return;
}
void glDepthRangef (GLfloat n_ , GLfloat f_ ){
    /* <command>
            <proto>void <name>glDepthRangef</name></proto>
            <param><ptype>GLfloat</ptype> <name>n</name></param>
            <param><ptype>GLfloat</ptype> <name>f</name></param>
        </command>
         */
    static PFNGLDEPTHRANGEFPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDEPTHRANGEFPROC ) mygetprocaddr("glDepthRangef");
    glfunc(n_, f_);
    return;
}
void glDetachShader (GLuint program_ , GLuint shader_ ){
    /* <command>
            <proto>void <name>glDetachShader</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
        </command>
         */
    static PFNGLDETACHSHADERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDETACHSHADERPROC ) mygetprocaddr("glDetachShader");
    glfunc(program_, shader_);
    return;
}
void glDisable (GLenum cap_ ){
    /* <command>
            <proto>void <name>glDisable</name></proto>
            <param group="EnableCap"><ptype>GLenum</ptype> <name>cap</name></param>
            <glx opcode="138" type="render" />
        </command>
         */
    static PFNGLDISABLEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDISABLEPROC ) mygetprocaddr("glDisable");
    glfunc(cap_);
    return;
}
void glDisableVertexArrayAttrib (GLuint vaobj_ , GLuint index_ ){
    /* <command>
            <proto>void <name>glDisableVertexArrayAttrib</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLDISABLEVERTEXARRAYATTRIBPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDISABLEVERTEXARRAYATTRIBPROC ) mygetprocaddr("glDisableVertexArrayAttrib");
    glfunc(vaobj_, index_);
    return;
}
void glDisableVertexAttribArray (GLuint index_ ){
    /* <command>
            <proto>void <name>glDisableVertexAttribArray</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLDISABLEVERTEXATTRIBARRAYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDISABLEVERTEXATTRIBARRAYPROC ) mygetprocaddr("glDisableVertexAttribArray");
    glfunc(index_);
    return;
}
void glDisablei (GLenum target_ , GLuint index_ ){
    /* <command>
            <proto>void <name>glDisablei</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLDISABLEIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDISABLEIPROC ) mygetprocaddr("glDisablei");
    glfunc(target_, index_);
    return;
}
void glDispatchCompute (GLuint num_groups_x_ , GLuint num_groups_y_ , GLuint num_groups_z_ ){
    /* <command>
            <proto>void <name>glDispatchCompute</name></proto>
            <param><ptype>GLuint</ptype> <name>num_groups_x</name></param>
            <param><ptype>GLuint</ptype> <name>num_groups_y</name></param>
            <param><ptype>GLuint</ptype> <name>num_groups_z</name></param>
        </command>
         */
    static PFNGLDISPATCHCOMPUTEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDISPATCHCOMPUTEPROC ) mygetprocaddr("glDispatchCompute");
    glfunc(num_groups_x_, num_groups_y_, num_groups_z_);
    return;
}
void glDispatchComputeIndirect (GLintptr indirect_ ){
    /* <command>
            <proto>void <name>glDispatchComputeIndirect</name></proto>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>indirect</name></param>
        </command>
         */
    static PFNGLDISPATCHCOMPUTEINDIRECTPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDISPATCHCOMPUTEINDIRECTPROC ) mygetprocaddr("glDispatchComputeIndirect");
    glfunc(indirect_);
    return;
}
void glDrawArrays (GLenum mode_ , GLint first_ , GLsizei count_ ){
    /* <command>
            <proto>void <name>glDrawArrays</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <glx opcode="193" type="render" />
        </command>
         */
    static PFNGLDRAWARRAYSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWARRAYSPROC ) mygetprocaddr("glDrawArrays");
    glfunc(mode_, first_, count_);
    return;
}
void glDrawArraysIndirect (GLenum mode_ , const void * indirect_ ){
    /* <command>
            <proto>void <name>glDrawArraysIndirect</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param>const void *<name>indirect</name></param>
        </command>
         */
    static PFNGLDRAWARRAYSINDIRECTPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWARRAYSINDIRECTPROC ) mygetprocaddr("glDrawArraysIndirect");
    glfunc(mode_, indirect_);
    return;
}
void glDrawArraysInstanced (GLenum mode_ , GLint first_ , GLsizei count_ , GLsizei instancecount_ ){
    /* <command>
            <proto>void <name>glDrawArraysInstanced</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
        </command>
         */
    static PFNGLDRAWARRAYSINSTANCEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWARRAYSINSTANCEDPROC ) mygetprocaddr("glDrawArraysInstanced");
    glfunc(mode_, first_, count_, instancecount_);
    return;
}
void glDrawArraysInstancedBaseInstance (GLenum mode_ , GLint first_ , GLsizei count_ , GLsizei instancecount_ , GLuint baseinstance_ ){
    /* <command>
            <proto>void <name>glDrawArraysInstancedBaseInstance</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
            <param><ptype>GLuint</ptype> <name>baseinstance</name></param>
        </command>
         */
    static PFNGLDRAWARRAYSINSTANCEDBASEINSTANCEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWARRAYSINSTANCEDBASEINSTANCEPROC ) mygetprocaddr("glDrawArraysInstancedBaseInstance");
    glfunc(mode_, first_, count_, instancecount_, baseinstance_);
    return;
}
void glDrawBuffer (GLenum buf_ ){
    /* <command>
            <proto>void <name>glDrawBuffer</name></proto>
            <param group="DrawBufferMode"><ptype>GLenum</ptype> <name>buf</name></param>
            <glx opcode="126" type="render" />
        </command>
         */
    static PFNGLDRAWBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWBUFFERPROC ) mygetprocaddr("glDrawBuffer");
    glfunc(buf_);
    return;
}
void glDrawBuffers (GLsizei n_ , const GLenum * bufs_ ){
    /* <command>
            <proto>void <name>glDrawBuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param group="DrawBufferModeATI" len="n">const <ptype>GLenum</ptype> *<name>bufs</name></param>
            <glx opcode="233" type="render" />
        </command>
         */
    static PFNGLDRAWBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWBUFFERSPROC ) mygetprocaddr("glDrawBuffers");
    glfunc(n_, bufs_);
    return;
}
void glDrawElements (GLenum mode_ , GLsizei count_ , GLenum type_ , const void * indices_ ){
    /* <command>
            <proto>void <name>glDrawElements</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
        </command>
         */
    static PFNGLDRAWELEMENTSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWELEMENTSPROC ) mygetprocaddr("glDrawElements");
    glfunc(mode_, count_, type_, indices_);
    return;
}
void glDrawElementsBaseVertex (GLenum mode_ , GLsizei count_ , GLenum type_ , const void * indices_ , GLint basevertex_ ){
    /* <command>
            <proto>void <name>glDrawElementsBaseVertex</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
            <param><ptype>GLint</ptype> <name>basevertex</name></param>
        </command>
         */
    static PFNGLDRAWELEMENTSBASEVERTEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWELEMENTSBASEVERTEXPROC ) mygetprocaddr("glDrawElementsBaseVertex");
    glfunc(mode_, count_, type_, indices_, basevertex_);
    return;
}
void glDrawElementsIndirect (GLenum mode_ , GLenum type_ , const void * indirect_ ){
    /* <command>
            <proto>void <name>glDrawElementsIndirect</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param>const void *<name>indirect</name></param>
        </command>
         */
    static PFNGLDRAWELEMENTSINDIRECTPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWELEMENTSINDIRECTPROC ) mygetprocaddr("glDrawElementsIndirect");
    glfunc(mode_, type_, indirect_);
    return;
}
void glDrawElementsInstanced (GLenum mode_ , GLsizei count_ , GLenum type_ , const void * indices_ , GLsizei instancecount_ ){
    /* <command>
            <proto>void <name>glDrawElementsInstanced</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
        </command>
         */
    static PFNGLDRAWELEMENTSINSTANCEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWELEMENTSINSTANCEDPROC ) mygetprocaddr("glDrawElementsInstanced");
    glfunc(mode_, count_, type_, indices_, instancecount_);
    return;
}
void glDrawElementsInstancedBaseInstance (GLenum mode_ , GLsizei count_ , GLenum type_ , const void * indices_ , GLsizei instancecount_ , GLuint baseinstance_ ){
    /* <command>
            <proto>void <name>glDrawElementsInstancedBaseInstance</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param len="count">const void *<name>indices</name></param>
            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
            <param><ptype>GLuint</ptype> <name>baseinstance</name></param>
        </command>
         */
    static PFNGLDRAWELEMENTSINSTANCEDBASEINSTANCEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWELEMENTSINSTANCEDBASEINSTANCEPROC ) mygetprocaddr("glDrawElementsInstancedBaseInstance");
    glfunc(mode_, count_, type_, indices_, instancecount_, baseinstance_);
    return;
}
void glDrawElementsInstancedBaseVertex (GLenum mode_ , GLsizei count_ , GLenum type_ , const void * indices_ , GLsizei instancecount_ , GLint basevertex_ ){
    /* <command>
            <proto>void <name>glDrawElementsInstancedBaseVertex</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
            <param><ptype>GLint</ptype> <name>basevertex</name></param>
        </command>
         */
    static PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXPROC ) mygetprocaddr("glDrawElementsInstancedBaseVertex");
    glfunc(mode_, count_, type_, indices_, instancecount_, basevertex_);
    return;
}
void glDrawElementsInstancedBaseVertexBaseInstance (GLenum mode_ , GLsizei count_ , GLenum type_ , const void * indices_ , GLsizei instancecount_ , GLint basevertex_ , GLuint baseinstance_ ){
    /* <command>
            <proto>void <name>glDrawElementsInstancedBaseVertexBaseInstance</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param len="count">const void *<name>indices</name></param>
            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
            <param><ptype>GLint</ptype> <name>basevertex</name></param>
            <param><ptype>GLuint</ptype> <name>baseinstance</name></param>
        </command>
         */
    static PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXBASEINSTANCEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXBASEINSTANCEPROC ) mygetprocaddr("glDrawElementsInstancedBaseVertexBaseInstance");
    glfunc(mode_, count_, type_, indices_, instancecount_, basevertex_, baseinstance_);
    return;
}
void glDrawRangeElements (GLenum mode_ , GLuint start_ , GLuint end_ , GLsizei count_ , GLenum type_ , const void * indices_ ){
    /* <command>
            <proto>void <name>glDrawRangeElements</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLuint</ptype> <name>start</name></param>
            <param><ptype>GLuint</ptype> <name>end</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
        </command>
         */
    static PFNGLDRAWRANGEELEMENTSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWRANGEELEMENTSPROC ) mygetprocaddr("glDrawRangeElements");
    glfunc(mode_, start_, end_, count_, type_, indices_);
    return;
}
void glDrawRangeElementsBaseVertex (GLenum mode_ , GLuint start_ , GLuint end_ , GLsizei count_ , GLenum type_ , const void * indices_ , GLint basevertex_ ){
    /* <command>
            <proto>void <name>glDrawRangeElementsBaseVertex</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLuint</ptype> <name>start</name></param>
            <param><ptype>GLuint</ptype> <name>end</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(count,type)">const void *<name>indices</name></param>
            <param><ptype>GLint</ptype> <name>basevertex</name></param>
        </command>
         */
    static PFNGLDRAWRANGEELEMENTSBASEVERTEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWRANGEELEMENTSBASEVERTEXPROC ) mygetprocaddr("glDrawRangeElementsBaseVertex");
    glfunc(mode_, start_, end_, count_, type_, indices_, basevertex_);
    return;
}
void glDrawTransformFeedback (GLenum mode_ , GLuint id_ ){
    /* <command>
            <proto>void <name>glDrawTransformFeedback</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
        </command>
         */
    static PFNGLDRAWTRANSFORMFEEDBACKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWTRANSFORMFEEDBACKPROC ) mygetprocaddr("glDrawTransformFeedback");
    glfunc(mode_, id_);
    return;
}
void glDrawTransformFeedbackInstanced (GLenum mode_ , GLuint id_ , GLsizei instancecount_ ){
    /* <command>
            <proto>void <name>glDrawTransformFeedbackInstanced</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
        </command>
         */
    static PFNGLDRAWTRANSFORMFEEDBACKINSTANCEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWTRANSFORMFEEDBACKINSTANCEDPROC ) mygetprocaddr("glDrawTransformFeedbackInstanced");
    glfunc(mode_, id_, instancecount_);
    return;
}
void glDrawTransformFeedbackStream (GLenum mode_ , GLuint id_ , GLuint stream_ ){
    /* <command>
            <proto>void <name>glDrawTransformFeedbackStream</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLuint</ptype> <name>stream</name></param>
        </command>
         */
    static PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROC ) mygetprocaddr("glDrawTransformFeedbackStream");
    glfunc(mode_, id_, stream_);
    return;
}
void glDrawTransformFeedbackStreamInstanced (GLenum mode_ , GLuint id_ , GLuint stream_ , GLsizei instancecount_ ){
    /* <command>
            <proto>void <name>glDrawTransformFeedbackStreamInstanced</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLuint</ptype> <name>stream</name></param>
            <param><ptype>GLsizei</ptype> <name>instancecount</name></param>
        </command>
         */
    static PFNGLDRAWTRANSFORMFEEDBACKSTREAMINSTANCEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLDRAWTRANSFORMFEEDBACKSTREAMINSTANCEDPROC ) mygetprocaddr("glDrawTransformFeedbackStreamInstanced");
    glfunc(mode_, id_, stream_, instancecount_);
    return;
}
void glEnable (GLenum cap_ ){
    /* <command>
            <proto>void <name>glEnable</name></proto>
            <param group="EnableCap"><ptype>GLenum</ptype> <name>cap</name></param>
            <glx opcode="139" type="render" />
        </command>
         */
    static PFNGLENABLEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLENABLEPROC ) mygetprocaddr("glEnable");
    glfunc(cap_);
    return;
}
void glEnableVertexArrayAttrib (GLuint vaobj_ , GLuint index_ ){
    /* <command>
            <proto>void <name>glEnableVertexArrayAttrib</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLENABLEVERTEXARRAYATTRIBPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLENABLEVERTEXARRAYATTRIBPROC ) mygetprocaddr("glEnableVertexArrayAttrib");
    glfunc(vaobj_, index_);
    return;
}
void glEnableVertexAttribArray (GLuint index_ ){
    /* <command>
            <proto>void <name>glEnableVertexAttribArray</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLENABLEVERTEXATTRIBARRAYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLENABLEVERTEXATTRIBARRAYPROC ) mygetprocaddr("glEnableVertexAttribArray");
    glfunc(index_);
    return;
}
void glEnablei (GLenum target_ , GLuint index_ ){
    /* <command>
            <proto>void <name>glEnablei</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLENABLEIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLENABLEIPROC ) mygetprocaddr("glEnablei");
    glfunc(target_, index_);
    return;
}
void glEndConditionalRender (){
    /* <command>
            <proto>void <name>glEndConditionalRender</name></proto>
            <glx opcode="349" type="render" />
        </command>
         */
    static PFNGLENDCONDITIONALRENDERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLENDCONDITIONALRENDERPROC ) mygetprocaddr("glEndConditionalRender");
    glfunc();
    return;
}
void glEndQuery (GLenum target_ ){
    /* <command>
            <proto>void <name>glEndQuery</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <glx opcode="232" type="render" />
        </command>
         */
    static PFNGLENDQUERYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLENDQUERYPROC ) mygetprocaddr("glEndQuery");
    glfunc(target_);
    return;
}
void glEndQueryIndexed (GLenum target_ , GLuint index_ ){
    /* <command>
            <proto>void <name>glEndQueryIndexed</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLENDQUERYINDEXEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLENDQUERYINDEXEDPROC ) mygetprocaddr("glEndQueryIndexed");
    glfunc(target_, index_);
    return;
}
void glEndTransformFeedback (){
    /* <command>
            <proto>void <name>glEndTransformFeedback</name></proto>
        </command>
         */
    static PFNGLENDTRANSFORMFEEDBACKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLENDTRANSFORMFEEDBACKPROC ) mygetprocaddr("glEndTransformFeedback");
    glfunc();
    return;
}
GLsync glFenceSync (GLenum condition_ , GLbitfield flags_ ){
    /* <command>
            <proto group="sync"><ptype>GLsync</ptype> <name>glFenceSync</name></proto>
            <param><ptype>GLenum</ptype> <name>condition</name></param>
            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
        </command>
         */
    static PFNGLFENCESYNCPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFENCESYNCPROC ) mygetprocaddr("glFenceSync");
    GLsync retval = glfunc(condition_, flags_);
    return retval;
}
void glFinish (){
    /* <command>
            <proto>void <name>glFinish</name></proto>
            <glx opcode="108" type="single" />
        </command>
         */
    static PFNGLFINISHPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFINISHPROC ) mygetprocaddr("glFinish");
    glfunc();
    return;
}
void glFlush (){
    /* <command>
            <proto>void <name>glFlush</name></proto>
            <glx opcode="142" type="single" />
        </command>
         */
    static PFNGLFLUSHPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFLUSHPROC ) mygetprocaddr("glFlush");
    glfunc();
    return;
}
void glFlushMappedBufferRange (GLenum target_ , GLintptr offset_ , GLsizeiptr length_ ){
    /* <command>
            <proto>void <name>glFlushMappedBufferRange</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
        </command>
         */
    static PFNGLFLUSHMAPPEDBUFFERRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFLUSHMAPPEDBUFFERRANGEPROC ) mygetprocaddr("glFlushMappedBufferRange");
    glfunc(target_, offset_, length_);
    return;
}
void glFlushMappedNamedBufferRange (GLuint buffer_ , GLintptr offset_ , GLsizeiptr length_ ){
    /* <command>
            <proto>void <name>glFlushMappedNamedBufferRange</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
        </command>
         */
    static PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEPROC ) mygetprocaddr("glFlushMappedNamedBufferRange");
    glfunc(buffer_, offset_, length_);
    return;
}
void glFramebufferParameteri (GLenum target_ , GLenum pname_ , GLint param_ ){
    /* <command>
            <proto>void <name>glFramebufferParameteri</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> <name>param</name></param>
        </command>
         */
    static PFNGLFRAMEBUFFERPARAMETERIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFRAMEBUFFERPARAMETERIPROC ) mygetprocaddr("glFramebufferParameteri");
    glfunc(target_, pname_, param_);
    return;
}
void glFramebufferRenderbuffer (GLenum target_ , GLenum attachment_ , GLenum renderbuffertarget_ , GLuint renderbuffer_ ){
    /* <command>
            <proto>void <name>glFramebufferRenderbuffer</name></proto>
            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
            <param group="RenderbufferTarget"><ptype>GLenum</ptype> <name>renderbuffertarget</name></param>
            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
            <glx opcode="4324" type="render" />
        </command>
         */
    static PFNGLFRAMEBUFFERRENDERBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFRAMEBUFFERRENDERBUFFERPROC ) mygetprocaddr("glFramebufferRenderbuffer");
    glfunc(target_, attachment_, renderbuffertarget_, renderbuffer_);
    return;
}
void glFramebufferTexture (GLenum target_ , GLenum attachment_ , GLuint texture_ , GLint level_ ){
    /* <command>
            <proto>void <name>glFramebufferTexture</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
        </command>
         */
    static PFNGLFRAMEBUFFERTEXTUREPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFRAMEBUFFERTEXTUREPROC ) mygetprocaddr("glFramebufferTexture");
    glfunc(target_, attachment_, texture_, level_);
    return;
}
void glFramebufferTexture1D (GLenum target_ , GLenum attachment_ , GLenum textarget_ , GLuint texture_ , GLint level_ ){
    /* <command>
            <proto>void <name>glFramebufferTexture1D</name></proto>
            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLenum</ptype> <name>textarget</name></param>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <glx opcode="4321" type="render" />
        </command>
         */
    static PFNGLFRAMEBUFFERTEXTURE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFRAMEBUFFERTEXTURE1DPROC ) mygetprocaddr("glFramebufferTexture1D");
    glfunc(target_, attachment_, textarget_, texture_, level_);
    return;
}
void glFramebufferTexture2D (GLenum target_ , GLenum attachment_ , GLenum textarget_ , GLuint texture_ , GLint level_ ){
    /* <command>
            <proto>void <name>glFramebufferTexture2D</name></proto>
            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLenum</ptype> <name>textarget</name></param>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <glx opcode="4322" type="render" />
        </command>
         */
    static PFNGLFRAMEBUFFERTEXTURE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFRAMEBUFFERTEXTURE2DPROC ) mygetprocaddr("glFramebufferTexture2D");
    glfunc(target_, attachment_, textarget_, texture_, level_);
    return;
}
void glFramebufferTexture3D (GLenum target_ , GLenum attachment_ , GLenum textarget_ , GLuint texture_ , GLint level_ , GLint zoffset_ ){
    /* <command>
            <proto>void <name>glFramebufferTexture3D</name></proto>
            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLenum</ptype> <name>textarget</name></param>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>zoffset</name></param>
            <glx opcode="4323" type="render" />
        </command>
         */
    static PFNGLFRAMEBUFFERTEXTURE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFRAMEBUFFERTEXTURE3DPROC ) mygetprocaddr("glFramebufferTexture3D");
    glfunc(target_, attachment_, textarget_, texture_, level_, zoffset_);
    return;
}
void glFramebufferTextureLayer (GLenum target_ , GLenum attachment_ , GLuint texture_ , GLint level_ , GLint layer_ ){
    /* <command>
            <proto>void <name>glFramebufferTextureLayer</name></proto>
            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
            <param group="Texture"><ptype>GLuint</ptype> <name>texture</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>layer</name></param>
            <glx opcode="237" type="render" />
        </command>
         */
    static PFNGLFRAMEBUFFERTEXTURELAYERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFRAMEBUFFERTEXTURELAYERPROC ) mygetprocaddr("glFramebufferTextureLayer");
    glfunc(target_, attachment_, texture_, level_, layer_);
    return;
}
void glFrontFace (GLenum mode_ ){
    /* <command>
            <proto>void <name>glFrontFace</name></proto>
            <param group="FrontFaceDirection"><ptype>GLenum</ptype> <name>mode</name></param>
            <glx opcode="84" type="render" />
        </command>
         */
    static PFNGLFRONTFACEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLFRONTFACEPROC ) mygetprocaddr("glFrontFace");
    glfunc(mode_);
    return;
}
void glGenBuffers (GLsizei n_ , GLuint * buffers_ ){
    /* <command>
            <proto>void <name>glGenBuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n"><ptype>GLuint</ptype> *<name>buffers</name></param>
        </command>
         */
    static PFNGLGENBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENBUFFERSPROC ) mygetprocaddr("glGenBuffers");
    glfunc(n_, buffers_);
    return;
}
void glGenFramebuffers (GLsizei n_ , GLuint * framebuffers_ ){
    /* <command>
            <proto>void <name>glGenFramebuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n"><ptype>GLuint</ptype> *<name>framebuffers</name></param>
            <glx opcode="1426" type="vendor" />
        </command>
         */
    static PFNGLGENFRAMEBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENFRAMEBUFFERSPROC ) mygetprocaddr("glGenFramebuffers");
    glfunc(n_, framebuffers_);
    return;
}
void glGenProgramPipelines (GLsizei n_ , GLuint * pipelines_ ){
    /* <command>
            <proto>void <name>glGenProgramPipelines</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n"><ptype>GLuint</ptype> *<name>pipelines</name></param>
        </command>
         */
    static PFNGLGENPROGRAMPIPELINESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENPROGRAMPIPELINESPROC ) mygetprocaddr("glGenProgramPipelines");
    glfunc(n_, pipelines_);
    return;
}
void glGenQueries (GLsizei n_ , GLuint * ids_ ){
    /* <command>
            <proto>void <name>glGenQueries</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n"><ptype>GLuint</ptype> *<name>ids</name></param>
            <glx opcode="162" type="single" />
        </command>
         */
    static PFNGLGENQUERIESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENQUERIESPROC ) mygetprocaddr("glGenQueries");
    glfunc(n_, ids_);
    return;
}
void glGenRenderbuffers (GLsizei n_ , GLuint * renderbuffers_ ){
    /* <command>
            <proto>void <name>glGenRenderbuffers</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n"><ptype>GLuint</ptype> *<name>renderbuffers</name></param>
            <glx opcode="1423" type="vendor" />
        </command>
         */
    static PFNGLGENRENDERBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENRENDERBUFFERSPROC ) mygetprocaddr("glGenRenderbuffers");
    glfunc(n_, renderbuffers_);
    return;
}
void glGenSamplers (GLsizei count_ , GLuint * samplers_ ){
    /* <command>
            <proto>void <name>glGenSamplers</name></proto>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count"><ptype>GLuint</ptype> *<name>samplers</name></param>
        </command>
         */
    static PFNGLGENSAMPLERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENSAMPLERSPROC ) mygetprocaddr("glGenSamplers");
    glfunc(count_, samplers_);
    return;
}
void glGenTextures (GLsizei n_ , GLuint * textures_ ){
    /* <command>
            <proto>void <name>glGenTextures</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param group="Texture" len="n"><ptype>GLuint</ptype> *<name>textures</name></param>
            <glx opcode="145" type="single" />
        </command>
         */
    static PFNGLGENTEXTURESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENTEXTURESPROC ) mygetprocaddr("glGenTextures");
    glfunc(n_, textures_);
    return;
}
void glGenTransformFeedbacks (GLsizei n_ , GLuint * ids_ ){
    /* <command>
            <proto>void <name>glGenTransformFeedbacks</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n"><ptype>GLuint</ptype> *<name>ids</name></param>
        </command>
         */
    static PFNGLGENTRANSFORMFEEDBACKSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENTRANSFORMFEEDBACKSPROC ) mygetprocaddr("glGenTransformFeedbacks");
    glfunc(n_, ids_);
    return;
}
void glGenVertexArrays (GLsizei n_ , GLuint * arrays_ ){
    /* <command>
            <proto>void <name>glGenVertexArrays</name></proto>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param len="n"><ptype>GLuint</ptype> *<name>arrays</name></param>
            <glx opcode="206" type="single" />
        </command>
         */
    static PFNGLGENVERTEXARRAYSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENVERTEXARRAYSPROC ) mygetprocaddr("glGenVertexArrays");
    glfunc(n_, arrays_);
    return;
}
void glGenerateMipmap (GLenum target_ ){
    /* <command>
            <proto>void <name>glGenerateMipmap</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <glx opcode="4325" type="render" />
        </command>
         */
    static PFNGLGENERATEMIPMAPPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENERATEMIPMAPPROC ) mygetprocaddr("glGenerateMipmap");
    glfunc(target_);
    return;
}
void glGenerateTextureMipmap (GLuint texture_ ){
    /* <command>
            <proto>void <name>glGenerateTextureMipmap</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
        </command>
         */
    static PFNGLGENERATETEXTUREMIPMAPPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGENERATETEXTUREMIPMAPPROC ) mygetprocaddr("glGenerateTextureMipmap");
    glfunc(texture_);
    return;
}
void glGetActiveAtomicCounterBufferiv (GLuint program_ , GLuint bufferIndex_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetActiveAtomicCounterBufferiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>bufferIndex</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETACTIVEATOMICCOUNTERBUFFERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVEATOMICCOUNTERBUFFERIVPROC ) mygetprocaddr("glGetActiveAtomicCounterBufferiv");
    glfunc(program_, bufferIndex_, pname_, params_);
    return;
}
void glGetActiveAttrib (GLuint program_ , GLuint index_ , GLsizei bufSize_ , GLsizei * length_ , GLint * size_ , GLenum * type_ , GLchar * name_ ){
    /* <command>
            <proto>void <name>glGetActiveAttrib</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="1"><ptype>GLint</ptype> *<name>size</name></param>
            <param len="1"><ptype>GLenum</ptype> *<name>type</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETACTIVEATTRIBPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVEATTRIBPROC ) mygetprocaddr("glGetActiveAttrib");
    glfunc(program_, index_, bufSize_, length_, size_, type_, name_);
    return;
}
void glGetActiveSubroutineName (GLuint program_ , GLenum shadertype_ , GLuint index_ , GLsizei bufsize_ , GLsizei * length_ , GLchar * name_ ){
    /* <command>
            <proto>void <name>glGetActiveSubroutineName</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLsizei</ptype> <name>bufsize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufsize"><ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETACTIVESUBROUTINENAMEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVESUBROUTINENAMEPROC ) mygetprocaddr("glGetActiveSubroutineName");
    glfunc(program_, shadertype_, index_, bufsize_, length_, name_);
    return;
}
void glGetActiveSubroutineUniformName (GLuint program_ , GLenum shadertype_ , GLuint index_ , GLsizei bufsize_ , GLsizei * length_ , GLchar * name_ ){
    /* <command>
            <proto>void <name>glGetActiveSubroutineUniformName</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLsizei</ptype> <name>bufsize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufsize"><ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROC ) mygetprocaddr("glGetActiveSubroutineUniformName");
    glfunc(program_, shadertype_, index_, bufsize_, length_, name_);
    return;
}
void glGetActiveSubroutineUniformiv (GLuint program_ , GLenum shadertype_ , GLuint index_ , GLenum pname_ , GLint * values_ ){
    /* <command>
            <proto>void <name>glGetActiveSubroutineUniformiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>values</name></param>
        </command>
         */
    static PFNGLGETACTIVESUBROUTINEUNIFORMIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVESUBROUTINEUNIFORMIVPROC ) mygetprocaddr("glGetActiveSubroutineUniformiv");
    glfunc(program_, shadertype_, index_, pname_, values_);
    return;
}
void glGetActiveUniform (GLuint program_ , GLuint index_ , GLsizei bufSize_ , GLsizei * length_ , GLint * size_ , GLenum * type_ , GLchar * name_ ){
    /* <command>
            <proto>void <name>glGetActiveUniform</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="1"><ptype>GLint</ptype> *<name>size</name></param>
            <param len="1"><ptype>GLenum</ptype> *<name>type</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETACTIVEUNIFORMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVEUNIFORMPROC ) mygetprocaddr("glGetActiveUniform");
    glfunc(program_, index_, bufSize_, length_, size_, type_, name_);
    return;
}
void glGetActiveUniformBlockName (GLuint program_ , GLuint uniformBlockIndex_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * uniformBlockName_ ){
    /* <command>
            <proto>void <name>glGetActiveUniformBlockName</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>uniformBlockIndex</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>uniformBlockName</name></param>
        </command>
         */
    static PFNGLGETACTIVEUNIFORMBLOCKNAMEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVEUNIFORMBLOCKNAMEPROC ) mygetprocaddr("glGetActiveUniformBlockName");
    glfunc(program_, uniformBlockIndex_, bufSize_, length_, uniformBlockName_);
    return;
}
void glGetActiveUniformBlockiv (GLuint program_ , GLuint uniformBlockIndex_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetActiveUniformBlockiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>uniformBlockIndex</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(program,uniformBlockIndex,pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETACTIVEUNIFORMBLOCKIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVEUNIFORMBLOCKIVPROC ) mygetprocaddr("glGetActiveUniformBlockiv");
    glfunc(program_, uniformBlockIndex_, pname_, params_);
    return;
}
void glGetActiveUniformName (GLuint program_ , GLuint uniformIndex_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * uniformName_ ){
    /* <command>
            <proto>void <name>glGetActiveUniformName</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>uniformIndex</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>uniformName</name></param>
        </command>
         */
    static PFNGLGETACTIVEUNIFORMNAMEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVEUNIFORMNAMEPROC ) mygetprocaddr("glGetActiveUniformName");
    glfunc(program_, uniformIndex_, bufSize_, length_, uniformName_);
    return;
}
void glGetActiveUniformsiv (GLuint program_ , GLsizei uniformCount_ , const GLuint * uniformIndices_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetActiveUniformsiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLsizei</ptype> <name>uniformCount</name></param>
            <param len="uniformCount">const <ptype>GLuint</ptype> *<name>uniformIndices</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(uniformCount,pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETACTIVEUNIFORMSIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETACTIVEUNIFORMSIVPROC ) mygetprocaddr("glGetActiveUniformsiv");
    glfunc(program_, uniformCount_, uniformIndices_, pname_, params_);
    return;
}
void glGetAttachedShaders (GLuint program_ , GLsizei maxCount_ , GLsizei * count_ , GLuint * shaders_ ){
    /* <command>
            <proto>void <name>glGetAttachedShaders</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLsizei</ptype> <name>maxCount</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>count</name></param>
            <param len="maxCount"><ptype>GLuint</ptype> *<name>shaders</name></param>
        </command>
         */
    static PFNGLGETATTACHEDSHADERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETATTACHEDSHADERSPROC ) mygetprocaddr("glGetAttachedShaders");
    glfunc(program_, maxCount_, count_, shaders_);
    return;
}
GLint glGetAttribLocation (GLuint program_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLint</ptype> <name>glGetAttribLocation</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETATTRIBLOCATIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETATTRIBLOCATIONPROC ) mygetprocaddr("glGetAttribLocation");
    GLint retval = glfunc(program_, name_);
    return retval;
}
void glGetBooleani_v (GLenum target_ , GLuint index_ , GLboolean * data_ ){
    /* <command>
            <proto>void <name>glGetBooleani_v</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param group="Boolean" len="COMPSIZE(target)"><ptype>GLboolean</ptype> *<name>data</name></param>
        </command>
         */
    static PFNGLGETBOOLEANI_VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETBOOLEANI_VPROC ) mygetprocaddr("glGetBooleani_v");
    glfunc(target_, index_, data_);
    return;
}
void glGetBooleanv (GLenum pname_ , GLboolean * data_ ){
    /* <command>
            <proto>void <name>glGetBooleanv</name></proto>
            <param group="GetPName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="Boolean" len="COMPSIZE(pname)"><ptype>GLboolean</ptype> *<name>data</name></param>
            <glx opcode="112" type="single" />
        </command>
         */
    static PFNGLGETBOOLEANVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETBOOLEANVPROC ) mygetprocaddr("glGetBooleanv");
    glfunc(pname_, data_);
    return;
}
void glGetBufferParameteri64v (GLenum target_ , GLenum pname_ , GLint64 * params_ ){
    /* <command>
            <proto>void <name>glGetBufferParameteri64v</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferPNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint64</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETBUFFERPARAMETERI64VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETBUFFERPARAMETERI64VPROC ) mygetprocaddr("glGetBufferParameteri64v");
    glfunc(target_, pname_, params_);
    return;
}
void glGetBufferParameteriv (GLenum target_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetBufferParameteriv</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferPNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETBUFFERPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETBUFFERPARAMETERIVPROC ) mygetprocaddr("glGetBufferParameteriv");
    glfunc(target_, pname_, params_);
    return;
}
void glGetBufferPointerv (GLenum target_ , GLenum pname_ , void ** params_ ){
    /* <command>
            <proto>void <name>glGetBufferPointerv</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferPointerNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="1">void **<name>params</name></param>
        </command>
         */
    static PFNGLGETBUFFERPOINTERVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETBUFFERPOINTERVPROC ) mygetprocaddr("glGetBufferPointerv");
    glfunc(target_, pname_, params_);
    return;
}
void glGetBufferSubData (GLenum target_ , GLintptr offset_ , GLsizeiptr size_ , void * data_ ){
    /* <command>
            <proto>void <name>glGetBufferSubData</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param len="size">void *<name>data</name></param>
        </command>
         */
    static PFNGLGETBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETBUFFERSUBDATAPROC ) mygetprocaddr("glGetBufferSubData");
    glfunc(target_, offset_, size_, data_);
    return;
}
void glGetCompressedTexImage (GLenum target_ , GLint level_ , void * img_ ){
    /* <command>
            <proto>void <name>glGetCompressedTexImage</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CompressedTextureARB" len="COMPSIZE(target,level)">void *<name>img</name></param>
            <glx opcode="160" type="single" />
            <glx comment="PBO protocol" name="glGetCompressedTexImagePBO" opcode="335" type="render" />
        </command>
         */
    static PFNGLGETCOMPRESSEDTEXIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETCOMPRESSEDTEXIMAGEPROC ) mygetprocaddr("glGetCompressedTexImage");
    glfunc(target_, level_, img_);
    return;
}
void glGetCompressedTextureImage (GLuint texture_ , GLint level_ , GLsizei bufSize_ , void * pixels_ ){
    /* <command>
            <proto>void <name>glGetCompressedTextureImage</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param>void *<name>pixels</name></param>
        </command>
         */
    static PFNGLGETCOMPRESSEDTEXTUREIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETCOMPRESSEDTEXTUREIMAGEPROC ) mygetprocaddr("glGetCompressedTextureImage");
    glfunc(texture_, level_, bufSize_, pixels_);
    return;
}
void glGetCompressedTextureSubImage (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLsizei bufSize_ , void * pixels_ ){
    /* <command>
            <proto>void <name>glGetCompressedTextureSubImage</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param>void *<name>pixels</name></param>
        </command>
         */
    static PFNGLGETCOMPRESSEDTEXTURESUBIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETCOMPRESSEDTEXTURESUBIMAGEPROC ) mygetprocaddr("glGetCompressedTextureSubImage");
    glfunc(texture_, level_, xoffset_, yoffset_, zoffset_, width_, height_, depth_, bufSize_, pixels_);
    return;
}
GLuint glGetDebugMessageLog (GLuint count_ , GLsizei bufSize_ , GLenum * sources_ , GLenum * types_ , GLuint * ids_ , GLenum * severities_ , GLsizei * lengths_ , GLchar * messageLog_ ){
    /* <command>
            <proto><ptype>GLuint</ptype> <name>glGetDebugMessageLog</name></proto>
            <param><ptype>GLuint</ptype> <name>count</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="count"><ptype>GLenum</ptype> *<name>sources</name></param>
            <param len="count"><ptype>GLenum</ptype> *<name>types</name></param>
            <param len="count"><ptype>GLuint</ptype> *<name>ids</name></param>
            <param len="count"><ptype>GLenum</ptype> *<name>severities</name></param>
            <param len="count"><ptype>GLsizei</ptype> *<name>lengths</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>messageLog</name></param>
        </command>
         */
    static PFNGLGETDEBUGMESSAGELOGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETDEBUGMESSAGELOGPROC ) mygetprocaddr("glGetDebugMessageLog");
    GLuint retval = glfunc(count_, bufSize_, sources_, types_, ids_, severities_, lengths_, messageLog_);
    return retval;
}
void glGetDoublei_v (GLenum target_ , GLuint index_ , GLdouble * data_ ){
    /* <command>
            <proto>void <name>glGetDoublei_v</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="COMPSIZE(target)"><ptype>GLdouble</ptype> *<name>data</name></param>
        </command>
         */
    static PFNGLGETDOUBLEI_VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETDOUBLEI_VPROC ) mygetprocaddr("glGetDoublei_v");
    glfunc(target_, index_, data_);
    return;
}
void glGetDoublev (GLenum pname_ , GLdouble * data_ ){
    /* <command>
            <proto>void <name>glGetDoublev</name></proto>
            <param group="GetPName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLdouble</ptype> *<name>data</name></param>
            <glx opcode="114" type="single" />
        </command>
         */
    static PFNGLGETDOUBLEVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETDOUBLEVPROC ) mygetprocaddr("glGetDoublev");
    glfunc(pname_, data_);
    return;
}
GLenum glGetError (){
    /* <command>
            <proto group="ErrorCode"><ptype>GLenum</ptype> <name>glGetError</name></proto>
            <glx opcode="115" type="single" />
        </command>
         */
    static PFNGLGETERRORPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETERRORPROC ) mygetprocaddr("glGetError");
    GLenum retval = glfunc();
    return retval;
}
void glGetFloati_v (GLenum target_ , GLuint index_ , GLfloat * data_ ){
    /* <command>
            <proto>void <name>glGetFloati_v</name></proto>
            <param group="TypeEnum"><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="COMPSIZE(target)"><ptype>GLfloat</ptype> *<name>data</name></param>
        </command>
         */
    static PFNGLGETFLOATI_VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETFLOATI_VPROC ) mygetprocaddr("glGetFloati_v");
    glfunc(target_, index_, data_);
    return;
}
void glGetFloatv (GLenum pname_ , GLfloat * data_ ){
    /* <command>
            <proto>void <name>glGetFloatv</name></proto>
            <param group="GetPName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>data</name></param>
            <glx opcode="116" type="single" />
        </command>
         */
    static PFNGLGETFLOATVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETFLOATVPROC ) mygetprocaddr("glGetFloatv");
    glfunc(pname_, data_);
    return;
}
GLint glGetFragDataIndex (GLuint program_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLint</ptype> <name>glGetFragDataIndex</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETFRAGDATAINDEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETFRAGDATAINDEXPROC ) mygetprocaddr("glGetFragDataIndex");
    GLint retval = glfunc(program_, name_);
    return retval;
}
GLint glGetFragDataLocation (GLuint program_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLint</ptype> <name>glGetFragDataLocation</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETFRAGDATALOCATIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETFRAGDATALOCATIONPROC ) mygetprocaddr("glGetFragDataLocation");
    GLint retval = glfunc(program_, name_);
    return retval;
}
void glGetFramebufferAttachmentParameteriv (GLenum target_ , GLenum attachment_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetFramebufferAttachmentParameteriv</name></proto>
            <param group="FramebufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="FramebufferAttachment"><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="1428" type="vendor" />
        </command>
         */
    static PFNGLGETFRAMEBUFFERATTACHMENTPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETFRAMEBUFFERATTACHMENTPARAMETERIVPROC ) mygetprocaddr("glGetFramebufferAttachmentParameteriv");
    glfunc(target_, attachment_, pname_, params_);
    return;
}
void glGetFramebufferParameteriv (GLenum target_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetFramebufferParameteriv</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETFRAMEBUFFERPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETFRAMEBUFFERPARAMETERIVPROC ) mygetprocaddr("glGetFramebufferParameteriv");
    glfunc(target_, pname_, params_);
    return;
}
GLenum glGetGraphicsResetStatus (){
    /* <command>
            <proto><ptype>GLenum</ptype> <name>glGetGraphicsResetStatus</name></proto>
        </command>
         */
    static PFNGLGETGRAPHICSRESETSTATUSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETGRAPHICSRESETSTATUSPROC ) mygetprocaddr("glGetGraphicsResetStatus");
    GLenum retval = glfunc();
    return retval;
}
void glGetInteger64i_v (GLenum target_ , GLuint index_ , GLint64 * data_ ){
    /* <command>
            <proto>void <name>glGetInteger64i_v</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="COMPSIZE(target)"><ptype>GLint64</ptype> *<name>data</name></param>
        </command>
         */
    static PFNGLGETINTEGER64I_VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETINTEGER64I_VPROC ) mygetprocaddr("glGetInteger64i_v");
    glfunc(target_, index_, data_);
    return;
}
void glGetInteger64v (GLenum pname_ , GLint64 * data_ ){
    /* <command>
            <proto>void <name>glGetInteger64v</name></proto>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint64</ptype> *<name>data</name></param>
        </command>
         */
    static PFNGLGETINTEGER64VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETINTEGER64VPROC ) mygetprocaddr("glGetInteger64v");
    glfunc(pname_, data_);
    return;
}
void glGetIntegeri_v (GLenum target_ , GLuint index_ , GLint * data_ ){
    /* <command>
            <proto>void <name>glGetIntegeri_v</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="COMPSIZE(target)"><ptype>GLint</ptype> *<name>data</name></param>
        </command>
         */
    static PFNGLGETINTEGERI_VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETINTEGERI_VPROC ) mygetprocaddr("glGetIntegeri_v");
    glfunc(target_, index_, data_);
    return;
}
void glGetIntegerv (GLenum pname_ , GLint * data_ ){
    /* <command>
            <proto>void <name>glGetIntegerv</name></proto>
            <param group="GetPName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>data</name></param>
            <glx opcode="117" type="single" />
        </command>
         */
    static PFNGLGETINTEGERVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETINTEGERVPROC ) mygetprocaddr("glGetIntegerv");
    glfunc(pname_, data_);
    return;
}
void glGetInternalformati64v (GLenum target_ , GLenum internalformat_ , GLenum pname_ , GLsizei bufSize_ , GLint64 * params_ ){
    /* <command>
            <proto>void <name>glGetInternalformati64v</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="bufSize"><ptype>GLint64</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETINTERNALFORMATI64VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETINTERNALFORMATI64VPROC ) mygetprocaddr("glGetInternalformati64v");
    glfunc(target_, internalformat_, pname_, bufSize_, params_);
    return;
}
void glGetInternalformativ (GLenum target_ , GLenum internalformat_ , GLenum pname_ , GLsizei bufSize_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetInternalformativ</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="bufSize"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETINTERNALFORMATIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETINTERNALFORMATIVPROC ) mygetprocaddr("glGetInternalformativ");
    glfunc(target_, internalformat_, pname_, bufSize_, params_);
    return;
}
void glGetMultisamplefv (GLenum pname_ , GLuint index_ , GLfloat * val_ ){
    /* <command>
            <proto>void <name>glGetMultisamplefv</name></proto>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>val</name></param>
        </command>
         */
    static PFNGLGETMULTISAMPLEFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETMULTISAMPLEFVPROC ) mygetprocaddr("glGetMultisamplefv");
    glfunc(pname_, index_, val_);
    return;
}
void glGetNamedBufferParameteri64v (GLuint buffer_ , GLenum pname_ , GLint64 * params_ ){
    /* <command>
            <proto>void <name>glGetNamedBufferParameteri64v</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint64</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETNAMEDBUFFERPARAMETERI64VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNAMEDBUFFERPARAMETERI64VPROC ) mygetprocaddr("glGetNamedBufferParameteri64v");
    glfunc(buffer_, pname_, params_);
    return;
}
void glGetNamedBufferParameteriv (GLuint buffer_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetNamedBufferParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETNAMEDBUFFERPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNAMEDBUFFERPARAMETERIVPROC ) mygetprocaddr("glGetNamedBufferParameteriv");
    glfunc(buffer_, pname_, params_);
    return;
}
void glGetNamedBufferPointerv (GLuint buffer_ , GLenum pname_ , void ** params_ ){
    /* <command>
            <proto>void <name>glGetNamedBufferPointerv</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param>void **<name>params</name></param>
        </command>
         */
    static PFNGLGETNAMEDBUFFERPOINTERVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNAMEDBUFFERPOINTERVPROC ) mygetprocaddr("glGetNamedBufferPointerv");
    glfunc(buffer_, pname_, params_);
    return;
}
void glGetNamedBufferSubData (GLuint buffer_ , GLintptr offset_ , GLsizeiptr size_ , void * data_ ){
    /* <command>
            <proto>void <name>glGetNamedBufferSubData</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param>void *<name>data</name></param>
        </command>
         */
    static PFNGLGETNAMEDBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNAMEDBUFFERSUBDATAPROC ) mygetprocaddr("glGetNamedBufferSubData");
    glfunc(buffer_, offset_, size_, data_);
    return;
}
void glGetNamedFramebufferAttachmentParameteriv (GLuint framebuffer_ , GLenum attachment_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetNamedFramebufferAttachmentParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVPROC ) mygetprocaddr("glGetNamedFramebufferAttachmentParameteriv");
    glfunc(framebuffer_, attachment_, pname_, params_);
    return;
}
void glGetNamedFramebufferParameteriv (GLuint framebuffer_ , GLenum pname_ , GLint * param_ ){
    /* <command>
            <proto>void <name>glGetNamedFramebufferParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVPROC ) mygetprocaddr("glGetNamedFramebufferParameteriv");
    glfunc(framebuffer_, pname_, param_);
    return;
}
void glGetNamedRenderbufferParameteriv (GLuint renderbuffer_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetNamedRenderbufferParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETNAMEDRENDERBUFFERPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNAMEDRENDERBUFFERPARAMETERIVPROC ) mygetprocaddr("glGetNamedRenderbufferParameteriv");
    glfunc(renderbuffer_, pname_, params_);
    return;
}
void glGetObjectLabel (GLenum identifier_ , GLuint name_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * label_ ){
    /* <command>
            <proto>void <name>glGetObjectLabel</name></proto>
            <param><ptype>GLenum</ptype> <name>identifier</name></param>
            <param><ptype>GLuint</ptype> <name>name</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>label</name></param>
        </command>
         */
    static PFNGLGETOBJECTLABELPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETOBJECTLABELPROC ) mygetprocaddr("glGetObjectLabel");
    glfunc(identifier_, name_, bufSize_, length_, label_);
    return;
}
void glGetObjectPtrLabel (const void * ptr_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * label_ ){
    /* <command>
            <proto>void <name>glGetObjectPtrLabel</name></proto>
            <param>const void *<name>ptr</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>label</name></param>
        </command>
         */
    static PFNGLGETOBJECTPTRLABELPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETOBJECTPTRLABELPROC ) mygetprocaddr("glGetObjectPtrLabel");
    glfunc(ptr_, bufSize_, length_, label_);
    return;
}
void glGetProgramBinary (GLuint program_ , GLsizei bufSize_ , GLsizei * length_ , GLenum * binaryFormat_ , void * binary_ ){
    /* <command>
            <proto>void <name>glGetProgramBinary</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="1"><ptype>GLenum</ptype> *<name>binaryFormat</name></param>
            <param len="bufSize">void *<name>binary</name></param>
        </command>
         */
    static PFNGLGETPROGRAMBINARYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMBINARYPROC ) mygetprocaddr("glGetProgramBinary");
    glfunc(program_, bufSize_, length_, binaryFormat_, binary_);
    return;
}
void glGetProgramInfoLog (GLuint program_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * infoLog_ ){
    /* <command>
            <proto>void <name>glGetProgramInfoLog</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>infoLog</name></param>
            <glx opcode="201" type="single" />
        </command>
         */
    static PFNGLGETPROGRAMINFOLOGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMINFOLOGPROC ) mygetprocaddr("glGetProgramInfoLog");
    glfunc(program_, bufSize_, length_, infoLog_);
    return;
}
void glGetProgramInterfaceiv (GLuint program_ , GLenum programInterface_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetProgramInterfaceiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETPROGRAMINTERFACEIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMINTERFACEIVPROC ) mygetprocaddr("glGetProgramInterfaceiv");
    glfunc(program_, programInterface_, pname_, params_);
    return;
}
void glGetProgramPipelineInfoLog (GLuint pipeline_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * infoLog_ ){
    /* <command>
            <proto>void <name>glGetProgramPipelineInfoLog</name></proto>
            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>infoLog</name></param>
        </command>
         */
    static PFNGLGETPROGRAMPIPELINEINFOLOGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMPIPELINEINFOLOGPROC ) mygetprocaddr("glGetProgramPipelineInfoLog");
    glfunc(pipeline_, bufSize_, length_, infoLog_);
    return;
}
void glGetProgramPipelineiv (GLuint pipeline_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetProgramPipelineiv</name></proto>
            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETPROGRAMPIPELINEIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMPIPELINEIVPROC ) mygetprocaddr("glGetProgramPipelineiv");
    glfunc(pipeline_, pname_, params_);
    return;
}
GLuint glGetProgramResourceIndex (GLuint program_ , GLenum programInterface_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLuint</ptype> <name>glGetProgramResourceIndex</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETPROGRAMRESOURCEINDEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMRESOURCEINDEXPROC ) mygetprocaddr("glGetProgramResourceIndex");
    GLuint retval = glfunc(program_, programInterface_, name_);
    return retval;
}
GLint glGetProgramResourceLocation (GLuint program_ , GLenum programInterface_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLint</ptype> <name>glGetProgramResourceLocation</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETPROGRAMRESOURCELOCATIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMRESOURCELOCATIONPROC ) mygetprocaddr("glGetProgramResourceLocation");
    GLint retval = glfunc(program_, programInterface_, name_);
    return retval;
}
GLint glGetProgramResourceLocationIndex (GLuint program_ , GLenum programInterface_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLint</ptype> <name>glGetProgramResourceLocationIndex</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
            <param len="COMPSIZE(name)">const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETPROGRAMRESOURCELOCATIONINDEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMRESOURCELOCATIONINDEXPROC ) mygetprocaddr("glGetProgramResourceLocationIndex");
    GLint retval = glfunc(program_, programInterface_, name_);
    return retval;
}
void glGetProgramResourceName (GLuint program_ , GLenum programInterface_ , GLuint index_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * name_ ){
    /* <command>
            <proto>void <name>glGetProgramResourceName</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETPROGRAMRESOURCENAMEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMRESOURCENAMEPROC ) mygetprocaddr("glGetProgramResourceName");
    glfunc(program_, programInterface_, index_, bufSize_, length_, name_);
    return;
}
void glGetProgramResourceiv (GLuint program_ , GLenum programInterface_ , GLuint index_ , GLsizei propCount_ , const GLenum * props_ , GLsizei bufSize_ , GLsizei * length_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetProgramResourceiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>programInterface</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLsizei</ptype> <name>propCount</name></param>
            <param len="propCount">const <ptype>GLenum</ptype> *<name>props</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETPROGRAMRESOURCEIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMRESOURCEIVPROC ) mygetprocaddr("glGetProgramResourceiv");
    glfunc(program_, programInterface_, index_, propCount_, props_, bufSize_, length_, params_);
    return;
}
void glGetProgramStageiv (GLuint program_ , GLenum shadertype_ , GLenum pname_ , GLint * values_ ){
    /* <command>
            <proto>void <name>glGetProgramStageiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="1"><ptype>GLint</ptype> *<name>values</name></param>
        </command>
         */
    static PFNGLGETPROGRAMSTAGEIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMSTAGEIVPROC ) mygetprocaddr("glGetProgramStageiv");
    glfunc(program_, shadertype_, pname_, values_);
    return;
}
void glGetProgramiv (GLuint program_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetProgramiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="199" type="single" />
        </command>
         */
    static PFNGLGETPROGRAMIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETPROGRAMIVPROC ) mygetprocaddr("glGetProgramiv");
    glfunc(program_, pname_, params_);
    return;
}
void glGetQueryBufferObjecti64v (GLuint id_ , GLuint buffer_ , GLenum pname_ , GLintptr offset_ ){
    /* <command>
            <proto>void <name>glGetQueryBufferObjecti64v</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
        </command>
         */
    static PFNGLGETQUERYBUFFEROBJECTI64VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYBUFFEROBJECTI64VPROC ) mygetprocaddr("glGetQueryBufferObjecti64v");
    glfunc(id_, buffer_, pname_, offset_);
    return;
}
void glGetQueryBufferObjectiv (GLuint id_ , GLuint buffer_ , GLenum pname_ , GLintptr offset_ ){
    /* <command>
            <proto>void <name>glGetQueryBufferObjectiv</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
        </command>
         */
    static PFNGLGETQUERYBUFFEROBJECTIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYBUFFEROBJECTIVPROC ) mygetprocaddr("glGetQueryBufferObjectiv");
    glfunc(id_, buffer_, pname_, offset_);
    return;
}
void glGetQueryBufferObjectui64v (GLuint id_ , GLuint buffer_ , GLenum pname_ , GLintptr offset_ ){
    /* <command>
            <proto>void <name>glGetQueryBufferObjectui64v</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
        </command>
         */
    static PFNGLGETQUERYBUFFEROBJECTUI64VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYBUFFEROBJECTUI64VPROC ) mygetprocaddr("glGetQueryBufferObjectui64v");
    glfunc(id_, buffer_, pname_, offset_);
    return;
}
void glGetQueryBufferObjectuiv (GLuint id_ , GLuint buffer_ , GLenum pname_ , GLintptr offset_ ){
    /* <command>
            <proto>void <name>glGetQueryBufferObjectuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
        </command>
         */
    static PFNGLGETQUERYBUFFEROBJECTUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYBUFFEROBJECTUIVPROC ) mygetprocaddr("glGetQueryBufferObjectuiv");
    glfunc(id_, buffer_, pname_, offset_);
    return;
}
void glGetQueryIndexediv (GLenum target_ , GLuint index_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetQueryIndexediv</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETQUERYINDEXEDIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYINDEXEDIVPROC ) mygetprocaddr("glGetQueryIndexediv");
    glfunc(target_, index_, pname_, params_);
    return;
}
void glGetQueryObjecti64v (GLuint id_ , GLenum pname_ , GLint64 * params_ ){
    /* <command>
            <proto>void <name>glGetQueryObjecti64v</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint64</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETQUERYOBJECTI64VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYOBJECTI64VPROC ) mygetprocaddr("glGetQueryObjecti64v");
    glfunc(id_, pname_, params_);
    return;
}
void glGetQueryObjectiv (GLuint id_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetQueryObjectiv</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="165" type="single" />
        </command>
         */
    static PFNGLGETQUERYOBJECTIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYOBJECTIVPROC ) mygetprocaddr("glGetQueryObjectiv");
    glfunc(id_, pname_, params_);
    return;
}
void glGetQueryObjectui64v (GLuint id_ , GLenum pname_ , GLuint64 * params_ ){
    /* <command>
            <proto>void <name>glGetQueryObjectui64v</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLuint64</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETQUERYOBJECTUI64VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYOBJECTUI64VPROC ) mygetprocaddr("glGetQueryObjectui64v");
    glfunc(id_, pname_, params_);
    return;
}
void glGetQueryObjectuiv (GLuint id_ , GLenum pname_ , GLuint * params_ ){
    /* <command>
            <proto>void <name>glGetQueryObjectuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLuint</ptype> *<name>params</name></param>
            <glx opcode="166" type="single" />
        </command>
         */
    static PFNGLGETQUERYOBJECTUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYOBJECTUIVPROC ) mygetprocaddr("glGetQueryObjectuiv");
    glfunc(id_, pname_, params_);
    return;
}
void glGetQueryiv (GLenum target_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetQueryiv</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="164" type="single" />
        </command>
         */
    static PFNGLGETQUERYIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETQUERYIVPROC ) mygetprocaddr("glGetQueryiv");
    glfunc(target_, pname_, params_);
    return;
}
void glGetRenderbufferParameteriv (GLenum target_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetRenderbufferParameteriv</name></proto>
            <param group="RenderbufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="1424" type="vendor" />
        </command>
         */
    static PFNGLGETRENDERBUFFERPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETRENDERBUFFERPARAMETERIVPROC ) mygetprocaddr("glGetRenderbufferParameteriv");
    glfunc(target_, pname_, params_);
    return;
}
void glGetSamplerParameterIiv (GLuint sampler_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetSamplerParameterIiv</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETSAMPLERPARAMETERIIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSAMPLERPARAMETERIIVPROC ) mygetprocaddr("glGetSamplerParameterIiv");
    glfunc(sampler_, pname_, params_);
    return;
}
void glGetSamplerParameterIuiv (GLuint sampler_ , GLenum pname_ , GLuint * params_ ){
    /* <command>
            <proto>void <name>glGetSamplerParameterIuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLuint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETSAMPLERPARAMETERIUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSAMPLERPARAMETERIUIVPROC ) mygetprocaddr("glGetSamplerParameterIuiv");
    glfunc(sampler_, pname_, params_);
    return;
}
void glGetSamplerParameterfv (GLuint sampler_ , GLenum pname_ , GLfloat * params_ ){
    /* <command>
            <proto>void <name>glGetSamplerParameterfv</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETSAMPLERPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSAMPLERPARAMETERFVPROC ) mygetprocaddr("glGetSamplerParameterfv");
    glfunc(sampler_, pname_, params_);
    return;
}
void glGetSamplerParameteriv (GLuint sampler_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetSamplerParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETSAMPLERPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSAMPLERPARAMETERIVPROC ) mygetprocaddr("glGetSamplerParameteriv");
    glfunc(sampler_, pname_, params_);
    return;
}
void glGetShaderInfoLog (GLuint shader_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * infoLog_ ){
    /* <command>
            <proto>void <name>glGetShaderInfoLog</name></proto>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>infoLog</name></param>
            <glx opcode="200" type="single" />
        </command>
         */
    static PFNGLGETSHADERINFOLOGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSHADERINFOLOGPROC ) mygetprocaddr("glGetShaderInfoLog");
    glfunc(shader_, bufSize_, length_, infoLog_);
    return;
}
void glGetShaderPrecisionFormat (GLenum shadertype_ , GLenum precisiontype_ , GLint * range_ , GLint * precision_ ){
    /* <command>
            <proto>void <name>glGetShaderPrecisionFormat</name></proto>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param><ptype>GLenum</ptype> <name>precisiontype</name></param>
            <param len="2"><ptype>GLint</ptype> *<name>range</name></param>
            <param len="2"><ptype>GLint</ptype> *<name>precision</name></param>
        </command>
         */
    static PFNGLGETSHADERPRECISIONFORMATPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSHADERPRECISIONFORMATPROC ) mygetprocaddr("glGetShaderPrecisionFormat");
    glfunc(shadertype_, precisiontype_, range_, precision_);
    return;
}
void glGetShaderSource (GLuint shader_ , GLsizei bufSize_ , GLsizei * length_ , GLchar * source_ ){
    /* <command>
            <proto>void <name>glGetShaderSource</name></proto>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>source</name></param>
        </command>
         */
    static PFNGLGETSHADERSOURCEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSHADERSOURCEPROC ) mygetprocaddr("glGetShaderSource");
    glfunc(shader_, bufSize_, length_, source_);
    return;
}
void glGetShaderiv (GLuint shader_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetShaderiv</name></proto>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="198" type="single" />
        </command>
         */
    static PFNGLGETSHADERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSHADERIVPROC ) mygetprocaddr("glGetShaderiv");
    glfunc(shader_, pname_, params_);
    return;
}
const GLubyte * glGetString (GLenum name_ ){
    /* <command>
            <proto group="String">const <ptype>GLubyte</ptype> *<name>glGetString</name></proto>
            <param group="StringName"><ptype>GLenum</ptype> <name>name</name></param>
            <glx opcode="129" type="single" />
        </command>
         */
    static PFNGLGETSTRINGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSTRINGPROC ) mygetprocaddr("glGetString");
    const GLubyte * retval = glfunc(name_);
    return retval;
}
const GLubyte * glGetStringi (GLenum name_ , GLuint index_ ){
    /* <command>
            <proto group="String">const <ptype>GLubyte</ptype> *<name>glGetStringi</name></proto>
            <param><ptype>GLenum</ptype> <name>name</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLGETSTRINGIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSTRINGIPROC ) mygetprocaddr("glGetStringi");
    const GLubyte * retval = glfunc(name_, index_);
    return retval;
}
GLuint glGetSubroutineIndex (GLuint program_ , GLenum shadertype_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLuint</ptype> <name>glGetSubroutineIndex</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETSUBROUTINEINDEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSUBROUTINEINDEXPROC ) mygetprocaddr("glGetSubroutineIndex");
    GLuint retval = glfunc(program_, shadertype_, name_);
    return retval;
}
GLint glGetSubroutineUniformLocation (GLuint program_ , GLenum shadertype_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLint</ptype> <name>glGetSubroutineUniformLocation</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETSUBROUTINEUNIFORMLOCATIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSUBROUTINEUNIFORMLOCATIONPROC ) mygetprocaddr("glGetSubroutineUniformLocation");
    GLint retval = glfunc(program_, shadertype_, name_);
    return retval;
}
void glGetSynciv (GLsync sync_ , GLenum pname_ , GLsizei bufSize_ , GLsizei * length_ , GLint * values_ ){
    /* <command>
            <proto>void <name>glGetSynciv</name></proto>
            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="bufSize"><ptype>GLint</ptype> *<name>values</name></param>
        </command>
         */
    static PFNGLGETSYNCIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETSYNCIVPROC ) mygetprocaddr("glGetSynciv");
    glfunc(sync_, pname_, bufSize_, length_, values_);
    return;
}
void glGetTexImage (GLenum target_ , GLint level_ , GLenum format_ , GLenum type_ , void * pixels_ ){
    /* <command>
            <proto>void <name>glGetTexImage</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(target,level,format,type)">void *<name>pixels</name></param>
            <glx opcode="135" type="single" />
            <glx comment="PBO protocol" name="glGetTexImagePBO" opcode="344" type="render" />
        </command>
         */
    static PFNGLGETTEXIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXIMAGEPROC ) mygetprocaddr("glGetTexImage");
    glfunc(target_, level_, format_, type_, pixels_);
    return;
}
void glGetTexLevelParameterfv (GLenum target_ , GLint level_ , GLenum pname_ , GLfloat * params_ ){
    /* <command>
            <proto>void <name>glGetTexLevelParameterfv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>params</name></param>
            <glx opcode="138" type="single" />
        </command>
         */
    static PFNGLGETTEXLEVELPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXLEVELPARAMETERFVPROC ) mygetprocaddr("glGetTexLevelParameterfv");
    glfunc(target_, level_, pname_, params_);
    return;
}
void glGetTexLevelParameteriv (GLenum target_ , GLint level_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetTexLevelParameteriv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="139" type="single" />
        </command>
         */
    static PFNGLGETTEXLEVELPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXLEVELPARAMETERIVPROC ) mygetprocaddr("glGetTexLevelParameteriv");
    glfunc(target_, level_, pname_, params_);
    return;
}
void glGetTexParameterIiv (GLenum target_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetTexParameterIiv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="203" type="single" />
        </command>
         */
    static PFNGLGETTEXPARAMETERIIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXPARAMETERIIVPROC ) mygetprocaddr("glGetTexParameterIiv");
    glfunc(target_, pname_, params_);
    return;
}
void glGetTexParameterIuiv (GLenum target_ , GLenum pname_ , GLuint * params_ ){
    /* <command>
            <proto>void <name>glGetTexParameterIuiv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLuint</ptype> *<name>params</name></param>
            <glx opcode="204" type="single" />
        </command>
         */
    static PFNGLGETTEXPARAMETERIUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXPARAMETERIUIVPROC ) mygetprocaddr("glGetTexParameterIuiv");
    glfunc(target_, pname_, params_);
    return;
}
void glGetTexParameterfv (GLenum target_ , GLenum pname_ , GLfloat * params_ ){
    /* <command>
            <proto>void <name>glGetTexParameterfv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLfloat</ptype> *<name>params</name></param>
            <glx opcode="136" type="single" />
        </command>
         */
    static PFNGLGETTEXPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXPARAMETERFVPROC ) mygetprocaddr("glGetTexParameterfv");
    glfunc(target_, pname_, params_);
    return;
}
void glGetTexParameteriv (GLenum target_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetTexParameteriv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="GetTextureParameter"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="137" type="single" />
        </command>
         */
    static PFNGLGETTEXPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXPARAMETERIVPROC ) mygetprocaddr("glGetTexParameteriv");
    glfunc(target_, pname_, params_);
    return;
}
void glGetTextureImage (GLuint texture_ , GLint level_ , GLenum format_ , GLenum type_ , GLsizei bufSize_ , void * pixels_ ){
    /* <command>
            <proto>void <name>glGetTextureImage</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param>void *<name>pixels</name></param>
        </command>
         */
    static PFNGLGETTEXTUREIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXTUREIMAGEPROC ) mygetprocaddr("glGetTextureImage");
    glfunc(texture_, level_, format_, type_, bufSize_, pixels_);
    return;
}
void glGetTextureLevelParameterfv (GLuint texture_ , GLint level_ , GLenum pname_ , GLfloat * params_ ){
    /* <command>
            <proto>void <name>glGetTextureLevelParameterfv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLfloat</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETTEXTURELEVELPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXTURELEVELPARAMETERFVPROC ) mygetprocaddr("glGetTextureLevelParameterfv");
    glfunc(texture_, level_, pname_, params_);
    return;
}
void glGetTextureLevelParameteriv (GLuint texture_ , GLint level_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetTextureLevelParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETTEXTURELEVELPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXTURELEVELPARAMETERIVPROC ) mygetprocaddr("glGetTextureLevelParameteriv");
    glfunc(texture_, level_, pname_, params_);
    return;
}
void glGetTextureParameterIiv (GLuint texture_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetTextureParameterIiv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETTEXTUREPARAMETERIIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXTUREPARAMETERIIVPROC ) mygetprocaddr("glGetTextureParameterIiv");
    glfunc(texture_, pname_, params_);
    return;
}
void glGetTextureParameterIuiv (GLuint texture_ , GLenum pname_ , GLuint * params_ ){
    /* <command>
            <proto>void <name>glGetTextureParameterIuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLuint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETTEXTUREPARAMETERIUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXTUREPARAMETERIUIVPROC ) mygetprocaddr("glGetTextureParameterIuiv");
    glfunc(texture_, pname_, params_);
    return;
}
void glGetTextureParameterfv (GLuint texture_ , GLenum pname_ , GLfloat * params_ ){
    /* <command>
            <proto>void <name>glGetTextureParameterfv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLfloat</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETTEXTUREPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXTUREPARAMETERFVPROC ) mygetprocaddr("glGetTextureParameterfv");
    glfunc(texture_, pname_, params_);
    return;
}
void glGetTextureParameteriv (GLuint texture_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetTextureParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETTEXTUREPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXTUREPARAMETERIVPROC ) mygetprocaddr("glGetTextureParameteriv");
    glfunc(texture_, pname_, params_);
    return;
}
void glGetTextureSubImage (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLenum format_ , GLenum type_ , GLsizei bufSize_ , void * pixels_ ){
    /* <command>
            <proto>void <name>glGetTextureSubImage</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param>void *<name>pixels</name></param>
        </command>
         */
    static PFNGLGETTEXTURESUBIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTEXTURESUBIMAGEPROC ) mygetprocaddr("glGetTextureSubImage");
    glfunc(texture_, level_, xoffset_, yoffset_, zoffset_, width_, height_, depth_, format_, type_, bufSize_, pixels_);
    return;
}
void glGetTransformFeedbackVarying (GLuint program_ , GLuint index_ , GLsizei bufSize_ , GLsizei * length_ , GLsizei * size_ , GLenum * type_ , GLchar * name_ ){
    /* <command>
            <proto>void <name>glGetTransformFeedbackVarying</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>length</name></param>
            <param len="1"><ptype>GLsizei</ptype> *<name>size</name></param>
            <param len="1"><ptype>GLenum</ptype> *<name>type</name></param>
            <param len="bufSize"><ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETTRANSFORMFEEDBACKVARYINGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTRANSFORMFEEDBACKVARYINGPROC ) mygetprocaddr("glGetTransformFeedbackVarying");
    glfunc(program_, index_, bufSize_, length_, size_, type_, name_);
    return;
}
void glGetTransformFeedbacki64_v (GLuint xfb_ , GLenum pname_ , GLuint index_ , GLint64 * param_ ){
    /* <command>
            <proto>void <name>glGetTransformFeedbacki64_v</name></proto>
            <param><ptype>GLuint</ptype> <name>xfb</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLint64</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLGETTRANSFORMFEEDBACKI64_VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTRANSFORMFEEDBACKI64_VPROC ) mygetprocaddr("glGetTransformFeedbacki64_v");
    glfunc(xfb_, pname_, index_, param_);
    return;
}
void glGetTransformFeedbacki_v (GLuint xfb_ , GLenum pname_ , GLuint index_ , GLint * param_ ){
    /* <command>
            <proto>void <name>glGetTransformFeedbacki_v</name></proto>
            <param><ptype>GLuint</ptype> <name>xfb</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLGETTRANSFORMFEEDBACKI_VPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTRANSFORMFEEDBACKI_VPROC ) mygetprocaddr("glGetTransformFeedbacki_v");
    glfunc(xfb_, pname_, index_, param_);
    return;
}
void glGetTransformFeedbackiv (GLuint xfb_ , GLenum pname_ , GLint * param_ ){
    /* <command>
            <proto>void <name>glGetTransformFeedbackiv</name></proto>
            <param><ptype>GLuint</ptype> <name>xfb</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLGETTRANSFORMFEEDBACKIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETTRANSFORMFEEDBACKIVPROC ) mygetprocaddr("glGetTransformFeedbackiv");
    glfunc(xfb_, pname_, param_);
    return;
}
GLuint glGetUniformBlockIndex (GLuint program_ , const GLchar * uniformBlockName_ ){
    /* <command>
            <proto><ptype>GLuint</ptype> <name>glGetUniformBlockIndex</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param len="COMPSIZE()">const <ptype>GLchar</ptype> *<name>uniformBlockName</name></param>
        </command>
         */
    static PFNGLGETUNIFORMBLOCKINDEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETUNIFORMBLOCKINDEXPROC ) mygetprocaddr("glGetUniformBlockIndex");
    GLuint retval = glfunc(program_, uniformBlockName_);
    return retval;
}
void glGetUniformIndices (GLuint program_ , GLsizei uniformCount_ , const GLchar ** uniformNames_ , GLuint * uniformIndices_ ){
    /* <command>
            <proto>void <name>glGetUniformIndices</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLsizei</ptype> <name>uniformCount</name></param>
            <param len="COMPSIZE(uniformCount)">const <ptype>GLchar</ptype> *const*<name>uniformNames</name></param>
            <param len="COMPSIZE(uniformCount)"><ptype>GLuint</ptype> *<name>uniformIndices</name></param>
        </command>
         */
    static PFNGLGETUNIFORMINDICESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETUNIFORMINDICESPROC ) mygetprocaddr("glGetUniformIndices");
    glfunc(program_, uniformCount_, uniformNames_, uniformIndices_);
    return;
}
GLint glGetUniformLocation (GLuint program_ , const GLchar * name_ ){
    /* <command>
            <proto><ptype>GLint</ptype> <name>glGetUniformLocation</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param>const <ptype>GLchar</ptype> *<name>name</name></param>
        </command>
         */
    static PFNGLGETUNIFORMLOCATIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETUNIFORMLOCATIONPROC ) mygetprocaddr("glGetUniformLocation");
    GLint retval = glfunc(program_, name_);
    return retval;
}
void glGetUniformSubroutineuiv (GLenum shadertype_ , GLint location_ , GLuint * params_ ){
    /* <command>
            <proto>void <name>glGetUniformSubroutineuiv</name></proto>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param len="1"><ptype>GLuint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETUNIFORMSUBROUTINEUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETUNIFORMSUBROUTINEUIVPROC ) mygetprocaddr("glGetUniformSubroutineuiv");
    glfunc(shadertype_, location_, params_);
    return;
}
void glGetUniformdv (GLuint program_ , GLint location_ , GLdouble * params_ ){
    /* <command>
            <proto>void <name>glGetUniformdv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param len="COMPSIZE(program,location)"><ptype>GLdouble</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETUNIFORMDVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETUNIFORMDVPROC ) mygetprocaddr("glGetUniformdv");
    glfunc(program_, location_, params_);
    return;
}
void glGetUniformfv (GLuint program_ , GLint location_ , GLfloat * params_ ){
    /* <command>
            <proto>void <name>glGetUniformfv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param len="COMPSIZE(program,location)"><ptype>GLfloat</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETUNIFORMFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETUNIFORMFVPROC ) mygetprocaddr("glGetUniformfv");
    glfunc(program_, location_, params_);
    return;
}
void glGetUniformiv (GLuint program_ , GLint location_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetUniformiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param len="COMPSIZE(program,location)"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETUNIFORMIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETUNIFORMIVPROC ) mygetprocaddr("glGetUniformiv");
    glfunc(program_, location_, params_);
    return;
}
void glGetUniformuiv (GLuint program_ , GLint location_ , GLuint * params_ ){
    /* <command>
            <proto>void <name>glGetUniformuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param len="COMPSIZE(program,location)"><ptype>GLuint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETUNIFORMUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETUNIFORMUIVPROC ) mygetprocaddr("glGetUniformuiv");
    glfunc(program_, location_, params_);
    return;
}
void glGetVertexArrayIndexed64iv (GLuint vaobj_ , GLuint index_ , GLenum pname_ , GLint64 * param_ ){
    /* <command>
            <proto>void <name>glGetVertexArrayIndexed64iv</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint64</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLGETVERTEXARRAYINDEXED64IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXARRAYINDEXED64IVPROC ) mygetprocaddr("glGetVertexArrayIndexed64iv");
    glfunc(vaobj_, index_, pname_, param_);
    return;
}
void glGetVertexArrayIndexediv (GLuint vaobj_ , GLuint index_ , GLenum pname_ , GLint * param_ ){
    /* <command>
            <proto>void <name>glGetVertexArrayIndexediv</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLGETVERTEXARRAYINDEXEDIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXARRAYINDEXEDIVPROC ) mygetprocaddr("glGetVertexArrayIndexediv");
    glfunc(vaobj_, index_, pname_, param_);
    return;
}
void glGetVertexArrayiv (GLuint vaobj_ , GLenum pname_ , GLint * param_ ){
    /* <command>
            <proto>void <name>glGetVertexArrayiv</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLGETVERTEXARRAYIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXARRAYIVPROC ) mygetprocaddr("glGetVertexArrayiv");
    glfunc(vaobj_, pname_, param_);
    return;
}
void glGetVertexAttribIiv (GLuint index_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetVertexAttribIiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param group="VertexAttribEnum"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="1"><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETVERTEXATTRIBIIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXATTRIBIIVPROC ) mygetprocaddr("glGetVertexAttribIiv");
    glfunc(index_, pname_, params_);
    return;
}
void glGetVertexAttribIuiv (GLuint index_ , GLenum pname_ , GLuint * params_ ){
    /* <command>
            <proto>void <name>glGetVertexAttribIuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param group="VertexAttribEnum"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="1"><ptype>GLuint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETVERTEXATTRIBIUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXATTRIBIUIVPROC ) mygetprocaddr("glGetVertexAttribIuiv");
    glfunc(index_, pname_, params_);
    return;
}
void glGetVertexAttribLdv (GLuint index_ , GLenum pname_ , GLdouble * params_ ){
    /* <command>
            <proto>void <name>glGetVertexAttribLdv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)"><ptype>GLdouble</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETVERTEXATTRIBLDVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXATTRIBLDVPROC ) mygetprocaddr("glGetVertexAttribLdv");
    glfunc(index_, pname_, params_);
    return;
}
void glGetVertexAttribPointerv (GLuint index_ , GLenum pname_ , void ** pointer_ ){
    /* <command>
            <proto>void <name>glGetVertexAttribPointerv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param group="VertexAttribPointerPropertyARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="1">void **<name>pointer</name></param>
            <glx opcode="209" type="single" />
        </command>
         */
    static PFNGLGETVERTEXATTRIBPOINTERVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXATTRIBPOINTERVPROC ) mygetprocaddr("glGetVertexAttribPointerv");
    glfunc(index_, pname_, pointer_);
    return;
}
void glGetVertexAttribdv (GLuint index_ , GLenum pname_ , GLdouble * params_ ){
    /* <command>
            <proto>void <name>glGetVertexAttribdv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param group="VertexAttribPropertyARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="4"><ptype>GLdouble</ptype> *<name>params</name></param>
            <glx opcode="1301" type="vendor" />
        </command>
         */
    static PFNGLGETVERTEXATTRIBDVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXATTRIBDVPROC ) mygetprocaddr("glGetVertexAttribdv");
    glfunc(index_, pname_, params_);
    return;
}
void glGetVertexAttribfv (GLuint index_ , GLenum pname_ , GLfloat * params_ ){
    /* <command>
            <proto>void <name>glGetVertexAttribfv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param group="VertexAttribPropertyARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="4"><ptype>GLfloat</ptype> *<name>params</name></param>
            <glx opcode="1302" type="vendor" />
        </command>
         */
    static PFNGLGETVERTEXATTRIBFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXATTRIBFVPROC ) mygetprocaddr("glGetVertexAttribfv");
    glfunc(index_, pname_, params_);
    return;
}
void glGetVertexAttribiv (GLuint index_ , GLenum pname_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetVertexAttribiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param group="VertexAttribPropertyARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="4"><ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="1303" type="vendor" />
        </command>
         */
    static PFNGLGETVERTEXATTRIBIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETVERTEXATTRIBIVPROC ) mygetprocaddr("glGetVertexAttribiv");
    glfunc(index_, pname_, params_);
    return;
}
void glGetnCompressedTexImage (GLenum target_ , GLint lod_ , GLsizei bufSize_ , void * pixels_ ){
    /* <command>
            <proto>void <name>glGetnCompressedTexImage</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLint</ptype> <name>lod</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param>void *<name>pixels</name></param>
        </command>
         */
    static PFNGLGETNCOMPRESSEDTEXIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNCOMPRESSEDTEXIMAGEPROC ) mygetprocaddr("glGetnCompressedTexImage");
    glfunc(target_, lod_, bufSize_, pixels_);
    return;
}
void glGetnTexImage (GLenum target_ , GLint level_ , GLenum format_ , GLenum type_ , GLsizei bufSize_ , void * pixels_ ){
    /* <command>
            <proto>void <name>glGetnTexImage</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param>void *<name>pixels</name></param>
        </command>
         */
    static PFNGLGETNTEXIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNTEXIMAGEPROC ) mygetprocaddr("glGetnTexImage");
    glfunc(target_, level_, format_, type_, bufSize_, pixels_);
    return;
}
void glGetnUniformdv (GLuint program_ , GLint location_ , GLsizei bufSize_ , GLdouble * params_ ){
    /* <command>
            <proto>void <name>glGetnUniformdv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param><ptype>GLdouble</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETNUNIFORMDVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNUNIFORMDVPROC ) mygetprocaddr("glGetnUniformdv");
    glfunc(program_, location_, bufSize_, params_);
    return;
}
void glGetnUniformfv (GLuint program_ , GLint location_ , GLsizei bufSize_ , GLfloat * params_ ){
    /* <command>
            <proto>void <name>glGetnUniformfv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param><ptype>GLfloat</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETNUNIFORMFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNUNIFORMFVPROC ) mygetprocaddr("glGetnUniformfv");
    glfunc(program_, location_, bufSize_, params_);
    return;
}
void glGetnUniformiv (GLuint program_ , GLint location_ , GLsizei bufSize_ , GLint * params_ ){
    /* <command>
            <proto>void <name>glGetnUniformiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param><ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETNUNIFORMIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNUNIFORMIVPROC ) mygetprocaddr("glGetnUniformiv");
    glfunc(program_, location_, bufSize_, params_);
    return;
}
void glGetnUniformuiv (GLuint program_ , GLint location_ , GLsizei bufSize_ , GLuint * params_ ){
    /* <command>
            <proto>void <name>glGetnUniformuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param><ptype>GLuint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLGETNUNIFORMUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLGETNUNIFORMUIVPROC ) mygetprocaddr("glGetnUniformuiv");
    glfunc(program_, location_, bufSize_, params_);
    return;
}
void glHint (GLenum target_ , GLenum mode_ ){
    /* <command>
            <proto>void <name>glHint</name></proto>
            <param group="HintTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="HintMode"><ptype>GLenum</ptype> <name>mode</name></param>
            <glx opcode="85" type="render" />
        </command>
         */
    static PFNGLHINTPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLHINTPROC ) mygetprocaddr("glHint");
    glfunc(target_, mode_);
    return;
}
void glInvalidateBufferData (GLuint buffer_ ){
    /* <command>
            <proto>void <name>glInvalidateBufferData</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLINVALIDATEBUFFERDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLINVALIDATEBUFFERDATAPROC ) mygetprocaddr("glInvalidateBufferData");
    glfunc(buffer_);
    return;
}
void glInvalidateBufferSubData (GLuint buffer_ , GLintptr offset_ , GLsizeiptr length_ ){
    /* <command>
            <proto>void <name>glInvalidateBufferSubData</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
        </command>
         */
    static PFNGLINVALIDATEBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLINVALIDATEBUFFERSUBDATAPROC ) mygetprocaddr("glInvalidateBufferSubData");
    glfunc(buffer_, offset_, length_);
    return;
}
void glInvalidateFramebuffer (GLenum target_ , GLsizei numAttachments_ , const GLenum * attachments_ ){
    /* <command>
            <proto>void <name>glInvalidateFramebuffer</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizei</ptype> <name>numAttachments</name></param>
            <param len="numAttachments">const <ptype>GLenum</ptype> *<name>attachments</name></param>
        </command>
         */
    static PFNGLINVALIDATEFRAMEBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLINVALIDATEFRAMEBUFFERPROC ) mygetprocaddr("glInvalidateFramebuffer");
    glfunc(target_, numAttachments_, attachments_);
    return;
}
void glInvalidateNamedFramebufferData (GLuint framebuffer_ , GLsizei numAttachments_ , const GLenum * attachments_ ){
    /* <command>
            <proto>void <name>glInvalidateNamedFramebufferData</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLsizei</ptype> <name>numAttachments</name></param>
            <param>const <ptype>GLenum</ptype> *<name>attachments</name></param>
        </command>
         */
    static PFNGLINVALIDATENAMEDFRAMEBUFFERDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLINVALIDATENAMEDFRAMEBUFFERDATAPROC ) mygetprocaddr("glInvalidateNamedFramebufferData");
    glfunc(framebuffer_, numAttachments_, attachments_);
    return;
}
void glInvalidateNamedFramebufferSubData (GLuint framebuffer_ , GLsizei numAttachments_ , const GLenum * attachments_ , GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glInvalidateNamedFramebufferSubData</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLsizei</ptype> <name>numAttachments</name></param>
            <param>const <ptype>GLenum</ptype> *<name>attachments</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLINVALIDATENAMEDFRAMEBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLINVALIDATENAMEDFRAMEBUFFERSUBDATAPROC ) mygetprocaddr("glInvalidateNamedFramebufferSubData");
    glfunc(framebuffer_, numAttachments_, attachments_, x_, y_, width_, height_);
    return;
}
void glInvalidateSubFramebuffer (GLenum target_ , GLsizei numAttachments_ , const GLenum * attachments_ , GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glInvalidateSubFramebuffer</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizei</ptype> <name>numAttachments</name></param>
            <param len="numAttachments">const <ptype>GLenum</ptype> *<name>attachments</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLINVALIDATESUBFRAMEBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLINVALIDATESUBFRAMEBUFFERPROC ) mygetprocaddr("glInvalidateSubFramebuffer");
    glfunc(target_, numAttachments_, attachments_, x_, y_, width_, height_);
    return;
}
void glInvalidateTexImage (GLuint texture_ , GLint level_ ){
    /* <command>
            <proto>void <name>glInvalidateTexImage</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
        </command>
         */
    static PFNGLINVALIDATETEXIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLINVALIDATETEXIMAGEPROC ) mygetprocaddr("glInvalidateTexImage");
    glfunc(texture_, level_);
    return;
}
void glInvalidateTexSubImage (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ ){
    /* <command>
            <proto>void <name>glInvalidateTexSubImage</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
        </command>
         */
    static PFNGLINVALIDATETEXSUBIMAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLINVALIDATETEXSUBIMAGEPROC ) mygetprocaddr("glInvalidateTexSubImage");
    glfunc(texture_, level_, xoffset_, yoffset_, zoffset_, width_, height_, depth_);
    return;
}
GLboolean glIsBuffer (GLuint buffer_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLISBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISBUFFERPROC ) mygetprocaddr("glIsBuffer");
    GLboolean retval = glfunc(buffer_);
    return retval;
}
GLboolean glIsEnabled (GLenum cap_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsEnabled</name></proto>
            <param group="EnableCap"><ptype>GLenum</ptype> <name>cap</name></param>
            <glx opcode="140" type="single" />
        </command>
         */
    static PFNGLISENABLEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISENABLEDPROC ) mygetprocaddr("glIsEnabled");
    GLboolean retval = glfunc(cap_);
    return retval;
}
GLboolean glIsEnabledi (GLenum target_ , GLuint index_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsEnabledi</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLISENABLEDIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISENABLEDIPROC ) mygetprocaddr("glIsEnabledi");
    GLboolean retval = glfunc(target_, index_);
    return retval;
}
GLboolean glIsFramebuffer (GLuint framebuffer_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsFramebuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <glx opcode="1425" type="vendor" />
        </command>
         */
    static PFNGLISFRAMEBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISFRAMEBUFFERPROC ) mygetprocaddr("glIsFramebuffer");
    GLboolean retval = glfunc(framebuffer_);
    return retval;
}
GLboolean glIsProgram (GLuint program_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsProgram</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <glx opcode="197" type="single" />
        </command>
         */
    static PFNGLISPROGRAMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISPROGRAMPROC ) mygetprocaddr("glIsProgram");
    GLboolean retval = glfunc(program_);
    return retval;
}
GLboolean glIsProgramPipeline (GLuint pipeline_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsProgramPipeline</name></proto>
            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
        </command>
         */
    static PFNGLISPROGRAMPIPELINEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISPROGRAMPIPELINEPROC ) mygetprocaddr("glIsProgramPipeline");
    GLboolean retval = glfunc(pipeline_);
    return retval;
}
GLboolean glIsQuery (GLuint id_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsQuery</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <glx opcode="163" type="single" />
        </command>
         */
    static PFNGLISQUERYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISQUERYPROC ) mygetprocaddr("glIsQuery");
    GLboolean retval = glfunc(id_);
    return retval;
}
GLboolean glIsRenderbuffer (GLuint renderbuffer_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsRenderbuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
            <glx opcode="1422" type="vendor" />
        </command>
         */
    static PFNGLISRENDERBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISRENDERBUFFERPROC ) mygetprocaddr("glIsRenderbuffer");
    GLboolean retval = glfunc(renderbuffer_);
    return retval;
}
GLboolean glIsSampler (GLuint sampler_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsSampler</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
        </command>
         */
    static PFNGLISSAMPLERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISSAMPLERPROC ) mygetprocaddr("glIsSampler");
    GLboolean retval = glfunc(sampler_);
    return retval;
}
GLboolean glIsShader (GLuint shader_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsShader</name></proto>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
            <glx opcode="196" type="single" />
        </command>
         */
    static PFNGLISSHADERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISSHADERPROC ) mygetprocaddr("glIsShader");
    GLboolean retval = glfunc(shader_);
    return retval;
}
GLboolean glIsSync (GLsync sync_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsSync</name></proto>
            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
        </command>
         */
    static PFNGLISSYNCPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISSYNCPROC ) mygetprocaddr("glIsSync");
    GLboolean retval = glfunc(sync_);
    return retval;
}
GLboolean glIsTexture (GLuint texture_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsTexture</name></proto>
            <param group="Texture"><ptype>GLuint</ptype> <name>texture</name></param>
            <glx opcode="146" type="single" />
        </command>
         */
    static PFNGLISTEXTUREPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISTEXTUREPROC ) mygetprocaddr("glIsTexture");
    GLboolean retval = glfunc(texture_);
    return retval;
}
GLboolean glIsTransformFeedback (GLuint id_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsTransformFeedback</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
        </command>
         */
    static PFNGLISTRANSFORMFEEDBACKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISTRANSFORMFEEDBACKPROC ) mygetprocaddr("glIsTransformFeedback");
    GLboolean retval = glfunc(id_);
    return retval;
}
GLboolean glIsVertexArray (GLuint array_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glIsVertexArray</name></proto>
            <param><ptype>GLuint</ptype> <name>array</name></param>
            <glx opcode="207" type="single" />
        </command>
         */
    static PFNGLISVERTEXARRAYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLISVERTEXARRAYPROC ) mygetprocaddr("glIsVertexArray");
    GLboolean retval = glfunc(array_);
    return retval;
}
void glLineWidth (GLfloat width_ ){
    /* <command>
            <proto>void <name>glLineWidth</name></proto>
            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>width</name></param>
            <glx opcode="95" type="render" />
        </command>
         */
    static PFNGLLINEWIDTHPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLLINEWIDTHPROC ) mygetprocaddr("glLineWidth");
    glfunc(width_);
    return;
}
void glLinkProgram (GLuint program_ ){
    /* <command>
            <proto>void <name>glLinkProgram</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
        </command>
         */
    static PFNGLLINKPROGRAMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLLINKPROGRAMPROC ) mygetprocaddr("glLinkProgram");
    glfunc(program_);
    return;
}
void glLogicOp (GLenum opcode_ ){
    /* <command>
            <proto>void <name>glLogicOp</name></proto>
            <param group="LogicOp"><ptype>GLenum</ptype> <name>opcode</name></param>
            <glx opcode="161" type="render" />
        </command>
         */
    static PFNGLLOGICOPPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLLOGICOPPROC ) mygetprocaddr("glLogicOp");
    glfunc(opcode_);
    return;
}
void * glMapBuffer (GLenum target_ , GLenum access_ ){
    /* <command>
            <proto>void *<name>glMapBuffer</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferAccessARB"><ptype>GLenum</ptype> <name>access</name></param>
        </command>
         */
    static PFNGLMAPBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMAPBUFFERPROC ) mygetprocaddr("glMapBuffer");
    void * retval = glfunc(target_, access_);
    return retval;
}
void * glMapBufferRange (GLenum target_ , GLintptr offset_ , GLsizeiptr length_ , GLbitfield access_ ){
    /* <command>
            <proto>void *<name>glMapBufferRange</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
            <param group="BufferAccessMask"><ptype>GLbitfield</ptype> <name>access</name></param>
            <glx opcode="205" type="single" />
        </command>
         */
    static PFNGLMAPBUFFERRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMAPBUFFERRANGEPROC ) mygetprocaddr("glMapBufferRange");
    void * retval = glfunc(target_, offset_, length_, access_);
    return retval;
}
void * glMapNamedBuffer (GLuint buffer_ , GLenum access_ ){
    /* <command>
            <proto>void *<name>glMapNamedBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLenum</ptype> <name>access</name></param>
        </command>
         */
    static PFNGLMAPNAMEDBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMAPNAMEDBUFFERPROC ) mygetprocaddr("glMapNamedBuffer");
    void * retval = glfunc(buffer_, access_);
    return retval;
}
void * glMapNamedBufferRange (GLuint buffer_ , GLintptr offset_ , GLsizeiptr length_ , GLbitfield access_ ){
    /* <command>
            <proto>void *<name>glMapNamedBufferRange</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>length</name></param>
            <param><ptype>GLbitfield</ptype> <name>access</name></param>
        </command>
         */
    static PFNGLMAPNAMEDBUFFERRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMAPNAMEDBUFFERRANGEPROC ) mygetprocaddr("glMapNamedBufferRange");
    void * retval = glfunc(buffer_, offset_, length_, access_);
    return retval;
}
void glMemoryBarrier (GLbitfield barriers_ ){
    /* <command>
            <proto>void <name>glMemoryBarrier</name></proto>
            <param><ptype>GLbitfield</ptype> <name>barriers</name></param>
        </command>
         */
    static PFNGLMEMORYBARRIERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMEMORYBARRIERPROC ) mygetprocaddr("glMemoryBarrier");
    glfunc(barriers_);
    return;
}
void glMemoryBarrierByRegion (GLbitfield barriers_ ){
    /* <command>
            <proto>void <name>glMemoryBarrierByRegion</name></proto>
            <param><ptype>GLbitfield</ptype> <name>barriers</name></param>
        </command>
         */
    static PFNGLMEMORYBARRIERBYREGIONPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMEMORYBARRIERBYREGIONPROC ) mygetprocaddr("glMemoryBarrierByRegion");
    glfunc(barriers_);
    return;
}
void glMinSampleShading (GLfloat value_ ){
    /* <command>
            <proto>void <name>glMinSampleShading</name></proto>
            <param group="ColorF"><ptype>GLfloat</ptype> <name>value</name></param>
        </command>
         */
    static PFNGLMINSAMPLESHADINGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMINSAMPLESHADINGPROC ) mygetprocaddr("glMinSampleShading");
    glfunc(value_);
    return;
}
void glMultiDrawArrays (GLenum mode_ , const GLint * first_ , const GLsizei * count_ , GLsizei drawcount_ ){
    /* <command>
            <proto>void <name>glMultiDrawArrays</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param len="COMPSIZE(count)">const <ptype>GLint</ptype> *<name>first</name></param>
            <param len="COMPSIZE(drawcount)">const <ptype>GLsizei</ptype> *<name>count</name></param>
            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
        </command>
         */
    static PFNGLMULTIDRAWARRAYSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMULTIDRAWARRAYSPROC ) mygetprocaddr("glMultiDrawArrays");
    glfunc(mode_, first_, count_, drawcount_);
    return;
}
void glMultiDrawArraysIndirect (GLenum mode_ , const void * indirect_ , GLsizei drawcount_ , GLsizei stride_ ){
    /* <command>
            <proto>void <name>glMultiDrawArraysIndirect</name></proto>
            <param><ptype>GLenum</ptype> <name>mode</name></param>
            <param len="COMPSIZE(drawcount,stride)">const void *<name>indirect</name></param>
            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
            <param><ptype>GLsizei</ptype> <name>stride</name></param>
        </command>
         */
    static PFNGLMULTIDRAWARRAYSINDIRECTPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMULTIDRAWARRAYSINDIRECTPROC ) mygetprocaddr("glMultiDrawArraysIndirect");
    glfunc(mode_, indirect_, drawcount_, stride_);
    return;
}
void glMultiDrawElements (GLenum mode_ , const GLsizei * count_ , GLenum type_ , const void ** indices_ , GLsizei drawcount_ ){
    /* <command>
            <proto>void <name>glMultiDrawElements</name></proto>
            <param group="PrimitiveType"><ptype>GLenum</ptype> <name>mode</name></param>
            <param len="COMPSIZE(drawcount)">const <ptype>GLsizei</ptype> *<name>count</name></param>
            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(drawcount)">const void *const*<name>indices</name></param>
            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
        </command>
         */
    static PFNGLMULTIDRAWELEMENTSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMULTIDRAWELEMENTSPROC ) mygetprocaddr("glMultiDrawElements");
    glfunc(mode_, count_, type_, indices_, drawcount_);
    return;
}
void glMultiDrawElementsBaseVertex (GLenum mode_ , const GLsizei * count_ , GLenum type_ , const void ** indices_ , GLsizei drawcount_ , const GLint * basevertex_ ){
    /* <command>
            <proto>void <name>glMultiDrawElementsBaseVertex</name></proto>
            <param><ptype>GLenum</ptype> <name>mode</name></param>
            <param len="COMPSIZE(drawcount)">const <ptype>GLsizei</ptype> *<name>count</name></param>
            <param group="DrawElementsType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(drawcount)">const void *const*<name>indices</name></param>
            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
            <param len="COMPSIZE(drawcount)">const <ptype>GLint</ptype> *<name>basevertex</name></param>
        </command>
         */
    static PFNGLMULTIDRAWELEMENTSBASEVERTEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMULTIDRAWELEMENTSBASEVERTEXPROC ) mygetprocaddr("glMultiDrawElementsBaseVertex");
    glfunc(mode_, count_, type_, indices_, drawcount_, basevertex_);
    return;
}
void glMultiDrawElementsIndirect (GLenum mode_ , GLenum type_ , const void * indirect_ , GLsizei drawcount_ , GLsizei stride_ ){
    /* <command>
            <proto>void <name>glMultiDrawElementsIndirect</name></proto>
            <param><ptype>GLenum</ptype> <name>mode</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(drawcount,stride)">const void *<name>indirect</name></param>
            <param><ptype>GLsizei</ptype> <name>drawcount</name></param>
            <param><ptype>GLsizei</ptype> <name>stride</name></param>
        </command>
         */
    static PFNGLMULTIDRAWELEMENTSINDIRECTPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLMULTIDRAWELEMENTSINDIRECTPROC ) mygetprocaddr("glMultiDrawElementsIndirect");
    glfunc(mode_, type_, indirect_, drawcount_, stride_);
    return;
}
void glNamedBufferData (GLuint buffer_ , GLsizeiptr size_ , const void * data_ , GLenum usage_ ){
    /* <command>
            <proto>void <name>glNamedBufferData</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param>const void *<name>data</name></param>
            <param><ptype>GLenum</ptype> <name>usage</name></param>
        </command>
         */
    static PFNGLNAMEDBUFFERDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDBUFFERDATAPROC ) mygetprocaddr("glNamedBufferData");
    glfunc(buffer_, size_, data_, usage_);
    return;
}
void glNamedBufferStorage (GLuint buffer_ , GLsizeiptr size_ , const void * data_ , GLbitfield flags_ ){
    /* <command>
            <proto>void <name>glNamedBufferStorage</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param len="size">const void *<name>data</name></param>
            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
        </command>
         */
    static PFNGLNAMEDBUFFERSTORAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDBUFFERSTORAGEPROC ) mygetprocaddr("glNamedBufferStorage");
    glfunc(buffer_, size_, data_, flags_);
    return;
}
void glNamedBufferSubData (GLuint buffer_ , GLintptr offset_ , GLsizeiptr size_ , const void * data_ ){
    /* <command>
            <proto>void <name>glNamedBufferSubData</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
            <param len="COMPSIZE(size)">const void *<name>data</name></param>
        </command>
         */
    static PFNGLNAMEDBUFFERSUBDATAPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDBUFFERSUBDATAPROC ) mygetprocaddr("glNamedBufferSubData");
    glfunc(buffer_, offset_, size_, data_);
    return;
}
void glNamedFramebufferDrawBuffer (GLuint framebuffer_ , GLenum buf_ ){
    /* <command>
            <proto>void <name>glNamedFramebufferDrawBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>buf</name></param>
        </command>
         */
    static PFNGLNAMEDFRAMEBUFFERDRAWBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDFRAMEBUFFERDRAWBUFFERPROC ) mygetprocaddr("glNamedFramebufferDrawBuffer");
    glfunc(framebuffer_, buf_);
    return;
}
void glNamedFramebufferDrawBuffers (GLuint framebuffer_ , GLsizei n_ , const GLenum * bufs_ ){
    /* <command>
            <proto>void <name>glNamedFramebufferDrawBuffers</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLsizei</ptype> <name>n</name></param>
            <param>const <ptype>GLenum</ptype> *<name>bufs</name></param>
        </command>
         */
    static PFNGLNAMEDFRAMEBUFFERDRAWBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDFRAMEBUFFERDRAWBUFFERSPROC ) mygetprocaddr("glNamedFramebufferDrawBuffers");
    glfunc(framebuffer_, n_, bufs_);
    return;
}
void glNamedFramebufferParameteri (GLuint framebuffer_ , GLenum pname_ , GLint param_ ){
    /* <command>
            <proto>void <name>glNamedFramebufferParameteri</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> <name>param</name></param>
        </command>
         */
    static PFNGLNAMEDFRAMEBUFFERPARAMETERIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDFRAMEBUFFERPARAMETERIPROC ) mygetprocaddr("glNamedFramebufferParameteri");
    glfunc(framebuffer_, pname_, param_);
    return;
}
void glNamedFramebufferReadBuffer (GLuint framebuffer_ , GLenum src_ ){
    /* <command>
            <proto>void <name>glNamedFramebufferReadBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>src</name></param>
        </command>
         */
    static PFNGLNAMEDFRAMEBUFFERREADBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDFRAMEBUFFERREADBUFFERPROC ) mygetprocaddr("glNamedFramebufferReadBuffer");
    glfunc(framebuffer_, src_);
    return;
}
void glNamedFramebufferRenderbuffer (GLuint framebuffer_ , GLenum attachment_ , GLenum renderbuffertarget_ , GLuint renderbuffer_ ){
    /* <command>
            <proto>void <name>glNamedFramebufferRenderbuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLenum</ptype> <name>renderbuffertarget</name></param>
            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
        </command>
         */
    static PFNGLNAMEDFRAMEBUFFERRENDERBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDFRAMEBUFFERRENDERBUFFERPROC ) mygetprocaddr("glNamedFramebufferRenderbuffer");
    glfunc(framebuffer_, attachment_, renderbuffertarget_, renderbuffer_);
    return;
}
void glNamedFramebufferTexture (GLuint framebuffer_ , GLenum attachment_ , GLuint texture_ , GLint level_ ){
    /* <command>
            <proto>void <name>glNamedFramebufferTexture</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
        </command>
         */
    static PFNGLNAMEDFRAMEBUFFERTEXTUREPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDFRAMEBUFFERTEXTUREPROC ) mygetprocaddr("glNamedFramebufferTexture");
    glfunc(framebuffer_, attachment_, texture_, level_);
    return;
}
void glNamedFramebufferTextureLayer (GLuint framebuffer_ , GLenum attachment_ , GLuint texture_ , GLint level_ , GLint layer_ ){
    /* <command>
            <proto>void <name>glNamedFramebufferTextureLayer</name></proto>
            <param><ptype>GLuint</ptype> <name>framebuffer</name></param>
            <param><ptype>GLenum</ptype> <name>attachment</name></param>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>layer</name></param>
        </command>
         */
    static PFNGLNAMEDFRAMEBUFFERTEXTURELAYERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDFRAMEBUFFERTEXTURELAYERPROC ) mygetprocaddr("glNamedFramebufferTextureLayer");
    glfunc(framebuffer_, attachment_, texture_, level_, layer_);
    return;
}
void glNamedRenderbufferStorage (GLuint renderbuffer_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glNamedRenderbufferStorage</name></proto>
            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLNAMEDRENDERBUFFERSTORAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDRENDERBUFFERSTORAGEPROC ) mygetprocaddr("glNamedRenderbufferStorage");
    glfunc(renderbuffer_, internalformat_, width_, height_);
    return;
}
void glNamedRenderbufferStorageMultisample (GLuint renderbuffer_ , GLsizei samples_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glNamedRenderbufferStorageMultisample</name></proto>
            <param><ptype>GLuint</ptype> <name>renderbuffer</name></param>
            <param><ptype>GLsizei</ptype> <name>samples</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEPROC ) mygetprocaddr("glNamedRenderbufferStorageMultisample");
    glfunc(renderbuffer_, samples_, internalformat_, width_, height_);
    return;
}
void glObjectLabel (GLenum identifier_ , GLuint name_ , GLsizei length_ , const GLchar * label_ ){
    /* <command>
            <proto>void <name>glObjectLabel</name></proto>
            <param><ptype>GLenum</ptype> <name>identifier</name></param>
            <param><ptype>GLuint</ptype> <name>name</name></param>
            <param><ptype>GLsizei</ptype> <name>length</name></param>
            <param len="COMPSIZE(label,length)">const <ptype>GLchar</ptype> *<name>label</name></param>
        </command>
         */
    static PFNGLOBJECTLABELPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLOBJECTLABELPROC ) mygetprocaddr("glObjectLabel");
    glfunc(identifier_, name_, length_, label_);
    return;
}
void glObjectPtrLabel (const void * ptr_ , GLsizei length_ , const GLchar * label_ ){
    /* <command>
            <proto>void <name>glObjectPtrLabel</name></proto>
            <param>const void *<name>ptr</name></param>
            <param><ptype>GLsizei</ptype> <name>length</name></param>
            <param len="COMPSIZE(label,length)">const <ptype>GLchar</ptype> *<name>label</name></param>
        </command>
         */
    static PFNGLOBJECTPTRLABELPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLOBJECTPTRLABELPROC ) mygetprocaddr("glObjectPtrLabel");
    glfunc(ptr_, length_, label_);
    return;
}
void glPatchParameterfv (GLenum pname_ , const GLfloat * values_ ){
    /* <command>
            <proto>void <name>glPatchParameterfv</name></proto>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)">const <ptype>GLfloat</ptype> *<name>values</name></param>
        </command>
         */
    static PFNGLPATCHPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPATCHPARAMETERFVPROC ) mygetprocaddr("glPatchParameterfv");
    glfunc(pname_, values_);
    return;
}
void glPatchParameteri (GLenum pname_ , GLint value_ ){
    /* <command>
            <proto>void <name>glPatchParameteri</name></proto>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> <name>value</name></param>
        </command>
         */
    static PFNGLPATCHPARAMETERIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPATCHPARAMETERIPROC ) mygetprocaddr("glPatchParameteri");
    glfunc(pname_, value_);
    return;
}
void glPauseTransformFeedback (){
    /* <command>
            <proto>void <name>glPauseTransformFeedback</name></proto>
        </command>
         */
    static PFNGLPAUSETRANSFORMFEEDBACKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPAUSETRANSFORMFEEDBACKPROC ) mygetprocaddr("glPauseTransformFeedback");
    glfunc();
    return;
}
void glPixelStoref (GLenum pname_ , GLfloat param_ ){
    /* <command>
            <proto>void <name>glPixelStoref</name></proto>
            <param group="PixelStoreParameter"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>param</name></param>
            <glx opcode="109" type="single" />
        </command>
         */
    static PFNGLPIXELSTOREFPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPIXELSTOREFPROC ) mygetprocaddr("glPixelStoref");
    glfunc(pname_, param_);
    return;
}
void glPixelStorei (GLenum pname_ , GLint param_ ){
    /* <command>
            <proto>void <name>glPixelStorei</name></proto>
            <param group="PixelStoreParameter"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>param</name></param>
            <glx opcode="110" type="single" />
        </command>
         */
    static PFNGLPIXELSTOREIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPIXELSTOREIPROC ) mygetprocaddr("glPixelStorei");
    glfunc(pname_, param_);
    return;
}
void glPointParameterf (GLenum pname_ , GLfloat param_ ){
    /* <command>
            <proto>void <name>glPointParameterf</name></proto>
            <param group="PointParameterNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>param</name></param>
            <glx opcode="2065" type="render" />
        </command>
         */
    static PFNGLPOINTPARAMETERFPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPOINTPARAMETERFPROC ) mygetprocaddr("glPointParameterf");
    glfunc(pname_, param_);
    return;
}
void glPointParameterfv (GLenum pname_ , const GLfloat * params_ ){
    /* <command>
            <proto>void <name>glPointParameterfv</name></proto>
            <param group="PointParameterNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="CheckedFloat32" len="COMPSIZE(pname)">const <ptype>GLfloat</ptype> *<name>params</name></param>
            <glx opcode="2066" type="render" />
        </command>
         */
    static PFNGLPOINTPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPOINTPARAMETERFVPROC ) mygetprocaddr("glPointParameterfv");
    glfunc(pname_, params_);
    return;
}
void glPointParameteri (GLenum pname_ , GLint param_ ){
    /* <command>
            <proto>void <name>glPointParameteri</name></proto>
            <param group="PointParameterNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> <name>param</name></param>
            <glx opcode="4221" type="render" />
        </command>
         */
    static PFNGLPOINTPARAMETERIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPOINTPARAMETERIPROC ) mygetprocaddr("glPointParameteri");
    glfunc(pname_, param_);
    return;
}
void glPointParameteriv (GLenum pname_ , const GLint * params_ ){
    /* <command>
            <proto>void <name>glPointParameteriv</name></proto>
            <param group="PointParameterNameARB"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="4222" type="render" />
        </command>
         */
    static PFNGLPOINTPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPOINTPARAMETERIVPROC ) mygetprocaddr("glPointParameteriv");
    glfunc(pname_, params_);
    return;
}
void glPointSize (GLfloat size_ ){
    /* <command>
            <proto>void <name>glPointSize</name></proto>
            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>size</name></param>
            <glx opcode="100" type="render" />
        </command>
         */
    static PFNGLPOINTSIZEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPOINTSIZEPROC ) mygetprocaddr("glPointSize");
    glfunc(size_);
    return;
}
void glPolygonMode (GLenum face_ , GLenum mode_ ){
    /* <command>
            <proto>void <name>glPolygonMode</name></proto>
            <param group="MaterialFace"><ptype>GLenum</ptype> <name>face</name></param>
            <param group="PolygonMode"><ptype>GLenum</ptype> <name>mode</name></param>
            <glx opcode="101" type="render" />
        </command>
         */
    static PFNGLPOLYGONMODEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPOLYGONMODEPROC ) mygetprocaddr("glPolygonMode");
    glfunc(face_, mode_);
    return;
}
void glPolygonOffset (GLfloat factor_ , GLfloat units_ ){
    /* <command>
            <proto>void <name>glPolygonOffset</name></proto>
            <param><ptype>GLfloat</ptype> <name>factor</name></param>
            <param><ptype>GLfloat</ptype> <name>units</name></param>
            <glx opcode="192" type="render" />
        </command>
         */
    static PFNGLPOLYGONOFFSETPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPOLYGONOFFSETPROC ) mygetprocaddr("glPolygonOffset");
    glfunc(factor_, units_);
    return;
}
void glPopDebugGroup (){
    /* <command>
            <proto>void <name>glPopDebugGroup</name></proto>
        </command>
         */
    static PFNGLPOPDEBUGGROUPPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPOPDEBUGGROUPPROC ) mygetprocaddr("glPopDebugGroup");
    glfunc();
    return;
}
void glPrimitiveRestartIndex (GLuint index_ ){
    /* <command>
            <proto>void <name>glPrimitiveRestartIndex</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
        </command>
         */
    static PFNGLPRIMITIVERESTARTINDEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPRIMITIVERESTARTINDEXPROC ) mygetprocaddr("glPrimitiveRestartIndex");
    glfunc(index_);
    return;
}
void glProgramBinary (GLuint program_ , GLenum binaryFormat_ , const void * binary_ , GLsizei length_ ){
    /* <command>
            <proto>void <name>glProgramBinary</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLenum</ptype> <name>binaryFormat</name></param>
            <param len="length">const void *<name>binary</name></param>
            <param><ptype>GLsizei</ptype> <name>length</name></param>
        </command>
         */
    static PFNGLPROGRAMBINARYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMBINARYPROC ) mygetprocaddr("glProgramBinary");
    glfunc(program_, binaryFormat_, binary_, length_);
    return;
}
void glProgramParameteri (GLuint program_ , GLenum pname_ , GLint value_ ){
    /* <command>
            <proto>void <name>glProgramParameteri</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param group="ProgramParameterPName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> <name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMPARAMETERIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMPARAMETERIPROC ) mygetprocaddr("glProgramParameteri");
    glfunc(program_, pname_, value_);
    return;
}
void glProgramUniform1d (GLuint program_ , GLint location_ , GLdouble v0_ ){
    /* <command>
            <proto>void <name>glProgramUniform1d</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLdouble</ptype> <name>v0</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM1DPROC ) mygetprocaddr("glProgramUniform1d");
    glfunc(program_, location_, v0_);
    return;
}
void glProgramUniform1dv (GLuint program_ , GLint location_ , GLsizei count_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform1dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="1">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM1DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM1DVPROC ) mygetprocaddr("glProgramUniform1dv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform1f (GLuint program_ , GLint location_ , GLfloat v0_ ){
    /* <command>
            <proto>void <name>glProgramUniform1f</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLfloat</ptype> <name>v0</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM1FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM1FPROC ) mygetprocaddr("glProgramUniform1f");
    glfunc(program_, location_, v0_);
    return;
}
void glProgramUniform1fv (GLuint program_ , GLint location_ , GLsizei count_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform1fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="1">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM1FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM1FVPROC ) mygetprocaddr("glProgramUniform1fv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform1i (GLuint program_ , GLint location_ , GLint v0_ ){
    /* <command>
            <proto>void <name>glProgramUniform1i</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLint</ptype> <name>v0</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM1IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM1IPROC ) mygetprocaddr("glProgramUniform1i");
    glfunc(program_, location_, v0_);
    return;
}
void glProgramUniform1iv (GLuint program_ , GLint location_ , GLsizei count_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform1iv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="1">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM1IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM1IVPROC ) mygetprocaddr("glProgramUniform1iv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform1ui (GLuint program_ , GLint location_ , GLuint v0_ ){
    /* <command>
            <proto>void <name>glProgramUniform1ui</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLuint</ptype> <name>v0</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM1UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM1UIPROC ) mygetprocaddr("glProgramUniform1ui");
    glfunc(program_, location_, v0_);
    return;
}
void glProgramUniform1uiv (GLuint program_ , GLint location_ , GLsizei count_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform1uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM1UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM1UIVPROC ) mygetprocaddr("glProgramUniform1uiv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform2d (GLuint program_ , GLint location_ , GLdouble v0_ , GLdouble v1_ ){
    /* <command>
            <proto>void <name>glProgramUniform2d</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLdouble</ptype> <name>v0</name></param>
            <param><ptype>GLdouble</ptype> <name>v1</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM2DPROC ) mygetprocaddr("glProgramUniform2d");
    glfunc(program_, location_, v0_, v1_);
    return;
}
void glProgramUniform2dv (GLuint program_ , GLint location_ , GLsizei count_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform2dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="2">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM2DVPROC ) mygetprocaddr("glProgramUniform2dv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform2f (GLuint program_ , GLint location_ , GLfloat v0_ , GLfloat v1_ ){
    /* <command>
            <proto>void <name>glProgramUniform2f</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLfloat</ptype> <name>v0</name></param>
            <param><ptype>GLfloat</ptype> <name>v1</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM2FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM2FPROC ) mygetprocaddr("glProgramUniform2f");
    glfunc(program_, location_, v0_, v1_);
    return;
}
void glProgramUniform2fv (GLuint program_ , GLint location_ , GLsizei count_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform2fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="2">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM2FVPROC ) mygetprocaddr("glProgramUniform2fv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform2i (GLuint program_ , GLint location_ , GLint v0_ , GLint v1_ ){
    /* <command>
            <proto>void <name>glProgramUniform2i</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLint</ptype> <name>v0</name></param>
            <param><ptype>GLint</ptype> <name>v1</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM2IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM2IPROC ) mygetprocaddr("glProgramUniform2i");
    glfunc(program_, location_, v0_, v1_);
    return;
}
void glProgramUniform2iv (GLuint program_ , GLint location_ , GLsizei count_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform2iv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="2">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM2IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM2IVPROC ) mygetprocaddr("glProgramUniform2iv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform2ui (GLuint program_ , GLint location_ , GLuint v0_ , GLuint v1_ ){
    /* <command>
            <proto>void <name>glProgramUniform2ui</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLuint</ptype> <name>v0</name></param>
            <param><ptype>GLuint</ptype> <name>v1</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM2UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM2UIPROC ) mygetprocaddr("glProgramUniform2ui");
    glfunc(program_, location_, v0_, v1_);
    return;
}
void glProgramUniform2uiv (GLuint program_ , GLint location_ , GLsizei count_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform2uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="2">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM2UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM2UIVPROC ) mygetprocaddr("glProgramUniform2uiv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform3d (GLuint program_ , GLint location_ , GLdouble v0_ , GLdouble v1_ , GLdouble v2_ ){
    /* <command>
            <proto>void <name>glProgramUniform3d</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLdouble</ptype> <name>v0</name></param>
            <param><ptype>GLdouble</ptype> <name>v1</name></param>
            <param><ptype>GLdouble</ptype> <name>v2</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM3DPROC ) mygetprocaddr("glProgramUniform3d");
    glfunc(program_, location_, v0_, v1_, v2_);
    return;
}
void glProgramUniform3dv (GLuint program_ , GLint location_ , GLsizei count_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform3dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="3">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM3DVPROC ) mygetprocaddr("glProgramUniform3dv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform3f (GLuint program_ , GLint location_ , GLfloat v0_ , GLfloat v1_ , GLfloat v2_ ){
    /* <command>
            <proto>void <name>glProgramUniform3f</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLfloat</ptype> <name>v0</name></param>
            <param><ptype>GLfloat</ptype> <name>v1</name></param>
            <param><ptype>GLfloat</ptype> <name>v2</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM3FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM3FPROC ) mygetprocaddr("glProgramUniform3f");
    glfunc(program_, location_, v0_, v1_, v2_);
    return;
}
void glProgramUniform3fv (GLuint program_ , GLint location_ , GLsizei count_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform3fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="3">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM3FVPROC ) mygetprocaddr("glProgramUniform3fv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform3i (GLuint program_ , GLint location_ , GLint v0_ , GLint v1_ , GLint v2_ ){
    /* <command>
            <proto>void <name>glProgramUniform3i</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLint</ptype> <name>v0</name></param>
            <param><ptype>GLint</ptype> <name>v1</name></param>
            <param><ptype>GLint</ptype> <name>v2</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM3IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM3IPROC ) mygetprocaddr("glProgramUniform3i");
    glfunc(program_, location_, v0_, v1_, v2_);
    return;
}
void glProgramUniform3iv (GLuint program_ , GLint location_ , GLsizei count_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform3iv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="3">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM3IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM3IVPROC ) mygetprocaddr("glProgramUniform3iv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform3ui (GLuint program_ , GLint location_ , GLuint v0_ , GLuint v1_ , GLuint v2_ ){
    /* <command>
            <proto>void <name>glProgramUniform3ui</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLuint</ptype> <name>v0</name></param>
            <param><ptype>GLuint</ptype> <name>v1</name></param>
            <param><ptype>GLuint</ptype> <name>v2</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM3UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM3UIPROC ) mygetprocaddr("glProgramUniform3ui");
    glfunc(program_, location_, v0_, v1_, v2_);
    return;
}
void glProgramUniform3uiv (GLuint program_ , GLint location_ , GLsizei count_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform3uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="3">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM3UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM3UIVPROC ) mygetprocaddr("glProgramUniform3uiv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform4d (GLuint program_ , GLint location_ , GLdouble v0_ , GLdouble v1_ , GLdouble v2_ , GLdouble v3_ ){
    /* <command>
            <proto>void <name>glProgramUniform4d</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLdouble</ptype> <name>v0</name></param>
            <param><ptype>GLdouble</ptype> <name>v1</name></param>
            <param><ptype>GLdouble</ptype> <name>v2</name></param>
            <param><ptype>GLdouble</ptype> <name>v3</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM4DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM4DPROC ) mygetprocaddr("glProgramUniform4d");
    glfunc(program_, location_, v0_, v1_, v2_, v3_);
    return;
}
void glProgramUniform4dv (GLuint program_ , GLint location_ , GLsizei count_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform4dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="4">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM4DVPROC ) mygetprocaddr("glProgramUniform4dv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform4f (GLuint program_ , GLint location_ , GLfloat v0_ , GLfloat v1_ , GLfloat v2_ , GLfloat v3_ ){
    /* <command>
            <proto>void <name>glProgramUniform4f</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLfloat</ptype> <name>v0</name></param>
            <param><ptype>GLfloat</ptype> <name>v1</name></param>
            <param><ptype>GLfloat</ptype> <name>v2</name></param>
            <param><ptype>GLfloat</ptype> <name>v3</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM4FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM4FPROC ) mygetprocaddr("glProgramUniform4f");
    glfunc(program_, location_, v0_, v1_, v2_, v3_);
    return;
}
void glProgramUniform4fv (GLuint program_ , GLint location_ , GLsizei count_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform4fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="4">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM4FVPROC ) mygetprocaddr("glProgramUniform4fv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform4i (GLuint program_ , GLint location_ , GLint v0_ , GLint v1_ , GLint v2_ , GLint v3_ ){
    /* <command>
            <proto>void <name>glProgramUniform4i</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLint</ptype> <name>v0</name></param>
            <param><ptype>GLint</ptype> <name>v1</name></param>
            <param><ptype>GLint</ptype> <name>v2</name></param>
            <param><ptype>GLint</ptype> <name>v3</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM4IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM4IPROC ) mygetprocaddr("glProgramUniform4i");
    glfunc(program_, location_, v0_, v1_, v2_, v3_);
    return;
}
void glProgramUniform4iv (GLuint program_ , GLint location_ , GLsizei count_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform4iv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="4">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM4IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM4IVPROC ) mygetprocaddr("glProgramUniform4iv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniform4ui (GLuint program_ , GLint location_ , GLuint v0_ , GLuint v1_ , GLuint v2_ , GLuint v3_ ){
    /* <command>
            <proto>void <name>glProgramUniform4ui</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLuint</ptype> <name>v0</name></param>
            <param><ptype>GLuint</ptype> <name>v1</name></param>
            <param><ptype>GLuint</ptype> <name>v2</name></param>
            <param><ptype>GLuint</ptype> <name>v3</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM4UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM4UIPROC ) mygetprocaddr("glProgramUniform4ui");
    glfunc(program_, location_, v0_, v1_, v2_, v3_);
    return;
}
void glProgramUniform4uiv (GLuint program_ , GLint location_ , GLsizei count_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glProgramUniform4uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="4">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORM4UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORM4UIVPROC ) mygetprocaddr("glProgramUniform4uiv");
    glfunc(program_, location_, count_, value_);
    return;
}
void glProgramUniformMatrix2dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix2dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="2">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX2DVPROC ) mygetprocaddr("glProgramUniformMatrix2dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix2fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix2fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="2">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX2FVPROC ) mygetprocaddr("glProgramUniformMatrix2fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix2x3dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix2x3dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX2X3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX2X3DVPROC ) mygetprocaddr("glProgramUniformMatrix2x3dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix2x3fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix2x3fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX2X3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX2X3FVPROC ) mygetprocaddr("glProgramUniformMatrix2x3fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix2x4dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix2x4dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX2X4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX2X4DVPROC ) mygetprocaddr("glProgramUniformMatrix2x4dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix2x4fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix2x4fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX2X4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX2X4FVPROC ) mygetprocaddr("glProgramUniformMatrix2x4fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix3dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix3dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="3">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX3DVPROC ) mygetprocaddr("glProgramUniformMatrix3dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix3fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix3fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="3">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX3FVPROC ) mygetprocaddr("glProgramUniformMatrix3fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix3x2dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix3x2dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX3X2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX3X2DVPROC ) mygetprocaddr("glProgramUniformMatrix3x2dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix3x2fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix3x2fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX3X2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX3X2FVPROC ) mygetprocaddr("glProgramUniformMatrix3x2fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix3x4dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix3x4dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX3X4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX3X4DVPROC ) mygetprocaddr("glProgramUniformMatrix3x4dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix3x4fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix3x4fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX3X4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX3X4FVPROC ) mygetprocaddr("glProgramUniformMatrix3x4fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix4dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix4dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="4">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX4DVPROC ) mygetprocaddr("glProgramUniformMatrix4dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix4fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix4fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="4">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX4FVPROC ) mygetprocaddr("glProgramUniformMatrix4fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix4x2dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix4x2dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX4X2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX4X2DVPROC ) mygetprocaddr("glProgramUniformMatrix4x2dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix4x2fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix4x2fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX4X2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX4X2FVPROC ) mygetprocaddr("glProgramUniformMatrix4x2fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix4x3dv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix4x3dv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX4X3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX4X3DVPROC ) mygetprocaddr("glProgramUniformMatrix4x3dv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProgramUniformMatrix4x3fv (GLuint program_ , GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glProgramUniformMatrix4x3fv</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLPROGRAMUNIFORMMATRIX4X3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROGRAMUNIFORMMATRIX4X3FVPROC ) mygetprocaddr("glProgramUniformMatrix4x3fv");
    glfunc(program_, location_, count_, transpose_, value_);
    return;
}
void glProvokingVertex (GLenum mode_ ){
    /* <command>
            <proto>void <name>glProvokingVertex</name></proto>
            <param><ptype>GLenum</ptype> <name>mode</name></param>
        </command>
         */
    static PFNGLPROVOKINGVERTEXPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPROVOKINGVERTEXPROC ) mygetprocaddr("glProvokingVertex");
    glfunc(mode_);
    return;
}
void glPushDebugGroup (GLenum source_ , GLuint id_ , GLsizei length_ , const GLchar * message_ ){
    /* <command>
            <proto>void <name>glPushDebugGroup</name></proto>
            <param><ptype>GLenum</ptype> <name>source</name></param>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLsizei</ptype> <name>length</name></param>
            <param len="COMPSIZE(message,length)">const <ptype>GLchar</ptype> *<name>message</name></param>
        </command>
         */
    static PFNGLPUSHDEBUGGROUPPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLPUSHDEBUGGROUPPROC ) mygetprocaddr("glPushDebugGroup");
    glfunc(source_, id_, length_, message_);
    return;
}
void glQueryCounter (GLuint id_ , GLenum target_ ){
    /* <command>
            <proto>void <name>glQueryCounter</name></proto>
            <param><ptype>GLuint</ptype> <name>id</name></param>
            <param><ptype>GLenum</ptype> <name>target</name></param>
        </command>
         */
    static PFNGLQUERYCOUNTERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLQUERYCOUNTERPROC ) mygetprocaddr("glQueryCounter");
    glfunc(id_, target_);
    return;
}
void glReadBuffer (GLenum src_ ){
    /* <command>
            <proto>void <name>glReadBuffer</name></proto>
            <param group="ReadBufferMode"><ptype>GLenum</ptype> <name>src</name></param>
            <glx opcode="171" type="render" />
        </command>
         */
    static PFNGLREADBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLREADBUFFERPROC ) mygetprocaddr("glReadBuffer");
    glfunc(src_);
    return;
}
void glReadPixels (GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ , GLenum format_ , GLenum type_ , void * pixels_ ){
    /* <command>
            <proto>void <name>glReadPixels</name></proto>
            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type,width,height)">void *<name>pixels</name></param>
            <glx opcode="111" type="single" />
            <glx comment="PBO protocol" name="glReadPixelsPBO" opcode="345" type="render" />
        </command>
         */
    static PFNGLREADPIXELSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLREADPIXELSPROC ) mygetprocaddr("glReadPixels");
    glfunc(x_, y_, width_, height_, format_, type_, pixels_);
    return;
}
void glReadnPixels (GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ , GLenum format_ , GLenum type_ , GLsizei bufSize_ , void * data_ ){
    /* <command>
            <proto>void <name>glReadnPixels</name></proto>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param><ptype>GLsizei</ptype> <name>bufSize</name></param>
            <param>void *<name>data</name></param>
        </command>
         */
    static PFNGLREADNPIXELSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLREADNPIXELSPROC ) mygetprocaddr("glReadnPixels");
    glfunc(x_, y_, width_, height_, format_, type_, bufSize_, data_);
    return;
}
void glReleaseShaderCompiler (){
    /* <command>
            <proto>void <name>glReleaseShaderCompiler</name></proto>
        </command>
         */
    static PFNGLRELEASESHADERCOMPILERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLRELEASESHADERCOMPILERPROC ) mygetprocaddr("glReleaseShaderCompiler");
    glfunc();
    return;
}
void glRenderbufferStorage (GLenum target_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glRenderbufferStorage</name></proto>
            <param group="RenderbufferTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <glx opcode="4318" type="render" />
        </command>
         */
    static PFNGLRENDERBUFFERSTORAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLRENDERBUFFERSTORAGEPROC ) mygetprocaddr("glRenderbufferStorage");
    glfunc(target_, internalformat_, width_, height_);
    return;
}
void glRenderbufferStorageMultisample (GLenum target_ , GLsizei samples_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glRenderbufferStorageMultisample</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizei</ptype> <name>samples</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <glx opcode="4331" type="render" />
        </command>
         */
    static PFNGLRENDERBUFFERSTORAGEMULTISAMPLEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLRENDERBUFFERSTORAGEMULTISAMPLEPROC ) mygetprocaddr("glRenderbufferStorageMultisample");
    glfunc(target_, samples_, internalformat_, width_, height_);
    return;
}
void glResumeTransformFeedback (){
    /* <command>
            <proto>void <name>glResumeTransformFeedback</name></proto>
        </command>
         */
    static PFNGLRESUMETRANSFORMFEEDBACKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLRESUMETRANSFORMFEEDBACKPROC ) mygetprocaddr("glResumeTransformFeedback");
    glfunc();
    return;
}
void glSampleCoverage (GLfloat value_ , GLboolean invert_ ){
    /* <command>
            <proto>void <name>glSampleCoverage</name></proto>
            <param><ptype>GLfloat</ptype> <name>value</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>invert</name></param>
            <glx opcode="229" type="render" />
        </command>
         */
    static PFNGLSAMPLECOVERAGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSAMPLECOVERAGEPROC ) mygetprocaddr("glSampleCoverage");
    glfunc(value_, invert_);
    return;
}
void glSampleMaski (GLuint maskNumber_ , GLbitfield mask_ ){
    /* <command>
            <proto>void <name>glSampleMaski</name></proto>
            <param><ptype>GLuint</ptype> <name>maskNumber</name></param>
            <param><ptype>GLbitfield</ptype> <name>mask</name></param>
        </command>
         */
    static PFNGLSAMPLEMASKIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSAMPLEMASKIPROC ) mygetprocaddr("glSampleMaski");
    glfunc(maskNumber_, mask_);
    return;
}
void glSamplerParameterIiv (GLuint sampler_ , GLenum pname_ , const GLint * param_ ){
    /* <command>
            <proto>void <name>glSamplerParameterIiv</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLSAMPLERPARAMETERIIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSAMPLERPARAMETERIIVPROC ) mygetprocaddr("glSamplerParameterIiv");
    glfunc(sampler_, pname_, param_);
    return;
}
void glSamplerParameterIuiv (GLuint sampler_ , GLenum pname_ , const GLuint * param_ ){
    /* <command>
            <proto>void <name>glSamplerParameterIuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)">const <ptype>GLuint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLSAMPLERPARAMETERIUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSAMPLERPARAMETERIUIVPROC ) mygetprocaddr("glSamplerParameterIuiv");
    glfunc(sampler_, pname_, param_);
    return;
}
void glSamplerParameterf (GLuint sampler_ , GLenum pname_ , GLfloat param_ ){
    /* <command>
            <proto>void <name>glSamplerParameterf</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLfloat</ptype> <name>param</name></param>
        </command>
         */
    static PFNGLSAMPLERPARAMETERFPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSAMPLERPARAMETERFPROC ) mygetprocaddr("glSamplerParameterf");
    glfunc(sampler_, pname_, param_);
    return;
}
void glSamplerParameterfv (GLuint sampler_ , GLenum pname_ , const GLfloat * param_ ){
    /* <command>
            <proto>void <name>glSamplerParameterfv</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)">const <ptype>GLfloat</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLSAMPLERPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSAMPLERPARAMETERFVPROC ) mygetprocaddr("glSamplerParameterfv");
    glfunc(sampler_, pname_, param_);
    return;
}
void glSamplerParameteri (GLuint sampler_ , GLenum pname_ , GLint param_ ){
    /* <command>
            <proto>void <name>glSamplerParameteri</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> <name>param</name></param>
        </command>
         */
    static PFNGLSAMPLERPARAMETERIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSAMPLERPARAMETERIPROC ) mygetprocaddr("glSamplerParameteri");
    glfunc(sampler_, pname_, param_);
    return;
}
void glSamplerParameteriv (GLuint sampler_ , GLenum pname_ , const GLint * param_ ){
    /* <command>
            <proto>void <name>glSamplerParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>sampler</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLSAMPLERPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSAMPLERPARAMETERIVPROC ) mygetprocaddr("glSamplerParameteriv");
    glfunc(sampler_, pname_, param_);
    return;
}
void glScissor (GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glScissor</name></proto>
            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <glx opcode="103" type="render" />
        </command>
         */
    static PFNGLSCISSORPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSCISSORPROC ) mygetprocaddr("glScissor");
    glfunc(x_, y_, width_, height_);
    return;
}
void glScissorArrayv (GLuint first_ , GLsizei count_ , const GLint * v_ ){
    /* <command>
            <proto>void <name>glScissorArrayv</name></proto>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="COMPSIZE(count)">const <ptype>GLint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLSCISSORARRAYVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSCISSORARRAYVPROC ) mygetprocaddr("glScissorArrayv");
    glfunc(first_, count_, v_);
    return;
}
void glScissorIndexed (GLuint index_ , GLint left_ , GLint bottom_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glScissorIndexed</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLint</ptype> <name>left</name></param>
            <param><ptype>GLint</ptype> <name>bottom</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLSCISSORINDEXEDPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSCISSORINDEXEDPROC ) mygetprocaddr("glScissorIndexed");
    glfunc(index_, left_, bottom_, width_, height_);
    return;
}
void glScissorIndexedv (GLuint index_ , const GLint * v_ ){
    /* <command>
            <proto>void <name>glScissorIndexedv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLSCISSORINDEXEDVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSCISSORINDEXEDVPROC ) mygetprocaddr("glScissorIndexedv");
    glfunc(index_, v_);
    return;
}
void glShaderBinary (GLsizei count_ , const GLuint * shaders_ , GLenum binaryformat_ , const void * binary_ , GLsizei length_ ){
    /* <command>
            <proto>void <name>glShaderBinary</name></proto>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>shaders</name></param>
            <param><ptype>GLenum</ptype> <name>binaryformat</name></param>
            <param len="length">const void *<name>binary</name></param>
            <param><ptype>GLsizei</ptype> <name>length</name></param>
        </command>
         */
    static PFNGLSHADERBINARYPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSHADERBINARYPROC ) mygetprocaddr("glShaderBinary");
    glfunc(count_, shaders_, binaryformat_, binary_, length_);
    return;
}
void glShaderSource (GLuint shader_ , GLsizei count_ , const GLchar ** string_ , const GLint * length_ ){
    /* <command>
            <proto>void <name>glShaderSource</name></proto>
            <param><ptype>GLuint</ptype> <name>shader</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLchar</ptype> *const*<name>string</name></param>
            <param len="count">const <ptype>GLint</ptype> *<name>length</name></param>
        </command>
         */
    static PFNGLSHADERSOURCEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSHADERSOURCEPROC ) mygetprocaddr("glShaderSource");
    glfunc(shader_, count_, string_, length_);
    return;
}
void glShaderStorageBlockBinding (GLuint program_ , GLuint storageBlockIndex_ , GLuint storageBlockBinding_ ){
    /* <command>
            <proto>void <name>glShaderStorageBlockBinding</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>storageBlockIndex</name></param>
            <param><ptype>GLuint</ptype> <name>storageBlockBinding</name></param>
        </command>
         */
    static PFNGLSHADERSTORAGEBLOCKBINDINGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSHADERSTORAGEBLOCKBINDINGPROC ) mygetprocaddr("glShaderStorageBlockBinding");
    glfunc(program_, storageBlockIndex_, storageBlockBinding_);
    return;
}
void glStencilFunc (GLenum func_ , GLint ref_ , GLuint mask_ ){
    /* <command>
            <proto>void <name>glStencilFunc</name></proto>
            <param group="StencilFunction"><ptype>GLenum</ptype> <name>func</name></param>
            <param group="StencilValue"><ptype>GLint</ptype> <name>ref</name></param>
            <param group="MaskedStencilValue"><ptype>GLuint</ptype> <name>mask</name></param>
            <glx opcode="162" type="render" />
        </command>
         */
    static PFNGLSTENCILFUNCPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSTENCILFUNCPROC ) mygetprocaddr("glStencilFunc");
    glfunc(func_, ref_, mask_);
    return;
}
void glStencilFuncSeparate (GLenum face_ , GLenum func_ , GLint ref_ , GLuint mask_ ){
    /* <command>
            <proto>void <name>glStencilFuncSeparate</name></proto>
            <param group="StencilFaceDirection"><ptype>GLenum</ptype> <name>face</name></param>
            <param group="StencilFunction"><ptype>GLenum</ptype> <name>func</name></param>
            <param group="StencilValue"><ptype>GLint</ptype> <name>ref</name></param>
            <param group="MaskedStencilValue"><ptype>GLuint</ptype> <name>mask</name></param>
        </command>
         */
    static PFNGLSTENCILFUNCSEPARATEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSTENCILFUNCSEPARATEPROC ) mygetprocaddr("glStencilFuncSeparate");
    glfunc(face_, func_, ref_, mask_);
    return;
}
void glStencilMask (GLuint mask_ ){
    /* <command>
            <proto>void <name>glStencilMask</name></proto>
            <param group="MaskedStencilValue"><ptype>GLuint</ptype> <name>mask</name></param>
            <glx opcode="133" type="render" />
        </command>
         */
    static PFNGLSTENCILMASKPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSTENCILMASKPROC ) mygetprocaddr("glStencilMask");
    glfunc(mask_);
    return;
}
void glStencilMaskSeparate (GLenum face_ , GLuint mask_ ){
    /* <command>
            <proto>void <name>glStencilMaskSeparate</name></proto>
            <param group="StencilFaceDirection"><ptype>GLenum</ptype> <name>face</name></param>
            <param group="MaskedStencilValue"><ptype>GLuint</ptype> <name>mask</name></param>
        </command>
         */
    static PFNGLSTENCILMASKSEPARATEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSTENCILMASKSEPARATEPROC ) mygetprocaddr("glStencilMaskSeparate");
    glfunc(face_, mask_);
    return;
}
void glStencilOp (GLenum fail_ , GLenum zfail_ , GLenum zpass_ ){
    /* <command>
            <proto>void <name>glStencilOp</name></proto>
            <param group="StencilOp"><ptype>GLenum</ptype> <name>fail</name></param>
            <param group="StencilOp"><ptype>GLenum</ptype> <name>zfail</name></param>
            <param group="StencilOp"><ptype>GLenum</ptype> <name>zpass</name></param>
            <glx opcode="163" type="render" />
        </command>
         */
    static PFNGLSTENCILOPPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSTENCILOPPROC ) mygetprocaddr("glStencilOp");
    glfunc(fail_, zfail_, zpass_);
    return;
}
void glStencilOpSeparate (GLenum face_ , GLenum sfail_ , GLenum dpfail_ , GLenum dppass_ ){
    /* <command>
            <proto>void <name>glStencilOpSeparate</name></proto>
            <param group="StencilFaceDirection"><ptype>GLenum</ptype> <name>face</name></param>
            <param group="StencilOp"><ptype>GLenum</ptype> <name>sfail</name></param>
            <param group="StencilOp"><ptype>GLenum</ptype> <name>dpfail</name></param>
            <param group="StencilOp"><ptype>GLenum</ptype> <name>dppass</name></param>
        </command>
         */
    static PFNGLSTENCILOPSEPARATEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLSTENCILOPSEPARATEPROC ) mygetprocaddr("glStencilOpSeparate");
    glfunc(face_, sfail_, dpfail_, dppass_);
    return;
}
void glTexBuffer (GLenum target_ , GLenum internalformat_ , GLuint buffer_ ){
    /* <command>
            <proto>void <name>glTexBuffer</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLTEXBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXBUFFERPROC ) mygetprocaddr("glTexBuffer");
    glfunc(target_, internalformat_, buffer_);
    return;
}
void glTexBufferRange (GLenum target_ , GLenum internalformat_ , GLuint buffer_ , GLintptr offset_ , GLsizeiptr size_ ){
    /* <command>
            <proto>void <name>glTexBufferRange</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param group="BufferOffset"><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
        </command>
         */
    static PFNGLTEXBUFFERRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXBUFFERRANGEPROC ) mygetprocaddr("glTexBufferRange");
    glfunc(target_, internalformat_, buffer_, offset_, size_);
    return;
}
void glTexImage1D (GLenum target_ , GLint level_ , GLint internalformat_ , GLsizei width_ , GLint border_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTexImage1D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="TextureComponentCount"><ptype>GLint</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type,width)">const void *<name>pixels</name></param>
            <glx opcode="109" type="render" />
            <glx comment="PBO protocol" name="glTexImage1DPBO" opcode="328" type="render" />
        </command>
         */
    static PFNGLTEXIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXIMAGE1DPROC ) mygetprocaddr("glTexImage1D");
    glfunc(target_, level_, internalformat_, width_, border_, format_, type_, pixels_);
    return;
}
void glTexImage2D (GLenum target_ , GLint level_ , GLint internalformat_ , GLsizei width_ , GLsizei height_ , GLint border_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTexImage2D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="TextureComponentCount"><ptype>GLint</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type,width,height)">const void *<name>pixels</name></param>
            <glx opcode="110" type="render" />
            <glx comment="PBO protocol" name="glTexImage2DPBO" opcode="329" type="render" />
        </command>
         */
    static PFNGLTEXIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXIMAGE2DPROC ) mygetprocaddr("glTexImage2D");
    glfunc(target_, level_, internalformat_, width_, height_, border_, format_, type_, pixels_);
    return;
}
void glTexImage3D (GLenum target_ , GLint level_ , GLint internalformat_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLint border_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTexImage3D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="TextureComponentCount"><ptype>GLint</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>border</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type,width,height,depth)">const void *<name>pixels</name></param>
            <glx opcode="4114" type="render" />
            <glx comment="PBO protocol" name="glTexImage3DPBO" opcode="330" type="render" />
        </command>
         */
    static PFNGLTEXIMAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXIMAGE3DPROC ) mygetprocaddr("glTexImage3D");
    glfunc(target_, level_, internalformat_, width_, height_, depth_, border_, format_, type_, pixels_);
    return;
}
void glTexParameterIiv (GLenum target_ , GLenum pname_ , const GLint * params_ ){
    /* <command>
            <proto>void <name>glTexParameterIiv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="346" type="render" />
        </command>
         */
    static PFNGLTEXPARAMETERIIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXPARAMETERIIVPROC ) mygetprocaddr("glTexParameterIiv");
    glfunc(target_, pname_, params_);
    return;
}
void glTexParameterIuiv (GLenum target_ , GLenum pname_ , const GLuint * params_ ){
    /* <command>
            <proto>void <name>glTexParameterIuiv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param len="COMPSIZE(pname)">const <ptype>GLuint</ptype> *<name>params</name></param>
            <glx opcode="347" type="render" />
        </command>
         */
    static PFNGLTEXPARAMETERIUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXPARAMETERIUIVPROC ) mygetprocaddr("glTexParameterIuiv");
    glfunc(target_, pname_, params_);
    return;
}
void glTexParameterf (GLenum target_ , GLenum pname_ , GLfloat param_ ){
    /* <command>
            <proto>void <name>glTexParameterf</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="CheckedFloat32"><ptype>GLfloat</ptype> <name>param</name></param>
            <glx opcode="105" type="render" />
        </command>
         */
    static PFNGLTEXPARAMETERFPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXPARAMETERFPROC ) mygetprocaddr("glTexParameterf");
    glfunc(target_, pname_, param_);
    return;
}
void glTexParameterfv (GLenum target_ , GLenum pname_ , const GLfloat * params_ ){
    /* <command>
            <proto>void <name>glTexParameterfv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="CheckedFloat32" len="COMPSIZE(pname)">const <ptype>GLfloat</ptype> *<name>params</name></param>
            <glx opcode="106" type="render" />
        </command>
         */
    static PFNGLTEXPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXPARAMETERFVPROC ) mygetprocaddr("glTexParameterfv");
    glfunc(target_, pname_, params_);
    return;
}
void glTexParameteri (GLenum target_ , GLenum pname_ , GLint param_ ){
    /* <command>
            <proto>void <name>glTexParameteri</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>param</name></param>
            <glx opcode="107" type="render" />
        </command>
         */
    static PFNGLTEXPARAMETERIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXPARAMETERIPROC ) mygetprocaddr("glTexParameteri");
    glfunc(target_, pname_, param_);
    return;
}
void glTexParameteriv (GLenum target_ , GLenum pname_ , const GLint * params_ ){
    /* <command>
            <proto>void <name>glTexParameteriv</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="TextureParameterName"><ptype>GLenum</ptype> <name>pname</name></param>
            <param group="CheckedInt32" len="COMPSIZE(pname)">const <ptype>GLint</ptype> *<name>params</name></param>
            <glx opcode="108" type="render" />
        </command>
         */
    static PFNGLTEXPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXPARAMETERIVPROC ) mygetprocaddr("glTexParameteriv");
    glfunc(target_, pname_, params_);
    return;
}
void glTexStorage1D (GLenum target_ , GLsizei levels_ , GLenum internalformat_ , GLsizei width_ ){
    /* <command>
            <proto>void <name>glTexStorage1D</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizei</ptype> <name>levels</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
        </command>
         */
    static PFNGLTEXSTORAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXSTORAGE1DPROC ) mygetprocaddr("glTexStorage1D");
    glfunc(target_, levels_, internalformat_, width_);
    return;
}
void glTexStorage2D (GLenum target_ , GLsizei levels_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glTexStorage2D</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizei</ptype> <name>levels</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLTEXSTORAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXSTORAGE2DPROC ) mygetprocaddr("glTexStorage2D");
    glfunc(target_, levels_, internalformat_, width_, height_);
    return;
}
void glTexStorage3D (GLenum target_ , GLsizei levels_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ ){
    /* <command>
            <proto>void <name>glTexStorage3D</name></proto>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLsizei</ptype> <name>levels</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
        </command>
         */
    static PFNGLTEXSTORAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXSTORAGE3DPROC ) mygetprocaddr("glTexStorage3D");
    glfunc(target_, levels_, internalformat_, width_, height_, depth_);
    return;
}
void glTexSubImage1D (GLenum target_ , GLint level_ , GLint xoffset_ , GLsizei width_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTexSubImage1D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type,width)">const void *<name>pixels</name></param>
            <glx opcode="4099" type="render" />
            <glx comment="PBO protocol" name="glTexSubImage1DPBO" opcode="331" type="render" />
        </command>
         */
    static PFNGLTEXSUBIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXSUBIMAGE1DPROC ) mygetprocaddr("glTexSubImage1D");
    glfunc(target_, level_, xoffset_, width_, format_, type_, pixels_);
    return;
}
void glTexSubImage2D (GLenum target_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLsizei width_ , GLsizei height_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTexSubImage2D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type,width,height)">const void *<name>pixels</name></param>
            <glx opcode="4100" type="render" />
            <glx comment="PBO protocol" name="glTexSubImage2DPBO" opcode="332" type="render" />
        </command>
         */
    static PFNGLTEXSUBIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXSUBIMAGE2DPROC ) mygetprocaddr("glTexSubImage2D");
    glfunc(target_, level_, xoffset_, yoffset_, width_, height_, format_, type_, pixels_);
    return;
}
void glTexSubImage3D (GLenum target_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTexSubImage3D</name></proto>
            <param group="TextureTarget"><ptype>GLenum</ptype> <name>target</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>level</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>xoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>yoffset</name></param>
            <param group="CheckedInt32"><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param group="PixelFormat"><ptype>GLenum</ptype> <name>format</name></param>
            <param group="PixelType"><ptype>GLenum</ptype> <name>type</name></param>
            <param len="COMPSIZE(format,type,width,height,depth)">const void *<name>pixels</name></param>
            <glx opcode="4115" type="render" />
            <glx comment="PBO protocol" name="glTexSubImage3DPBO" opcode="333" type="render" />
        </command>
         */
    static PFNGLTEXSUBIMAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXSUBIMAGE3DPROC ) mygetprocaddr("glTexSubImage3D");
    glfunc(target_, level_, xoffset_, yoffset_, zoffset_, width_, height_, depth_, format_, type_, pixels_);
    return;
}
void glTextureBarrier (){
    /* <command>
            <proto>void <name>glTextureBarrier</name></proto>
        </command>
         */
    static PFNGLTEXTUREBARRIERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREBARRIERPROC ) mygetprocaddr("glTextureBarrier");
    glfunc();
    return;
}
void glTextureBuffer (GLuint texture_ , GLenum internalformat_ , GLuint buffer_ ){
    /* <command>
            <proto>void <name>glTextureBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLTEXTUREBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREBUFFERPROC ) mygetprocaddr("glTextureBuffer");
    glfunc(texture_, internalformat_, buffer_);
    return;
}
void glTextureBufferRange (GLuint texture_ , GLenum internalformat_ , GLuint buffer_ , GLintptr offset_ , GLsizeiptr size_ ){
    /* <command>
            <proto>void <name>glTextureBufferRange</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
        </command>
         */
    static PFNGLTEXTUREBUFFERRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREBUFFERRANGEPROC ) mygetprocaddr("glTextureBufferRange");
    glfunc(texture_, internalformat_, buffer_, offset_, size_);
    return;
}
void glTextureParameterIiv (GLuint texture_ , GLenum pname_ , const GLint * params_ ){
    /* <command>
            <proto>void <name>glTextureParameterIiv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param>const <ptype>GLint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLTEXTUREPARAMETERIIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREPARAMETERIIVPROC ) mygetprocaddr("glTextureParameterIiv");
    glfunc(texture_, pname_, params_);
    return;
}
void glTextureParameterIuiv (GLuint texture_ , GLenum pname_ , const GLuint * params_ ){
    /* <command>
            <proto>void <name>glTextureParameterIuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param>const <ptype>GLuint</ptype> *<name>params</name></param>
        </command>
         */
    static PFNGLTEXTUREPARAMETERIUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREPARAMETERIUIVPROC ) mygetprocaddr("glTextureParameterIuiv");
    glfunc(texture_, pname_, params_);
    return;
}
void glTextureParameterf (GLuint texture_ , GLenum pname_ , GLfloat param_ ){
    /* <command>
            <proto>void <name>glTextureParameterf</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLfloat</ptype> <name>param</name></param>
        </command>
         */
    static PFNGLTEXTUREPARAMETERFPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREPARAMETERFPROC ) mygetprocaddr("glTextureParameterf");
    glfunc(texture_, pname_, param_);
    return;
}
void glTextureParameterfv (GLuint texture_ , GLenum pname_ , const GLfloat * param_ ){
    /* <command>
            <proto>void <name>glTextureParameterfv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param>const <ptype>GLfloat</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLTEXTUREPARAMETERFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREPARAMETERFVPROC ) mygetprocaddr("glTextureParameterfv");
    glfunc(texture_, pname_, param_);
    return;
}
void glTextureParameteri (GLuint texture_ , GLenum pname_ , GLint param_ ){
    /* <command>
            <proto>void <name>glTextureParameteri</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param><ptype>GLint</ptype> <name>param</name></param>
        </command>
         */
    static PFNGLTEXTUREPARAMETERIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREPARAMETERIPROC ) mygetprocaddr("glTextureParameteri");
    glfunc(texture_, pname_, param_);
    return;
}
void glTextureParameteriv (GLuint texture_ , GLenum pname_ , const GLint * param_ ){
    /* <command>
            <proto>void <name>glTextureParameteriv</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>pname</name></param>
            <param>const <ptype>GLint</ptype> *<name>param</name></param>
        </command>
         */
    static PFNGLTEXTUREPARAMETERIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREPARAMETERIVPROC ) mygetprocaddr("glTextureParameteriv");
    glfunc(texture_, pname_, param_);
    return;
}
void glTextureStorage1D (GLuint texture_ , GLsizei levels_ , GLenum internalformat_ , GLsizei width_ ){
    /* <command>
            <proto>void <name>glTextureStorage1D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLsizei</ptype> <name>levels</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
        </command>
         */
    static PFNGLTEXTURESTORAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTURESTORAGE1DPROC ) mygetprocaddr("glTextureStorage1D");
    glfunc(texture_, levels_, internalformat_, width_);
    return;
}
void glTextureStorage2D (GLuint texture_ , GLsizei levels_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glTextureStorage2D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLsizei</ptype> <name>levels</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
        </command>
         */
    static PFNGLTEXTURESTORAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTURESTORAGE2DPROC ) mygetprocaddr("glTextureStorage2D");
    glfunc(texture_, levels_, internalformat_, width_, height_);
    return;
}
void glTextureStorage3D (GLuint texture_ , GLsizei levels_ , GLenum internalformat_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ ){
    /* <command>
            <proto>void <name>glTextureStorage3D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLsizei</ptype> <name>levels</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
        </command>
         */
    static PFNGLTEXTURESTORAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTURESTORAGE3DPROC ) mygetprocaddr("glTextureStorage3D");
    glfunc(texture_, levels_, internalformat_, width_, height_, depth_);
    return;
}
void glTextureSubImage1D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLsizei width_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTextureSubImage1D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param>const void *<name>pixels</name></param>
        </command>
         */
    static PFNGLTEXTURESUBIMAGE1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTURESUBIMAGE1DPROC ) mygetprocaddr("glTextureSubImage1D");
    glfunc(texture_, level_, xoffset_, width_, format_, type_, pixels_);
    return;
}
void glTextureSubImage2D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLsizei width_ , GLsizei height_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTextureSubImage2D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param>const void *<name>pixels</name></param>
        </command>
         */
    static PFNGLTEXTURESUBIMAGE2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTURESUBIMAGE2DPROC ) mygetprocaddr("glTextureSubImage2D");
    glfunc(texture_, level_, xoffset_, yoffset_, width_, height_, format_, type_, pixels_);
    return;
}
void glTextureSubImage3D (GLuint texture_ , GLint level_ , GLint xoffset_ , GLint yoffset_ , GLint zoffset_ , GLsizei width_ , GLsizei height_ , GLsizei depth_ , GLenum format_ , GLenum type_ , const void * pixels_ ){
    /* <command>
            <proto>void <name>glTextureSubImage3D</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLint</ptype> <name>level</name></param>
            <param><ptype>GLint</ptype> <name>xoffset</name></param>
            <param><ptype>GLint</ptype> <name>yoffset</name></param>
            <param><ptype>GLint</ptype> <name>zoffset</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <param><ptype>GLsizei</ptype> <name>depth</name></param>
            <param><ptype>GLenum</ptype> <name>format</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param>const void *<name>pixels</name></param>
        </command>
         */
    static PFNGLTEXTURESUBIMAGE3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTURESUBIMAGE3DPROC ) mygetprocaddr("glTextureSubImage3D");
    glfunc(texture_, level_, xoffset_, yoffset_, zoffset_, width_, height_, depth_, format_, type_, pixels_);
    return;
}
void glTextureView (GLuint texture_ , GLenum target_ , GLuint origtexture_ , GLenum internalformat_ , GLuint minlevel_ , GLuint numlevels_ , GLuint minlayer_ , GLuint numlayers_ ){
    /* <command>
            <proto>void <name>glTextureView</name></proto>
            <param><ptype>GLuint</ptype> <name>texture</name></param>
            <param><ptype>GLenum</ptype> <name>target</name></param>
            <param><ptype>GLuint</ptype> <name>origtexture</name></param>
            <param><ptype>GLenum</ptype> <name>internalformat</name></param>
            <param><ptype>GLuint</ptype> <name>minlevel</name></param>
            <param><ptype>GLuint</ptype> <name>numlevels</name></param>
            <param><ptype>GLuint</ptype> <name>minlayer</name></param>
            <param><ptype>GLuint</ptype> <name>numlayers</name></param>
        </command>
         */
    static PFNGLTEXTUREVIEWPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTEXTUREVIEWPROC ) mygetprocaddr("glTextureView");
    glfunc(texture_, target_, origtexture_, internalformat_, minlevel_, numlevels_, minlayer_, numlayers_);
    return;
}
void glTransformFeedbackBufferBase (GLuint xfb_ , GLuint index_ , GLuint buffer_ ){
    /* <command>
            <proto>void <name>glTransformFeedbackBufferBase</name></proto>
            <param><ptype>GLuint</ptype> <name>xfb</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLTRANSFORMFEEDBACKBUFFERBASEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTRANSFORMFEEDBACKBUFFERBASEPROC ) mygetprocaddr("glTransformFeedbackBufferBase");
    glfunc(xfb_, index_, buffer_);
    return;
}
void glTransformFeedbackBufferRange (GLuint xfb_ , GLuint index_ , GLuint buffer_ , GLintptr offset_ , GLsizeiptr size_ ){
    /* <command>
            <proto>void <name>glTransformFeedbackBufferRange</name></proto>
            <param><ptype>GLuint</ptype> <name>xfb</name></param>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
            <param group="BufferSize"><ptype>GLsizeiptr</ptype> <name>size</name></param>
        </command>
         */
    static PFNGLTRANSFORMFEEDBACKBUFFERRANGEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTRANSFORMFEEDBACKBUFFERRANGEPROC ) mygetprocaddr("glTransformFeedbackBufferRange");
    glfunc(xfb_, index_, buffer_, offset_, size_);
    return;
}
void glTransformFeedbackVaryings (GLuint program_ , GLsizei count_ , const GLchar ** varyings_ , GLenum bufferMode_ ){
    /* <command>
            <proto>void <name>glTransformFeedbackVaryings</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLchar</ptype> *const*<name>varyings</name></param>
            <param><ptype>GLenum</ptype> <name>bufferMode</name></param>
        </command>
         */
    static PFNGLTRANSFORMFEEDBACKVARYINGSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLTRANSFORMFEEDBACKVARYINGSPROC ) mygetprocaddr("glTransformFeedbackVaryings");
    glfunc(program_, count_, varyings_, bufferMode_);
    return;
}
void glUniform1d (GLint location_ , GLdouble x_ ){
    /* <command>
            <proto>void <name>glUniform1d</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
        </command>
         */
    static PFNGLUNIFORM1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM1DPROC ) mygetprocaddr("glUniform1d");
    glfunc(location_, x_);
    return;
}
void glUniform1dv (GLint location_ , GLsizei count_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniform1dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*1">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM1DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM1DVPROC ) mygetprocaddr("glUniform1dv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform1f (GLint location_ , GLfloat v0_ ){
    /* <command>
            <proto>void <name>glUniform1f</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLfloat</ptype> <name>v0</name></param>
        </command>
         */
    static PFNGLUNIFORM1FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM1FPROC ) mygetprocaddr("glUniform1f");
    glfunc(location_, v0_);
    return;
}
void glUniform1fv (GLint location_ , GLsizei count_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniform1fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*1">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM1FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM1FVPROC ) mygetprocaddr("glUniform1fv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform1i (GLint location_ , GLint v0_ ){
    /* <command>
            <proto>void <name>glUniform1i</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLint</ptype> <name>v0</name></param>
        </command>
         */
    static PFNGLUNIFORM1IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM1IPROC ) mygetprocaddr("glUniform1i");
    glfunc(location_, v0_);
    return;
}
void glUniform1iv (GLint location_ , GLsizei count_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glUniform1iv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*1">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM1IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM1IVPROC ) mygetprocaddr("glUniform1iv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform1ui (GLint location_ , GLuint v0_ ){
    /* <command>
            <proto>void <name>glUniform1ui</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLuint</ptype> <name>v0</name></param>
        </command>
         */
    static PFNGLUNIFORM1UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM1UIPROC ) mygetprocaddr("glUniform1ui");
    glfunc(location_, v0_);
    return;
}
void glUniform1uiv (GLint location_ , GLsizei count_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glUniform1uiv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*1">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM1UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM1UIVPROC ) mygetprocaddr("glUniform1uiv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform2d (GLint location_ , GLdouble x_ , GLdouble y_ ){
    /* <command>
            <proto>void <name>glUniform2d</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
        </command>
         */
    static PFNGLUNIFORM2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM2DPROC ) mygetprocaddr("glUniform2d");
    glfunc(location_, x_, y_);
    return;
}
void glUniform2dv (GLint location_ , GLsizei count_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniform2dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*2">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM2DVPROC ) mygetprocaddr("glUniform2dv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform2f (GLint location_ , GLfloat v0_ , GLfloat v1_ ){
    /* <command>
            <proto>void <name>glUniform2f</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLfloat</ptype> <name>v0</name></param>
            <param><ptype>GLfloat</ptype> <name>v1</name></param>
        </command>
         */
    static PFNGLUNIFORM2FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM2FPROC ) mygetprocaddr("glUniform2f");
    glfunc(location_, v0_, v1_);
    return;
}
void glUniform2fv (GLint location_ , GLsizei count_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniform2fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*2">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM2FVPROC ) mygetprocaddr("glUniform2fv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform2i (GLint location_ , GLint v0_ , GLint v1_ ){
    /* <command>
            <proto>void <name>glUniform2i</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLint</ptype> <name>v0</name></param>
            <param><ptype>GLint</ptype> <name>v1</name></param>
        </command>
         */
    static PFNGLUNIFORM2IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM2IPROC ) mygetprocaddr("glUniform2i");
    glfunc(location_, v0_, v1_);
    return;
}
void glUniform2iv (GLint location_ , GLsizei count_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glUniform2iv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*2">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM2IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM2IVPROC ) mygetprocaddr("glUniform2iv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform2ui (GLint location_ , GLuint v0_ , GLuint v1_ ){
    /* <command>
            <proto>void <name>glUniform2ui</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLuint</ptype> <name>v0</name></param>
            <param><ptype>GLuint</ptype> <name>v1</name></param>
        </command>
         */
    static PFNGLUNIFORM2UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM2UIPROC ) mygetprocaddr("glUniform2ui");
    glfunc(location_, v0_, v1_);
    return;
}
void glUniform2uiv (GLint location_ , GLsizei count_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glUniform2uiv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*2">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM2UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM2UIVPROC ) mygetprocaddr("glUniform2uiv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform3d (GLint location_ , GLdouble x_ , GLdouble y_ , GLdouble z_ ){
    /* <command>
            <proto>void <name>glUniform3d</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
            <param><ptype>GLdouble</ptype> <name>z</name></param>
        </command>
         */
    static PFNGLUNIFORM3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM3DPROC ) mygetprocaddr("glUniform3d");
    glfunc(location_, x_, y_, z_);
    return;
}
void glUniform3dv (GLint location_ , GLsizei count_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniform3dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*3">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM3DVPROC ) mygetprocaddr("glUniform3dv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform3f (GLint location_ , GLfloat v0_ , GLfloat v1_ , GLfloat v2_ ){
    /* <command>
            <proto>void <name>glUniform3f</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLfloat</ptype> <name>v0</name></param>
            <param><ptype>GLfloat</ptype> <name>v1</name></param>
            <param><ptype>GLfloat</ptype> <name>v2</name></param>
        </command>
         */
    static PFNGLUNIFORM3FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM3FPROC ) mygetprocaddr("glUniform3f");
    glfunc(location_, v0_, v1_, v2_);
    return;
}
void glUniform3fv (GLint location_ , GLsizei count_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniform3fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*3">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM3FVPROC ) mygetprocaddr("glUniform3fv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform3i (GLint location_ , GLint v0_ , GLint v1_ , GLint v2_ ){
    /* <command>
            <proto>void <name>glUniform3i</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLint</ptype> <name>v0</name></param>
            <param><ptype>GLint</ptype> <name>v1</name></param>
            <param><ptype>GLint</ptype> <name>v2</name></param>
        </command>
         */
    static PFNGLUNIFORM3IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM3IPROC ) mygetprocaddr("glUniform3i");
    glfunc(location_, v0_, v1_, v2_);
    return;
}
void glUniform3iv (GLint location_ , GLsizei count_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glUniform3iv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*3">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM3IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM3IVPROC ) mygetprocaddr("glUniform3iv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform3ui (GLint location_ , GLuint v0_ , GLuint v1_ , GLuint v2_ ){
    /* <command>
            <proto>void <name>glUniform3ui</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLuint</ptype> <name>v0</name></param>
            <param><ptype>GLuint</ptype> <name>v1</name></param>
            <param><ptype>GLuint</ptype> <name>v2</name></param>
        </command>
         */
    static PFNGLUNIFORM3UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM3UIPROC ) mygetprocaddr("glUniform3ui");
    glfunc(location_, v0_, v1_, v2_);
    return;
}
void glUniform3uiv (GLint location_ , GLsizei count_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glUniform3uiv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*3">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM3UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM3UIVPROC ) mygetprocaddr("glUniform3uiv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform4d (GLint location_ , GLdouble x_ , GLdouble y_ , GLdouble z_ , GLdouble w_ ){
    /* <command>
            <proto>void <name>glUniform4d</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
            <param><ptype>GLdouble</ptype> <name>z</name></param>
            <param><ptype>GLdouble</ptype> <name>w</name></param>
        </command>
         */
    static PFNGLUNIFORM4DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM4DPROC ) mygetprocaddr("glUniform4d");
    glfunc(location_, x_, y_, z_, w_);
    return;
}
void glUniform4dv (GLint location_ , GLsizei count_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniform4dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*4">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM4DVPROC ) mygetprocaddr("glUniform4dv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform4f (GLint location_ , GLfloat v0_ , GLfloat v1_ , GLfloat v2_ , GLfloat v3_ ){
    /* <command>
            <proto>void <name>glUniform4f</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLfloat</ptype> <name>v0</name></param>
            <param><ptype>GLfloat</ptype> <name>v1</name></param>
            <param><ptype>GLfloat</ptype> <name>v2</name></param>
            <param><ptype>GLfloat</ptype> <name>v3</name></param>
        </command>
         */
    static PFNGLUNIFORM4FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM4FPROC ) mygetprocaddr("glUniform4f");
    glfunc(location_, v0_, v1_, v2_, v3_);
    return;
}
void glUniform4fv (GLint location_ , GLsizei count_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniform4fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*4">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM4FVPROC ) mygetprocaddr("glUniform4fv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform4i (GLint location_ , GLint v0_ , GLint v1_ , GLint v2_ , GLint v3_ ){
    /* <command>
            <proto>void <name>glUniform4i</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLint</ptype> <name>v0</name></param>
            <param><ptype>GLint</ptype> <name>v1</name></param>
            <param><ptype>GLint</ptype> <name>v2</name></param>
            <param><ptype>GLint</ptype> <name>v3</name></param>
        </command>
         */
    static PFNGLUNIFORM4IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM4IPROC ) mygetprocaddr("glUniform4i");
    glfunc(location_, v0_, v1_, v2_, v3_);
    return;
}
void glUniform4iv (GLint location_ , GLsizei count_ , const GLint * value_ ){
    /* <command>
            <proto>void <name>glUniform4iv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*4">const <ptype>GLint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM4IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM4IVPROC ) mygetprocaddr("glUniform4iv");
    glfunc(location_, count_, value_);
    return;
}
void glUniform4ui (GLint location_ , GLuint v0_ , GLuint v1_ , GLuint v2_ , GLuint v3_ ){
    /* <command>
            <proto>void <name>glUniform4ui</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLuint</ptype> <name>v0</name></param>
            <param><ptype>GLuint</ptype> <name>v1</name></param>
            <param><ptype>GLuint</ptype> <name>v2</name></param>
            <param><ptype>GLuint</ptype> <name>v3</name></param>
        </command>
         */
    static PFNGLUNIFORM4UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM4UIPROC ) mygetprocaddr("glUniform4ui");
    glfunc(location_, v0_, v1_, v2_, v3_);
    return;
}
void glUniform4uiv (GLint location_ , GLsizei count_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glUniform4uiv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count*4">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORM4UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORM4UIVPROC ) mygetprocaddr("glUniform4uiv");
    glfunc(location_, count_, value_);
    return;
}
void glUniformBlockBinding (GLuint program_ , GLuint uniformBlockIndex_ , GLuint uniformBlockBinding_ ){
    /* <command>
            <proto>void <name>glUniformBlockBinding</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
            <param><ptype>GLuint</ptype> <name>uniformBlockIndex</name></param>
            <param><ptype>GLuint</ptype> <name>uniformBlockBinding</name></param>
        </command>
         */
    static PFNGLUNIFORMBLOCKBINDINGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMBLOCKBINDINGPROC ) mygetprocaddr("glUniformBlockBinding");
    glfunc(program_, uniformBlockIndex_, uniformBlockBinding_);
    return;
}
void glUniformMatrix2dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix2dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*4">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX2DVPROC ) mygetprocaddr("glUniformMatrix2dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix2fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix2fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*4">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX2FVPROC ) mygetprocaddr("glUniformMatrix2fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix2x3dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix2x3dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*6">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX2X3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX2X3DVPROC ) mygetprocaddr("glUniformMatrix2x3dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix2x3fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix2x3fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*6">const <ptype>GLfloat</ptype> *<name>value</name></param>
            <glx opcode="305" type="render" />
        </command>
         */
    static PFNGLUNIFORMMATRIX2X3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX2X3FVPROC ) mygetprocaddr("glUniformMatrix2x3fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix2x4dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix2x4dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*8">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX2X4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX2X4DVPROC ) mygetprocaddr("glUniformMatrix2x4dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix2x4fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix2x4fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*8">const <ptype>GLfloat</ptype> *<name>value</name></param>
            <glx opcode="307" type="render" />
        </command>
         */
    static PFNGLUNIFORMMATRIX2X4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX2X4FVPROC ) mygetprocaddr("glUniformMatrix2x4fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix3dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix3dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*9">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX3DVPROC ) mygetprocaddr("glUniformMatrix3dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix3fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix3fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*9">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX3FVPROC ) mygetprocaddr("glUniformMatrix3fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix3x2dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix3x2dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*6">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX3X2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX3X2DVPROC ) mygetprocaddr("glUniformMatrix3x2dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix3x2fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix3x2fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*6">const <ptype>GLfloat</ptype> *<name>value</name></param>
            <glx opcode="306" type="render" />
        </command>
         */
    static PFNGLUNIFORMMATRIX3X2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX3X2FVPROC ) mygetprocaddr("glUniformMatrix3x2fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix3x4dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix3x4dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*12">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX3X4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX3X4DVPROC ) mygetprocaddr("glUniformMatrix3x4dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix3x4fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix3x4fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*12">const <ptype>GLfloat</ptype> *<name>value</name></param>
            <glx opcode="309" type="render" />
        </command>
         */
    static PFNGLUNIFORMMATRIX3X4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX3X4FVPROC ) mygetprocaddr("glUniformMatrix3x4fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix4dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix4dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*16">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX4DVPROC ) mygetprocaddr("glUniformMatrix4dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix4fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix4fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*16">const <ptype>GLfloat</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX4FVPROC ) mygetprocaddr("glUniformMatrix4fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix4x2dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix4x2dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*8">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX4X2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX4X2DVPROC ) mygetprocaddr("glUniformMatrix4x2dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix4x2fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix4x2fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*8">const <ptype>GLfloat</ptype> *<name>value</name></param>
            <glx opcode="308" type="render" />
        </command>
         */
    static PFNGLUNIFORMMATRIX4X2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX4X2FVPROC ) mygetprocaddr("glUniformMatrix4x2fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix4x3dv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLdouble * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix4x3dv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*12">const <ptype>GLdouble</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLUNIFORMMATRIX4X3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX4X3DVPROC ) mygetprocaddr("glUniformMatrix4x3dv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformMatrix4x3fv (GLint location_ , GLsizei count_ , GLboolean transpose_ , const GLfloat * value_ ){
    /* <command>
            <proto>void <name>glUniformMatrix4x3fv</name></proto>
            <param><ptype>GLint</ptype> <name>location</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>transpose</name></param>
            <param len="count*12">const <ptype>GLfloat</ptype> *<name>value</name></param>
            <glx opcode="310" type="render" />
        </command>
         */
    static PFNGLUNIFORMMATRIX4X3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMMATRIX4X3FVPROC ) mygetprocaddr("glUniformMatrix4x3fv");
    glfunc(location_, count_, transpose_, value_);
    return;
}
void glUniformSubroutinesuiv (GLenum shadertype_ , GLsizei count_ , const GLuint * indices_ ){
    /* <command>
            <proto>void <name>glUniformSubroutinesuiv</name></proto>
            <param><ptype>GLenum</ptype> <name>shadertype</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="count">const <ptype>GLuint</ptype> *<name>indices</name></param>
        </command>
         */
    static PFNGLUNIFORMSUBROUTINESUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNIFORMSUBROUTINESUIVPROC ) mygetprocaddr("glUniformSubroutinesuiv");
    glfunc(shadertype_, count_, indices_);
    return;
}
GLboolean glUnmapBuffer (GLenum target_ ){
    /* <command>
            <proto group="Boolean"><ptype>GLboolean</ptype> <name>glUnmapBuffer</name></proto>
            <param group="BufferTargetARB"><ptype>GLenum</ptype> <name>target</name></param>
        </command>
         */
    static PFNGLUNMAPBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNMAPBUFFERPROC ) mygetprocaddr("glUnmapBuffer");
    GLboolean retval = glfunc(target_);
    return retval;
}
GLboolean glUnmapNamedBuffer (GLuint buffer_ ){
    /* <command>
            <proto><ptype>GLboolean</ptype> <name>glUnmapNamedBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLUNMAPNAMEDBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUNMAPNAMEDBUFFERPROC ) mygetprocaddr("glUnmapNamedBuffer");
    GLboolean retval = glfunc(buffer_);
    return retval;
}
void glUseProgram (GLuint program_ ){
    /* <command>
            <proto>void <name>glUseProgram</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
        </command>
         */
    static PFNGLUSEPROGRAMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUSEPROGRAMPROC ) mygetprocaddr("glUseProgram");
    glfunc(program_);
    return;
}
void glUseProgramStages (GLuint pipeline_ , GLbitfield stages_ , GLuint program_ ){
    /* <command>
            <proto>void <name>glUseProgramStages</name></proto>
            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
            <param><ptype>GLbitfield</ptype> <name>stages</name></param>
            <param><ptype>GLuint</ptype> <name>program</name></param>
        </command>
         */
    static PFNGLUSEPROGRAMSTAGESPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLUSEPROGRAMSTAGESPROC ) mygetprocaddr("glUseProgramStages");
    glfunc(pipeline_, stages_, program_);
    return;
}
void glValidateProgram (GLuint program_ ){
    /* <command>
            <proto>void <name>glValidateProgram</name></proto>
            <param><ptype>GLuint</ptype> <name>program</name></param>
        </command>
         */
    static PFNGLVALIDATEPROGRAMPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVALIDATEPROGRAMPROC ) mygetprocaddr("glValidateProgram");
    glfunc(program_);
    return;
}
void glValidateProgramPipeline (GLuint pipeline_ ){
    /* <command>
            <proto>void <name>glValidateProgramPipeline</name></proto>
            <param><ptype>GLuint</ptype> <name>pipeline</name></param>
        </command>
         */
    static PFNGLVALIDATEPROGRAMPIPELINEPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVALIDATEPROGRAMPIPELINEPROC ) mygetprocaddr("glValidateProgramPipeline");
    glfunc(pipeline_);
    return;
}
void glVertexArrayAttribBinding (GLuint vaobj_ , GLuint attribindex_ , GLuint bindingindex_ ){
    /* <command>
            <proto>void <name>glVertexArrayAttribBinding</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>attribindex</name></param>
            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
        </command>
         */
    static PFNGLVERTEXARRAYATTRIBBINDINGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXARRAYATTRIBBINDINGPROC ) mygetprocaddr("glVertexArrayAttribBinding");
    glfunc(vaobj_, attribindex_, bindingindex_);
    return;
}
void glVertexArrayAttribFormat (GLuint vaobj_ , GLuint attribindex_ , GLint size_ , GLenum type_ , GLboolean normalized_ , GLuint relativeoffset_ ){
    /* <command>
            <proto>void <name>glVertexArrayAttribFormat</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>attribindex</name></param>
            <param><ptype>GLint</ptype> <name>size</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param><ptype>GLuint</ptype> <name>relativeoffset</name></param>
        </command>
         */
    static PFNGLVERTEXARRAYATTRIBFORMATPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXARRAYATTRIBFORMATPROC ) mygetprocaddr("glVertexArrayAttribFormat");
    glfunc(vaobj_, attribindex_, size_, type_, normalized_, relativeoffset_);
    return;
}
void glVertexArrayBindingDivisor (GLuint vaobj_ , GLuint bindingindex_ , GLuint divisor_ ){
    /* <command>
            <proto>void <name>glVertexArrayBindingDivisor</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
            <param><ptype>GLuint</ptype> <name>divisor</name></param>
        </command>
         */
    static PFNGLVERTEXARRAYBINDINGDIVISORPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXARRAYBINDINGDIVISORPROC ) mygetprocaddr("glVertexArrayBindingDivisor");
    glfunc(vaobj_, bindingindex_, divisor_);
    return;
}
void glVertexArrayElementBuffer (GLuint vaobj_ , GLuint buffer_ ){
    /* <command>
            <proto>void <name>glVertexArrayElementBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
        </command>
         */
    static PFNGLVERTEXARRAYELEMENTBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXARRAYELEMENTBUFFERPROC ) mygetprocaddr("glVertexArrayElementBuffer");
    glfunc(vaobj_, buffer_);
    return;
}
void glVertexArrayVertexBuffer (GLuint vaobj_ , GLuint bindingindex_ , GLuint buffer_ , GLintptr offset_ , GLsizei stride_ ){
    /* <command>
            <proto>void <name>glVertexArrayVertexBuffer</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
            <param><ptype>GLuint</ptype> <name>buffer</name></param>
            <param><ptype>GLintptr</ptype> <name>offset</name></param>
            <param><ptype>GLsizei</ptype> <name>stride</name></param>
        </command>
         */
    static PFNGLVERTEXARRAYVERTEXBUFFERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXARRAYVERTEXBUFFERPROC ) mygetprocaddr("glVertexArrayVertexBuffer");
    glfunc(vaobj_, bindingindex_, buffer_, offset_, stride_);
    return;
}
void glVertexArrayVertexBuffers (GLuint vaobj_ , GLuint first_ , GLsizei count_ , const GLuint * buffers_ , const GLintptr * offsets_ , const GLsizei * strides_ ){
    /* <command>
            <proto>void <name>glVertexArrayVertexBuffers</name></proto>
            <param><ptype>GLuint</ptype> <name>vaobj</name></param>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param>const <ptype>GLuint</ptype> *<name>buffers</name></param>
            <param>const <ptype>GLintptr</ptype> *<name>offsets</name></param>
            <param>const <ptype>GLsizei</ptype> *<name>strides</name></param>
        </command>
         */
    static PFNGLVERTEXARRAYVERTEXBUFFERSPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXARRAYVERTEXBUFFERSPROC ) mygetprocaddr("glVertexArrayVertexBuffers");
    glfunc(vaobj_, first_, count_, buffers_, offsets_, strides_);
    return;
}
void glVertexAttrib1d (GLuint index_ , GLdouble x_ ){
    /* <command>
            <proto>void <name>glVertexAttrib1d</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <vecequiv name="glVertexAttrib1dv" />
        </command>
         */
    static PFNGLVERTEXATTRIB1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB1DPROC ) mygetprocaddr("glVertexAttrib1d");
    glfunc(index_, x_);
    return;
}
void glVertexAttrib1dv (GLuint index_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib1dv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="1">const <ptype>GLdouble</ptype> *<name>v</name></param>
            <glx opcode="4197" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB1DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB1DVPROC ) mygetprocaddr("glVertexAttrib1dv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib1f (GLuint index_ , GLfloat x_ ){
    /* <command>
            <proto>void <name>glVertexAttrib1f</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLfloat</ptype> <name>x</name></param>
            <vecequiv name="glVertexAttrib1fv" />
        </command>
         */
    static PFNGLVERTEXATTRIB1FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB1FPROC ) mygetprocaddr("glVertexAttrib1f");
    glfunc(index_, x_);
    return;
}
void glVertexAttrib1fv (GLuint index_ , const GLfloat * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib1fv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="1">const <ptype>GLfloat</ptype> *<name>v</name></param>
            <glx opcode="4193" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB1FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB1FVPROC ) mygetprocaddr("glVertexAttrib1fv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib1s (GLuint index_ , GLshort x_ ){
    /* <command>
            <proto>void <name>glVertexAttrib1s</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLshort</ptype> <name>x</name></param>
            <vecequiv name="glVertexAttrib1sv" />
        </command>
         */
    static PFNGLVERTEXATTRIB1SPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB1SPROC ) mygetprocaddr("glVertexAttrib1s");
    glfunc(index_, x_);
    return;
}
void glVertexAttrib1sv (GLuint index_ , const GLshort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib1sv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="1">const <ptype>GLshort</ptype> *<name>v</name></param>
            <glx opcode="4189" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB1SVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB1SVPROC ) mygetprocaddr("glVertexAttrib1sv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib2d (GLuint index_ , GLdouble x_ , GLdouble y_ ){
    /* <command>
            <proto>void <name>glVertexAttrib2d</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
            <vecequiv name="glVertexAttrib2dv" />
        </command>
         */
    static PFNGLVERTEXATTRIB2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB2DPROC ) mygetprocaddr("glVertexAttrib2d");
    glfunc(index_, x_, y_);
    return;
}
void glVertexAttrib2dv (GLuint index_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib2dv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="2">const <ptype>GLdouble</ptype> *<name>v</name></param>
            <glx opcode="4198" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB2DVPROC ) mygetprocaddr("glVertexAttrib2dv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib2f (GLuint index_ , GLfloat x_ , GLfloat y_ ){
    /* <command>
            <proto>void <name>glVertexAttrib2f</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLfloat</ptype> <name>x</name></param>
            <param><ptype>GLfloat</ptype> <name>y</name></param>
            <vecequiv name="glVertexAttrib2fv" />
        </command>
         */
    static PFNGLVERTEXATTRIB2FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB2FPROC ) mygetprocaddr("glVertexAttrib2f");
    glfunc(index_, x_, y_);
    return;
}
void glVertexAttrib2fv (GLuint index_ , const GLfloat * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib2fv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="2">const <ptype>GLfloat</ptype> *<name>v</name></param>
            <glx opcode="4194" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB2FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB2FVPROC ) mygetprocaddr("glVertexAttrib2fv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib2s (GLuint index_ , GLshort x_ , GLshort y_ ){
    /* <command>
            <proto>void <name>glVertexAttrib2s</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLshort</ptype> <name>x</name></param>
            <param><ptype>GLshort</ptype> <name>y</name></param>
            <vecequiv name="glVertexAttrib2sv" />
        </command>
         */
    static PFNGLVERTEXATTRIB2SPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB2SPROC ) mygetprocaddr("glVertexAttrib2s");
    glfunc(index_, x_, y_);
    return;
}
void glVertexAttrib2sv (GLuint index_ , const GLshort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib2sv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="2">const <ptype>GLshort</ptype> *<name>v</name></param>
            <glx opcode="4190" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB2SVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB2SVPROC ) mygetprocaddr("glVertexAttrib2sv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib3d (GLuint index_ , GLdouble x_ , GLdouble y_ , GLdouble z_ ){
    /* <command>
            <proto>void <name>glVertexAttrib3d</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
            <param><ptype>GLdouble</ptype> <name>z</name></param>
            <vecequiv name="glVertexAttrib3dv" />
        </command>
         */
    static PFNGLVERTEXATTRIB3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB3DPROC ) mygetprocaddr("glVertexAttrib3d");
    glfunc(index_, x_, y_, z_);
    return;
}
void glVertexAttrib3dv (GLuint index_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib3dv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="3">const <ptype>GLdouble</ptype> *<name>v</name></param>
            <glx opcode="4199" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB3DVPROC ) mygetprocaddr("glVertexAttrib3dv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib3f (GLuint index_ , GLfloat x_ , GLfloat y_ , GLfloat z_ ){
    /* <command>
            <proto>void <name>glVertexAttrib3f</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLfloat</ptype> <name>x</name></param>
            <param><ptype>GLfloat</ptype> <name>y</name></param>
            <param><ptype>GLfloat</ptype> <name>z</name></param>
            <vecequiv name="glVertexAttrib3fv" />
        </command>
         */
    static PFNGLVERTEXATTRIB3FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB3FPROC ) mygetprocaddr("glVertexAttrib3f");
    glfunc(index_, x_, y_, z_);
    return;
}
void glVertexAttrib3fv (GLuint index_ , const GLfloat * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib3fv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="3">const <ptype>GLfloat</ptype> *<name>v</name></param>
            <glx opcode="4195" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB3FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB3FVPROC ) mygetprocaddr("glVertexAttrib3fv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib3s (GLuint index_ , GLshort x_ , GLshort y_ , GLshort z_ ){
    /* <command>
            <proto>void <name>glVertexAttrib3s</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLshort</ptype> <name>x</name></param>
            <param><ptype>GLshort</ptype> <name>y</name></param>
            <param><ptype>GLshort</ptype> <name>z</name></param>
            <vecequiv name="glVertexAttrib3sv" />
        </command>
         */
    static PFNGLVERTEXATTRIB3SPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB3SPROC ) mygetprocaddr("glVertexAttrib3s");
    glfunc(index_, x_, y_, z_);
    return;
}
void glVertexAttrib3sv (GLuint index_ , const GLshort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib3sv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="3">const <ptype>GLshort</ptype> *<name>v</name></param>
            <glx opcode="4191" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB3SVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB3SVPROC ) mygetprocaddr("glVertexAttrib3sv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4Nbv (GLuint index_ , const GLbyte * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4Nbv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLbyte</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4NBVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4NBVPROC ) mygetprocaddr("glVertexAttrib4Nbv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4Niv (GLuint index_ , const GLint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4Niv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4NIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4NIVPROC ) mygetprocaddr("glVertexAttrib4Niv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4Nsv (GLuint index_ , const GLshort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4Nsv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLshort</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4NSVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4NSVPROC ) mygetprocaddr("glVertexAttrib4Nsv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4Nub (GLuint index_ , GLubyte x_ , GLubyte y_ , GLubyte z_ , GLubyte w_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4Nub</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLubyte</ptype> <name>x</name></param>
            <param><ptype>GLubyte</ptype> <name>y</name></param>
            <param><ptype>GLubyte</ptype> <name>z</name></param>
            <param><ptype>GLubyte</ptype> <name>w</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4NUBPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4NUBPROC ) mygetprocaddr("glVertexAttrib4Nub");
    glfunc(index_, x_, y_, z_, w_);
    return;
}
void glVertexAttrib4Nubv (GLuint index_ , const GLubyte * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4Nubv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLubyte</ptype> *<name>v</name></param>
            <glx opcode="4201" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB4NUBVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4NUBVPROC ) mygetprocaddr("glVertexAttrib4Nubv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4Nuiv (GLuint index_ , const GLuint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4Nuiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLuint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4NUIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4NUIVPROC ) mygetprocaddr("glVertexAttrib4Nuiv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4Nusv (GLuint index_ , const GLushort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4Nusv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLushort</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4NUSVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4NUSVPROC ) mygetprocaddr("glVertexAttrib4Nusv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4bv (GLuint index_ , const GLbyte * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4bv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLbyte</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4BVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4BVPROC ) mygetprocaddr("glVertexAttrib4bv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4d (GLuint index_ , GLdouble x_ , GLdouble y_ , GLdouble z_ , GLdouble w_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4d</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
            <param><ptype>GLdouble</ptype> <name>z</name></param>
            <param><ptype>GLdouble</ptype> <name>w</name></param>
            <vecequiv name="glVertexAttrib4dv" />
        </command>
         */
    static PFNGLVERTEXATTRIB4DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4DPROC ) mygetprocaddr("glVertexAttrib4d");
    glfunc(index_, x_, y_, z_, w_);
    return;
}
void glVertexAttrib4dv (GLuint index_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4dv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLdouble</ptype> *<name>v</name></param>
            <glx opcode="4200" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4DVPROC ) mygetprocaddr("glVertexAttrib4dv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4f (GLuint index_ , GLfloat x_ , GLfloat y_ , GLfloat z_ , GLfloat w_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4f</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLfloat</ptype> <name>x</name></param>
            <param><ptype>GLfloat</ptype> <name>y</name></param>
            <param><ptype>GLfloat</ptype> <name>z</name></param>
            <param><ptype>GLfloat</ptype> <name>w</name></param>
            <vecequiv name="glVertexAttrib4fv" />
        </command>
         */
    static PFNGLVERTEXATTRIB4FPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4FPROC ) mygetprocaddr("glVertexAttrib4f");
    glfunc(index_, x_, y_, z_, w_);
    return;
}
void glVertexAttrib4fv (GLuint index_ , const GLfloat * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4fv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLfloat</ptype> *<name>v</name></param>
            <glx opcode="4196" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB4FVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4FVPROC ) mygetprocaddr("glVertexAttrib4fv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4iv (GLuint index_ , const GLint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4iv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4IVPROC ) mygetprocaddr("glVertexAttrib4iv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4s (GLuint index_ , GLshort x_ , GLshort y_ , GLshort z_ , GLshort w_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4s</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLshort</ptype> <name>x</name></param>
            <param><ptype>GLshort</ptype> <name>y</name></param>
            <param><ptype>GLshort</ptype> <name>z</name></param>
            <param><ptype>GLshort</ptype> <name>w</name></param>
            <vecequiv name="glVertexAttrib4sv" />
        </command>
         */
    static PFNGLVERTEXATTRIB4SPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4SPROC ) mygetprocaddr("glVertexAttrib4s");
    glfunc(index_, x_, y_, z_, w_);
    return;
}
void glVertexAttrib4sv (GLuint index_ , const GLshort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4sv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLshort</ptype> *<name>v</name></param>
            <glx opcode="4192" type="render" />
        </command>
         */
    static PFNGLVERTEXATTRIB4SVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4SVPROC ) mygetprocaddr("glVertexAttrib4sv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4ubv (GLuint index_ , const GLubyte * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4ubv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLubyte</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4UBVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4UBVPROC ) mygetprocaddr("glVertexAttrib4ubv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4uiv (GLuint index_ , const GLuint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLuint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4UIVPROC ) mygetprocaddr("glVertexAttrib4uiv");
    glfunc(index_, v_);
    return;
}
void glVertexAttrib4usv (GLuint index_ , const GLushort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttrib4usv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLushort</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIB4USVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIB4USVPROC ) mygetprocaddr("glVertexAttrib4usv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribBinding (GLuint attribindex_ , GLuint bindingindex_ ){
    /* <command>
            <proto>void <name>glVertexAttribBinding</name></proto>
            <param><ptype>GLuint</ptype> <name>attribindex</name></param>
            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBBINDINGPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBBINDINGPROC ) mygetprocaddr("glVertexAttribBinding");
    glfunc(attribindex_, bindingindex_);
    return;
}
void glVertexAttribDivisor (GLuint index_ , GLuint divisor_ ){
    /* <command>
            <proto>void <name>glVertexAttribDivisor</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>divisor</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBDIVISORPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBDIVISORPROC ) mygetprocaddr("glVertexAttribDivisor");
    glfunc(index_, divisor_);
    return;
}
void glVertexAttribFormat (GLuint attribindex_ , GLint size_ , GLenum type_ , GLboolean normalized_ , GLuint relativeoffset_ ){
    /* <command>
            <proto>void <name>glVertexAttribFormat</name></proto>
            <param><ptype>GLuint</ptype> <name>attribindex</name></param>
            <param><ptype>GLint</ptype> <name>size</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param><ptype>GLuint</ptype> <name>relativeoffset</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBFORMATPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBFORMATPROC ) mygetprocaddr("glVertexAttribFormat");
    glfunc(attribindex_, size_, type_, normalized_, relativeoffset_);
    return;
}
void glVertexAttribI1i (GLuint index_ , GLint x_ ){
    /* <command>
            <proto>void <name>glVertexAttribI1i</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <vecequiv name="glVertexAttribI1iv" />
        </command>
         */
    static PFNGLVERTEXATTRIBI1IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI1IPROC ) mygetprocaddr("glVertexAttribI1i");
    glfunc(index_, x_);
    return;
}
void glVertexAttribI1iv (GLuint index_ , const GLint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI1iv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="1">const <ptype>GLint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI1IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI1IVPROC ) mygetprocaddr("glVertexAttribI1iv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI1ui (GLuint index_ , GLuint x_ ){
    /* <command>
            <proto>void <name>glVertexAttribI1ui</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>x</name></param>
            <vecequiv name="glVertexAttribI1uiv" />
        </command>
         */
    static PFNGLVERTEXATTRIBI1UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI1UIPROC ) mygetprocaddr("glVertexAttribI1ui");
    glfunc(index_, x_);
    return;
}
void glVertexAttribI1uiv (GLuint index_ , const GLuint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI1uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="1">const <ptype>GLuint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI1UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI1UIVPROC ) mygetprocaddr("glVertexAttribI1uiv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI2i (GLuint index_ , GLint x_ , GLint y_ ){
    /* <command>
            <proto>void <name>glVertexAttribI2i</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <vecequiv name="glVertexAttribI2iv" />
        </command>
         */
    static PFNGLVERTEXATTRIBI2IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI2IPROC ) mygetprocaddr("glVertexAttribI2i");
    glfunc(index_, x_, y_);
    return;
}
void glVertexAttribI2iv (GLuint index_ , const GLint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI2iv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="2">const <ptype>GLint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI2IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI2IVPROC ) mygetprocaddr("glVertexAttribI2iv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI2ui (GLuint index_ , GLuint x_ , GLuint y_ ){
    /* <command>
            <proto>void <name>glVertexAttribI2ui</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>x</name></param>
            <param><ptype>GLuint</ptype> <name>y</name></param>
            <vecequiv name="glVertexAttribI2uiv" />
        </command>
         */
    static PFNGLVERTEXATTRIBI2UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI2UIPROC ) mygetprocaddr("glVertexAttribI2ui");
    glfunc(index_, x_, y_);
    return;
}
void glVertexAttribI2uiv (GLuint index_ , const GLuint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI2uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="2">const <ptype>GLuint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI2UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI2UIVPROC ) mygetprocaddr("glVertexAttribI2uiv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI3i (GLuint index_ , GLint x_ , GLint y_ , GLint z_ ){
    /* <command>
            <proto>void <name>glVertexAttribI3i</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLint</ptype> <name>z</name></param>
            <vecequiv name="glVertexAttribI3iv" />
        </command>
         */
    static PFNGLVERTEXATTRIBI3IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI3IPROC ) mygetprocaddr("glVertexAttribI3i");
    glfunc(index_, x_, y_, z_);
    return;
}
void glVertexAttribI3iv (GLuint index_ , const GLint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI3iv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="3">const <ptype>GLint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI3IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI3IVPROC ) mygetprocaddr("glVertexAttribI3iv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI3ui (GLuint index_ , GLuint x_ , GLuint y_ , GLuint z_ ){
    /* <command>
            <proto>void <name>glVertexAttribI3ui</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>x</name></param>
            <param><ptype>GLuint</ptype> <name>y</name></param>
            <param><ptype>GLuint</ptype> <name>z</name></param>
            <vecequiv name="glVertexAttribI3uiv" />
        </command>
         */
    static PFNGLVERTEXATTRIBI3UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI3UIPROC ) mygetprocaddr("glVertexAttribI3ui");
    glfunc(index_, x_, y_, z_);
    return;
}
void glVertexAttribI3uiv (GLuint index_ , const GLuint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI3uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="3">const <ptype>GLuint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI3UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI3UIVPROC ) mygetprocaddr("glVertexAttribI3uiv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI4bv (GLuint index_ , const GLbyte * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI4bv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLbyte</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI4BVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI4BVPROC ) mygetprocaddr("glVertexAttribI4bv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI4i (GLuint index_ , GLint x_ , GLint y_ , GLint z_ , GLint w_ ){
    /* <command>
            <proto>void <name>glVertexAttribI4i</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLint</ptype> <name>x</name></param>
            <param><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLint</ptype> <name>z</name></param>
            <param><ptype>GLint</ptype> <name>w</name></param>
            <vecequiv name="glVertexAttribI4iv" />
        </command>
         */
    static PFNGLVERTEXATTRIBI4IPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI4IPROC ) mygetprocaddr("glVertexAttribI4i");
    glfunc(index_, x_, y_, z_, w_);
    return;
}
void glVertexAttribI4iv (GLuint index_ , const GLint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI4iv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI4IVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI4IVPROC ) mygetprocaddr("glVertexAttribI4iv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI4sv (GLuint index_ , const GLshort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI4sv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLshort</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI4SVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI4SVPROC ) mygetprocaddr("glVertexAttribI4sv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI4ubv (GLuint index_ , const GLubyte * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI4ubv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLubyte</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI4UBVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI4UBVPROC ) mygetprocaddr("glVertexAttribI4ubv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI4ui (GLuint index_ , GLuint x_ , GLuint y_ , GLuint z_ , GLuint w_ ){
    /* <command>
            <proto>void <name>glVertexAttribI4ui</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLuint</ptype> <name>x</name></param>
            <param><ptype>GLuint</ptype> <name>y</name></param>
            <param><ptype>GLuint</ptype> <name>z</name></param>
            <param><ptype>GLuint</ptype> <name>w</name></param>
            <vecequiv name="glVertexAttribI4uiv" />
        </command>
         */
    static PFNGLVERTEXATTRIBI4UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI4UIPROC ) mygetprocaddr("glVertexAttribI4ui");
    glfunc(index_, x_, y_, z_, w_);
    return;
}
void glVertexAttribI4uiv (GLuint index_ , const GLuint * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI4uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLuint</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI4UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI4UIVPROC ) mygetprocaddr("glVertexAttribI4uiv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribI4usv (GLuint index_ , const GLushort * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribI4usv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLushort</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBI4USVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBI4USVPROC ) mygetprocaddr("glVertexAttribI4usv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribL1d (GLuint index_ , GLdouble x_ ){
    /* <command>
            <proto>void <name>glVertexAttribL1d</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBL1DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBL1DPROC ) mygetprocaddr("glVertexAttribL1d");
    glfunc(index_, x_);
    return;
}
void glVertexAttribL1dv (GLuint index_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribL1dv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="1">const <ptype>GLdouble</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBL1DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBL1DVPROC ) mygetprocaddr("glVertexAttribL1dv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribL2d (GLuint index_ , GLdouble x_ , GLdouble y_ ){
    /* <command>
            <proto>void <name>glVertexAttribL2d</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBL2DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBL2DPROC ) mygetprocaddr("glVertexAttribL2d");
    glfunc(index_, x_, y_);
    return;
}
void glVertexAttribL2dv (GLuint index_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribL2dv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="2">const <ptype>GLdouble</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBL2DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBL2DVPROC ) mygetprocaddr("glVertexAttribL2dv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribL3d (GLuint index_ , GLdouble x_ , GLdouble y_ , GLdouble z_ ){
    /* <command>
            <proto>void <name>glVertexAttribL3d</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
            <param><ptype>GLdouble</ptype> <name>z</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBL3DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBL3DPROC ) mygetprocaddr("glVertexAttribL3d");
    glfunc(index_, x_, y_, z_);
    return;
}
void glVertexAttribL3dv (GLuint index_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribL3dv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="3">const <ptype>GLdouble</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBL3DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBL3DVPROC ) mygetprocaddr("glVertexAttribL3dv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribL4d (GLuint index_ , GLdouble x_ , GLdouble y_ , GLdouble z_ , GLdouble w_ ){
    /* <command>
            <proto>void <name>glVertexAttribL4d</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLdouble</ptype> <name>x</name></param>
            <param><ptype>GLdouble</ptype> <name>y</name></param>
            <param><ptype>GLdouble</ptype> <name>z</name></param>
            <param><ptype>GLdouble</ptype> <name>w</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBL4DPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBL4DPROC ) mygetprocaddr("glVertexAttribL4d");
    glfunc(index_, x_, y_, z_, w_);
    return;
}
void glVertexAttribL4dv (GLuint index_ , const GLdouble * v_ ){
    /* <command>
            <proto>void <name>glVertexAttribL4dv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLdouble</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBL4DVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBL4DVPROC ) mygetprocaddr("glVertexAttribL4dv");
    glfunc(index_, v_);
    return;
}
void glVertexAttribP1ui (GLuint index_ , GLenum type_ , GLboolean normalized_ , GLuint value_ ){
    /* <command>
            <proto>void <name>glVertexAttribP1ui</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param><ptype>GLuint</ptype> <name>value</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBP1UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBP1UIPROC ) mygetprocaddr("glVertexAttribP1ui");
    glfunc(index_, type_, normalized_, value_);
    return;
}
void glVertexAttribP1uiv (GLuint index_ , GLenum type_ , GLboolean normalized_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glVertexAttribP1uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBP1UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBP1UIVPROC ) mygetprocaddr("glVertexAttribP1uiv");
    glfunc(index_, type_, normalized_, value_);
    return;
}
void glVertexAttribP2ui (GLuint index_ , GLenum type_ , GLboolean normalized_ , GLuint value_ ){
    /* <command>
            <proto>void <name>glVertexAttribP2ui</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param><ptype>GLuint</ptype> <name>value</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBP2UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBP2UIPROC ) mygetprocaddr("glVertexAttribP2ui");
    glfunc(index_, type_, normalized_, value_);
    return;
}
void glVertexAttribP2uiv (GLuint index_ , GLenum type_ , GLboolean normalized_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glVertexAttribP2uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBP2UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBP2UIVPROC ) mygetprocaddr("glVertexAttribP2uiv");
    glfunc(index_, type_, normalized_, value_);
    return;
}
void glVertexAttribP3ui (GLuint index_ , GLenum type_ , GLboolean normalized_ , GLuint value_ ){
    /* <command>
            <proto>void <name>glVertexAttribP3ui</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param><ptype>GLuint</ptype> <name>value</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBP3UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBP3UIPROC ) mygetprocaddr("glVertexAttribP3ui");
    glfunc(index_, type_, normalized_, value_);
    return;
}
void glVertexAttribP3uiv (GLuint index_ , GLenum type_ , GLboolean normalized_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glVertexAttribP3uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBP3UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBP3UIVPROC ) mygetprocaddr("glVertexAttribP3uiv");
    glfunc(index_, type_, normalized_, value_);
    return;
}
void glVertexAttribP4ui (GLuint index_ , GLenum type_ , GLboolean normalized_ , GLuint value_ ){
    /* <command>
            <proto>void <name>glVertexAttribP4ui</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param><ptype>GLuint</ptype> <name>value</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBP4UIPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBP4UIPROC ) mygetprocaddr("glVertexAttribP4ui");
    glfunc(index_, type_, normalized_, value_);
    return;
}
void glVertexAttribP4uiv (GLuint index_ , GLenum type_ , GLboolean normalized_ , const GLuint * value_ ){
    /* <command>
            <proto>void <name>glVertexAttribP4uiv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param len="1">const <ptype>GLuint</ptype> *<name>value</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBP4UIVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBP4UIVPROC ) mygetprocaddr("glVertexAttribP4uiv");
    glfunc(index_, type_, normalized_, value_);
    return;
}
void glVertexAttribPointer (GLuint index_ , GLint size_ , GLenum type_ , GLboolean normalized_ , GLsizei stride_ , const void * pointer_ ){
    /* <command>
            <proto>void <name>glVertexAttribPointer</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLint</ptype> <name>size</name></param>
            <param group="VertexAttribPointerType"><ptype>GLenum</ptype> <name>type</name></param>
            <param group="Boolean"><ptype>GLboolean</ptype> <name>normalized</name></param>
            <param><ptype>GLsizei</ptype> <name>stride</name></param>
            <param len="COMPSIZE(size,type,stride)">const void *<name>pointer</name></param>
        </command>
         */
    static PFNGLVERTEXATTRIBPOINTERPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXATTRIBPOINTERPROC ) mygetprocaddr("glVertexAttribPointer");
    glfunc(index_, size_, type_, normalized_, stride_, pointer_);
    return;
}
void glVertexBindingDivisor (GLuint bindingindex_ , GLuint divisor_ ){
    /* <command>
            <proto>void <name>glVertexBindingDivisor</name></proto>
            <param><ptype>GLuint</ptype> <name>bindingindex</name></param>
            <param><ptype>GLuint</ptype> <name>divisor</name></param>
        </command>
         */
    static PFNGLVERTEXBINDINGDIVISORPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVERTEXBINDINGDIVISORPROC ) mygetprocaddr("glVertexBindingDivisor");
    glfunc(bindingindex_, divisor_);
    return;
}
void glViewport (GLint x_ , GLint y_ , GLsizei width_ , GLsizei height_ ){
    /* <command>
            <proto>void <name>glViewport</name></proto>
            <param group="WinCoord"><ptype>GLint</ptype> <name>x</name></param>
            <param group="WinCoord"><ptype>GLint</ptype> <name>y</name></param>
            <param><ptype>GLsizei</ptype> <name>width</name></param>
            <param><ptype>GLsizei</ptype> <name>height</name></param>
            <glx opcode="191" type="render" />
        </command>
         */
    static PFNGLVIEWPORTPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVIEWPORTPROC ) mygetprocaddr("glViewport");
    glfunc(x_, y_, width_, height_);
    return;
}
void glViewportArrayv (GLuint first_ , GLsizei count_ , const GLfloat * v_ ){
    /* <command>
            <proto>void <name>glViewportArrayv</name></proto>
            <param><ptype>GLuint</ptype> <name>first</name></param>
            <param><ptype>GLsizei</ptype> <name>count</name></param>
            <param len="COMPSIZE(count)">const <ptype>GLfloat</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVIEWPORTARRAYVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVIEWPORTARRAYVPROC ) mygetprocaddr("glViewportArrayv");
    glfunc(first_, count_, v_);
    return;
}
void glViewportIndexedf (GLuint index_ , GLfloat x_ , GLfloat y_ , GLfloat w_ , GLfloat h_ ){
    /* <command>
            <proto>void <name>glViewportIndexedf</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param><ptype>GLfloat</ptype> <name>x</name></param>
            <param><ptype>GLfloat</ptype> <name>y</name></param>
            <param><ptype>GLfloat</ptype> <name>w</name></param>
            <param><ptype>GLfloat</ptype> <name>h</name></param>
        </command>
         */
    static PFNGLVIEWPORTINDEXEDFPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVIEWPORTINDEXEDFPROC ) mygetprocaddr("glViewportIndexedf");
    glfunc(index_, x_, y_, w_, h_);
    return;
}
void glViewportIndexedfv (GLuint index_ , const GLfloat * v_ ){
    /* <command>
            <proto>void <name>glViewportIndexedfv</name></proto>
            <param><ptype>GLuint</ptype> <name>index</name></param>
            <param len="4">const <ptype>GLfloat</ptype> *<name>v</name></param>
        </command>
         */
    static PFNGLVIEWPORTINDEXEDFVPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLVIEWPORTINDEXEDFVPROC ) mygetprocaddr("glViewportIndexedfv");
    glfunc(index_, v_);
    return;
}
void glWaitSync (GLsync sync_ , GLbitfield flags_ , GLuint64 timeout_ ){
    /* <command>
            <proto>void <name>glWaitSync</name></proto>
            <param group="sync"><ptype>GLsync</ptype> <name>sync</name></param>
            <param><ptype>GLbitfield</ptype> <name>flags</name></param>
            <param><ptype>GLuint64</ptype> <name>timeout</name></param>
        </command>
         */
    static PFNGLWAITSYNCPROC glfunc;
    if(!glfunc)
        glfunc = ( PFNGLWAITSYNCPROC ) mygetprocaddr("glWaitSync");
    glfunc(sync_, flags_, timeout_);
    return;
}
