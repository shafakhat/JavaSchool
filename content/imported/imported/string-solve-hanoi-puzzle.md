---
title: Java Algorithms How to - Solve Hanoi puzzle
nav: Java Algorithms How to - S...
description: publicstaticvoid hanoiTower(int topN, char src, char inter, char dest) {
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20170428082807/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/String/Solve_Hanoi_puzzle.htm
---
```java title=Example.java
Back to String  ↑
```

## Question

We would like to know how to solve Hanoi puzzle.

## Answer

```java title=Example.java
/*www.java2s.com*/publicclass HanoiTower {
  staticint nDisks = 3;

  publicstaticvoid main(String[] args) {
    hanoiTower(nDisks, 'A', 'B', 'C');
  }

  publicstaticvoid hanoiTower(int topN, char src, char inter, char dest) {
    if (topN == 1)
      System.out.println("Disk 1 from " + src + " to " + dest);
    else {
      // src to inter
      hanoiTower(topN - 1, src, dest, inter);
      // move bottom
      System.out.println("Disk " + topN + " from " + src + " to " + dest);
      //inter to dest
      hanoiTower(topN - 1, inter, src, dest);
    }
  }
}
```

The code above generates the following result.

- Back to String ↑
