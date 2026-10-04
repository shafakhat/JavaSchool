---
title: static Initialization block
nav: static Initialization block
description: Imported from the java2s.com archive: static Initialization block
section: Imported - java2s Archive
order: 1073
source: https://web.archive.org/web/20100213071119/http://java2s.com/Code/Java/Class/staticInitializationblock.htm
---
```java title=Example.java
class TryInitialization {
  static int[] values = new int[10];
  static {
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
    example = new TryInitialization();
    example.listValues();
  }
}
```

1.  Initialization block Demo
---  ---
2.  Shared array
3.  To show that certain things really must be initialized
4.  Java Instance Initialization
5.  Initialization order
