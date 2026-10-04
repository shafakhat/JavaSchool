---
title: Java Arithmetic Operator convert celsius to fahrenheit
nav: Java Arithmetic Operator c...
description: We would like to convert celsius to fahrenheit using double type:
section: Imported - java2s Archive
order: 1068
source: https://web.archive.org/web/20210102113216/http://www.java2s.com/ref/java/java-arithmetic-operator-convert-celsius-to-fahrenheit.html
---
## Question

We would like to convert celsius to fahrenheit using double type:

Write a program that reads a Celsius degree in a double value from the console.

Convert it to Fahrenheit and displays the result.

The formula for the conversion is as follows:

```java title=Example.java

fahrenheit = (9 / 5) * celsius + 32
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);

    System.out.print("Enter a degree in Celsius: ");
    double celsius = input.nextDouble();

    //your code here/*fromwww.java2s.com*/System.out.println(celsius + " degree Celsius is equal to " + fahrenheit + " in Fahrenheit");
  }
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    Scanner input = newScanner(System.in);

    System.out.print("Enter a degree in Celsius: ");
    double celsius = input.nextDouble();

    double fahrenheit = (9.0 / 5.0) * celsius + 32.0;
    System.out.println(celsius + " degree Celsius is equal to " + fahrenheit + " in Fahrenheit");
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate/approximate PI
- Java Arithmetic Operator compound operator result
- Java Arithmetic Operator compute expressions
- Java Arithmetic Operator convert feet into meters
- Java Arithmetic Operator convert pounds into kilograms
