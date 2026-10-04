---
title: Java array remove duplicate elements
nav: Java array remove duplicat...
description: String[] s = {"CSS", "HTML", "CSS","Java","Java", "Javascript",
section: Imported
order: 20009
source: http://www.java2s.com/ref/java/java-array-remove-duplicate-elements.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array remove duplicate elements

```java title=Example.java
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

publicclass Main {
  publicstaticvoid main(String[] args) {
    String[] s = {"CSS", "HTML", "CSS","Java","Java", "Javascript",
        "CSS","SQL","CSS"};
    System.out.println(Arrays.toString(s));
    //fromwww.java2s.com
    s = clean(s);

    System.out.println(Arrays.toString(s));
  }

  publicstaticString[] clean(String[] input) {
    Set<String> unique = newHashSet<>(Arrays.asList(input));
    return unique.toArray(newString[unique.size()]);
  }
}
```

PreviousNext

## Related

- Java array join to String with char separator
- Java array join to String with String separator
- Java array length double
- Java array reverse
- Java array shift left and right by one element
