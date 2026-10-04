---
title: Using Objects
nav: Using Objects
description: return Math.sqrt((x - aPoint.x) * (x - aPoint.x) + (y - aPoint.y) * (y - aPoint.y));
section: Imported - java2s Archive
order: 1225
source: https://web.archive.org/web/20140829090236/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/UsingObjects.htm
---
```java title=Example.java
class Point {
  double x;
  double y;
  Point(double xVal, double yVal) {
    x = xVal;
    y = yVal;
  }
  Point(final Point oldPoint) {
    x = oldPoint.x;
    y = oldPoint.y;
  }
  void move(double xDelta, double yDelta) {
    x += xDelta;
    y += yDelta;
  }
  double distance(final Point aPoint) {
    return Math.sqrt((x - aPoint.x) * (x - aPoint.x) + (y - aPoint.y) * (y - aPoint.y));
  }
  public String toString() {
    return Double.toString(x) + ", " + y;
  }
}
// You can use Point objects in the definition of the class Line:
class Line {
  Point start;
  Point end;
  Line(final Point start, final Point end) {
    this.start = new Point(start);
    this.end = new Point(end);
  }
  Line(double xStart, double yStart, double xEnd, double yEnd) {
    start = new Point(xStart, yStart);
    end = new Point(xEnd, yEnd);
  }
  double length() {
    return start.distance(end);
  }
  public String toString() {
    return "(" + start + "):(" + end + ")";
  }
}
public class MainClass{
  public static void main(String[] arg){
    Line l1 = new Line(new Point(1,2), new Point(3,4));
    System.out.println(l1);
  }
}
java title=Example.java
(1.0, 2.0):(3.0, 4.0)
```
