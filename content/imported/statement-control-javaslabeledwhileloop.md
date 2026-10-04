---
title: Java's 'labeled while' loop
nav: Java's 'labeled while' loop
description: Imported from the java2s.com archive: Java's 'labeled while' loop
section: Imported - java2s Archive
order: 1060
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Javaslabeledwhileloop.htm
---
```java title=Example.java
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    int i = 0;
    outer: while (true) {
      System.out.println("Outer while loop");
      while (true) {
        i++;
        System.out.println("i = " + i);
        if (i == 1) {
          System.out.println("continue");
          continue;
        }
        if (i == 3) {
          System.out.println("continue outer");
          continue outer;
        }
        if (i == 5) {
          System.out.println("break");
          break;
        }
        if (i == 7) {
          System.out.println("break outer");
          break outer;
        }
      }
    }
  }
}
java title=Example.java
Outer while loop
i = 1
continue
i = 2
i = 3
continue outer
Outer while loop
i = 4
i = 5
break
Outer while loop
i = 6
i = 7
break outer
```
