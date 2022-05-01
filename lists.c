#include <stdio.h>
#include <stdlib.h>
struct Node{
    int data;
    struct Node *link;
};

void append(struct Node **q, int num){
    struct Node *temp, *r;
    temp = *q;

    if(*q == NULL){
        temp = malloc(sizeof(struct Node));
        temp->data = num;
        temp->link = NULL;
        *q = temp;
    }
    else{
        temp = *q;
        while(temp->link!=NULL){
            temp = temp->link;
        }
        r = malloc(sizeof(struct Node));
        r->data = num;
        r->link = NULL;
        temp->link = r;
    }
}
void addatbeg(struct Node **q, int num){
    struct Node *temp;
    temp = malloc(sizeof(struct Node));

    temp->data = num;
    temp->link = *q;

    *q = temp;
}
void INSERT(struct Node *q, int loc, int num){
    struct Node *temp, *r;
    int i = 0;
    temp = q;
    for(i=0;i<loc;i++){
        temp = temp->link;
        if(temp==NULL){
            return;
        }
    }
    r = malloc(sizeof(struct Node));
    r->data = num;
    r->link = temp->link;
    temp->link = r;
}

void display(struct Node *q){
    printf("\n\n[  ");
    while(q!=NULL){
        printf("%d  ", q->data);
        q = q->link;
    }
    printf("]\n\n\n");
}

void delete(struct Node **q, int num){
    struct Node *old, *temp;

    temp = *q;

    while(temp!=NULL){
        if(temp->link == num){
            if(temp == *q){
                *q = temp->link;
                free(temp);
                return;
            }
            else{
                old->link = temp->link;
                free(temp);
                return
            }
        }
        else{
            old = temp;
            temp = temp->link;
        }
    }
}



void main(){
    struct Node *p;
    p = NULL;
    //printf("\nNUMBER OF ELEMENTS IN THE LIST: %d", count(p));
    append(&p,1);
    append(&p,2);
    append(&p,3);
    append(&p,5);
    append(&p,17);

    //system("clear");
    display(p);

    addatbeg(&p, 999);
    addatbeg(&p, 888);
    addatbeg(&p, 777);

    display(p);
    
    INSERT(&p,7, 0);
    INSERT(&p,2, 1);
    INSERT(&p,1, 99);

    display(p);

    delete(&p, 888);
    delete(&p, 1);
    delete(&p, 10);
    
    display(p);

    
    

}




    
