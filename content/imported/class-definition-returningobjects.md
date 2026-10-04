---
title: Returning Objects
nav: Returning Objects
description: Imported from the java2s.com archive: Returning Objects
section: Imported - java2s Archive
order: 1199
source: https://web.archive.org/web/20140829092009/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/ReturningObjects.htm
---
```java title=Example.java
class Test {
  int a;
  Test(int i) {
    a = i;
  }
  Test incrByTen() {
    Test temp = new Test(a + 10);
    return temp;
  }
}
class ReturnObjectTest {
  public static void main(String args[]) {
    Test ob1 = new Test(2);
    Test ob2;
    ob2 = ob1.incrByTen();
    System.out.println("ob1.a: " + ob1.a);
    System.out.println("ob2.a: " + ob2.a);
    ob2 = ob2.incrByTen();
    System.out.println("ob2.a after second increase: " + ob2.a);
  }
}
```
