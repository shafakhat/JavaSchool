---
title: Java Algorithms Sort Shell Sort
nav: Java Algorithms Sort Shell...
description: class MyArray {/*from w w w . j a v a2s .c o m*/ private long[] theArray; // ref to array theArray private int nElems;
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-algorithms-sort-shell-sort.html
---
## Description

```java title=Example.java
class MyArray { private long[] theArray; // ref to array theArray private int nElems;
   public MyArray(int max) {
      theArray = new long[max]; // create the array
      nElems = 0;
   }
   public void insert(long value) // put element into array
   {
      theArray[nElems] = value;
      nElems++;
   }
   public void display() {
      System.out.print("A=");
      for (int j = 0; j < nElems; j++) // for each element, System.out.print(theArray[j] + " "); // display it System.out.println("");
   }
   public void shellSort() {
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
public class Main {
   public static void main(String[] args) {
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

- Java byte array compare for differences
- Java byte array convert from hex string
