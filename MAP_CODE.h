#include "MAPS.h"
static const int BLOCK_SIZE = 100;

void SETUP(int width,int height,struct PLAYER* p){
    for(int y = 0; y < Y_VAL_MAPS; y++){
        for(int x = 0; x < X_VAL_MAPS; x++){
            if(maps[p->MAP_NUM][y][x] == 'S'){
                p->X = x*BLOCK_SIZE+BLOCK_SIZE/2-p->side/2;
                p->Y = y*BLOCK_SIZE+BLOCK_SIZE/2-p->side/2;
                
                p->speed_x = 0;
                p->speed_y = 0;
                p->ON_GROUND = true;
                
                return;
            }
        }
    }
    
    
}

void DRAW_MAP(SDL_Renderer *r, int width, int height,struct PLAYER *p){
    
    for(int y = 0; y < Y_VAL_MAPS; y++){
        for(int x = 0; x < X_VAL_MAPS; x++){
            if(p->Y>=Y_VAL_MAPS*BLOCK_SIZE){
                SETUP(width,height, p);
                return;
            }
            if(maps[p->MAP_NUM][y][x] == 'P'){
                int xval = x*BLOCK_SIZE;
                int yval = y*BLOCK_SIZE;
                SDL_SetRenderDrawColor(r, 200, 0, 255, 255);
                SDL_Rect rect = {xval+p->MX,yval+p->MY,BLOCK_SIZE,BLOCK_SIZE};
                SDL_RenderFillRect(r,&rect);
                
                if(xval >= p->X && xval <= p->X+p->side || xval+BLOCK_SIZE >= p->X && xval+BLOCK_SIZE <= p->X+p->side || p->X>=xval && p->X<=xval+BLOCK_SIZE || p->X+p->side>=xval && p->X+p->side<=xval+BLOCK_SIZE){
                    if(yval >= p->Y && yval <= p->Y+p->side || yval+BLOCK_SIZE >= p->Y && yval+BLOCK_SIZE <= p->Y+p->side || p->Y>=yval && p->Y<=yval+BLOCK_SIZE || p->Y+p->side>=yval && p->Y+p->side<=yval+BLOCK_SIZE){
                        p->MAP_NUM+=1;
                        SETUP(width,height, p);
                        return;
                        
                    }
                }
            }

            
            if(maps[p->MAP_NUM][y][x] == 'D'){
                int xval = x*BLOCK_SIZE;
                int yval = y*BLOCK_SIZE;
                SDL_SetRenderDrawColor(r, 100, 100, 100, 255);
                SDL_Rect rect = {xval+p->MX,yval+p->MY,BLOCK_SIZE,BLOCK_SIZE};
                SDL_RenderFillRect(r,&rect);
                
                if(xval >= p->X && xval <= p->X+p->side || xval+BLOCK_SIZE >= p->X && xval+BLOCK_SIZE <= p->X+p->side || p->X>=xval && p->X<=xval+BLOCK_SIZE || p->X+p->side>=xval && p->X+p->side<=xval+BLOCK_SIZE){
                    if(yval >= p->Y && yval <= p->Y+p->side || yval+BLOCK_SIZE >= p->Y && yval+BLOCK_SIZE <= p->Y+p->side || p->Y>=yval && p->Y<=yval+BLOCK_SIZE || p->Y+p->side>=yval && p->Y+p->side<=yval+BLOCK_SIZE){
                        SETUP(width,height, p);
                        return;
                        
                    }
                }    
                
            }
            if(maps[p->MAP_NUM][y][x] == 'X'){
                int xval = x*BLOCK_SIZE;
                int yval = y*BLOCK_SIZE;
                SDL_SetRenderDrawColor(r, 255, 0, 0, 255);
                SDL_Rect rect = {xval+p->MX,yval+p->MY,BLOCK_SIZE,BLOCK_SIZE};
                SDL_RenderFillRect(r,&rect);
                
                if(xval >= p->X && xval <= p->X+p->side || xval+BLOCK_SIZE >= p->X && xval+BLOCK_SIZE <= p->X+p->side || p->X>=xval && p->X<=xval+BLOCK_SIZE || p->X+p->side>=xval && p->X+p->side<=xval+BLOCK_SIZE){
                    if(yval >= p->Y && yval <= p->Y+p->side || yval+BLOCK_SIZE >= p->Y && yval+BLOCK_SIZE <= p->Y+p->side || p->Y>=yval && p->Y<=yval+BLOCK_SIZE || p->Y+p->side>=yval && p->Y+p->side<=yval+BLOCK_SIZE){
                        
                        
                        p->Y = yval-p->side;
                        
                        p->ON_GROUND = true;
                        
                        p->speed_y = 0;
                    }
                }
                
            }

            if(maps[p->MAP_NUM][y][x] == 'B'){
                int xval = x*BLOCK_SIZE;
                int yval = y*BLOCK_SIZE;
                SDL_SetRenderDrawColor(r, 255, 255, 0, 255);
                SDL_Rect rect = {xval+p->MX,yval+p->MY,BLOCK_SIZE,BLOCK_SIZE};
                SDL_RenderFillRect(r,&rect);
                
                if(xval >= p->X && xval <= p->X+p->side || xval+BLOCK_SIZE >= p->X && xval+BLOCK_SIZE <= p->X+p->side || p->X>=xval && p->X<=xval+BLOCK_SIZE || p->X+p->side>=xval && p->X+p->side<=xval+BLOCK_SIZE){
                    if(yval >= p->Y && yval <= p->Y+p->side || yval+BLOCK_SIZE >= p->Y && yval+BLOCK_SIZE <= p->Y+p->side || p->Y>=yval && p->Y<=yval+BLOCK_SIZE || p->Y+p->side>=yval && p->Y+p->side<=yval+BLOCK_SIZE){
                        p->Y = yval-p->side;
                        p->speed_y *= -1;
                        p->speed_y-=3;
                        p->ON_GROUND = false;
                    }
                }
                
            }
            
        }
    }
}
