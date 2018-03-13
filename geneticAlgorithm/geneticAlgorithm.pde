int h = 500;
int w = 500;
int r = 0;
int x = int(random(w));
int y = int(random(h));
ArrayList<Circle> circles;
PImage image;

// The statements in the setup() function 
// execute once when the program begins
void setup() {
  size(500, 500);  // Size must be the first statement
  image = loadImage("dog.jpg");
  image.resize(500, 0);
  image.loadPixels();
  stroke(255);
  noFill();// Set line drawing color to white
  circles = new ArrayList<Circle>();
  //frameRate(25);
  background(255);
}
// The statements in draw() are executed until the 
// program is stopped. Each statement is executed in 
// sequence and after the last line is read, the first 
// line is executed again.
void draw() { 
  int count = 0;
  //int attempts = 100;
  int total = 500;
  //background(image);
  background(255);
  while(count < total){
      Circle c = addCircle();
      if(c != null){
        circles.add(c);
        count++;
      }
  }
  

    
    
  for(Circle circle : circles){
      circle.show();
      if(circle.growing){
        if(circle.safeToGrow())
        {
          for(Circle other : circles){
            if(other != circle ){
              float d = dist(circle.x, circle.y, other.x, other.y);  
            if(d - 1 < circle.r + other.r){
              circle.growing = false;
              break;
            }
         }
        }
      }
      else
        circle.growing = false;
    }
  circle.show();
  circle.grow();
  }
}

Circle addCircle(){
  boolean valid = true;
  color col;
  float x = random(w);
  float y = random(h);
  for(Circle c : circles){
    float d = dist(x, y, c.x, c.y);
    if(d < c.r){
      valid = false;
      break;
    }
  }
  if(valid){
    int index = int(x) + int(y) * image.width;
    col = image.pixels[index];
    return(new Circle(x, y, col));
  }
   else
   return null;

}