
#include <stdio.h>
#include <stdlib.h>

void main(){
    int n=10;
    int *ptr=NULL;
    ptr = (int*)malloc(n * sizeof(int));
    *ptr=35;
    printf("%d",*ptr);
}
