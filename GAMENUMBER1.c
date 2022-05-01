#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <SDL2/SDL.h>

struct PLAYER{
    int X;
    int Y;
    int side;
    int speed_x;
    int speed_y;
    int x_move;
    int jump;
    int gravity;
    bool ON_GROUND;
    int MX;
    int MY;
    int MAP_NUM;
};


#include "MAP_CODE.h"

static const int width = 800;
static const int height = 800;


void UPDATE(struct PLAYER *p){
    p->speed_y+=p->gravity;
    p->Y+=p->speed_y;
    p->MX = width/2 - (p->side)/2 - p->X;
    p->MY = height/2 - (p->side)/2 - p->Y;
}

int main() {
    
    struct PLAYER player = {0,0,50 ,0,0,0,-25,1,true};
    player.x_move = 7;
    player.MAP_NUM = 0;
    
    SETUP(width, height, &player);
    
    const Uint8* keystate = SDL_GetKeyboardState(NULL);
    
    // Initialize SDL
    SDL_Init(SDL_INIT_VIDEO);

    // Create a SDL window
    SDL_Window *window = SDL_CreateWindow(
		    "GAMENUMBER1",
		    SDL_WINDOWPOS_UNDEFINED,
		    SDL_WINDOWPOS_UNDEFINED,
		    width,
		    height,
		    0);

    // Create a renderer (accelerated and in sync with the display refresh rate)
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    
    bool running = true;
    SDL_Event event;
    while (running)
    {
        // Process events
        while(SDL_PollEvent(&event))
        {
            if(event.type == SDL_QUIT)
            {
                running = false;
            }
        }

        // Clear screen
        SDL_RenderClear(renderer);
        //keys
        // Draw
        DRAW_MAP(renderer, width, height, &player);

        if(keystate[SDL_SCANCODE_UP] && player.ON_GROUND == true){
            player.speed_y = player.jump;
            
            player.ON_GROUND = false;
        }

        if(keystate[SDL_SCANCODE_RIGHT]){
            player.X+=player.x_move;
        }
        if(keystate[SDL_SCANCODE_LEFT]){
            player.X-=player.x_move;
        }
        
        UPDATE(&player);
        SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255);
        SDL_Rect rect = {player.X+player.MX,player.Y+player.MY,player.side,player.side};
        SDL_RenderFillRect(renderer,&rect);
        
        // Show what was drawn
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderPresent(renderer);        
    }

    // Release resources
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
