---
title: Using Static Variables
nav: Using Static Variables
description: In this example, the Box class contains a static variable, numBoxes, which is incremented
section: Imported - java2s Archive
order: 1100
source: https://web.archive.org/web/20090531211334/http://www.java2s.com:80/Code/Java/Class/UsingStaticVariables.htm
---
Using Static Variables

```java title=Example.java
/*
In this example, the Box class contains a static variable, numBoxes, which is incremented
each time a Box object is created. The main() method of the TestStaticVar class creates
two Box objects, then prints out the value of the static variable.
*/
class Box {
  double width;
  public static int numBoxes = 0; // static variable is declared and initialized
  public Box() {
    width = 5.0;
    numBoxes++; // numBoxes is incremented to count number of objects.
  }
}
public class TestStaticVar {
  public static void main (String args[]) {
    Box box1 = new Box();
    Box box2 = new Box();
    System.out.println("Number of objects = " + Box.numBoxes);
  }
}
```

1.  Java static member variable example
---  ---
2.  Java static method
3.  Static Init Demo
4.  Show that you do inherit static fields
5.  Show that you can't have static variables in a method
6.  Explicit static initialization with the static clause
7.  Static field, constructor and exception
