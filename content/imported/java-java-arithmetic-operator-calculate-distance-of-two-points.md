---
title: Java Arithmetic Operator calculate distance of two points
nav: Java Arithmetic Operator c...
description: //your code hereSystem.out.println("The distance between the two points is " + distance);
section: Imported - java2s Archive
order: 1060
source: https://web.archive.org/web/20210102113215/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-distance-of-two-points.html
---
## Question

We would like to calculate distance of two points.

Prompt the user to enter two points (x1, y1) and (x2, y2).

Display their distance between them.

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] String) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter x1 and y1: ");
    double x1 = input.nextDouble();
    double y1 = input.nextDouble();
    System.out.print("Enter x2 and y2: ");
    double x2 = input.nextDouble();
    double y2 = input.nextDouble();
    //your code hereSystem.out.println("The distance between the two points is " + distance);
  }
}
java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] String) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter x1 and y1: ");
    double x1 = input.nextDouble();
    double y1 = input.nextDouble();
    System.out.print("Enter x2 and y2: ");
    double x2 = input.nextDouble();
    double y2 = input.nextDouble();
    double a = (Math.pow((x2 - x1), 2)) + (Math.pow((y2 - y1), 2));
    double distance = Math.pow(a, 0.5);
    System.out.println("The distance between the two points is " + distance);
  }
}
```

## Note

To define a method to do the calculation:

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter x1 and y1: ");
    double x1 = input.nextDouble();
    double y1 = input.nextDouble();
    System.out.print("Enter x2 and y2: ");
    double x2 = input.nextDouble();
    double y2 = input.nextDouble();
    double distance = distance(x1, y1, x2, y2);
    System.out.println("The distance between the two points is " + distance);
  }privatestaticdouble distance(double x1, double y1, double x2, double y2) {
    returnMath.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate circle area with console input
- Java Arithmetic Operator calculate compound value
- Java Arithmetic Operator calculate cylinder volume
- Java Arithmetic Operator calculate floating point value
- Java Arithmetic Operator calculate leap year
