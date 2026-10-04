---
title: Java Algorithms Sort Insertion Sort
nav: Java Algorithms Sort Inser...
description: class MyArray {/*fromwww.java2s.com*/privatelong[] a; // ref to array aprivateint nElems; // number of data itemspublic MyArray(int max) {
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20210102113327/http://www.java2s.com/ref/java/java-algorithms-sort-insertion-sort.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Sort Insertion Sort

```java title=Example.java
class MyArray {/*fromwww.java2s.com*/privatelong[] a; // ref to array aprivateint nElems; // number of data itemspublic MyArray(int max) {
      a = newlong[max]; // create the array
      nElems = 0; // no items yet
   }

   publicvoid insert(long value) {
      a[nElems] = value; // insert it
      nElems++; // increment size
   }

   publicvoid display() {
      for (int j = 0; j < nElems; j++)
         System.out.print(a[j] + " ");
      System.out.println("");
   }

   publicvoid insertionSort() {
      int in, out;

      for (out = 1; out < nElems; out++) // out is dividing line
      {
         long temp = a[out]; // remove marked item
         in = out; // start shifts at outwhile (in > 0 && a[in - 1] >= temp) // until one is smaller,
         {
            a[in] = a[in - 1]; // shift item to right
            --in; // go left one position
         }
         a[in] = temp; // insert marked item
      }
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      int maxSize = 100; // array size
      MyArray arr = new MyArray(maxSize); // create the array

      arr.insert(7); // insert 10 items
      arr.insert(9);
      arr.insert(4);
      arr.insert(5);
      arr.insert(2);
      arr.insert(8);
      arr.insert(1);
      arr.insert(0);
      arr.insert(6);
      arr.insert(3);

      arr.display(); // display items

      arr.insertionSort(); // insertion-sort them

      arr.display(); // display them again
   }
}
```

PreviousNext

## Related

- Java Algorithms Solve Towers of Hanoi puzzle
- Java Algorithms Sort Bubble Sort
- Java Algorithms Sort Heap Sort
- Java Algorithms Sort Insertion Sort on custom objects
- Java Algorithms Sort point along circle in clockwise order
