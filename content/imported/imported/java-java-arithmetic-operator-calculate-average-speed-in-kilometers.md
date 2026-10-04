---
title: Java Arithmetic Operator calculate average speed in kilometers
nav: Java Arithmetic Operator c...
description: Assume a runner runs 24 miles in 1 hour, 40 ?minutes, and 35 seconds.
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20210102113213/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-average-speed-in-kilometers.html
---
## Question

Assume a runner runs 24 miles in 1 hour, 40 ?minutes, and 35 seconds.

We would like to write a program that displays the average speed in kilometers per hour.

1 mile is 1.6 kilometers.

Code structure you can use:

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] agrs) {
       //your code here
  }
}
```

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] agrs) {
    System.out.println("Miles / (hour + (minutes / 60) + (seconds / 3600)) * 1.6");
    System.out.println("24    / (1    + (40      / 60) + (35      / 3600))  * 1.6");
    System.out.println((24 / (1 + (40 / 60.0) + (35 / 3600.0))) * 1.6);
  }
}
```

## Note

The following code creates method to clear the calculation steps.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    System.out.println("kph: " + mphToKph(milesPerHour(24, 100.58)));
  }//fromwww.java2s.comprivatestaticdouble milesPerHour(double miles, double minutes) {
    return 60.0 * (miles / minutes);
  }

  privatestaticdouble mphToKph(double mph) {
    return mph * 1.6;
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate area and perimeter of a circle
- Java Arithmetic Operator calculate area and perimeter of a rectangle
- Java Arithmetic Operator calculate area of a triangle
- Java Arithmetic Operator calculate average speed in miles
- Java Arithmetic Operator calculate circle area
