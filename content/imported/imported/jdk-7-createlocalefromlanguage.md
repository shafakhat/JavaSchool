---
title: Create Locale from Language
nav: Create Locale from Language
description: System.out.printf("Creating from BCP 47 language tags...\n\n");
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20130821170442/http://java2s.com/Code/Java/JDK-7/CreateLocalefromLanguage.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.text.NumberFormat;
import java.util.Date;
import java.util.Locale;
public class Test {
  public static void main(String[] args) {
    long SAMPLE_NUMBER = 123456789L;
    Date NOW = new Date();
    System.out.printf("Creating from BCP 47 language tags...\n\n");
    String[] bcp47LangTags= {"fr-FR", "ja-JP", "en-US"};
    Locale l = null;
    for (String langTag: bcp47LangTags) {
        l = Locale.forLanguageTag(langTag);
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
3.  Create Locale with Locale Builder
