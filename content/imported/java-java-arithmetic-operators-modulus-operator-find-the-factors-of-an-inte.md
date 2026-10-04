---
title: Java Arithmetic Operators Modulus Operator find the factors of an integer
nav: Java Arithmetic Operators ...
description: For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/20210102113206/http://www.java2s.com/ref/java/java-arithmetic-operators-modulus-operator-find-the-factors-of-an-inte.html
---
## Question

We would like to write a program that reads an integer.

Display all its smallest factors in increasing order.

For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter an integer: ");
    int n = input.nextInt();
    int i = 2;//your code hereSystem.out.println();
  }
}
```

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    System.out.print("Enter an integer: ");
    int n = input.nextInt();
    int i = 2;
    while (n != 1) {
      if (n % i == 0) {
        System.out.print(i + " ");
        n /= i;
      } else {
        i++;
      }
    }
    System.out.println();
  }
}
```

PreviousNext

## Related

- Java switch two int values without using the third variable
- Java Arithmetic Operators
- Java Arithmetic Operators Modulus Operator
- Java Arithmetic Operators Modulus Operator start new line every 10 elements
- Java Arithmetic Operators Modulus Operator find three digit palindrome number
