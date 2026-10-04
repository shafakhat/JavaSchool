---
title: Shell sort implementation in Java
nav: Shell sort implementation ...
description: /*w w w . j a va2 s. co m*/ for (int j = 0; j < maxSize; j++) {
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20140713164348/http://java2s.com/Tutorials/Java/Algorithms/Shell_sort_implementation_in_Java.htm
---
### Shell sort implementation

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int maxSize = 10;
    ShellSort arr = new ShellSort(maxSize);
 for (int j = 0; j < maxSize; j++) {
      long n = (int) (java.lang.Math.random() * 99);
      arr.insert(n);
    }
    arr.display();
    arr.shellSort();
    arr.display();
  }
}
class ShellSort {
  private long[] data;
  private int len;
  public ShellSort(int max) {
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
  public void shellSort() {
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
