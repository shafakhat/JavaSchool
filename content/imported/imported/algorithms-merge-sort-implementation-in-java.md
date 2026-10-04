---
title: Merge Sort implementation in Java
nav: Merge Sort implementation ...
description: privatevoid recMergeSort(long[] workSpace, int lowerBound, int upperBound) {
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20130905010011/http://java2s.com/Tutorials/Java/Algorithms/Merge_Sort_implementation_in_Java.htm
---
In this chapter you will learn:

- Merge Sort implementation
- Fast Merge Sort

### Merge Sort implementation

```java title=Example.java
publicclass Main{
  publicstaticvoid main(String[] args) {
    MergeSortArray arr = new MergeSortArray(20);
    arr.insert(4);//fromjava2s.com
    arr.insert(1);
    arr.insert(3);
    arr.insert(0);
    arr.insert(2);
    arr.insert(5);
    arr.insert(4);
    arr.insert(2);
    arr.insert(9);
    arr.insert(5);
    arr.insert(8);
    arr.insert(6);

    arr.display();

    arr.mergeSort();

    arr.display();
  }
}
class MergeSortArray {
  privatelong[] theArray;

  privateint nElems;

  public MergeSortArray(int max) {
    theArray = newlong[max];
    nElems = 0;
  }

  publicvoid insert(long value) {
    theArray[nElems] = value; // insert it
    nElems++; // increment size
  }

  publicvoid display() {
    for (int j = 0; j < nElems; j++){
      System.out.print(theArray[j] + " ");
    }
    System.out.println("");
  }

  publicvoid mergeSort() {
    long[] workSpace = newlong[nElems];
    recMergeSort(workSpace, 0, nElems - 1);
  }

  privatevoid recMergeSort(long[] workSpace, int lowerBound, int upperBound) {
    if (lowerBound == upperBound){ // if range is 1,
return;
    }else { // find midpoint
int mid = (lowerBound + upperBound) / 2;
      // sort low half
      recMergeSort(workSpace, lowerBound, mid);
      // sort high half
      recMergeSort(workSpace, mid + 1, upperBound);
      // merge them
      merge(workSpace, lowerBound, mid + 1, upperBound);
    }
  }

  privatevoid merge(long[] workSpace, int lowPtr, int highPtr, int upperBound) {
    int j = 0; // workspace index
int lowerBound = lowPtr;
    int mid = highPtr - 1;
    int n = upperBound - lowerBound + 1; // # of items
while (lowPtr <= mid && highPtr <= upperBound){
      if (theArray[lowPtr] < theArray[highPtr]){
        workSpace[j++] = theArray[lowPtr++];
      }else{
        workSpace[j++] = theArray[highPtr++];
      }
    }
    while (lowPtr <= mid){
      workSpace[j++] = theArray[lowPtr++];
    }
    while (highPtr <= upperBound){
      workSpace[j++] = theArray[highPtr++];
    }
    for (j = 0; j < n; j++){
      theArray[lowerBound + j] = workSpace[j];
    }
  }
}
```

The code above generates the following result.

### Fast Merge Sort

The following code has an open source implementation of merge sort.

```java title=Example.java
// Copyright (c) 2003-2009, Jodd Team (jodd.org). All Rights Reserved.
//java2s.comimport java.util.Comparator;

/**
 * Faster merge sort. When original JDK routine runs 5s for sorting 1 million
 * objects this one runs for 3.5s.
 *
 * reference: Arrays.mergeSort (private method).
 */publicclass FastMergeSort {

  @SuppressWarnings( { "unchecked" })
  privatestaticvoid mergeSort(Object src[], Object dest[], int low, int high, int off,
      Comparator c) {
    int length = high - low;

    // use insertion sort on smallest arrays
if (length < 7) {
      for (int i = low; i < high; i++) {
        for (int j = i; j > low && c.compare(dest[j - 1], dest[j]) > 0; j--) {
          Object temp = dest[j];
          dest[j] = dest[j - 1];
          dest[j - 1] = temp;
        }
      }
      return;
    }

    // recursively sort halves of dest into src
int destLow = low;
    int destHigh = high;
    low += off;
    high += off;
    int mid = (low + high) >> 1;
    mergeSort(dest, src, low, mid, -off, c);
    mergeSort(dest, src, mid, high, -off, c);

    // is list already sorted?
if (c.compare(src[mid - 1], src[mid]) <= 0) {
      System.arraycopy(src, low, dest, destLow, length);
      return;
    }

    // merge sorted halves from src into dest
for (int i = destLow, p = low, q = mid; i < destHigh; i++) {
      if (q >= high || p < mid && c.compare(src[p], src[q]) <= 0) {
        dest[i] = src[p++];
      } else {
        dest[i] = src[q++];
      }
    }
  }

  publicvoid sort(Object[] a, Comparator c) {
    Object aux[] = a.clone();
    mergeSort(aux, a, 0, a.length, 0, c);
  }

  publicvoid sort(Comparable[] a) {
    Object aux[] = a.clone();
    mergeSort(aux, a, 0, a.length, 0, ComparableComparator.INSTANCE);
  }

  // ---------------------------------------------------------------- static
publicstaticvoid doSort(Object[] a, Comparator c) {
    Object aux[] = a.clone();
    mergeSort(aux, a, 0, a.length, 0, c);
  }

  publicstaticvoid doSort(Comparable[] a) {
    Object aux[] = a.clone();
    mergeSort(aux, a, 0, a.length, 0, ComparableComparator.INSTANCE);
  }

}

// Copyright (c) 2003-2009, Jodd Team (jodd.org). All Rights Reserved.
/**
 * Comparator that adapts Comparables to the
 * Comparator interface.
 */class ComparableComparator<T extends Comparable<T>> implements Comparator<T> {

  /**
   * Cached instance.
   */publicstaticfinal ComparableComparator INSTANCE = new ComparableComparator();

  publicint compare(T o1, T o2) {
    return o1.compareTo(o2);
  }

}
```

#### Next chapter...

What you will learn in the next chapter:

- Quick Sort implementation
- Quick Sort implementation from jodd.org
- QuickSort dealing with small amount of elements
- Quick sort with median-of-three partitioning
