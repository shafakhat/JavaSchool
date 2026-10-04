---
title: The Lifetime of an Object
nav: The Lifetime of an Object
description: Imported from the java2s.com archive: The Lifetime of an Object
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/20070228141630/http://www.java2s.com:80/Tutorial/Java/0020__Language/TheLifetimeofanObject.htm
---
- The process of disposing of dead objects is called garbage collection.
- Encouraging the Java Virtual Machine (JVM) to do some garbage collecting and recover the memory.

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
    System.gc();
  }
}
```
