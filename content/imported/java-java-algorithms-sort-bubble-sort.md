---
title: Java Algorithms Sort Bubble Sort
nav: Java Algorithms Sort Bubbl...
description: for (out = nElems - 1; out > 1; out--) // outer loop (backward)for (in = 0; in < out; in++) // inner loop (forward)if (a[in] > a[in + 1]) // out of order?
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20210102113327/http://www.java2s.com/ref/java/java-algorithms-sort-bubble-sort.html
---
## Description

```java title=Example.java
import java.util.Arrays;
publicclass Main {
   publicstaticvoid bubbleSort(Integer[] arr) {
      int j = 0;Integer tmp;
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
   publicstaticvoid main(String[] args) {
      Integer[] myArray = { 15, 21, 17, 31, 19 };
      bubbleSort(myArray);
      System.out.println(Arrays.toString(myArray));
   }
}
```

```java title=Example.java
class MyArray {privatelong[] a;
   privateint nElems;
   public MyArray(int max) {
      a = newlong[max]; // create the array
      nElems = 0; // no items yet
   }
   publicvoid insert(long value) {
      a[nElems] = value;
      nElems++;
   }
   publicvoid display() {
      for (int j = 0; j < nElems; j++)
         System.out.print(a[j] + " ");
      System.out.println("");
   }
   publicvoid bubbleSort() {
      int out, in;
      for (out = nElems - 1; out > 1; out--) // outer loop (backward)for (in = 0; in < out; in++) // inner loop (forward)if (a[in] > a[in + 1]) // out of order?
               swap(in, in + 1); // swap them
   }
   privatevoid swap(int one, int two) {
      long temp = a[one];
      a[one] = a[two];
      a[two] = temp;
   }
}
publicclass Main {
   publicstaticvoid main(String[] args) {
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
