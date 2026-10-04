---
title: Shared array
nav: Shared array
description: Imported from the java2s.com archive: Shared array
section: Imported - java2s Archive
order: 1069
source: https://web.archive.org/web/20100213071226/http://java2s.com/Code/Java/Class/Sharedarray.htm
---
```java title=Example.java
class TryInitialization {
  static int[] values = new int[10];
  {
    System.out.println("Running initialization block.");
    for (int i = 0; i < values.length; i++)
      values[i] = (int) (100.0 * Math.random());
  }
  void listValues() {
    for (int i = 0; i < values.length; i++)
      System.out.print(" " + values[i]);
  }
  public static void main(String[] args) {
    TryInitialization example = new TryInitialization();
    example.listValues();
    TryInitialization nextexample = new TryInitialization();
    nextexample.listValues();
    example.listValues();
  }
}
```

1.  static Initialization block
---  ---
2.  Initialization block Demo
3.  To show that certain things really must be initialized
4.  Java Instance Initialization
5.  Initialization order
