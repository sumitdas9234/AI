class Circle {
  float x;
  float y;
  float r;
  color c;
  boolean growing;
  
  
  Circle(float _x, float _y, color _c){
    x = _x;
    y = _y;
    r = 0;
    c = _c;
    growing = true;
  }
  void grow(){
    if(growing)
    r = r + 1;
  }
  
  boolean safeToGrow(){
    return (x + r < w && x - r > 0 && y + r < h && y - r > 0);
  }
  
  void show(){
    noStroke();
    fill(c);
    ellipse(x, y, 2*r, 2*r);
  }

}