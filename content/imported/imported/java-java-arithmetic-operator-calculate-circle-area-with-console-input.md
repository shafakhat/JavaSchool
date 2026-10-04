---
title: Java Arithmetic Operator calculate circle area with console input
nav: Java Arithmetic Operator c...
description: import java.util.Scanner; // Scanner is in the java.util packagepublicclass Main {
section: Imported - java2s Archive
order: 1056
source: https://web.archive.org/web/20210102113214/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-circle-area-with-console-input.html
---
## Question

We would like to calculate circle area with console input.

Code structure you can use:

```java title=Example.java
import java.util.Scanner; // Scanner is in the java.util packagepublicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a Scanner objectScanner input = newScanner(System.in);
    /*fromwww.java2s.com*/// Prompt the user to enter a radiusSystem.out.print("Enter a number for radius: ");
    double radius = input.nextDouble();

    //your code here
  }
}
```

```java title=Example.java
import java.util.Scanner; // Scanner is in the java.util packagepublicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a Scanner objectScanner input = newScanner(System.in);

    // Prompt the user to enter a radiusSystem.out.print("Enter a number for radius: ");
    double radius = input.nextDouble();

    // Compute areadouble area = radius * radius * 3.14159;

    // Display resultSystem.out.println("The area for the circle of radius " +
      radius + " is " + area);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate average speed in kilometers
- Java Arithmetic Operator calculate average speed in miles
- Java Arithmetic Operator calculate circle area
- Java Arithmetic Operator calculate compound value
- Java Arithmetic Operator calculate cylinder volume
