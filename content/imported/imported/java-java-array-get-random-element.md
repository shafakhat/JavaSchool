---
title: Java array get random element
nav: Java array get random elem...
description: String[] peoples = { "CSS", "HTML", "Java", "Javascript", "SQL", "JVM" };
section: Imported
order: 20005
source: http://www.java2s.com/ref/java/java-array-get-random-element.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array get random element

```java title=Example.java
import java.util.Random;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] peoples = { "CSS", "HTML", "Java", "Javascript", "SQL", "JVM" };
    for (int i = 0; i < peoples.length; i++) {
      int index = newRandom().nextInt(peoples.length);
      String anynames = peoples[index];
      System.out.println(anynames);
    }/*fromwww.java2s.com*/
  }
}
```

PreviousNext

## Related

- Java array find the largest and smallest number using for loop
- Java array find the max and min value via Collections.min/max
- Java array find the max and min value via sorting
- Java array get sub array
- Java array join int[] array to String
