#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define X  1
#define O -1

//1 = 'X' and -1 = 'O'

//returns a random number 
static inline int random_number (int range) {
    return (range == 0) ? 0 : rand() % range;
}

//prints the BOARD
void print_BOARD(char* C_BOARD){
    system("clear");
    printf("\n-------\n");
    for (int i = 0; i<9; i+=3){
        printf("|%d|%d|%d|\n",i+1,i+2,i+3);
        printf("-------\n");
    }
    
    printf("\n\n\n-------\n");
    
    for (int i = 0; i<9; i+=3){
        printf("|%c|%c|%c|\n",C_BOARD[i],C_BOARD[i+1],C_BOARD[i+2]);
        printf("-------\n");
    }
}
//updates and prints the BOARD
void update_BOARD(int* I_BOARD, char* C_BOARD){
    //updates I_BOARD AND C_BOARD
    for (int i = 0; i<9; ++i){
        switch (I_BOARD[i]){
            case X:
                C_BOARD[i] = 'X';
                break;
            case O:
                C_BOARD[i] = 'O';
                break;
            default:
                C_BOARD[i] = ' ';
                break;
        }
    }
    //prints BOARD
    print_BOARD(C_BOARD);
}
//scan for the slot number
void SCAN(int person, int* I_BOARD, char* C_BOARD) {
    int where = 0;
    char where_inp[1];
    int TRUE_FALSE = -1;
    
    while (1) {
        if (TRUE_FALSE == -1) {
            printf("ENTER A SLOT: ");
        }
        else {
            printf("PLEASE RETRY - ENTER A SLOT: ");
        }
        
        scanf("%s", &where_inp);
        where = atoi(where_inp);
        where -= 1;
        //checking if the slot is available
        if(where < 9 && where >= 0 && I_BOARD[where] == 0){
            I_BOARD[where] = person;
            break;     
        }
        
        TRUE_FALSE = 0;
    }
    //updates board afterwards
    update_BOARD(I_BOARD, C_BOARD);
}
void FILL_IN(int* I_BOARD,char* C_BOARD, int what, int position){
    //fills in a lot for the computer
    
    I_BOARD[position] = what;
    usleep(333333);
    update_BOARD(I_BOARD,C_BOARD);
    
}
int COMPUTER_MOVE(int computer, int* I_BOARD, char* C_BOARD){
    
    for(int number = 0;number<=6;number+=3){
        if((I_BOARD[number] + I_BOARD[number+1] + I_BOARD[number+2])==computer*2){
            for(int n = number;n<=number+3;n+=1){
                if(I_BOARD[n] == 0){
                    FILL_IN(I_BOARD, C_BOARD, computer, n);
                    return 0;
                }
            }
        }
    }
    for(int number = 0;number<=2;number+=1){
        if((I_BOARD[number] + I_BOARD[number+3] + I_BOARD[number+6])==computer*2){
            for(int n = number;n<=number+6;n+=3){
                if(I_BOARD[n] == 0){
                    FILL_IN(I_BOARD, C_BOARD, computer, n);
                    return 0;
                }
            }
        }
    }
    if((I_BOARD[0] + I_BOARD[4] + I_BOARD[8])==computer*2){
        for(int n = 0; n<=8; n+=4){
            if(I_BOARD[n]==0){
                FILL_IN(I_BOARD, C_BOARD, computer, n);
                return 0;
            }
        }
    }
    if((I_BOARD[2] + I_BOARD[4] + I_BOARD[6])==computer*2){
        for(int n = 2; n<=6; n+=2){
            if(I_BOARD[n]==0){
                FILL_IN(I_BOARD, C_BOARD, computer, n);
                return 0;
            }
        }
    }
    for(int number = 0;number<=6;number+=3){
        if((I_BOARD[number] + I_BOARD[number+1] + I_BOARD[number+2])==computer*-2){
            for(int n = number;n<=number+3;n+=1){
                if(I_BOARD[n] == 0){
                    FILL_IN(I_BOARD, C_BOARD, computer, n);
                    return 0;
                }
            }
        }
    }
    for(int number = 0;number<=2;number+=1){
        if((I_BOARD[number] + I_BOARD[number+3] + I_BOARD[number+6])==computer*-2){
            for(int n = number;n<=number+6;n+=3){
                if(I_BOARD[n] == 0){
                    FILL_IN(I_BOARD, C_BOARD, computer, n);
                    return 0;
                }
            }
        }
    }
    if((I_BOARD[0] + I_BOARD[4] + I_BOARD[8])==computer*-2){
        for(int n = 0; n<=8; n+=4){
            if(I_BOARD[n]==0){
                FILL_IN(I_BOARD, C_BOARD, computer, n);
                return 0;
            }
        }
    }
    if((I_BOARD[2] + I_BOARD[4] + I_BOARD[6])==computer*-2){
        for(int n = 2; n<=6; n+=2){
            if(I_BOARD[n]==0){
                FILL_IN(I_BOARD, C_BOARD, computer, n);
                return 0;
            }
        }
    }
    while(1) {
        int where = random_number(9);
            
        if (where<=8 && where>=0 && I_BOARD[where]==0){
            FILL_IN(I_BOARD, C_BOARD, computer, where);
            return 0;
            }
        
    }
}

