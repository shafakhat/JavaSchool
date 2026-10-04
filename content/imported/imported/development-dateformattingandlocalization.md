---
title: Date Formatting and Localization
nav: Date Formatting and Locali...
description: Imported from the java2s.com archive: Date Formatting and Localization
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/20100505183127/http://www.java2s.com:80/Tutorial/Java/0120__Development/DateFormattingandLocalization.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.text.SimpleDateFormat;
public class Main {
  public static void main(String[] args) {
    DateFormat df = DateFormat.getDateInstance();
    if (df instanceof SimpleDateFormat) {
      SimpleDateFormat sdf = (SimpleDateFormat) df;
      System.out.println(sdf.toPattern());
    } else {
      System.out.println("sorry");
    }
  }
}
```
