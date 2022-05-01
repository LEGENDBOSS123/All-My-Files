#include <stdio.h>
#include <stdlib.h>

typedef struct LIST {
    int data;
    struct LIST *link;
} LIST;

void DISPLAY(LIST* q) {
    printf("\n\n[  ");
    LIST* first_link = q;
    while(q != NULL) {
        printf("%d  ", q->data);
        q = q->link;
        if (q == first_link) {
            printf("]");
            printf(" ~You have loop in the input H_N\n\n");
            return;
        }
    }
    printf("]\n\n\n");
}

void FREE_LIST(LIST* q) {
    int free_cnt = 0;
    LIST* first_link = q;
    while(q != NULL){
        LIST* temp = q;
        q = q->link;
        ++free_cnt;
        free(temp);
        if (q == first_link) {
            printf("You have loop in the input H_N\n");
            break;
        }
    }
    printf("Number of elements freed %d\n", free_cnt);
}

int INSERT(LIST** H_N, int data, int location) {
    LIST* insertion = (LIST*) malloc(sizeof(LIST));
    if (insertion == NULL){
        return 0;
    }
    insertion->data = data;
    
    if(*H_N == NULL) {
        *H_N = insertion;
        return 1;
    }
    else{
        int loc = 1;
        LIST* temp = *H_N;
        if(location <= 0) {
            insertion->link = temp;
            *H_N = insertion;
            return 1;
        }
        else {
            while(temp->link != NULL && loc < location){
                loc++;
                temp = temp->link;
            }
            insertion->link = temp->link;
            temp->link = insertion;
        }   
    }
    return 1;
}

LIST* EXTRACT(LIST** H_N, int location){
    if(*H_N==NULL){
        return NULL;
    }

    LIST* temp = *H_N;
    if(location<=0){
        LIST* returning = temp;
        *H_N = temp->link;    
        temp->link = NULL;     
        return returning;
    }
    

    location -= 1;
    int loc = 0;
    while(temp->link!=NULL && loc < location-1) {
        temp = temp->link;
        loc++;
    }
    LIST* temp2 = temp->link;
    LIST* returning = temp2->link;
    if (returning==NULL){
        returning = temp2;
    }
    temp2->link = returning->link;
    returning->link = NULL;
    return returning;
}

void PUT(LIST** H_N, LIST* INSERTION, int location){
    LIST* temp = *H_N;
    
    if(*H_N==NULL){
        *H_N = INSERTION;
        return;
    }
    if(location<=0){
        INSERTION->link = temp;
        *H_N = INSERTION;
        return;
    }
    
    int loc = 1;
    while(temp->link != NULL && loc<location){
        loc++;
        temp = temp->link;
    }
    INSERTION->link = temp->link;
    temp->link = INSERTION;
}

void MOVE(LIST** H_N, int location, int newloc) {
    printf("In Move\n");
    LIST* temp = EXTRACT(H_N, location);
    if (temp != NULL) {
        printf("temp->data : %d\n", temp->data);
        PUT(H_N, temp, newloc);
    }
}

void REVERSE(LIST** H_N){
    /*
    DISPLAY(*H_N);
    MOVE(H_N, 10, 0);
    DISPLAY(*H_N);
    */


    LIST* temp = *H_N;
    
    int index = 1;
    while(temp->link != NULL) {
        printf("Calling Move\n");
        MOVE(H_N, index, 0);   
        temp = temp->link;
        printf("Index: %d\n", index);
        DISPLAY(*H_N);
        index++;
    }
    printf("Exiting Reverse\n");

}   



