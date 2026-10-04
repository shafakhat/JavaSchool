---
title: Using the Floating-Point Values as the control value in a for loop
nav: Using the Floating-Point V...
description: System.out.println("radius = " + radius + "area = " + Math.PI * radius * radius);
section: Imported - java2s Archive
order: 1322
source: https://web.archive.org/web/20140829092240/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/UsingtheFloatingPointValuesasthecontrolvalueinaforloop.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    for (double radius = 1.0; radius <= 2.0; radius += 0.2) {
      System.out.println("radius = " + radius + "area = " + Math.PI * radius * radius);
    }
  }
}
java title=Example.java
radius = 1.0area = 3.141592653589793
radius = 1.2area = 4.523893421169302
radius = 1.4area = 6.157521601035994
radius = 1.5999999999999999area = 8.04247719318987
radius = 1.7999999999999998area = 10.178760197630927
radius = 1.9999999999999998area = 12.566370614359169
```
