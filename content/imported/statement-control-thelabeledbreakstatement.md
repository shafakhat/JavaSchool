---
title: The Labeled break Statement
nav: The Labeled break Statement
description: The break statement can be followed by a label. The presence of a label will transfer control to the start of the code identified by the label. For example, consider this
section: Imported - java2s Archive
order: 1193
source: https://web.archive.org/web/20140829090606/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/TheLabeledbreakStatement.htm
---
The break statement can be followed by a label. The presence of a label will transfer control to the start of the code identified by the label. For example, consider this code.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    OuterLoop: for (int i = 2;; i++) {
      for (int j = 2; j < i; j++) {
        if (i % j == 0) {
          continue OuterLoop;
        }
      }
      System.out.println(i);
      if (i == 37) {
        break OuterLoop;
      }
    }
  }
}
java title=Example.java
2
3
5
7
11
13
17
19
23
29
31
37
```
