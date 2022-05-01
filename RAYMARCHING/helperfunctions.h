#define PI 3.14159265358979323846
#define SCREEN_WIDTH 1000
#define SCREEN_HEIGHT 1000
#define CHUNK_MAP_SIZE 100
#define BLOCK_MAP_SIZE 5000
#define CHUNK_SIZE 32


Uint8 bg[3] = {120,180,250};

float RESOLUTION_SIZE = 8;



float MAX(float a, float b){
    if(a > b){
        return a;
    }
    else{
        return b;
    }
}

float MIN(float a, float b){
    if(a < b){
        return a;
    }
    else{
        return b;
    }
}
float ABS(float a){
    if(a < 0){
        return (-1)*a;
    }
    
}

float CLAMP(float a,float b, float c){
    
    if (a<b){
        a = b;
    }
    else if (a>c){
        a = c;
    }
    return a;
}


float FLOAT_FLOAT_FLOAT_ARRAY_DOT(struct FLOAT_FLOAT_FLOAT a, float b[3]){
    return a.x*b[0] + a.y*b[1] + a.z*b[2];
}
