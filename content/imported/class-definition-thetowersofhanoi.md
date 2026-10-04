---
title: The Towers of Hanoi
nav: The Towers of Hanoi
description: public static void doTowers(int topN, char from, char inter, char to) {
section: Imported - java2s Archive
order: 1241
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/TheTowersofHanoi.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int nDisks = 3;
    doTowers(nDisks, 'A', 'B', 'C');
  }
  public static void doTowers(int topN, char from, char inter, char to) {
    if (topN == 1){
      System.out.println("Disk 1 from " + from + " to " + to);
    }else {
      doTowers(topN - 1, from, to, inter);
      System.out.println("Disk " + topN + " from " + from + " to " + to);
      doTowers(topN - 1, inter, from, to);
    }
  }
}
java title=Example.java
Disk 1 from A to C
Disk 2 from A to B
Disk 1 from C to B
Disk 3 from A to C
Disk 1 from B to A
Disk 2 from B to C
Disk 1 from A to C
```
