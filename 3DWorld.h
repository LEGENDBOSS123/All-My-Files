
struct SPHERE{
    int x;
    int y;
    int z;
    int radius;
    int texture;

};

struct WORLD {
    int length;
    struct SPHERE spheres[6];
};

float SDF_SPHERE(float p[3],struct SPHERE *ob){
    float X = (float) ob->x-p[0];
    float Y = (float) ob->y-p[1];
    float Z = (float) ob->z-p[2];
    float R = (float) ob->radius;
    float D = (float) sqrtf(pow(X,2)+pow(Y,2)+pow(Z,2))-R;

    return D;
}

float SDF_CUBE(float p[3],struct SPHERE *ob){
    float X = (float) ob->x-p[0];
    float Y = (float) ob->y-p[1];
    float Z = (float) ob->z-p[2];
    float R = (float) ob->radius;
    float D = (float) sqrtf(pow(MAX(ABS(X)-R,0),2)+pow(MAX(ABS(Y)-R,0),2)+pow(MAX(ABS(Z)-R,0),2));

    return D;
}

struct FLOAT_INT SDF(float p[3],struct WORLD *W,struct PLAYER *P){
    float distance = INFINITY;
    float distancetoobject = 0;
    int Id = -1; 
    struct SPHERE *ob;
    int i = 0;
    float D2 = (float)sqrtf(pow(P->x-p[0],2)+pow(P->y-p[1],2)+pow(P->z-p[2],2))-2;
    for(i;i < W->length;i++){
        ob = &W->spheres[i];
        
        distancetoobject = MAX(-D2,SDF_SPHERE(p,ob));
        //distancetoobject = SDF_SPHERE(p,ob);
        
        
        
        if(distancetoobject<distance){
            distance = distancetoobject;
            Id = ob->texture;
            
        }
        
        
    }
    
    
    
    struct FLOAT_INT sdf_info = {distance,Id};
    
    return sdf_info;
    
}
struct FLOAT_INT_FLOATARRAY3 RAYMARCH(struct WORLD *W,float point[3],struct PLAYER *P,float DIRECTION[3],bool T,float precision){
    float distance = 0;
    float step_size = 0;
    float old_step_size = 0;
    
    bool running = 1;
    float default_over_relaxation = 1.25;
    float over_relaxation = default_over_relaxation;
    float more_over_relaxation = 1.25;
    struct FLOAT_INT sdf_info_for_object;
    struct FLOAT_INT_FLOATARRAY3 sdf_info;
    bool near = 0;
    
    float dx = 0;
    float dy = 0;
    float dz = 0;
    float dd = 0;
    
    while(distance < P->render_distance && running == 1){
        sdf_info_for_object = SDF(point,W,P);
        step_size = sdf_info_for_object.x;
        if(ABS(step_size - old_step_size) < precision){
            over_relaxation = more_over_relaxation;
        }
        if(near==0){
            dx = step_size*DIRECTION[0]*over_relaxation;
            dy = step_size*DIRECTION[1]*over_relaxation;
            dz = step_size*DIRECTION[2]*over_relaxation;
            dd = step_size*over_relaxation;
        }
        else{
            dx = step_size*DIRECTION[0];
            dy = step_size*DIRECTION[1];
            dz = step_size*DIRECTION[2];
            dd = step_size;
        }
        
        
        if(step_size<=precision && step_size>=0){
            running = 0;
            
        }
        else if(step_size<0 && near == 0){
            near = 1;
            dx = -old_step_size*over_relaxation*DIRECTION[0];
            dy = -old_step_size*over_relaxation*DIRECTION[1];
            dz = -old_step_size*over_relaxation*DIRECTION[2];
            dd = -old_step_size*over_relaxation;
            
        }
        point[0]+=dx;
        point[1]+=dy;
        point[2]+=dz;
        distance += dd;
        old_step_size = step_size;
        over_relaxation = default_over_relaxation;
        
    }
    sdf_info.x = distance;
    sdf_info.y = sdf_info_for_object.y;
    sdf_info.z[0] = point[0];
    sdf_info.z[1] = point[1];
    sdf_info.z[2] = point[2];
    return sdf_info;
}
struct FLOAT_FLOAT_FLOAT FIND_NORMAL(float epsilon, struct WORLD *W, struct PLAYER *P,float p[3]){
    
    struct FLOAT_FLOAT_FLOAT normal;
    struct FLOAT_FLOAT_FLOAT normal1;
    struct FLOAT_FLOAT_FLOAT normal2;
    struct FLOAT_FLOAT_FLOAT normal3;
    
