---
title: Using Initialization Blocks
nav: Using Initialization Blocks
description: Executed for each object that is created. Can initialize instance variables in a class.
section: Imported - java2s Archive
order: 1255
source: https://web.archive.org/web/20140605074143/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/UsingInitializationBlocksAnonstaticinitializationblock.htm
---
Executed for each object that is created. Can initialize instance variables in a class.

```java title=Example.java
public class MainClass {
  static int[] values = new int[10];
  {
    System.out.println("Running initialization block.");
    for (int i = 0; i < values.length; i++) {
      values[i] = (int) (100.0 * Math.random());
    }
  }
  void listValues() {
    for (int value : values) {
      System.out.println(value);
    }
  }
  public static void main(String[] args) {
    MainClass example = new MainClass();
    System.out.println("\nFirst object:");
    example.listValues();
    example = new MainClass();
    System.out.println("\nSecond object:");
    example.listValues();
  }
}
java title=Example.java
Running initialization block.
First object:
35
17
1
10
42
38
42
71
24
7
Running initialization block.
Second object:
45
78
49
9
11
36
0
18
56
38
```
