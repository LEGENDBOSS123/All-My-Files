#include <stdio.h>
#include <stdlib.h>

    
int get_sum(int a, int b) {
    return a + b;
}

void main(){
    int x = 10;
    int y = 20;
    int z = get_sum(x, y);
    puts("Type something: ");
    char inp_str[64];
    scanf("%s",inp_str);
    puts(inp_str);
}