---
title: Java Arithmetic Operators Modulus Operator start new line every 10 elements
nav: Java Arithmetic Operators ...
description: Java Arithmetic Operators Modulus Operator start new line every 10 elements
section: Imported - java2s Archive
order: 1094
source: https://web.archive.org/web/20210102113206/http://www.java2s.com/ref/java/java-arithmetic-operators-modulus-operator-start-new-line-every-10-ele.html
---
## Description

```java title=Example.java
import java.util.Random;

publicclass Main {

  publicstaticvoid main(String... args) {

    Random rand = newRandom();
    int[] a = newint[100];
    for (int i = 0; i < 100; i++) {
      a[i] = rand.nextInt(100);//fromwww.java2s.comSystem.out.print(a[i] + ", ");
      if ((i + 1) % 10 == 0) {
        System.out.println();
      }
    }
  }
}
```

PreviousNext

## Related

- Java Arithmetic Operators
- Java Arithmetic Operators Modulus Operator
- Java Arithmetic Operators Modulus Operator find the factors of an integer
- Java Arithmetic Operators Modulus Operator find three digit palindrome number
- Java Arithmetic Operators Modulus Operator calculate Greatest Common Divisor
