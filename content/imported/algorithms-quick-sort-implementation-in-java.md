---
title: Quick Sort implementation in Java
nav: Quick Sort implementation ...
description: QuickSortSimpleVersion arr = new QuickSortSimpleVersion(maxSize); // create array
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://java2s.com/Tutorials/Java/Algorithms/Quick_Sort_implementation_in_Java.htm
---
In this chapter you will learn:

- Quick Sort implementation
- Quick Sort implementation from jodd.org
- QuickSort dealing with small amount of elements
- Quick sort with median-of-three partitioning

### Quick Sort implementation

```java title=Example.java
public class Main{
  public static void main(String[] args) {
    int maxSize = 16; // array size
    QuickSortSimpleVersion arr = new QuickSortSimpleVersion(maxSize); // create array
for (int j = 0; j < maxSize; j++){
      long n = (int) (java.lang.Math.random() * 99);
      arr.insert(n);
    }
    arr.display();
    arr.quickSort();
    arr.display();
  }
}
class QuickSortSimpleVersion {
  private long[] data;
  private int len;
  public QuickSortSimpleVersion(int max) {
    data = new long[max];
    len = 0;
  }
  public void insert(long value) {
    data[len] = value;
    len++;
  }
  public void display() {
    System.out.print("Data:");
    for (int j = 0; j < len; j++)
      System.out.print(data[j] + " ");
    System.out.println("");
  }
  public void quickSort() {
    recQuickSort(0, len - 1);
  }
  public void recQuickSort(int left, int right) {
    if (right - left <= 0){ // if size <= 1 already sorted
 return;
    }else{ // size is 2 or larger
 long pivot = data[right]; // rightmost item
 // partition range
 int partition = partitionData(left, right, pivot);
      recQuickSort(left, partition - 1); // sort left side
      recQuickSort(partition + 1, right); // sort right side
    }
  }
  public int partitionData(int left, int right, long pivot) {
    int leftPtr = left - 1; // left (after ++)
 int rightPtr = right; // right-1 (after --)
 while (true) { // find bigger item
 while (data[++leftPtr] < pivot){
        ;
      }
      // find smaller item
 while (rightPtr > 0 && data[--rightPtr] > pivot){
        ;
      }
      if (leftPtr >= rightPtr){ // if pointers cross, partition done
 break;
      }else{
        swap(leftPtr, rightPtr);
      }
    }
    swap(leftPtr, right); // restore pivot and return pivot location
 return leftPtr;
  }
  public void swap(int d1, int d2) {
    long temp = data[d1];
    data[d1] = data[d2];
    data[d2] = temp;
  }
}
```

The code above generates the following result.

### Quick Sort implementation from jodd.org

The following quick sort code is from joddy.org and released under open source license.

```java title=Example.java
// Copyright (c) 2003-2009, Jodd Team (jodd.org). All Rights Reserved.
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
public class Main{
  public static void main(String[] argv){
    Object[] objectArray = new Integer[]{1,2,3};
    FastQuickSort.qsort(objectArray, Collections.reverseOrder());
    System.out.println(Arrays.toString(objectArray));
  }
}
/**
 * Maybe the fastest implementation of famous Quick-Sort
 * algorithm. It is even faster than Denisa Ahrensa implementation that
 * performs 7.5s for sorting million objects, this implementation
 * sorts for 6.8s. However, {@link FastMergeSort} is much faster.
 */class FastQuickSort  {
  @SuppressWarnings({"unchecked"})
  public static void qsort(Object[] c, Comparator comparator) {
    int i, j, left = 0, right = c.length - 1, stack_pointer = -1;
    int[] stack = new int[128];
    Object swap, temp;
    while (true) {
      if (right - left <= 7) {
        for (j = left + 1; j <= right; j++) {
          swap = c[j];
          i = j - 1;
          while (i >= left && comparator.compare(c[i], swap) > 0) {
            c[i + 1] = c[i--];
          }
          c[i + 1] = swap;
        }
        if (stack_pointer == -1) {
          break;
        }
        right = stack[stack_pointer--];
        left = stack[stack_pointer--];
      } else {
        int median = (left + right) >> 1;
        i = left + 1;
        j = right;
        swap = c[median]; c[median] = c[i]; c[i] = swap;
        if (comparator.compare(c[left], c[right]) > 0) {
          swap = c[left]; c[left] = c[right]; c[right] = swap;
        }
        if (comparator.compare(c[i], c[right]) > 0) {
          swap = c[i]; c[i] = c[right]; c[right] = swap;
        }
        if (comparator.compare(c[left], c[i]) > 0) {
          swap = c[left]; c[left] = c[i]; c[i] = swap;
        }
        temp = c[i];
        while (true) {
          //noinspection ControlFlowStatementWithoutBraces,StatementWithEmptyBody
 while (comparator.compare(c[++i], temp) < 0);
          //noinspection ControlFlowStatementWithoutBraces,StatementWithEmptyBody
 while (comparator.compare(c[--j], temp) > 0);
          if (j < i) {
            break;
          }
          swap = c[i]; c[i] = c[j]; c[j] = swap;
        }
        c[left + 1] = c[j];
        c[j] = temp;
        if (right - i + 1 >= j - left) {
          stack[++stack_pointer] = i;
          stack[++stack_pointer] = right;
          right = j - 1;
        } else {
          stack[++stack_pointer] = left;
          stack[++stack_pointer] = j - 1;
          left = i;
        }
      }
    }
  }
}
```

