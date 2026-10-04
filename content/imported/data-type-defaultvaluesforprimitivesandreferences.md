---
title: Default values for primitives and references
nav: Default values for primiti...
description: Imported from the java2s.com archive: Default values for primitives and references
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Defaultvaluesforprimitivesandreferences.htm
---
Type  Default Value
---  ---
boolean  false
byte  0
short  0
int  0
long  0L
char  \u0000
float  0.0f
double  0.0d
object reference  null

```java title=Example.java
public class ClassInitializer1 {
  static boolean bool;
  static byte by;
  static char ch;
  static double d;
  static float f;
  static int i;
  static long l;
  static short sh;
  static String str;
  public static void main(String[] args) {
    System.out.println("bool = " + bool);
    System.out.println("by = " + by);
    System.out.println("ch = " + ch);
    System.out.println("d = " + d);
    System.out.println("f = " + f);
    System.out.println("i = " + i);
    System.out.println("l = " + l);
    System.out.println("sh = " + sh);
    System.out.println("str = " + str);
  }
}
```
