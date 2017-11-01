#pragma once

#include <png.h>

void png_read(string filename, int& w, int& h, vector<uint8_t>& data, map<string,int>& meta){
    FILE* fp = fopen(filename.c_str(),"rb");
    if(!fp)
        throw runtime_error(filename+": Cannot open");
    uint8_t hdr;
    fread(&hdr,1,1,fp);
    if(png_sig_cmp(&hdr,0,1))
        throw runtime_error(filename+": Not a PNG image");
    png_structp ps = png_create_read_struct(
        PNG_LIBPNG_VER_STRING, NULL,NULL,NULL );
    png_infop ip = png_create_info_struct(ps);
    png_init_io(ps,fp);
    png_set_sig_bytes(ps,1);
    png_read_png(ps,ip,PNG_TRANSFORM_IDENTITY,NULL);
    fclose(fp);
    png_bytep* rp = png_get_rows(ps,ip);
    
    meta["depth"] =  png_get_bit_depth(ps,ip);

    int bytes_per_component;
    bytes_per_component = meta["depth"]/8;
    if( bytes_per_component != 1 && bytes_per_component != 2 )
        throw runtime_error(filename+": PNG depth must be 8 or 16");
        
    int numcomponents;
    
    switch(png_get_color_type(ps,ip)){
        case PNG_COLOR_TYPE_RGB:
            numcomponents=3;
            break;
        case PNG_COLOR_TYPE_RGB_ALPHA:
            numcomponents=4;
            break;
        case PNG_COLOR_TYPE_GRAY:
            numcomponents=1;
            break;
        case PNG_COLOR_TYPE_GRAY_ALPHA:
            numcomponents=2;
            break;
        case PNG_COLOR_TYPE_PALETTE:
            png_set_palette_to_rgb(ps);
            numcomponents=3;
            break;
        default:
            throw runtime_error(filename+": Not one of {gray,gray_alpha,rgb,rgb_alpha}");
    }
    
        
    w = png_get_image_width(ps,ip);
    h = png_get_image_height(ps,ip);

    if( numcomponents == 3 || numcomponents == 4 || numcomponents == 1 ){
        meta["planes"]=numcomponents;
        //fast copy, but flip vertically
        data.resize( w*h*numcomponents*bytes_per_component );
        int i=0; //int(data.size()-w*numcomponents*bytes_per_component );
        int rowsize = numcomponents*w*bytes_per_component ;
        for(int r=0;r<h;++r){
            memcpy(&data[i],rp[h-r-1], rowsize );
            i+=rowsize;
        }
    }
    else if( numcomponents == 2 ){
        //upconvert ga to rgba
        //since it's somewhat inconvenient to
        //work with ga in opengl
        
        //this is hopefully an obscure case that we don't need to support.
        if( meta["depth"] != 8 )
            throw runtime_error(filename+": GA upconvert not supported for non 8-bit images");
            
        cout << filename << ": Note: Upconverting grey/alpha to RGBA\n";
        meta["planes"]=4;
        data.resize( w*h*4*bytes_per_component );
        int dd=0;
        for(int r=0;r<h;++r){
            for(int c=0,cc=0;c<w;++c){
                unsigned g = rp[h-r-1][cc++];
                unsigned a = rp[h-r-1][cc++];
                data[dd++] = g;
                data[dd++] = g;
                data[dd++] = g;
                data[dd++] = a;
            }
        }
    }
    else{
        assert(0);
    }
                
        

    png_destroy_read_struct(&ps,&ip,NULL);
    
    return;
}

//pv should be a pointer to RGBA data
void png_write(string filename, void* pv, int w, int h){
    png_structp png_ptr = png_create_write_struct(PNG_LIBPNG_VER_STRING,
        NULL, NULL,NULL);
    if(!png_ptr)
        throw runtime_error("Cannot create write struct");
    png_infop info_ptr = png_create_info_struct(png_ptr);
    if(!info_ptr)
        throw runtime_error("Cannot create info ptr");
    FILE* fp = fopen(filename.c_str(),"wb");
    if(!fp)
        throw runtime_error("Cannot create output file");
    png_init_io(png_ptr,fp);
    png_set_IHDR(png_ptr,info_ptr,w,h,8,
        PNG_COLOR_TYPE_RGB_ALPHA,PNG_INTERLACE_NONE,
        PNG_COMPRESSION_TYPE_DEFAULT, PNG_FILTER_TYPE_DEFAULT);
    png_byte* P = (png_byte*) pv;
    vector<png_byte*> R;
    for(int i=0;i<h;++i)
        R.push_back( &P[w*i*4] );
    png_set_rows(png_ptr,info_ptr,&R[0]);
    png_write_png(png_ptr,info_ptr,PNG_TRANSFORM_IDENTITY,NULL);
    png_write_end(png_ptr,info_ptr);
    png_destroy_write_struct(&png_ptr,&info_ptr);
    fclose(fp);
}
