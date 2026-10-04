---
title: Java Arithmetic Operator convert pounds into kilograms
nav: Java Arithmetic Operator c...
description: We would like to write a program that converts pounds into kilograms.
section: Imported - java2s Archive
order: 1070
source: https://web.archive.org/web/20210102113216/http://www.java2s.com/ref/java/java-arithmetic-operator-convert-pounds-into-kilograms.html
---
## Question

We would like to write a program that converts pounds into kilograms.

The program prompts the user to enter a number in pounds, converts it to kilograms.

Display the result.

One pound is 0.454 kilograms.

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] Strings) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter a number in pounds: ");
    //your code
  }
}
java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] Strings) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter a number in pounds: ");
    double pounds = input.nextDouble();
    double kilograms = pounds * 0.454;
    System.out.println(pounds + " pounds is " + kilograms + " kilograms.");
  }
}
```

## Note

Define a method to do the conversion.

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter a number in pounds: ");
    double pounds = input.nextDouble();
    double kilograms = poundsToKilograms(pounds);
    System.out.println(pounds + " pounds is " + kilograms + " kilograms");
  }privatestaticdouble poundsToKilograms(double pounds) {
    return pounds * 0.454;
  }
}
```

Create a constant for the conversion.

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);   // Create new Scanner objectfinaldouble KILOGRAMS_PER_POUND = 0.454; // Create constant value// Prompt user to enter the number of poundsSystem.out.print("Enter a number in pounds: ");
    double pounds = input.nextDouble();
    // Convert pounds into kilogramsdouble kilograms = pounds * KILOGRAMS_PER_POUND;
    // Display the resultsSystem.out.println(pounds + " pounds is " + kilograms + " kilograms");
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator compute expressions
- Java Arithmetic Operator convert celsius to fahrenheit
- Java Arithmetic Operator convert feet into meters
- Java Arithmetic Operator divide two integer
- Java Arithmetic Operator divisible by 3
