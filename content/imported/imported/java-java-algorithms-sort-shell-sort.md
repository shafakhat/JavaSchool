---
title: Java Algorithms Sort Shell Sort
nav: Java Algorithms Sort Shell...
description: class MyArray {/*fromwww.java2s.com*/privatelong[] theArray; // ref to array theArrayprivateint nElems;
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20210102113328/http://www.java2s.com/ref/java/java-algorithms-sort-shell-sort.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Sort Shell Sort

```java title=Example.java
class MyArray {/*fromwww.java2s.com*/privatelong[] theArray; // ref to array theArrayprivateint nElems;

   public MyArray(int max) {
      theArray = newlong[max]; // create the array
      nElems = 0;
   }

   publicvoid insert(long value) // put element into array
   {
      theArray[nElems] = value;
      nElems++;
   }

   publicvoid display() {
      System.out.print("A=");
      for (int j = 0; j < nElems; j++) // for each element,System.out.print(theArray[j] + " "); // display itSystem.out.println("");
   }

   publicvoid shellSort() {
      int inner, outer;
      long temp;

      int h = 1;
      while (h <= nElems / 3)
         h = h * 3 + 1;

      while (h > 0) {
         for (outer = h; outer < nElems; outer++) {
            temp = theArray[outer];
            inner = outer;

            while (inner > h - 1 && theArray[inner - h] >= temp) {
               theArray[inner] = theArray[inner - h];
               inner -= h;
            }
            theArray[inner] = temp;
         }
         h = (h - 1) / 3;
      }
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      int maxSize = 10;
      MyArray arr = new MyArray(maxSize);

      for (int j = 0; j < maxSize; j++) {
         long n = (int) (java.lang.Math.random() * 99);
         arr.insert(n);
      }
      arr.display();
      arr.shellSort();
      arr.display();
   }
}
```

PreviousNext

## Related

- Java Algorithms Sort Insertion Sort on custom objects
- Java Algorithms Sort point along circle in clockwise order
- Java Algorithms Sort Selection Sort
- Java byte array compare for differences
- Java byte array convert from hex string
