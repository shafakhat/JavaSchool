---
title: Java array shuffle
nav: Java array shuffle
description: int[] i = shuffle(newint[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 });
section: Imported
order: 20014
source: http://www.java2s.com/ref/java/java-array-shuffle.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array shuffle

```java title=Example.java
import java.util.Arrays;
import java.util.Random;

publicclass Main {
  publicstaticint[] shuffle(int[] numbers) {
    for (int i = 0; i < numbers.length; i++) {
      int index = newRandom().nextInt(i + 1);
      int swap = numbers[index];
      numbers[index] = numbers[i];//fromwww.java2s.com
      numbers[i] = swap;
    }
    return numbers;
  }
  publicstaticvoid main(String[] args) {
    int[] i = shuffle(newint[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 });
    System.out.print(Arrays.toString(i));
  }
}
```

```java title=Example.java
import java.util.Arrays;
import java.util.Random;

publicclass Main {
  publicstaticvoid main(String args[]) {
    int[] array = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 };
    shuffleArray(array);//fromwww.java2s.comSystem.out.println(Arrays.toString(array));
  }

  staticvoid shuffleArray(int[] ar) {
    Random rnd = newRandom();
    for (int i = ar.length - 1; i > 0; i--) {
      int index = rnd.nextInt(i + 1);
      // Simple swapint a = ar[index];
      ar[index] = ar[i];
      ar[i] = a;
    }
  }
}
```

PreviousNext

## Related

- Java array remove duplicate elements
- Java array reverse
- Java array shift left and right by one element
- Java array shuffle vis Collections.shuffle
- Java array sort elements
