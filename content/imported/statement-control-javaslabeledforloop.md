---
title: Java's 'labeled for' loop
nav: Java's 'labeled for' loop
description: Imported from the java2s.com archive: Java's 'labeled for' loop
section: Imported - java2s Archive
order: 1324
source: https://web.archive.org/web/20140829092246/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Javaslabeledforloop.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int i = 0;
    outer: for (; true;) {
      inner: for (; i < 10; i++) {
        System.out.println("i = " + i);
        if (i == 2) {
          System.out.println("continue");
          continue;
        }
        if (i == 3) {
          System.out.println("break");
          i++;
          break;
        }
        if (i == 7) {
          System.out.println("continue outer");
          i++;
          continue outer;
        }
        if (i == 8) {
          System.out.println("break outer");
          break outer;
        }
        for (int k = 0; k < 5; k++) {
          if (k == 3) {
            System.out.println("continue inner");
            continue inner;
          }
        }
      }
    }
  }
}
java title=Example.java
i = 0
continue inner
i = 1
continue inner
i = 2
continue
i = 3
break
i = 4
continue inner
i = 5
continue inner
i = 6
continue inner
i = 7
continue outer
i = 8
break outer
```