The code above generates the following result.

### QuickSort dealing with small amount of elements

The following code is an open source version of quick sort. The interesting part of it is that it checks the number of elements in the array. If there are only three elements in the array it would not use the quick sort algorithm which will take longer time and more resource.

```java title=Example.java
/*
 * Copyright (c) 1998 - 2005 Versant Corporation
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *
 * Contributors:
 * Versant Corporation - initial API and implementation
 */import java.util.Comparator;
/**
 * Quicksort implementation for sorting arrays. Unlike the merge sort in
 * java.utils.Collections this one does not create any objects. There are
 * two implementations, one for arrays of Comparable's and another that
 * uses a comparator.
 */ class Quicksort {
    /**
     * Sort the first size entries in a.
     */ public static void quicksort(Object[] a, int size) {
        quicksort(a, 0, size - 1);
    }
    /**
     * Sort the entries in a between left and right inclusive.
     */ public static void quicksort(Object[] a, int left, int right) {
        int size = right - left + 1;
        switch (size) {
            case 0:
            case 1:
                break;
            case 2:
                if (compare(a[left], a[right]) > 0) swap(a, left, right);
                break;
            case 3:
                if (compare(a[left], a[right - 1]) > 0) swap(a, left, right - 1);
                if (compare(a[left], a[right]) > 0) swap(a, left, right);
                if (compare(a[left + 1], a[right]) > 0) swap(a, left + 1, right);
                break;
            default:
                int median = median(a, left, right);
                int partition = partition(a, left, right, median);
                quicksort(a, left, partition - 1);
                quicksort(a, partition + 1, right);
        }
    }
    private static int compare(Object a, Object b) {
        if (a == null) {
            return b == null ? 0 : -1;
        } else if (b == null) {
            return +1;
        } else {
            return ((Comparable)a).compareTo(b);
        }
    }
    private static void swap(Object[] a, int left, int right) {
        Object t = a[left];
        a[left] = a[right];
        a[right] = t;
    }
    private static int median(Object[] a, int left, int right) {
        int center = (left + right) / 2;
        if (compare(a[left], a[center]) > 0) swap(a, left, center);
        if (compare(a[left], a[right]) > 0) swap(a, left, right);
        if (compare(a[center], a[right]) > 0) swap(a, center, right);
        swap(a, center, right - 1);
        return right - 1;
    }
    private static int partition(Object[] a, int left, int right, int pivotIndex) {
        int leftIndex = left;
        int rightIndex = right - 1;
        while (true) {
            while (compare(a[++leftIndex], a[pivotIndex]) < 0);
            while (compare(a[--rightIndex], a[pivotIndex]) > 0);
            if (leftIndex >= rightIndex) {
                break; // pointers cross so partition done
            } else {
                swap(a, leftIndex, rightIndex);
            }
        }
        swap(a, leftIndex, right - 1);         // restore pivot
 return leftIndex;                 // return pivot location
    }
    /**
     * Sort the first size entries in a.
     */ public static void quicksort(Object[] a, int size, Comparator c) {
        quicksort(a, 0, size - 1, c);
    }
    /**
     * Sort the entries in a between left and right inclusive.
     */ public static void quicksort(Object[] a, int left, int right, Comparator c) {
        int size = right - left + 1;
        switch (size) {
            case 0:
            case 1:
                break;
            case 2:
                if (c.compare(a[left], a[right]) > 0) swap(a, left, right);
                break;
            case 3:
                if (c.compare(a[left], a[right - 1]) > 0) swap(a, left, right - 1);
                if (c.compare(a[left], a[right]) > 0) swap(a, left, right);
                if (c.compare(a[left + 1], a[right]) > 0) swap(a, left + 1, right);
                break;
            default:
                int median = median(a, left, right, c);
                int partition = partition(a, left, right, median, c);
                quicksort(a, left, partition - 1, c);
                quicksort(a, partition + 1, right, c);
        }
    }
    private static int median(Object[] a, int left, int right, Comparator c) {
        int center = (left + right) / 2;
        if (c.compare(a[left], a[center]) > 0) swap(a, left, center);
        if (c.compare(a[left], a[right]) > 0) swap(a, left, right);
        if (c.compare(a[center], a[right]) > 0) swap(a, center, right);
        swap(a, center, right - 1);
        return right - 1;
    }
    private static int partition(Object[] a, int left, int right,
            int pivotIndex, Comparator c) {
        int leftIndex = left;
        int rightIndex = right - 1;
        while (true) {
            while (c.compare(a[++leftIndex], a[pivotIndex]) < 0);
            while (c.compare(a[--rightIndex], a[pivotIndex]) > 0);
            if (leftIndex >= rightIndex) {
                break; // pointers cross so partition done
            } else {
                swap(a, leftIndex, rightIndex);
            }
        }
        swap(a, leftIndex, right - 1);         // restore pivot
 return leftIndex;                 // return pivot location
    }
}
```

