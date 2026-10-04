---
title: Memory Leak Demo
nav: Memory Leak Demo
description: Imported from the java2s.com archive: Memory Leak Demo
section: Imported - java2s Archive
order: 1113
source: https://web.archive.org/web/20140829080651/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/MemoryLeakDemo.htm
---
```java title=Example.java
class List {
  MemoryLeak mem;
  List next;
}
class MemoryLeak {
  static List top;
  char[] memory = new char[100000];
  public static void main(String[] args) {
    for (int i = 0; i < 100000; i++) {
      List temp = new List();
      temp.mem = new MemoryLeak();
      temp.next = top;
      top = temp;
    }
  }
}
```
