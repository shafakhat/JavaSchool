---
title: Using the while loop to calculate sum
nav: Using the while loop to ca...
description: Imported from the java2s.com archive: Using the while loop to calculate sum
section: Imported - java2s Archive
order: 1179
source: https://web.archive.org/web/20140829082107/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Usingthewhilelooptocalculatesum.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    int limit = 20;
    int sum = 0;
    int i = 1;
    while (i <= limit) {
      sum += i++;
    }
    System.out.println("sum = " + sum);
  }
}
java title=Example.java
sum = 210
```
