---
title: Java Arithmetic Operator divisible by 3
nav: Java Arithmetic Operator d...
description: Imported from the java2s.com archive: Java Arithmetic Operator divisible by 3
section: Imported - java2s Archive
order: 1072
source: https://web.archive.org/web/20210102113217/http://www.java2s.com/ref/java/java-arithmetic-operator-divisible-by-3.html
---
## Question

We would like to check if a number is divisible by 3.

Read the integer from console.

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    int x;
    System.out.print("Enter integer you wish to check: ");
    x = input.nextInt();
    //your code here
    input.close();
  }
}
```

```java title=Example.java
import java.util.Scanner;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Scanner input = newScanner(System.in);
    int x;
    System.out.print("Enter integer you wish to check: ");
    x = input.nextInt();
    if (x % 3 == 0)
      System.out.println("Yep, it's divisible by 3!");
    if (x % 3 != 0)
      System.out.println("Nope, it's not divisible by 3!");
    input.close();
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operator convert feet into meters
- Java Arithmetic Operator convert pounds into kilograms
- Java Arithmetic Operator divide two integer
- Java Arithmetic Operator find the number of years
- Java Arithmetic Operator increment and decrement result 1
