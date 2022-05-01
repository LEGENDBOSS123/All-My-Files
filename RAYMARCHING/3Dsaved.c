#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <math.h>
#include <SDL2/SDL.h>
#include "Vector.h"
#include "helperfunctions.h"
#include "LinkedLists.h"
#include "Player.h"
#include "3DWorld.h"



void SET_PIXEL(unsigned char *PIXELS,int pitch,int x,int y, Uint8 color[3],int size){
    color[0] = pow((float)color[0]/255,0.4545)*255;
    color[1] = pow((float)color[1]/255,0.4545)*255;
    color[2] = pow((float)color[2]/255,0.4545)*255;
    for(int Y = y;Y<y+size;Y = Y + 1){
        for(int X = x;X<x+size;X = X + 1){
            PIXELS[(X+Y*SCREEN_WIDTH)*4] = color[0];
            PIXELS[(X+Y*SCREEN_WIDTH)*4+1] = color[1];
            PIXELS[(X+Y*SCREEN_WIDTH)*4+2] = color[2];
        }
    }
}


int main() { 
    
    
    SDL_Init(SDL_INIT_EVERYTHING);
    
    SDL_Window *WINDOW = SDL_CreateWindow("3D GAME", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    
    SDL_Renderer *RENDERER = SDL_CreateRenderer(WINDOW, -1, SDL_RENDERER_ACCELERATED);
    
    SDL_Texture *TEXTURE = SDL_CreateTexture(RENDERER,SDL_PIXELFORMAT_ABGR8888,SDL_TEXTUREACCESS_STREAMING,SCREEN_WIDTH,SCREEN_HEIGHT);
    
    unsigned char *PIXELS;
    int PITCH;
    
    Uint32 OTIME = 0;
    Uint32 NTIME = 0;
    double FPS = 0;
        
    const Uint8 *KEYSTATE = SDL_GetKeyboardState(NULL);
    if (KEYSTATE == NULL) {
        return -1;
    }
    
    
    //float x, float y,float z,int renderdis, float ax, float ay, float fov, float grav,float scroll,float speed, float jump
    struct PLAYER P = MAKE_PLAYER(15,15,10,64,130,45,90,0.5,2,1,1);

    struct WORLD W = {3,{{0,0,30,10,1},{0,-740,0,390,2},{0,-5,0,5,2},{2,5,10,5,2},{10,-3,0,5,1},{0,-10,-10,5,1}}};
    

    SDL_Event EVENT;
    
    bool RUNNING = true;
    
    int COUNTER = 0;
    float oldx;
    float oldy;
    float oldz = (float)P.calculation;
    float newx;
    float newy;
    float newz;
    float normalization;
    float direction[3];
    
    Uint8 color[3];
    
    
    while (RUNNING){
        OTIME = SDL_GetTicks();
        
        HANDLE_KEYPRESSES(KEYSTATE,&P);
        HANDLE(&P);
        
       
        
        
        
        
        SDL_LockTexture(TEXTURE,NULL,(void**)&PIXELS,&PITCH);
        while(SDL_PollEvent(&EVENT)){
            
            if(EVENT.type == SDL_QUIT)
            {
                RUNNING = false;
            }
        }
        
        float sx = sin(PI/180*P.anglex);
        float cx = cos(PI/180*P.anglex);
        
        float sy = sin(PI/180*P.angley);
        float cy = cos(PI/180*P.angley);
        
        int middlex = SCREEN_WIDTH/2;
        int middley = SCREEN_HEIGHT/2;
        
        
        for(int y = 0; y < SCREEN_HEIGHT; y = y + RESOLUTION_SIZE) {
            for(int x = 0; x < SCREEN_WIDTH; x = x + RESOLUTION_SIZE) {
                
                RAYMARCHING(color,&W,&P,direction,1);
                oldx = (float)(x-middlex)/SCREEN_WIDTH;
                oldy = (float)(middley-y)/SCREEN_WIDTH;
                   
                newy = (float)oldy*cy - oldz*sy;
                newz = (float)oldz*cy + oldy*sy;
                
                newx = (float)oldx*cx - newz*sx;
                newz = (float)newz*cx + oldx*sx;
                
                
                
                normalization = (float) sqrtf(newx*newx+newy*newy+newz*newz) + 1e-6;
                 
                
                
                newx=(float)newx/normalization;
                newy=(float)newy/normalization;
                newz=(float)newz/normalization;

                direction[0] = (float)newx;
                direction[1] = (float)newy;
                direction[2] = (float)newz;
                
                
                SET_PIXEL(PIXELS,4,x,y,color,RESOLUTION_SIZE);
                
            
            
            }
        }
        
        
        
        SDL_RenderClear(RENDERER);
        SDL_UnlockTexture(TEXTURE);
        SDL_RenderCopy(RENDERER,TEXTURE,NULL,NULL);
        SDL_RenderPresent(RENDERER);
        if(COUNTER>50){
            
            NTIME = SDL_GetTicks();
            FPS = 1000/(NTIME-OTIME);
            printf("%i FPS\n",(int)FPS);
            COUNTER = 0;
        }
        
        COUNTER++;
        
        
        
                
    }
    SDL_DestroyWindow(WINDOW);
    SDL_DestroyRenderer(RENDERER);
    SDL_Quit();

    return 0;
}

