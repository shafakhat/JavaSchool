---
title: Java Arithmetic Operator find the number of years
nav: Java Arithmetic Operator f...
description: We would like to write a program that prompts the user to enter the minutes (e.g., 1 billion)
section: Imported - java2s Archive
order: 1073
source: https://web.archive.org/web/20210102113217/http://www.java2s.com/ref/java/java-arithmetic-operator-find-the-number-of-years.html
---
## Question

We would like to write a program that prompts the user to enter the minutes (e.g., 1 billion)

Display the number of years and days for the minutes.

For simplicity, assume a year has 365 days.

Here is a sample run:

```java title=Example.java
Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days
java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    // Prompt the user to enter the number of minutesSystem.out.print("Enter the number of minutes: ");
    int minutes = input.nextInt();
    //your code // Display resultsSystem.out.println(minutes + " minutes is approximately " + years
      + " years and " + days + " days");
  }
}
java title=Example.java
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
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator convert pounds into kilograms
- Java Arithmetic Operator divide two integer
- Java Arithmetic Operator divisible by 3
- Java Arithmetic Operator increment and decrement result 1
- Java Arithmetic Operator increment and decrement result 2
