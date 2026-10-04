---
title: Print the limits of primitive types (e.g. byte, short, int ...) in Java
nav: Print the limits of primit...
description: System.out.println("Min int value = " + Integer.MIN_VALUE);
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/PrintthelimitsofprimitivetypesegbyteshortintinJava.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    System.out.println("Min byte value   = " + Byte.MIN_VALUE);
    System.out.println("Max byte value   = " + Byte.MAX_VALUE);
    System.out.println("Min short value  = " + Short.MIN_VALUE);
    System.out.println("Max short value  = " + Short.MAX_VALUE);
    System.out.println("Min int value    = " + Integer.MIN_VALUE);
    System.out.println("Max int value    = " + Integer.MAX_VALUE);
    System.out.println("Min float value  = " + Float.MIN_VALUE);
    System.out.println("Max float value  = " + Float.MAX_VALUE);
    System.out.println("Min double value = " + Double.MIN_VALUE);
    System.out.println("Max double value = " + Double.MAX_VALUE);
  }
}
```
