#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <SDL2/SDL.h>

#define xval 2300
#define yval 1400
    
Uint8 bg[3] = {0, 0, 0};

struct PLAYER {
    int x;
    int y;
    int limit;
    int anglex;
    int angley;
    int fov;
    int xvel;
    int yvel;
    float gravity;
};

struct VECTOR {
    int x;
    int y;
    int z;
};

struct TRIANGLE{
    struct VECTOR points[3];
};
int dot_product(struct VECTOR v, struct VECTOR v2){
    return v.x*v2.x+v.y*v2.y+v.z*v2.z;
}



int min3(int a,int b, int c){
    int ret = a;
    if (b<ret){
        ret = b;
    }
    if (c<ret){
        ret = c;
    }
    return ret;
}
int max3(int a,int b, int c){
    int ret = a;
    if (b>ret){
        ret = b;
    }
    if (c>ret){
        ret = c;
    }
    return ret;
}
int max(int a,int b){
    int ret = a;
    if (b>ret){
        ret = b;
    }
    
    return ret;
}
int min(int a,int b){
    int ret = a;
    if (b<ret){
        ret = b;
    }
    
    return ret;
}

int orient2d(const struct VECTOR const a, const struct VECTOR const b, const struct VECTOR const c){
    int ret = (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x);
    
    if (a.x*b.y - a.y*b.x>0){
        return ret;
    }
    
    return ret;
    
}

void draw_triangle(struct PLAYER *P,Uint8 color[3], SDL_Renderer *r,struct TRIANGLE *t){
    struct VECTOR a = t->points[0];
    struct VECTOR b = t->points[1];
    struct VECTOR c = t->points[2];
    int minx = min3(a.x,b.x,c.x);
    int maxx = max3(a.x,b.x,c.x);
    int miny = min3(a.y,b.y,c.y);
    int maxy = max3(a.y,b.y,c.y);
    
    minx = max(minx,0);
    miny = max(miny,0);
    minx = min(minx,xval-1);
    miny = min(miny,yval-1);
    int A01 = a.y - b.y;
    int B01 = b.x - a.x;
    int A12 = b.y - c.y;
    int B12 = c.x - b.x;
    int A20 = c.y - a.y;
    int B20 = a.x - c.x;
    struct VECTOR p = {minx,miny};
    int w0_row = orient2d(b,c,p);
    int w1_row = orient2d(c,a,p);
    int w2_row = orient2d(a,b,p);
    
    for(p.y = miny;p.y <= maxy; p.y++){
        int w0 = w0_row;
        int w1 = w1_row;
        int w2 = w2_row;
        for(p.x = minx;p.x <= maxx; p.x++){
            
            if(w0 >= 0 && w1 >= 0 && w2 >= 0){
                //SDL_SetRenderDrawColor(r,color[0],color[1],color[2],255);
                SDL_SetRenderDrawColor(r,w0,w1,w2,255);
                SDL_RenderDrawPoint(r,p.x,p.y);
                
            }
            w0+=A12;
            w1+=A20;
            w2+=A01;
            
        }
        w0_row += B12;
        w1_row += B20;
        w2_row += B01;
    }
    
    
    
}

/*struct SCREEN {
    int PIXELS[yval][xval];    
};

void SETUP_SCREEN(struct SCREEN *s,const struct PLAYER* const P){
    for (int y=0; y < yval; y++){
        for (int x=0; x < xval; x++){
            int p = P->limit;
            s->PIXELS[y][x] = p;
        }
    }
}

void DRAW_SCREEN(SDL_Renderer *r, const struct SCREEN* const s){
    for (int y=0; y < yval; y++){
        for (int x=0; x < xval; x++){
            SDL_SetRenderDrawColor(r, 
                                   s->PIXELS[y][x].color[0], 
                                   s->PIXELS[y][x].color[1], 
                                   s->PIXELS[y][x].color[2], 
                                   0xff);
            SDL_RenderDrawPoint(r,x,y);
        }
    } 
    SDL_RenderPresent(r);
}*/


int main() {    
    struct PLAYER P = {0, 0, 20, 0, 0, 90, 0, 0, 0.5};
    //struct SCREEN S;
    //SETUP_SCREEN(&S,&P);
    
    struct VECTOR p0 = {0,0,3};
    struct VECTOR p1 = {1000,1000,10};
    struct VECTOR p2 = {0,1000,20};
    Uint8 c[3] = {255,255,255};
    struct TRIANGLE t = {p0,p1,p2};
    const Uint8* keystate = SDL_GetKeyboardState(NULL);
    if (keystate == NULL) {
        return -1;
    }
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window = SDL_CreateWindow("3D GAME", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, xval, yval, 0);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    SDL_Event event;
    
    bool running = true;
    while (running)
    {
        while(SDL_PollEvent(&event))
        {
            if(event.type == SDL_QUIT)
            {
                running = false;
            }
        }

        
        t.points[0].x+=2;
        SDL_SetRenderDrawColor(renderer,bg[0],bg[1],bg[2],255);
        
        SDL_RenderClear(renderer);
        draw_triangle(&P,c,renderer,&t);
        
        SDL_RenderPresent(renderer);        
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}