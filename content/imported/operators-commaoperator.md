---
title: Comma Operator
nav: Comma Operator
description: Imported from the java2s.com archive: Comma Operator
section: Imported - java2s Archive
order: 1135
source: https://web.archive.org/web/20140829082149/http://www.java2s.com/Tutorial/Java/0060__Operators/CommaOperator.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    for(int i = 1, j = i + 10; i < 5;
        i++, j = i * 2) {
      System.out.println("i= " + i + " j= " + j);
    }
  }
}
java title=Example.java
i= 1 j= 11
i= 2 j= 4
i= 3 j= 6
i= 4 j= 8
```
