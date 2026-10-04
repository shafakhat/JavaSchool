---
title: NumberFormat.getCurrencyInstance(Locale.ENGLISH)
nav: NumberFormat.getCurrencyIn...
description: NumberFormat dollarFormat = NumberFormat.getCurrencyInstance(Locale.ENGLISH);
section: Imported - java2s Archive
order: 1116
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/NumberFormatgetCurrencyInstanceLocaleENGLISH.htm
---
```java title=Example.java
import java.text.NumberFormat;
import java.util.Locale;
public class MainClass {
  public static void main(String[] args) {
    NumberFormat dollarFormat = NumberFormat.getCurrencyInstance(Locale.ENGLISH);
    double minimumWage = 5.15;
    System.out.println(dollarFormat.format(minimumWage));
    System.out.println(dollarFormat.format(40 * 52 * minimumWage));
  }
}
java title=Example.java
5.15
10,712.00
```
