---
title: The Narrowing Conversion
nav: The Narrowing Conversion
description: The narrowing conversion occurs from a type to a different type that has a smaller size, such as from a long (64 bits) to an int (32 bits).
section: Imported - java2s Archive
order: 1078
source: https://web.archive.org/web/20140829082146/http://www.java2s.com/Tutorial/Java/0040__Data-Type/TheNarrowingConversion.htm
---
The narrowing conversion occurs from a type to a different type that has a smaller size, such as from a long (64 bits) to an int (32 bits).
---
In general, the narrowing primitive conversion can occur in these cases:
short to byte or char char to byte or short int to byte, short, or char long to byte, short, or char float to byte, short, char, int, or long double to byte, short, char, int, long, or float
The narrowing primitive conversion must be explicit. You need to specify the target type in parentheses.

```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    long a = 10;
    int b = (int) a; // narrowing conversion
    System.out.println(a);
    System.out.println(b);
  }
}
```
