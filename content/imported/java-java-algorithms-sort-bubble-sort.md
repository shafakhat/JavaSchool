---
title: Java Algorithms Sort Bubble Sort
nav: Java Algorithms Sort Bubbl...
description: int j = 0;/*from ww w .ja v a 2 s .c o m*/ Integer tmp;
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-algorithms-sort-bubble-sort.html
---
## Description

```java title=Example.java
import java.util.Arrays;
public class Main {
   public static void bubbleSort(Integer[] arr) {
      int j = 0; Integer tmp;
      boolean sorted = false;
      while (!sorted) {
         sorted = true;
         j++;
         for (int i = 0; i < arr.length - j; i++) {
            if (arr[i].compareTo(arr[i + 1]) > 0) {
               tmp = arr[i];
               arr[i] = arr[i + 1];
               arr[i + 1] = tmp;
               sorted = false;
            }
         }
      }
   }
   public static void main(String[] args) {
      Integer[] myArray = { 15, 21, 17, 31, 19 };
      bubbleSort(myArray);
      System.out.println(Arrays.toString(myArray));
   }
}
java title=Example.java
class MyArray {private long[] a;
   private int nElems;
   public MyArray(int max) {
      a = new long[max]; // create the array
      nElems = 0; // no items yet
   }
   public void insert(long value) {
      a[nElems] = value;
      nElems++;
   }
   public void display() {
      for (int j = 0; j < nElems; j++)
         System.out.print(a[j] + " ");
      System.out.println("");
   }
   public void bubbleSort() {
      int out, in;
      for (out = nElems - 1; out > 1; out--) // outer loop (backward) for (in = 0; in < out; in++) // inner loop (forward) if (a[in] > a[in + 1]) // out of order?
               swap(in, in + 1); // swap them
   }
   private void swap(int one, int two) {
      long temp = a[one];
      a[one] = a[two];
      a[two] = temp;
   }
}
public class Main {
   public static void main(String[] args) {
      int maxSize = 100; // array size
      MyArray arr = new MyArray(maxSize); // create the array
      arr.insert(7);
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
      arr.bubbleSort(); // bubble sort them
      arr.display(); // display them again
   }
}
```

PreviousNext

## Related
