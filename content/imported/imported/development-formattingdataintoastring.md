---
title: Formatting Data into a String
nav: Formatting Data into a Str...
description: String outString = String.format("x = %15.2f y = %14.3g", x, y);
section: Imported
order: 20019
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/FormattingDataintoaString.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] a) {
    double x = 27.5, y = 33.75;
    String outString = String.format("x = %15.2f y = %14.3g", x, y);
    System.out.println(outString);
  }
}
```

```java title=Example.java

x =           27.50 y =           33.8
```
