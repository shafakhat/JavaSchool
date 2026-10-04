---
title: Four different date formats for four countries
nav: Four different date format...
description: System.out.println("\nThe Date for " + locale.getDisplayCountry() + ":");
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20070319213003/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/FourdifferentdateformatsforfourcountriesUSUKGERMANYFRANCE.htm
---
```java title=Example.java
import static java.text.DateFormat.FULL;
import static java.text.DateFormat.LONG;
import static java.text.DateFormat.MEDIUM;
import static java.text.DateFormat.SHORT;
import static java.util.Locale.FRANCE;
import static java.util.Locale.GERMANY;
import static java.util.Locale.UK;
import static java.util.Locale.US;
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
public class MainClass {
  public static void main(String[] args) {
    Date today = new Date();
    Locale[] locales = { US, UK, GERMANY, FRANCE };
    int[] styles = { FULL, LONG, MEDIUM, SHORT };
    String[] styleNames = { "FULL", "LONG", "MEDIUM", "SHORT" };
    DateFormat fmt = null;
    for (Locale locale : locales) {
      System.out.println("\nThe Date for " + locale.getDisplayCountry() + ":");
      for (int i = 0; i < styles.length; i++) {
        fmt = DateFormat.getDateInstance(styles[i], locale);
        System.out.println("\tIn " + styleNames[i] + " is " + fmt.format(today));
      }
    }
  }
}
```

```java title=Example.java

The Date for United States:
  In FULL is Tuesday, January 16, 2007
  In LONG is January 16, 2007
  In MEDIUM is Jan 16, 2007
  In SHORT is 1/16/07
The Date for United Kingdom:
  In FULL is 16 January 2007
  In LONG is 16 January 2007
  In MEDIUM is 16-Jan-2007
  In SHORT is 16/01/07
The Date for Germany:
  In FULL is Dienstag, 16. Januar 2007
  In LONG is 16. Januar 2007
  In MEDIUM is 16.01.2007
  In SHORT is 16.01.07
The Date for France:
  In FULL is mardi 16 janvier 2007
  In LONG is 16 janvier 2007
  In MEDIUM is 16 janv. 2007
  In SHORT is 16/01/07
```
