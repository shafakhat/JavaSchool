---
title: Reference inner static class
nav: Reference inner static class
description: Imported from the java2s.com archive: Reference inner static class
section: Imported - java2s Archive
order: 1213
source: https://web.archive.org/web/20140829082752/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Referenceinnerstaticclass.htm
---
```java title=Example.java
class MyClassesDemo {
  public static void main(String[] args) {
    MyClass tlc = new MyClass();
    MyClass.NestedMyClass ntlc;
    ntlc = new MyClass.NestedMyClass();
  }
}
class MyClass {
  private int i;
  private static String name = "MyClass";
  {
    System.out.println("Assigning 1 to i");
    i = 1;
  }
  static class NestedMyClass {
    int j;
    {
      System.out.println("Assigning 2 to j");
      j = 2;
      System.out.println(name);
    }
  }
}
```
