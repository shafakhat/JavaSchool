---
title: How to write Bubble sort algorithm in Java
nav: How to write Bubble sort a...
description: Next »« PreviousHome » Java Tutorial » AlgorithmsBubble sortBinary SearchInsertion SortSelection sortShell sortHeap SortMerge SortQuick SortFibonacciHanoi puzzleFahrenhei
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20130807082531/http://java2s.com/Tutorials/Java/Algorithms/How_to_write_Bubble_sort_algorithm_in_Java.htm
---
In this chapter you will learn:

- Bubble sort implementation

### Bubble sort implementation

```java title=Example.java
publicclass Main{
  publicstaticvoid main(String[] args) {
    int maxSize = 100; // array size
    BubbleSort arr; // reference to array
    arr = new BubbleSort(maxSize);
//java2s.com
    arr.insert(77); // insert 10 items
    arr.insert(66);
    arr.insert(44);
    arr.insert(34);
    arr.insert(22);
    arr.insert(88);
    arr.insert(12);
    arr.insert(00);
    arr.insert(55);
    arr.insert(33);

    arr.display();

    arr.bubbleSort();

    arr.display();
  }
}
class BubbleSort {
  privatelong[] a;

  privateint nElems;

  public BubbleSort(int max) {
    a = newlong[max];
    nElems = 0;
  }

  //   put element into array
publicvoid insert(long value) {
    a[nElems] = value;
    nElems++;
  }

  //   displays array contents
publicvoid display() {
    for (int j = 0; j < nElems; j++)
      System.out.print(a[j] + " ");
    System.out.println("");
  }

  publicvoid bubbleSort() {
    int out, in;

    for (out = nElems - 1; out > 1; out--)
      // outer loop (backward)
for (in = 0; in < out; in++)
        // inner loop (forward)
if (a[in] > a[in + 1]) // out of order?
          swap(in, in + 1); // swap them
  }

  privatevoid swap(int one, int two) {
    long temp = a[one];
    a[one] = a[two];
    a[two] = temp;
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Recursive Binary Search Implementation
- Binary search without recursive
- Binary Search Insert