    float npoint[3];
    float ndistance;
    npoint[0] = p[0]+epsilon;
    npoint[1] = p[1]-epsilon;
    npoint[2] = p[2]-epsilon;
    ndistance = SDF(npoint,W,P).x;
    normal.x = ndistance;
    normal.y = -ndistance;
    normal.z = -ndistance;
    npoint[0] = p[0]-epsilon;
    npoint[1] = p[1]-epsilon;
    npoint[2] = p[2]+epsilon;
    ndistance = SDF(npoint,W,P).x;
    normal1.x = -ndistance;
    normal1.y = -ndistance;
    normal1.z = ndistance;
    npoint[0] = p[0]-epsilon;
    npoint[1] = p[1]+epsilon;
    npoint[2] = p[2]-epsilon;
    ndistance = SDF(npoint,W,P).x;
    normal2.x = -ndistance;
    normal2.y = ndistance;
    normal2.z = -ndistance;
    npoint[0] = p[0]+epsilon;
    npoint[1] = p[1]+epsilon;
    npoint[2] = p[2]+epsilon;
    ndistance = SDF(npoint,W,P).x;
    normal3.x = ndistance;
    normal3.y = ndistance;
    normal3.z = ndistance;
    normal.x+=normal1.x+normal2.x+normal3.x;
    normal.y+=normal1.y+normal2.y+normal3.y;
    normal.z+=normal1.z+normal2.z+normal3.z;
    float nlength = sqrtf(pow(normal.x,2)+pow(normal.y,2)+pow(normal.z,2));
    normal.x/= nlength;
    normal.y/= nlength;
    normal.z/= nlength;
    
    return normal;

}
void RAYMARCHING(Uint8 c[3],struct WORLD *W, struct PLAYER *P, float DIRECTION[3], bool T){
    
    float SUNLIGHT[3] = {0,1,0};
    
    Uint8 color[3] = {0,0,0};
    float dif = 1;
    float point[3] = {P->x,P->y,P->z};
    float epsilon = 0.001;
    float precision = 0.01;
    float shadow_darkness = 0.25;
    struct FLOAT_INT_FLOATARRAY3 sdf_info = RAYMARCH(W,point,P,DIRECTION,T,precision);
    if(sdf_info.x >= P->render_distance){
        c[0] = bg[0];
        c[1] = bg[1];
        c[2] = bg[2];
        return;
    }
    struct FLOAT_FLOAT_FLOAT normal = FIND_NORMAL(epsilon,W,P,sdf_info.z);
    
    dif = CLAMP(FLOAT_FLOAT_FLOAT_ARRAY_DOT(normal,SUNLIGHT),shadow_darkness,1);
    
    
    float new_pos[3] = {sdf_info.z[0]+normal.x*precision*2,sdf_info.z[1]+normal.y*precision*2,sdf_info.z[2]+normal.z*precision*2};
    
    struct FLOAT_INT_FLOATARRAY3 sdf_info2 = RAYMARCH(W,new_pos,P,SUNLIGHT,T,precision);
    if(sdf_info2.x<P->render_distance){
        dif*=shadow_darkness;
    }
    
    if(sdf_info.x >= P->render_distance){
        c[0] = bg[0];
        c[1] = bg[1];
        c[2] = bg[2];
        return;
    }
    if(sdf_info.y == 1){
        color[0] = 255;
        color[1] = 255;
        color[2] = 255;
        
    }
    else if(sdf_info.y == 2){
        color[0] = 200*(Uint8)fmod(1000+(sdf_info.z[0]+sdf_info.z[2])/5,2);
        color[1] = 200*(Uint8)fmod(1000+(sdf_info.z[0]+sdf_info.z[2])/5,2);
        color[2] = 200*(Uint8)fmod(1000+(sdf_info.z[0]+sdf_info.z[2])/5,2);
    }
    else if(sdf_info.y == 5){
        color[0] = sdf_info.z[0];
        color[1] = sdf_info.z[1];
        color[2] = sdf_info.z[2];
    }
    color[0] *= dif;
    color[1] *= dif;
    color[2] *= dif;
    color[0] += (bg[0]-color[0])*sdf_info.x/P->render_distance;
    color[1] += (bg[1]-color[1])*sdf_info.x/P->render_distance;
    color[2] += (bg[2]-color[2])*sdf_info.x/P->render_distance;
   
    c[0] = color[0];
    c[1] = color[1];
    c[2] = color[2];
    
    
    
}