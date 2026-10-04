---
title: Java Arithmetic Operator calculate average speed in miles
nav: Java Arithmetic Operator c...
description: Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/20210102113214/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-average-speed-in-miles.html
---
## Question

Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.

We would like to write a program that displays the average speed in miles per hour.

1 mile is 1.6 kilometers.

Code structure you can use:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println();
  }
}
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println((14 / 45.30) / 1.6);
  }
}
```

## Note

To define method for the calculation:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println("mph: " + kphToMph(kilometersPerHour(14, 45.5)));
  }privatestaticdouble kilometersPerHour(double kilometers, double minutes) {
    return 60.0 * (kilometers / minutes);
  }
  privatestaticdouble kphToMph(double kph) {
    return kph / 1.6;
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate area and perimeter of a rectangle
- Java Arithmetic Operator calculate area of a triangle
- Java Arithmetic Operator calculate average speed in kilometers
- Java Arithmetic Operator calculate circle area
- Java Arithmetic Operator calculate circle area with console input