### Quick sort with median-of-three partitioning

```java title=Example.java
public class Main {
  private long[] data;
private int len;
  public Main(int max) {
    data = new long[max];
    len = 0;
  }
  public void insert(long value) {
    data[len] = value; // insert and increment size
    len++;
  }
  public void display() {
    System.out.print("Data:");
    for (int j = 0; j < len; j++)
      System.out.print(data[j] + " ");
    System.out.println("");
  }
  public void quickSort() {
    recQuickSort(0, len - 1);
  }
  public void recQuickSort(int left, int right) {
    int size = right - left + 1;
    if (size <= 3) // manual sort if small
      manualSort(left, right);
    else // quicksort if large
    {
      long median = medianOf3(left, right);
      int partition = partitionIt(left, right, median);
      recQuickSort(left, partition - 1);
      recQuickSort(partition + 1, right);
    }
  }
  public long medianOf3(int left, int right) {
    int center = (left + right) / 2;
    // order left & center
 if (data[left] > data[center])
      swap(left, center);
    // order left & right
 if (data[left] > data[right])
      swap(left, right);
    // order center & right
 if (data[center] > data[right])
      swap(center, right);
    swap(center, right - 1); // put pivot on right
 return data[right - 1]; // return median value
  }
  public void swap(int dex1, int dex2) {
    long temp = data[dex1];
    data[dex1] = data[dex2];
    data[dex2] = temp;
  }
  public int partitionIt(int left, int right, long pivot) {
    int leftPtr = left; // right of first elem
 int rightPtr = right - 1; // left of pivot
 while (true) {
      //       find bigger
 while (data[++leftPtr] < pivot)
        ;
      //       find smaller
 while (data[--rightPtr] > pivot)
        ;
      if (leftPtr >= rightPtr) // if pointers cross, partition done
 break;
      else // not crossed, so
        swap(leftPtr, rightPtr); // swap elements
    }
    swap(leftPtr, right - 1); // restore pivot
 return leftPtr; // return pivot location
  }
  public void manualSort(int left, int right) {
    int size = right - left + 1;
    if (size <= 1)
      return; // no sort necessary
 if (size == 2) { // 2-sort left and right
 if (data[left] > data[right])
        swap(left, right);
      return;
    } else // size is 3
    { // 3-sort left, center, & right
 if (data[left] > data[right - 1])
        swap(left, right - 1); // left, center
 if (data[left] > data[right])
        swap(left, right); // left, right
 if (data[right - 1] > data[right])
        swap(right - 1, right); // center, right
    }
  }
  public static void main(String[] args) {
    int maxSize = 16;
    Main arr = new Main(maxSize);
    for (int j = 0; j < maxSize; j++) { // random numbers
 long n = (int) (java.lang.Math.random() * 99);
      arr.insert(n);
    }
    arr.display();
    arr.quickSort();
    arr.display();
  }
}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Fibonacci implementation
