---
title: Java Arithmetic Operator calculate tips
nav: Java Arithmetic Operator c...
description: We would like to write a program that reads the subtotal and the gratuity rate.
section: Imported - java2s Archive
order: 1064
source: https://web.archive.org/web/20210102113216/http://www.java2s.com/ref/java/java-arithmetic-operator-calculate-tips.html
---
## Question

We would like to write a program that reads the subtotal and the gratuity rate.

Then compute the gratuity and total.

For example, if the user enters 10 for subtotal and 15% for gratuity rate, the program displays $1.5 as gratuity and $11.5 as total.

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    double gratuityRate, gratuityTotal, total, subtotal;

    Scanner input = newScanner(System.in);

    //your code here

  }//www.java2s.com
}
```

```java title=Example.java
import java.util.Scanner;

publicclass Main {

  publicstaticvoid main(String[] Strings) {

    double gratuityRate, gratuityTotal, total, subtotal;

    Scanner input = newScanner(System.in);

    System.out.print("Please enter the subtotal and gratuity rate: ");
    subtotal = input.nextDouble();
    gratuityRate = input.nextDouble();

    gratuityTotal = subtotal * gratuityRate * .01;
    total = subtotal + gratuityTotal;

    System.out.print("The gratuity is $" + gratuityTotal + " and total is $" + total);

  }
}
```

## Note

To define a method for the calculation:

```java title=Example.java
import java.util.Scanner;

publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter the subtotal and gratuity rate: ");
    double subtotal = input.nextDouble();
    double gratuityRate = input.nextDouble();

    double gratuity = calculateGratuity(subtotal, gratuityRate);
    double total = calculateTotal(subtotal, gratuity);

    System.out.printf("The gratuity is $%.2f and total is $%.2f\n", gratuity, total);
  }/*fromwww.java2s.com*/privatestaticdouble calculateGratuity(double subtotal, double gratuityRate) {
    gratuityRate /= 100.0;
    return subtotal * gratuityRate;
  }

  privatestaticdouble calculateTotal(double subtotal, double gratuity) {
    return subtotal + gratuity;
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator calculate minutes and seconds
- Java Arithmetic Operator calculate on integer
- Java Arithmetic Operator calculate pentagonal numbers
- Java Arithmetic Operator calculate/approximate PI
- Java Arithmetic Operator compound operator result
