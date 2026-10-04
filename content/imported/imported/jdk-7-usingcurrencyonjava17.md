---
title: Using Currency on Java 1.7
nav: Using Currency on Java 1.7
description: Set<Currency> currencies = Currency.getAvailableCurrencies();
section: Imported - java2s Archive
order: 1143
source: https://web.archive.org/web/20130315045405/http://www.java2s.com:80/Code/Java/JDK-7/UsingCurrencyonJava17.htm
---
```java title=Example.java
import java.util.Currency;
import java.util.Locale;
import java.util.Set;
public class Test {
  public static void main(String[] args) {
    Set<Currency> currencies = Currency.getAvailableCurrencies();
    for (Currency currency : currencies) {
      System.out.println("" + currency.getDisplayName() + " - "
          + currency.getDisplayName(Locale.GERMAN) + " - "
          + currency.getNumericCode());
    }
  }
}
```

1.  Format currency
