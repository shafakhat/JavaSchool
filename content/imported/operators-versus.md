---
title: && versus &
nav: && versus &
description: Conditional && will not evaluate the right-hand operand if the left-hand operand is false.
section: Imported - java2s Archive
order: 1133
source: https://web.archive.org/web/20140829092540/http://www.java2s.com/Tutorial/Java/0060__Operators/versus.htm
---
Conditional && will not evaluate the right-hand operand if the left-hand operand is false.

```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int value = 8;
    int count = 10;
    int limit = 11;
    if (++value % 2 == 0 & ++count < limit) {
      System.out.println("here");
      System.out.println(value);
      System.out.println(count);
    }
    System.out.println("there");
    System.out.println(value);
    System.out.println(count);
  }
}
java title=Example.java
there
9
11
```
