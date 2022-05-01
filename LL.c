#include <stdio.h>
#include <stdlib.h>
#include "FUNCTIONS.h"
void main(){
    LIST* list1 = NULL;
    for(int i; i<2; i++){
        INSERT(&list1, i,i);
    }
    REVERSE(&list1);
    DISPLAY(list1);
    FREE_LIST(list1);
}


