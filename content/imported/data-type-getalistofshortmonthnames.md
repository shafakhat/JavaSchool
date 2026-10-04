---
title: Get a List of Short Month Names
nav: Get a List of Short Month ...
description: String[] shortMonths = new DateFormatSymbols().getShortMonths();
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20140128041556/http://www.java2s.com/Tutorial/Java/0040__Data-Type/GetaListofShortMonthNames.htm
---
```java title=Example.java
import java.text.DateFormatSymbols;
public class Main {
  public static void main(String[] args) {
    String[] shortMonths = new DateFormatSymbols().getShortMonths();
    for (int i = 0; i < shortMonths.length; i++) {
      String shortMonth = shortMonths[i];
      System.out.println("shortMonth = " + shortMonth);
    }
  }
}
```
