---
title: Labelled breaks breaks out of several levels of nested loops inside a pair of curly braces.
nav: Labelled breaks breaks out...
description: Imported from the java2s.com archive: Labelled breaks breaks out of several levels of nested loops inside a pair of curly braces.
section: Imported - java2s Archive
order: 1197
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Labelledbreaksbreaksoutofseverallevelsofnestedloopsinsideapairofcurlybraces.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    int len = 100;
    int key = 50;
    int k = 0;
    out: {
      for (int i = 0; i < len; i++) {
        for (int j = 0; j < len; j++) {
          if (i == key) {
            break out;
          }
          k += 1;
        }
      }
    }
    System.out.println(k);
  }
}
```
