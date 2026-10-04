---
title: Java Array search unsorted array for a value using for each loop
nav: Java Array search unsorted...
description: We have an unsorted array and we need to search it for a value.
section: Imported
order: 20008
source: http://www.java2s.com/ref/java/java-array-search-unsorted-array-for-a-value-using-for-each-loop.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Question

We have an unsorted array and we need to search it for a value.

If the value is found display 'value found', otherwise display 'not found'.

Code structure

```java title=Example.java
// Search an array using for-each style for.  publicclass Main {
  publicstaticvoid main(String args[]) {
    int nums[] = { 6, 8, 3, 7, 5, 6, 1, 4 };
    intval = 5;
    boolean found = false;
    /*www.java2s.com*///your code here if(found) {
      System.out.println("Value found!");
    }else{
      System.out.println("Not found!");
    }

  }
}
```

```java title=Example.java
// Search an array using for-each style for.  publicclass Main {
  publicstaticvoid main(String args[]) {
    int nums[] = { 6, 8, 3, 7, 5, 6, 1, 4 };
    intval = 5;
    boolean found = false;

    // use for-each style for to search nums for val  for(int x : nums) {
      if(x == val) {
        found = true;
        break;
      }
    }

    if(found) {
      System.out.println("Value found!");
    }else{
      System.out.println("Not found!");
    }

  }
}
```

PreviousNext

## Related

- Java Array multidimensional Arrays find the closest pair of points
- Java Array multidimensional Arrays pass to methods
- Java Array multidimensional Arrays reference element
- Java array check if an array of primitive chars is empty or null.
- Java Array append a char to char array
