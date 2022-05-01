import gpdraw.*; //This is very important!! 
public class drawtest {
    public static void main(String[] args) {
        SketchPad paper;                 // declare a SketchPad variable
        DrawingTool pencil;              // declare a DrawingTool variable

        paper = new SketchPad(1500,750,0);  // create the SketchPad
        pencil = new DrawingTool(paper); // create the DrawingTool

        fractal(pencil,2,100);
        
    }
    public static void fractal(DrawingTool p,double length, int level){
        if(level==0){
            p.forward(length);
            p.turnLeft(90);
        }
        else{
            fractal(p,level,level-1);
            fractal(p,level,level-1);
            p.turnRight(90);
        }

    }
       
}
