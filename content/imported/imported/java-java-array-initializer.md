---
title: Java Array Initializer
nav: Java Array Initializer
description: The following code uses for loop to initialize array elements.
section: Imported
order: 20002
source: http://www.java2s.com/ref/java/java-array-initializer.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Introduction

The following code uses for loop to initialize array elements.

```java title=Example.java
publicclass Main
{
   publicstaticvoid main(String[] args)
   {//fromwww.java2s.comfinalint ARRAY_LENGTH = 10; // constantint[] array = newint[ARRAY_LENGTH]; // create array// calculate value for each array elementfor (int counter = 0; counter < array.length; counter++)
         array[counter] = 2 + 2 * counter;

      System.out.printf("%s%8s%n", "Index", "Value"); // column headings// output each array element's value for (int counter = 0; counter < array.length; counter++)
         System.out.printf("%5d%8d%n", counter, array[counter]);
   }
}
```

Initializing the elements of an array with an array initializer.

```java title=Example.java
publicclass Main
{
   publicstaticvoid main(String[] args)
   {/*fromwww.java2s.com*/// initializer list specifies the initial value for each elementint[] array = {2, 7, 4, 8, 9, 10, 9, 13, 17, 19};

      System.out.printf("%s%8s%n", "Index", "Value"); // column headings// output each array element's value for (int counter = 0; counter < array.length; counter++)
         System.out.printf("%5d%8d%n", counter, array[counter]);
   }
}
```

Initializing the elements of an array to default values of zero.

```java title=Example.java
publicclass Main
{
   publicstaticvoid main(String[] args)
   {//fromwww.java2s.com// declare variable array and initialize it with an array object  int[] array = newint[10]; // new creates the array object System.out.printf("%s%8s%n", "Index", "Value"); // column headings// output each array element's value for (int counter = 0; counter < array.length; counter++)
         System.out.printf("%5d%8d%n", counter, array[counter]);
   }
}
```

PreviousNext

## Related

- Java Enumeration Type java.lang.Enum class
- Java Enumeration Type with validator
- Java Array Type
- Java Array length property
- Java Array as frequency counters
