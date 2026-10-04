---
title: Shell sort implementation in Java
nav: Shell sort implementation ...
description: Next »« PreviousHome » Java Tutorial » AlgorithmsBubble sortBinary SearchInsertion SortSelection sortShell sortHeap SortMerge SortQuick SortFibonacciHanoi puzzleFahrenhei
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20130905021518/http://java2s.com/Tutorials/Java/Algorithms/Shell_sort_implementation_in_Java.htm
---
In this chapter you will learn:

- Shell sort implementation

### Shell sort implementation

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    int maxSize = 10;
    ShellSort arr = new ShellSort(maxSize);
//java2s.comfor (int j = 0; j < maxSize; j++) {
      long n = (int) (java.lang.Math.random() * 99);
      arr.insert(n);
    }
    arr.display();
    arr.shellSort();
    arr.display();
  }
}

class ShellSort {
  privatelong[] data;

  privateint len;

  public ShellSort(int max) {
    data = newlong[max];
    len = 0;
  }

  publicvoid insert(long value) {
    data[len] = value;
    len++;
  }

  publicvoid display() {
    System.out.print("Data:");
    for (int j = 0; j < len; j++)
      System.out.print(data[j] + " ");
    System.out.println("");
  }

  publicvoid shellSort() {
    int inner, outer;
    long temp;
    // find initial value of h
int h = 1;
    while (h <= len / 3)
      h = h * 3 + 1; // (1, 4, 13, 40, 121, ...)
while (h > 0) // decreasing h, until h=1
    {
      // h-sort the file
for (outer = h; outer < len; outer++) {
        temp = data[outer];
        inner = outer;
        // one subpass (eg 0, 4, 8)
while (inner > h - 1 && data[inner - h] >= temp) {
          data[inner] = data[inner - h];
          inner -= h;
        }
        data[inner] = temp;
      }
      h = (h - 1) / 3; // decrease h
    }
  }

}
```

The code above generates the following result.

#### Next chapter...

What you will learn in the next chapter:

- Heap Sort Implementation
