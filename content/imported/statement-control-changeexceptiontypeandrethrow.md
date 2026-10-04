---
title: Change Exception type and rethrow
nav: Change Exception type and ...
description: Imported from the java2s.com archive: Change Exception type and rethrow
section: Imported - java2s Archive
order: 1196
source: https://web.archive.org/web/20140829080152/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/ChangeExceptiontypeandrethrow.htm
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
class ChainDemo {
  public static void main(String[] args) {
    try {
      someMethod1();
    } catch (MyException e) {
      e.printStackTrace();
    }
  }
  static void someMethod1() throws MyException {
    try {
      someMethod2();
    } catch (YourException e) {
      System.out.println(e.getMessage());
      MyException e2 = new MyException();
      e2.initCause(e);
      throw e2;
    }
  }
  static void someMethod2() throws YourException {
    throw new YourException();
  }
}
```
