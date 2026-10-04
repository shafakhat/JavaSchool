---
title: Using Initialization Blocks
nav: Using Initialization Blocks
description: A block defined using the keyword static. Executed once when the class is loaded. Can initialize only static data members of the class.
section: Imported - java2s Archive
order: 1259
source: https://web.archive.org/web/20140829084356/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/UsingInitializationBlocksstaticinitializationblock.htm
---
A block defined using the keyword static. Executed once when the class is loaded. Can initialize only static data members of the class.

```java title=Example.java
public class MainClass {
  static int[] values = new int[10];
  static {
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
58
22
49
75
1
35
76
19
27
63
Second object:
58
22
49
75
1
35
76
19
27
63
```
