---
title: Throw Exception through main method
nav: Throw Exception through ma...
description: Imported from the java2s.com archive: Throw Exception through main method
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20070612145557/http://www.java2s.com:80/Tutorial/Java/0020__Language/ThrowExceptionthroughmainmethod.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) throws Throwable {
    try {
      throw new Throwable();
    } catch (Exception e) {
      System.err.println("Caught in main()");
    }
  }
}
```
