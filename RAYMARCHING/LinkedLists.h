struct LIST_NODE{
    void *data;
    struct LIST_NODE *next_node;
};

struct LIST{
    int length;    
    struct LIST_NODE *starting_node;
};


struct LIST MAKE_LIST() {
    struct LIST L = {0, NULL};
    return L;
}


void FREE_LIST(struct LIST *list){
    struct LIST_NODE *node = list->starting_node;
    for(int i = 0;i<list->length;i++){
        struct LIST_NODE *erased_node = node;
        node = node->next_node;
        free(erased_node->data);
        free(erased_node);
    }
    

}

void PUSH(struct LIST *list, void *data, size_t data_size){
    struct LIST_NODE* new_node = (struct LIST_NODE*) malloc(sizeof(struct LIST_NODE));
    new_node->data = malloc(data_size);
    new_node->next_node = list->starting_node;
    
    memcpy(new_node->data, data, data_size);
    
    list->starting_node = new_node;
    list->length++;
}

void PUSH_INT(struct LIST *list, int data){
    void *voiddata = (void *) malloc(sizeof(data));
    voiddata = &data;
    PUSH(list, voiddata, sizeof(data)); 
}

void PRINT_LIST(struct LIST *list){
    struct LIST_NODE *node = list->starting_node;
    for(int i = 0;i<list->length;i++){
        
        printf("%d\n",*(int*)node->data);
        
        node = node->next_node;
    }
}