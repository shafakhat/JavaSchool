---
title: Format currency
nav: Format currency
description: System.out.printf("Default locale: %s\n", Locale.getDefault()
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20130315051019/http://www.java2s.com:80/Code/Java/JDK-7/Formatcurrency.htm
---
Format currency

```java title=Example.java
import java.math.BigDecimal;
import java.text.NumberFormat;
import java.util.Currency;
import java.util.Locale;
public class Test {
  public static void main(String[] args) {
    BigDecimal value = new BigDecimal(12345);
    Locale.setDefault(Locale.JAPAN);
    System.out.printf("Default locale: %s\n", Locale.getDefault()
        .getDisplayName());
    NumberFormat nf = NumberFormat.getCurrencyInstance();
    String formattedCurrency = nf.format(value);
    System.out.printf("%s\n", formattedCurrency);
    nf.setCurrency(Currency.getInstance(Locale.US));
    formattedCurrency = nf.format(value);
    System.out.printf("%s\n\n", formattedCurrency);
    Locale.setDefault(Locale.US);
    System.out.printf("Default locale: %s\n", Locale.getDefault()
        .getDisplayName());
    nf = NumberFormat.getCurrencyInstance();
    formattedCurrency = nf.format(value);
    System.out.printf("%s\n", formattedCurrency);
    nf.setCurrency(Currency.getInstance("JPY"));
    formattedCurrency = nf.format(value);
    System.out.printf("%s\n\n", formattedCurrency);
    Locale.setDefault(Locale.FRANCE);
    System.out.printf("Default locale: %s\n", Locale.getDefault()
        .getDisplayName());
    nf = NumberFormat.getCurrencyInstance();
    formattedCurrency = nf.format(value);
    System.out.printf("%s\n", formattedCurrency);
    nf.setCurrency(Currency.getInstance("USD"));
    formattedCurrency = nf.format(value);
    System.out.printf("%s\n\n", formattedCurrency);
  }
}
```

1.  Using Currency on Java 1.7
