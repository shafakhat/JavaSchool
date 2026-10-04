---
title: Catch different Exception types
nav: Catch different Exception ...
description: static void someMethod1() throws MyException, YourException {
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20100813145654/http://www.java2s.com:80/Tutorial/Java/0080__Statement-Control/CatchdifferentExceptiontypes.htm
---
```java title=Example.java
class MyException extends Exception {
  MyException() {
    super("My Exception");
  }
}
class YourException extends Exception {
  YourException() {
    super("Your Exception");
  }
}
class LostException {
  public static void main(String[] args) {
    try {
      someMethod1();
    } catch (MyException e) {
      System.out.println(e.getMessage());
    } catch (YourException e) {
      System.out.println(e.getMessage());
    }
  }
  static void someMethod1() throws MyException, YourException {
    try {
      someMethod2();
    } finally {
      throw new MyException();
    }
  }
  static void someMethod2() throws YourException {
    throw new YourException();
  }
}
```
