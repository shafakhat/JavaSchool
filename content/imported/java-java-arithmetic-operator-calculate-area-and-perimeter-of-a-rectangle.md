---
title: Java Arithmetic Operator calculate area and perimeter of a rectangle
nav: Java Arithmetic Operator c...
description: We would like to write a program to display the area and perimeter of a rectangle with the width of 4.5 and height of 7.9.
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-area-and-perimeter-of-a-rectangle.html
---
## Question

We would like to write a program to display the area and perimeter of a rectangle with the width of 4.5 and height of 7.9.

You can use the following formula:

```java title=Example.java
area  =  width  *  height
```

Code structure you can use:

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.println("Area = ");
    System.out.println("Perimeter = ");
  }
}
java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.println("Area = ");
    System.out.println(4.5 * 7.9);
    System.out.println("Perimeter = ");
    System.out.println((4.5 + 7.9) * 2);
  }
}
```

## Note

We can create method for the calculation:

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.println("area: " + area(4.5, 7.9));
    System.out.println("perimeter: " + perimeter(4.5, 7.9));
  } private static double area(double width, double height) {
    return width * height;
  }
  private static double perimeter(double width, double height) {
    return 2 * (width + height);
  }
}
```

PreviousNext

## Related

- Java two's complement Integer in binary form
- Java Arithmetic Operator Body Mass Index Calculator(BMI)
- Java Arithmetic Operator calculate area and perimeter of a circle
- Java Arithmetic Operator calculate area of a triangle
- Java Arithmetic Operator calculate average speed in kilometers
