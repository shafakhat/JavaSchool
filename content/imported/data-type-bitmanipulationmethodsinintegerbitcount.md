---
title: Bit manipulation methods in Integer
nav: Bit manipulation methods i...
description: System.out.println("Number of one bits: " + Integer.bitCount(n));
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20070319212911/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/BitmanipulationmethodsinIntegerbitCount.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int n = 170; // 10101010
    System.out.println("Value in binary: 10101010");
    System.out.println("Number of one bits: " + Integer.bitCount(n));
  }
}
```

```java title=Example.java
Value in binary: 10101010
Number of one bits: 4
```
