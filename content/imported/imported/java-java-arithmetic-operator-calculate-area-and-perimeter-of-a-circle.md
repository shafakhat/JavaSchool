---
title: Java Arithmetic Operator calculate area and perimeter of a circle
nav: Java Arithmetic Operator c...
description: We would like to write a program that displays the area and perimeter of a circle that has a radius of 5.5.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20210102113213/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-area-and-perimeter-of-a-circle.html
---
## Question

We would like to write a program that displays the area and perimeter of a circle that has a radius of 5.5.

The following formula you can use:

```java title=Example.java

perimeter   =  2  times  radius  times  pi
area  =  radius  times  radius  times  pi
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println("Perimeter = ");
    System.out.println(2 * 5.5 * 3.14159);
    System.out.println("Area = ");
    System.out.println(5.5 * 5.5 * 3.14159);
  }
}
```

## Note

We can also use the constant from Math class.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    double perimeter = perimeter(5.5);
    double area = area(5.5);
    System.out.println("perimeter: " + perimeter);
    System.out.println("area: " + area);
  }//fromwww.java2s.comprivatestaticdouble perimeter(double radius) {
    return 2 * radius * Math.PI;
  }

  privatestaticdouble area(double radius) {
    return radius * radius * Math.PI;
  }
}
```

PreviousNext

## Related

- Java Operator Precedence Question 1
- Java two's complement Integer in binary form
- Java Arithmetic Operator Body Mass Index Calculator(BMI)
- Java Arithmetic Operator calculate area and perimeter of a rectangle
- Java Arithmetic Operator calculate area of a triangle
