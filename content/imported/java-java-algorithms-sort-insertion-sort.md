---
title: Java Algorithms Sort Insertion Sort
nav: Java Algorithms Sort Inser...
description: class MyArray {/*fromwww.java2s.com*/privatelong[] a; // ref to array aprivateint nElems; // number of data itemspublic MyArray(int max) {
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20210102113327/http://www.java2s.com/ref/java/java-algorithms-sort-insertion-sort.html
---
## Description

```java title=Example.java
class MyArray {privatelong[] a; // ref to array aprivateint nElems; // number of data itemspublic MyArray(int max) {
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
