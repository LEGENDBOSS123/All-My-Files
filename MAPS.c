static const int BLOCK_SIZE = 50;
static const int Y_VAL_MAPS = 15;
static const int X_VAL_MAPS = 15;

static const char maps[][15][15] = {

    {
        "XSX",
        "XXX"
    }
};
void SETUP(int map_num,int width,int height, int *px, int *py){
    for(int y = 0; y < Y_VAL_MAPS; y++){
        for(int x = 0; x < X_VAL_MAPS; x++){
            if(maps[map_num][y][x] == 'S'){
                *px = x*BLOCK_SIZE;
                *py = y*BLOCK_SIZE;
                
                
                return;
            }
        }
    }
    
}
void DRAW_MAP(SDL_Renderer *r, int map_num, int width, int height, struct PLAYER *p){
    
    for(int y = 0; y < Y_VAL_MAPS; y++){
        for(int x = 0; x < X_VAL_MAPS; x++){
            if(maps[map_num][y][x] == 'X'){
                SDL_Rect rect = {x*BLOCK_SIZE,1*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE};
                SDL_RenderFillRect(r,&rect);
                
            }
        }
    }
}

void CHECK(int map_num,int px, int py, int width,int height, int *speed){
    for(int y = 0; y < Y_VAL_MAPS; y++){
        for(int x = 0; x < X_VAL_MAPS; x++){
            if(maps[map_num][y][x] == 'X'){
                int xval = (x)*BLOCK_SIZE-px+width/2;
                int yval = (y)*BLOCK_SIZE-py+width/2;
                
                if(width/2+BLOCK_SIZE/2<xval && width/2-BLOCK_SIZE/2>xval){
                    if(height/2+BLOCK_SIZE/2<yval && height/2+BLOCK_SIZE/2>yval){
                        *speed = 0;
                        
                    
                    }
                }
            }
        }
    }
}
