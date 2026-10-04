---
title: The continue Statement
nav: The continue Statement
description: The continue statement stops the execution of the current iteration and causes control to begin with the next iteration.
section: Imported - java2s Archive
order: 1184
source: https://web.archive.org/web/20140829084338/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/ThecontinueStatement.htm
---
The continue statement stops the execution of the current iteration and causes control to begin with the next iteration.
For example, the following code prints the number 0 to 9, except 5.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    for (int i = 0; i < 10; i++) {
      if (i == 5) {
        continue;
      }
      System.out.println(i);
    }
  }
}
```
