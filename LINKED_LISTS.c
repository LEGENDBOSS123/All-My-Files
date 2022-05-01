#include <stdio.h>
#include <stdlib.h>

struct NODE{
    int data;
    struct NODE* link;
};

void DISPLAY(struct NODE* HEAD_NODE){
    struct NODE* temp = HEAD_NODE;
    printf("\n");
    while(temp!=NULL){
        printf("%d  ", temp->data);
        temp = temp->link;
    }
}

void INSERT(struct NODE** HEAD_NODE, int data, int location){
    struct NODE* insertion = malloc(sizeof(struct NODE));
    insertion->data = data;

    struct NODE* temp = *HEAD_NODE;

    if(*HEAD_NODE == NULL){
        *HEAD_NODE = insertion;
        return;
    }
    if(location<=0){
        insertion->link = temp;
        *HEAD_NODE = insertion;
        return;
    }
    int loc = 1;

    while(temp->link!=NULL && loc<location){
        loc++;
        temp = temp->link;
    }
    insertion->link = temp->link;
    temp->link = insertion;
    

}
    
void main(){
    struct NODE* HEAD_NODE = NULL;
    INSERT(&HEAD_NODE, 1, 0);
    INSERT(&HEAD_NODE, 2, 0);
    INSERT(&HEAD_NODE, 3, 2);
    DISPLAY(HEAD_NODE);
}
