#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define X -1
#define O 1

// creating the board for tic-ta-toe
void PRINT_BOARD(int* I_BOARD, char* C_BOARD){
    printf("-------\n");
    printf("|%c|%c|%c|\n",C_BOARD[0],C_BOARD[1],C_BOARD[2]);
    printf("-------\n");
    printf("|%c|%c|%c|\n",C_BOARD[3],C_BOARD[4],C_BOARD[5]);
    printf("-------\n");
    printf("|%c|%c|%c|\n",C_BOARD[6],C_BOARD[7],C_BOARD[8]);
    printf("-------\n");
}
void update_BOARD(){
}
void main(){
    int player_letter = X;
    int computer_letter = O;
    int I_BOARD[9] = {0,0,0,0,0,0,0,0,0};
    char C_BOARD[9] = "         ";
    PRINT_BOARD(I_BOARD,C_BOARD);
}
