---
title: NumberFormat
nav: NumberFormat
description: System.out.println(degreeString + " " + radianString + " " + gradString);
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20140829092057/http://www.java2s.com/Tutorial/Java/0040__Data-Type/NumberFormatMinimumIntegerDigitsMaximumMinimumFractionDigits.htm
---
```java title=Example.java
import java.text.NumberFormat;
public class MainClass {
  public static void main(String[] args) {
    NumberFormat myFormat = NumberFormat.getInstance();
    myFormat.setMinimumIntegerDigits(3);
    myFormat.setMaximumFractionDigits(2);
    myFormat.setMinimumFractionDigits(2);
    for (double d = 0.0; d < 360.0; d++) {
      String radianString = myFormat.format(Math.PI * d / 180.0);
      String gradString = myFormat.format(400 * d / 360);
      String degreeString = myFormat.format(d);
      System.out.println(degreeString + "  " + radianString + "  " + gradString);
    }
  }
}
```
