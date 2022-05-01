#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int generate_random(int maxe, int mine){
    
    int random = rand() % maxe + mine;
    return random;
}



void main(){
    srand(time(NULL));
    int True = 1;
    int False = 0;
    int run_forevver = True;
    while(run_forevver == True){
        int min = 1;
        int max = 100;
        int computer_number = generate_random(max,min);
        int your_number;
        printf("%d",computer_number);

        
        
        printf("----- WELCOME TO NUMBER GAME -----\nCOMPUTER GUESSED A NUMBER %d - %d\n\n\n\n",min,max);
        while(computer_number!=your_number){
            printf("GUESS A NUMBER: ");
            scanf("%d",&your_number);
            
            
            if(your_number>computer_number){
                printf("GUESS LOWER\n\n");
            }
            else if(your_number<computer_number){
                printf("GUESS HIGHER\n\n");
            }
        }
        char input[20];
        printf("\n\n\n\nYOU GUESSED THE NUMBER\n");
        printf("WANT TO PLAY AGAIN (YES OR NO): ");
        scanf("%s",&input);
        int index = 0;
        int scan_for_y = False;
        while(input[index] != '\0'){
            index++;
            if (input[index] == 'y' || input[index] == 'Y'){
                scan_for_y = True;
                break;
            }

        }
        if (scan_for_y == False){
            run_forevver = False;
        }
    }
}


