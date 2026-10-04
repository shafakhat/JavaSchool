---
title: Java Arithmetic Operator find the number of years
nav: Java Arithmetic Operator f...
description: We would like to write a program that prompts the user to enter the minutes (e.g., 1 billion)
section: Imported - java2s Archive
order: 1073
source: https://web.archive.org/web/20210102113217/http://www.java2s.com/ref/java/java-arithmetic-operator-find-the-number-of-years.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We would like to write a program that prompts the user to enter the minutes (e.g., 1 billion)

Display the number of years and days for the minutes.

For simplicity, assume a year has 365 days.

Here is a sample run:

```java title=Example.java

Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);

    // Prompt the user to enter the number of minutesSystem.out.print("Enter the number of minutes: ");
    int minutes = input.nextInt();

    //your code /*fromwww.java2s.com*/// Display resultsSystem.out.println(minutes + " minutes is approximately " + years
      + " years and " + days + " days");
  }
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);

    // Prompt the user to enter the number of minutesSystem.out.print("Enter the number of minutes: ");
    int minutes = input.nextInt();

    // Compute the number of years and daysint years = minutes / 525600;
    int days = (minutes % 525600) / 1440;

    // Display resultsSystem.out.println(minutes + " minutes is approximately " + years
      + " years and " + days + " days");
  }
}
```

## Note

The following code shows the steps:

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    double minutesInYear = 60 * 24 * 365;

    Scanner input = newScanner(System.in);

    System.out.print("Enter the number of minutes: ");

    double minutes = input.nextDouble();

    long years = (long) (minutes / minutesInYear);
    int days = (int) (minutes / 60 / 24) % 365;

    System.out.println((int) minutes + " minutes is approximately " + years + " years and " + days + " days");
  }/*www.java2s.com*/
}
```

PreviousNext

## Related

- Java Arithmetic Operator convert pounds into kilograms
- Java Arithmetic Operator divide two integer
- Java Arithmetic Operator divisible by 3
- Java Arithmetic Operator increment and decrement result 1
- Java Arithmetic Operator increment and decrement result 2
