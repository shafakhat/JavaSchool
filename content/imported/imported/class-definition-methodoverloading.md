---
title: Method Overloading
nav: Method Overloading
description: Java allows you to have multiple methods having the same name, as long as each method accept different sets of argument types. In other words, in our example, it is legal
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20070701162333/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/MethodOverloading.htm
---
Java allows you to have multiple methods having the same name, as long as each method accept different sets of argument types. In other words, in our example, it is legal to have these two methods in the same class.

```java title=Example.java
public String printString(String string)
public String printString(String string, int offset)
```

This technique is called method overloading. The return value of the method is not taken into consideration. As such, these two methods must not exist in the same class:

```java title=Example.java
public int countRows(int number);
public String countRows(int number);
```
