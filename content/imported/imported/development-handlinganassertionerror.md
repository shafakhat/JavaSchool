---
title: Handling an Assertion Error
nav: Handling an Assertion Error
description: Imported from java2s.com: Handling an Assertion Error
section: Imported
order: 20043
source: http://java2s.com/Tutorial/Java/0120__Development/HandlinganAssertionError.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    try {
      assert argv.length > 0;
    } catch (AssertionError e) {
      String message = e.getMessage();
      System.out.println(message);
    }
  }
}
```
