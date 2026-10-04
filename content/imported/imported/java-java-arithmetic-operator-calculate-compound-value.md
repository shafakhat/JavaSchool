---
title: Java Arithmetic Operator calculate compound value
nav: Java Arithmetic Operator c...
description: Suppose you save $100 each month into a savings account with the annual interest rate 5%.
section: Imported - java2s Archive
order: 1058
source: https://web.archive.org/web/20210102113214/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-compound-value.html
---
## Question

We would like to calculate compound value.

Suppose you save $100 each month into a savings account with the annual interest rate 5%.

Thus, the monthly interest rate is 0.05/12 = 0.00417.

After the first month, the value in the account becomes 100 * (1 + 0.00417) = 100.417

After the second month, the value in the account becomes (100 + 100.417) * (1 + 0.00417) = 201.252

After the third month, the value in the account becomes (100 + 201.252) * (1 + 0.00417) = 302.507

Write a program that prompts the user to enter a monthly saving amount.

Display the account value after the sixth month.

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in); // Create a new Scanner object.finaldouble MONTHLY_INTEREST_RATE = 0.00417; // Initialize constant value// Prompt the user to enter a montly saving amountSystem.out.print("Enter the monthly saving amount: ");
    double savingAmount = input.nextDouble();

    //your code here// Display resultSystem.out.println("After the sixth month, the account value is " + total);
  }/*fromwww.java2s.com*/
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in); // Create a new Scanner object.finaldouble MONTHLY_INTEREST_RATE = 0.00417; // Initialize constant value// Prompt the user to enter a montly saving amountSystem.out.print("Enter the monthly saving amount: ");
    double savingAmount = input.nextDouble();

    // Compute first month account valuedouble total = savingAmount * (1 + MONTHLY_INTEREST_RATE);
    // Compute second month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);
    // Compute third month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);
    // Compute forth month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);
    // Compute fifth month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);
    // Compute sixth month account value
    total = (savingAmount + total) * (1 + MONTHLY_INTEREST_RATE);

    // Display resultSystem.out.println("After the sixth month, the account value is " + total);
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate average speed in miles
- Java Arithmetic Operator calculate circle area
- Java Arithmetic Operator calculate circle area with console input
- Java Arithmetic Operator calculate cylinder volume
- Java Arithmetic Operator calculate distance of two points
