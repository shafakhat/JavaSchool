---
title: How to write Binary Search algorithm in Java
nav: How to write Binary Search...
description: The following code implements the binary search algorithm. Its uses the Comparable interface to compare elements in the passed in array.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20130904182451/http://java2s.com/Tutorials/Java/Algorithms/How_to_write_Binary_Search_algorithm_in_Java.htm
---
Next »329/677« Previous

In this chapter you will learn:

- Recursive Binary Search Implementation
- Binary search without recursive
- Binary Search Insert

### Recursive Binary Search Implementation

The following code implements the binary search algorithm. Its uses the Comparable interface to compare elements in the passed in array.

Another feature is that it uses the recursive in the implementation.

```java title=Example.java
publicclass Main {
  publicstaticfinalint NOT_FOUND = -1;
  publicstaticint binarySearch(Comparable[] a, Comparable x) {
    return binarySearch(a, x, 0, a.length - 1);
  }//fromjava2s.comprivatestaticint binarySearch(Comparable[] a, Comparable x, int low, int high) {
    if (low > high)
      return NOT_FOUND;

    int mid = (low + high) / 2;

    if (a[mid].compareTo(x) < 0)
      return binarySearch(a, x, mid + 1, high);
    elseif (a[mid].compareTo(x) > 0)
      return binarySearch(a, x, low, mid - 1);
    elsereturn mid;
  }

  publicstaticvoid main(String[] args) {
    int SIZE = 8;
    Comparable[] a = newInteger[SIZE];
    for (int i = 0; i < SIZE; i++)
      a[i] = newInteger(i * 2);

    for (int i = 0; i < SIZE * 2; i++)
      System.out.println("Found " + i + " at " + binarySearch(a, newInteger(i)));
  }
}
```

The code above generates the following result.

### Binary search without recursive

The following code uses the binary search algorithm to search a hard code array against hard coded value.

```java title=Example.java
publicclass Main{
  publicstaticvoid main(String[] args) {
    double[] x = { -39, -3, 6, 10, 4, 9, 10 };
/*fromjava2s.com*/double value = 8;
    int lower = 0, upper = x.length - 1;

    while (lower <= upper) {
      int middle = (lower + upper) / 2;

      if (value > x[middle])
        lower = middle + 1;
      elseif (value < x[middle])
        upper = middle - 1;
      elsebreak;
    }

    if (lower > upper)
      System.out.println("Not found");
    else
      System.out.println("Found");
  }
}
```

The code above generates the following result.

### Binary Search Insert

```java title=Example.java
publicclass Main{
  publicstaticvoid main(String[] args) {
    int maxSize = 100;
    BinarySearchArray arr = new BinarySearchArray(maxSize);
    arr.insert(2);//java2s.com
    arr.insert(0);
    arr.insert(5);
    arr.insert(6);
    arr.insert(4);
    arr.insert(9);
    arr.insert(4);
    arr.insert(7);
    arr.insert(5);
    arr.insert(9);
    arr.insert(8);
    arr.insert(2);
    arr.insert(4);
    arr.insert(6);
    arr.insert(8);
    arr.insert(9);

    arr.display(); // display array
int searchKey = 27; // search for item
if (arr.find(searchKey) != arr.size())
      System.out.println("Found " + searchKey);
    else
      System.out.println("Can't find " + searchKey);
  }
}
class BinarySearchArray {
  privatelong[] a;

  privateint nElems;

  public BinarySearchArray(int max) {
    a = newlong[max]; // create array
    nElems = 0;
  }

  publicint size() {
    return nElems;
  }

  publicint find(long searchKey) {
    return recFind(searchKey, 0, nElems - 1);
  }

  privateint recFind(long searchKey, int lowerBound, int upperBound) {
    int curIn;

    curIn = (lowerBound + upperBound) / 2;
    if (a[curIn] == searchKey)
      return curIn; // found it
elseif (lowerBound > upperBound)
      return nElems; // can't find it
else// divide range
    {
      if (a[curIn] < searchKey) // in upper half
return recFind(searchKey, curIn + 1, upperBound);
      else// in lower half
return recFind(searchKey, lowerBound, curIn - 1);
    }
  }

  publicvoid insert(long value) {
    int j;
    for (j = 0; j < nElems; j++)
      // find where it goes
if (a[j] > value) // (linear search)
break;
    for (int k = nElems; k > j; k--)
      // move bigger ones up
      a[k] = a[k - 1];
    a[j] = value; // insert it
    nElems++; // increment size
  }

  publicvoid display() {
    for (int j = 0; j < nElems; j++)
      System.out.print(a[j] + " ");
    System.out.println("");
  }
}
```

The code above generates the following result.

```java title=Example.java
0 2 2 4 4 4 5 5 6 6 7 8 8 9 9 9
Can't find 27
```

#### Next chapter...

What you will learn in the next chapter:

- Insertion Sort Implementation
- Object Insertion Sort

Next »« PreviousHome » Java Tutorial » AlgorithmsBubble sortBinary SearchInsertion SortSelection sortShell sortHeap SortMerge SortQuick SortFibonacciHanoi puzzleFahrenheit to Celsius
