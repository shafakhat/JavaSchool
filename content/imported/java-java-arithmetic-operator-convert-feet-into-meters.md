---
title: Java Arithmetic Operator convert feet into meters
nav: Java Arithmetic Operator c...
description: We would like to write a program that reads a number in feet.
section: Imported - java2s Archive
order: 1069
source: https://web.archive.org/web/20210102113216/http://www.java2s.com/ref/java/java-arithmetic-operator-convert-feet-into-meters.html
---
## Question

We would like to write a program that reads a number in feet.

Convert it to meters, and displays the result.

One foot is 0.305 meter. Here is a sample run:

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] Strings) {
    Scanner input = newScanner(System.in);
    //your code here
  }
}
java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] Strings) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter a value for feet: ");
    double feet = input.nextDouble();
    double meters = feet * 0.305;
    System.out.println(feet + " feet is " + meters + " meters");
  }
}
```

## Note

To define a method

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter a value for feet: ");
    double feet = input.nextDouble();
    double meters = feetToMeters(feet);
    System.out.println(feet + " feet is " + meters + " meters");
  }privatestaticdouble feetToMeters(double feet) {
    return feet * 0.305;
  }
}
```

Define a constant for converting.

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a Scanner objectScanner input = newScanner(System.in);
    // Create constant valuefinaldouble METERS_PER_FOOT = 0.305;
    // Prompt user to enter a number in feetSystem.out.print("Enter a value for feet: ");
    double feet = input.nextDouble();
    // Convert feet into metersdouble meters = feet * METERS_PER_FOOT;
    // Display resultsSystem.out.println(feet + " feet is " + meters + " meters");
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator compound operator result
- Java Arithmetic Operator compute expressions
- Java Arithmetic Operator convert celsius to fahrenheit
- Java Arithmetic Operator convert pounds into kilograms
- Java Arithmetic Operator divide two integer