void check(const char person_char, int person, int* run, int* I_BOARD, char* C_BOARD){
    int check_win = 0;
    for(int num = 0; num<=6;num+=3){
        if(I_BOARD[num]==person && I_BOARD[num+1]==person && I_BOARD[num+2]==person){
            check_win = 1;
        }
    }
    for(int num = 0; num<=2;num+=1){
        if(I_BOARD[num]==person && I_BOARD[num+3]==person && I_BOARD[num+6]==person){
            check_win = 1;
        }
    }
    if(I_BOARD[0]==person && I_BOARD[4]==person && I_BOARD[8]==person){
        check_win = 1;
    }
    if(I_BOARD[6]==person && I_BOARD[4]==person && I_BOARD[2]==person){
        check_win = 1;
    }
    
    int check_it = 1;
    for (int num = 0; num <= 8; ++num){
        if (I_BOARD[num]==0){
            check_it = 0;
        }
    }
    
    if(check_it == 1 && check_win == 0){
        printf("\nITS A TIE\n");
        *run = 1;
    }
    
    if(check_win == 1){
        printf("\n%c WINS\n",person_char);
        *run = 1;
    }
}

void main() {
    
    char person_choose = 'X';
    int person_letter = X;
    /*while(1){
        system("clear");
        printf("CHOOSE A LETTER: X OR O: ");

        person_choose = getch();
        
        if(person_choose == 'X' || person_choose == 'x'){
            person_letter = X;
            system("clear");
            break;
        }
        if(person_choose == 'O' || person_choose == 'o'){
            person_letter = O;
            system("clear");
            break;
        }
    }*/
    const int person = person_letter;
    const int computer = -1 * person;
    const char person_char = (person == -1) ? 'O' : 'X';
    const char computer_char = (person == -1) ? 'X' : 'O';
    //we have 2 boards
    char C_BOARD[9] = {" "};    
    int I_BOARD[9] = {0};
    int run = 0;
    //sets up the rand
    srand(time(NULL));
    //starts of updating the board
    update_BOARD(I_BOARD, C_BOARD);
    //sets up the while loop which is the game loop
    while (run == 0) {
        
        SCAN(person, I_BOARD, C_BOARD);
        check(person_char, person, &run, I_BOARD, C_BOARD);
        if(run == 1) {
            break;
        }
        COMPUTER_MOVE(computer, I_BOARD, C_BOARD);
        check(computer_char,computer, &run, I_BOARD, C_BOARD);
    }
}
