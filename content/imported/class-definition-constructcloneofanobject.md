---
title: Construct clone of an object
nav: Construct clone of an object
description: Imported from the java2s.com archive: Construct clone of an object
section: Imported - java2s Archive
order: 1238
source: https://web.archive.org/web/20140829080356/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Constructcloneofanobject.htm
---
```java title=Example.java
class Box {
  double width;
  double height;
  double depth;
  Box(Box ob) {
    width = ob.width;
    height = ob.height;
    depth = ob.depth;
  }
  Box(double w, double h, double d) {
    width = w;
    height = h;
    depth = d;
  }
  Box() {
    width = -1;
    height = -1;
    depth = -1;
  }
  Box(double len) {
    width = height = depth = len;
  }
  double volume() {
    return width * height * depth;
  }
}
class BoxWeight extends Box {
  double weight;
  BoxWeight(double w, double h, double d, double m) {
    width = w;
    height = h;
    depth = d;
    weight = m;
  }
}
class DemoBoxWeight {
  public static void main(String args[]) {
    BoxWeight mybox1 = new BoxWeight(10, 20, 15, 34.3);
    BoxWeight mybox2 = new BoxWeight(2, 3, 4, 0.076);
    double vol;
    vol = mybox1.volume();
    System.out.println(vol);
    System.out.println(mybox1.weight);
    System.out.println();
    vol = mybox2.volume();
    System.out.println(vol);
    System.out.println(mybox2.weight);
  }
}
```
