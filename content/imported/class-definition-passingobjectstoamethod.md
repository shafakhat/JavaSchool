---
title: Passing Objects to a Method
nav: Passing Objects to a Method
description: Imported from the java2s.com archive: Passing Objects to a Method
section: Imported - java2s Archive
order: 1094
source: https://web.archive.org/web/20140829080019/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/PassingObjectstoaMethod.htm
---
```java title=Example.java
class Sphere {
  double radius; // Radius of a sphere
  Sphere() {
  }
  // Class constructor
  Sphere(double theRadius) {
    radius = theRadius; // Set the radius
  }
}
public class MainClass {
  public static void main(String[] arg){
    Sphere sp = new Sphere();
    aMethod(sp);
  }
  private static void aMethod(Sphere sp){
    System.out.println(sp);
  }
}
```

| 5.3.1. | Methods |
|---|---|
| 5.3.2. | Passing Objects to a Method |
| 5.3.3. | Returning From a Method |
