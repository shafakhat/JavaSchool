---
title: Initialization block Demo
nav: Initialization block Demo
description: Imported from the java2s.com archive: Initialization block Demo
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20100213071231/http://java2s.com/Code/Java/Class/InitializationblockDemo.htm
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
    System.out.println();
    for (int i = 0; i < values.length; i++)
      System.out.print(" " + values[i]);
    System.out.println();
  }
  public static void main(String[] args) {
    TryInitialization example = new TryInitialization();
    System.out.println("\nFirst object:");
    example.listValues();
    example = new TryInitialization();
    System.out.println("\nSecond object:");
    example.listValues();
  }
}
```

1.  static Initialization block
---  ---
2.  Shared array
3.  To show that certain things really must be initialized
4.  Java Instance Initialization
5.  Initialization order
