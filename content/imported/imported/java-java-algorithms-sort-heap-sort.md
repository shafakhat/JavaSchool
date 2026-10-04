---
title: Java Algorithms Sort Heap Sort
nav: Java Algorithms Sort Heap ...
description: privateint maxSize; // size of arrayprivateint currentSize; // number of items in arraypublic Heap(int mx) {
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20210102113327/http://www.java2s.com/ref/java/java-algorithms-sort-heap-sort.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java Algorithms Sort Heap Sort

```java title=Example.java
classNode {
   privateint iData; // data item (key)publicNode(int key) {
      iData = key;//www.java2s.com
   }

   publicint getKey() {
      return iData;
   }
}

class Heap {
   privateNode[] heapArray;
   privateint maxSize; // size of arrayprivateint currentSize; // number of items in arraypublic Heap(int mx) {
      maxSize = mx;
      currentSize = 0;
      heapArray = newNode[maxSize];
   }

   publicNode remove() {
      Node root = heapArray[0];
      heapArray[0] = heapArray[--currentSize];
      trickleDown(0);
      return root;
   }

   publicvoid trickleDown(int index) {
      int largerChild;
      Node top = heapArray[index]; // save rootwhile (index < currentSize / 2) // not on bottom row
      {
         int leftChild = 2 * index + 1;
         int rightChild = leftChild + 1;
         // find larger childif (rightChild < currentSize && // right ch exists?
               heapArray[leftChild].getKey() < heapArray[rightChild].getKey())
            largerChild = rightChild;
         else
            largerChild = leftChild;
         // top >= largerChild?if (top.getKey() >= heapArray[largerChild].getKey())
            break;
         heapArray[index] = heapArray[largerChild];
         index = largerChild;
      }
      heapArray[index] = top;
   }

   publicvoid displayHeap() {
      int nBlanks = 32;
      int itemsPerRow = 1;
      int column = 0;
      int j = 0;
      String dots = "...............................";
      System.out.println(dots + dots);

      while (currentSize > 0) // for each heap item
      {
         if (column == 0) // first item in row?for (int k = 0; k < nBlanks; k++) // preceding blanksSystem.out.print(' ');
         // display itemSystem.out.print(heapArray[j].getKey());

         if (++j == currentSize)
            break;

         if (++column == itemsPerRow) {
            nBlanks /= 2; // half the blanks
            itemsPerRow *= 2; // twice the items
            column = 0; // start over onSystem.out.println(); // new row
         } else// next item on rowfor (int k = 0; k < nBlanks * 2 - 2; k++)
               System.out.print(' '); // interim blanks
      }
      System.out.println("\n" + dots + dots); // dotted bottom line
   }

   publicvoid displayArray() {
      for (int j = 0; j < maxSize; j++)
         System.out.print(heapArray[j].getKey() + " ");
      System.out.println("");
   }

   publicvoid insertAt(int index, Node newNode) {
      heapArray[index] = newNode;
   }

   publicvoid incrementSize() {
      currentSize++;
   }
}

publicclass Main {
   publicstaticvoid main(String[] args) {
      int size = 10, j;

      Heap theHeap = new Heap(size);

      for (j = 0; j < size; j++) // fill array with
      { // random nodesint random = (int) (java.lang.Math.random() * 100);
         Node newNode = newNode(random);
         theHeap.insertAt(j, newNode);
         theHeap.incrementSize();
      }

      System.out.print("Random: ");
      theHeap.displayArray();

      for (j = size / 2 - 1; j >= 0; j--)
         theHeap.trickleDown(j);

      System.out.print("Heap:   ");
      theHeap.displayArray();
      theHeap.displayHeap();

      for (j = size - 1; j >= 0; j--) // remove from heap and
      {
         Node biggestNode = theHeap.remove();
         theHeap.insertAt(j, biggestNode);
      }
      System.out.print("Sorted: ");
      theHeap.displayArray(); // display sorted array
   }
}
```

PreviousNext

## Related

- Java Algorithms Search Linear Search
- Java Algorithms Solve Towers of Hanoi puzzle
- Java Algorithms Sort Bubble Sort
- Java Algorithms Sort Insertion Sort
- Java Algorithms Sort Insertion Sort on custom objects
