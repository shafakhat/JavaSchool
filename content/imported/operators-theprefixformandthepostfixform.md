---
title: The prefix form and the postfix form
nav: The prefix form and the po...
description: Imported from the java2s.com archive: The prefix form and the postfix form
section: Imported - java2s Archive
order: 1118
source: https://web.archive.org/web/20140829074722/http://www.java2s.com/Tutorial/Java/0060__Operators/Theprefixformandthepostfixform.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int numA = 5;
    int numB = 10;
    int numC = 0;
    numC = ++numA + numB;
    System.out.println(numA);
    System.out.println(numC);
  }
}
java title=Example.java
6
16
java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int numA = 5;
    int numB = 10;
    int numC = 0;
    numC = --numA + numB--;
    System.out.println(numA);
    System.out.println(numC);
  }
}
java title=Example.java
4
14
```
