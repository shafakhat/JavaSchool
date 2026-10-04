---
title: The do while loop in action
nav: The do while loop in action
description: Imported from the java2s.com archive: The do while loop in action
section: Imported - java2s Archive
order: 1170
source: https://web.archive.org/web/20140829092021/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Thedowhileloopinaction.htm
---
```java title=Example.java
do {
  // statements
} while (expression);
java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int limit = 20;
    int sum = 0;
    int i = 1;
    do {
      sum += i;
      i++;
    } while (i <= limit);
    System.out.println("sum = " + sum);
  }
}
java title=Example.java
sum = 210
```
