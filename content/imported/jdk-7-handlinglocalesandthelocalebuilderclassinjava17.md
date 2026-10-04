---
title: Handling locales and the Locale.Builder class in Java 1.7
nav: Handling locales and the L...
description: System.out.println(DateFormat.getDateTimeInstance(DateFormat.LONG,
section: Imported - java2s Archive
order: 1079
source: https://web.archive.org/web/20130821151553/http://java2s.com/Code/Java/JDK-7/HandlinglocalesandtheLocaleBuilderclassinJava17.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Calendar;
import java.util.Locale;
import java.util.Locale.Builder;
public class Test {
  public static void main(String[] args) {
    Calendar calendar = Calendar.getInstance();
    calendar.setWeekDate(2012, 16, 3);
    Builder builder = new Builder();
    builder.setLanguage("hy");
    builder.setScript("Latn");
    builder.setRegion("IT");
    builder.setVariant("arevela");
    Locale locale = builder.build();
    Locale.setDefault(locale);
    System.out.println(DateFormat.getDateTimeInstance(DateFormat.LONG,
        DateFormat.LONG).format(calendar.getTime()));
    System.out.println("" + locale.getDisplayLanguage());
    builder.setLanguage("zh");
    builder.setScript("Hans");
    builder.setRegion("CN");
    locale = builder.build();
    Locale.setDefault(locale);
    System.out.println(DateFormat.getDateTimeInstance(DateFormat.LONG,
        DateFormat.LONG).format(calendar.getTime()));
    System.out.println("" + locale.getDisplayLanguage());
  }
}
```

1.  Using the Locale.Category enumeration to display information using two different locales
---  ---
2.  Create Locale with Locale Builder
3.  Create Locale from Language
