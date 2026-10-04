---
title: Create Locale with Locale Builder
nav: Create Locale with Locale ...
description: String[][] langRegions = { { "fr", "FR" }, { "ja", "JP" }, { "en", "US" } };
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20130821153903/http://java2s.com/Code/Java/JDK-7/CreateLocalewithLocaleBuilder.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.text.NumberFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Locale.Builder;
public class Test {
  public static void main(String[] args) {
    long SAMPLE_NUMBER = 123456789L;
    Date NOW = new Date();
    String[][] langRegions = { { "fr", "FR" }, { "ja", "JP" }, { "en", "US" } };
    Builder builder = new Builder();
    Locale l = null;
    for (String[] lr : langRegions) {
      builder.clear();
      builder.setLanguage(lr[0]).setRegion(lr[1]);
      l = builder.build();
      displayLocalizedData(l, SAMPLE_NUMBER, NOW);
    }
  }
  static void displayLocalizedData(Locale l, long number, Date date) {
    NumberFormat nf = NumberFormat.getInstance(l);
    DateFormat df = DateFormat.getDateTimeInstance(DateFormat.LONG,
        DateFormat.LONG, l);
    System.out.printf("Locale: %s\nNumber: %s\nDate: %s\n\n",
        l.getDisplayName(), nf.format(number), df.format(date));
  }
}
```

1.  Handling locales and the Locale.Builder class in Java 1.7
---  ---
2.  Using the Locale.Category enumeration to display information using two different locales
3.  Create Locale from Language
