---
title: Selection sort implementation in Java
nav: Selection sort implementat...
description: SelectionSort arr = new SelectionSort(maxSize); // create the array
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/Algorithms/Selection_sort_implementation_in_Java.htm
---
### Selection sort implementation

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int maxSize = 100;
    SelectionSort arr = new SelectionSort(maxSize); // create the array
    arr.insert(2);
    arr.insert(1);
    arr.insert(4);
    arr.insert(3);
    arr.insert(6);
    arr.insert(5);
    arr.insert(9);
    arr.insert(8);
    arr.insert(10);
    arr.insert(3);
    arr.display();
    arr.selectionSort();
    arr.display();
  }
}
class SelectionSort {
  private long[] a;
  private int nElems;
  public SelectionSort(int max) {
    a = new long[max];
    nElems = 0;
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
  public void selectionSort() {
    int out, in, min;
    for (out = 0; out < nElems - 1; out++) // outer loop
    {
      min = out; // minimum
 for (in = out + 1; in < nElems; in++)
        // inner loop
 if (a[in] < a[min]) // if min greater,
          min = in; // a new min
      swap(out, min); // swap them
    }
  }
  private void swap(int one, int two) {
    long temp = a[one];
    a[one] = a[two];
    a[two] = temp;
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Shell sort implementation
