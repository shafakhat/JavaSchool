---
title: Define a constant value and use it
nav: Define a constant value an...
description: final double MM_PER_INCH = 25.4; // that cannot be changed
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20070513040521/http://www.java2s.com:80/Tutorial/Java/0020__Language/Defineaconstantvalueanduseit.htm
---
- Using the final keyword to declare a variable.
- The final keyword specifies that the value of a variable is final and cannot be changed.
- It is a convention in Java to write constants in uppercase letters.

```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    final int FEET_PER_YARD = 3;          // Constant values
    final double MM_PER_INCH = 25.4;      // that cannot be changed
    System.out.println(FEET_PER_YARD);
    System.out.println(MM_PER_INCH);
  }
}
java title=Example.java
3
25.4
```
