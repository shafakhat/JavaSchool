---
title: An error produced by manual unboxing.
nav: An error produced by manua...
description: 4. Autobox unbox takes place with method parameters and return values.
section: Imported - java2s Archive
order: 1140
source: https://web.archive.org/web/20090531101456/http://www.java2s.com:80/Code/Java/Data-Type/Anerrorproducedbymanualunboxing.htm
---
An error produced by manual unboxing.

```java title=Example.java
public class UnboxingError {
  public static void main(String args[]) {
    Integer iOb = 1000; // autobox the value 1000
    int i = iOb.byteValue(); // manually unbox as byte !!!
    System.out.println(i);  // does not display 1000 !
  }
}
```

1.  What is Autoboxing?
---  ---
2.  Type conversion (JDK1.5 Autoboxing/Unboxing)
3.  Demonstrate autobox and unbox.
4.  Autobox unbox takes place with method parameters and return values.
5.  Autobox unbox occurs inside expressions.
6.  Autobox unbox: convert
7.  Autobox unbox a Boolean and Character.
8.  Java Autobox and Unbox
9.  Autobox Demo
10.  Autoboxing/unboxing takes place with method parameters and return values.
11.  Autoboxing/unboxing occurs inside expressions.
12.  Auto-unboxing allows you to mix different types of numeric objects in an expression.
