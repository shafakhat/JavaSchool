---
title: Creating Objects of a Class
nav: Creating Objects of a Class
description: Imported from the java2s.com archive: Creating Objects of a Class
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20070328231831/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/CreatingObjectsofaClass.htm
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
  }
}
```
