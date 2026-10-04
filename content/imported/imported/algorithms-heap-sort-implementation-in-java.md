---
title: Heap Sort Implementation in Java
nav: Heap Sort Implementation i...
description: Next »« PreviousHome » Java Tutorial » AlgorithmsBubble sortBinary SearchInsertion SortSelection sortShell sortHeap SortMerge SortQuick SortFibonacciHanoi puzzleFahrenhei
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20130905043900/http://java2s.com/Tutorials/Java/Algorithms/Heap_Sort_Implementation_in_Java.htm
---
In this chapter you will learn:

- Heap Sort Implementation

### Heap Sort Implementation

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int size, i;/*fromjava2s.com*/
    size = 10;
    Heap theHeap = new Heap(size);

    for (i = 0; i < size; i++) {
      int random = (int) (java.lang.Math.random() * 100);
      int newNode = random;
      theHeap.insertAt(i, newNode);
      theHeap.incrementSize();
    }

    System.out.print("Random: ");
    theHeap.displayArray();
    for (i = size / 2 - 1; i >= 0; i--)
      theHeap.sort(i);

    System.out.println("Heap:   ");
    theHeap.displayArray();
    theHeap.displayHeap();
    for (i = size - 1; i >= 0; i--) {
      int biggestNode = theHeap.remove();
      theHeap.insertAt(i, biggestNode);
    }
    System.out.println("Sorted: ");
    theHeap.displayArray();
  }

}

class Heap {
  privateint[] heapArray;

  privateint maxSize;

  privateint currentSize; // number of items in array
public Heap(int mx) {
    maxSize = mx;
    currentSize = 0;
    heapArray = newint[maxSize];
  }

  publicint remove() {
    int root = heapArray[0];
    heapArray[0] = heapArray[--currentSize];
    sort(0);
    return root;
  }

  publicvoid sort(int index) {
    int largerChild;
    int top = heapArray[index];
    while (index < currentSize / 2) {
      int leftChild = 2 * index + 1;
      int rightChild = leftChild + 1;
      // find larger child
if (rightChild < currentSize
          && heapArray[leftChild] < heapArray[rightChild]) {
        largerChild = rightChild;
      } else {
        largerChild = leftChild;
      }
      if (top >= heapArray[largerChild]) {
        break;
      }
      heapArray[index] = heapArray[largerChild];
      index = largerChild;
    }
    heapArray[index] = top;
  }

  publicvoid displayHeap() {
    int nBlanks = 32;
    int itemsPerRow = 1;
    int column = 0;
    int currentIndex = 0;
    while (currentSize > 0) {
      if (column == 0)
        for (int k = 0; k < nBlanks; k++){
          System.out.print(' ');
        }
      System.out.print(heapArray[currentIndex]);

      if (++currentIndex == currentSize){ // done?
break;
      }
      if (++column == itemsPerRow) // end of row?
      {
        nBlanks /= 2;
        itemsPerRow *= 2;
        column = 0;
        System.out.println();
      } else{
        for (int k = 0; k < nBlanks * 2 - 2; k++){
          System.out.print(' '); // interim blanks
        }
      }
    }
    System.out.println();
  }

  publicvoid displayArray() {
    for (int j = 0; j < maxSize; j++)
      System.out.println(heapArray[j]);
  }

  publicvoid insertAt(int index, int newNode) {
    heapArray[index] = newNode;
  }

  publicvoid incrementSize() {
    currentSize++;
  }

}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Merge Sort implementation
- Fast Merge Sort
