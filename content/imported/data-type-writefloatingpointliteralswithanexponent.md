---
title: Write Floating-Point Literals with an exponent
nav: Write Floating-Point Liter...
description: Write the number as a decimal value followed by an E, or an e.
section: Imported - java2s Archive
order: 1147
source: https://web.archive.org/web/20070330084355/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/WriteFloatingPointLiteralswithanexponent.htm
---
Write the number as a decimal value followed by an E, or an e.

- Floating-point literals are of type double by default.
- To specify a value of type float, you append an f, or an F.

```java title=Example.java
public class MainClass{
  public static void main(String[] arg){
     double f1 = 1.496E8;
     double f2 = 9.0E-28;
     System.out.println(f1);
     System.out.println(f2);
     System.out.println(f2 + f1);
  }
}
java title=Example.java
1.496E8
9.0E-28
1.496E8
```
