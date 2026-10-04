---
title: Helper class for format number and currency
nav: Helper class for format nu...
description: /* Copyright 2004 Sun Microsystems, Inc. All rights reserved. You may not modify, use, reproduce, or distribute this software except in compliance with the terms of the
section: Imported - java2s Archive
order: 1181
source: https://web.archive.org/web/20140121023039/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Helperclassforformatnumberandcurrency.htm
---
```java title=Example.java
/* Copyright 2004 Sun Microsystems, Inc.  All rights reserved.  You may not modify, use, reproduce, or distribute this software except in compliance with the terms of the License at:
 http://adventurebuilder.dev.java.net/LICENSE.txt
 $Id: I18nUtil.java,v 1.2 2004/05/26 00:07:34 inder Exp $ */
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Locale;
/**
 * This utility class for internationalization. This class provides a central
 * location to do specialized formatting in both a default and a locale specfic
 * manner.
 */
public class Main {
  public static String formatCurrency(double amount, int precision, String pattern, Locale locale) {
    NumberFormat nf = NumberFormat.getCurrencyInstance(locale);
    DecimalFormat df = (DecimalFormat) nf;
    df.setMinimumFractionDigits(precision);
    df.setMaximumFractionDigits(precision);
    df.setDecimalSeparatorAlwaysShown(true);
    df.applyPattern(pattern);
    return df.format(amount);
  }
  public static String formatNumber(double amount, int precision, String pattern, Locale locale) {
    NumberFormat nf = NumberFormat.getNumberInstance(locale);
    DecimalFormat df = (DecimalFormat) nf;
    df.setMinimumFractionDigits(precision);
    df.setMaximumFractionDigits(precision);
    df.setDecimalSeparatorAlwaysShown(true);
    df.applyPattern(pattern);
    return df.format(amount);
  }
  public static String formatCurrency(double amount, int precision, Locale locale) {
    NumberFormat nf = NumberFormat.getCurrencyInstance(locale);
    nf.setMinimumFractionDigits(precision);
    nf.setMaximumFractionDigits(precision);
    return nf.format(amount);
  }
  public static String formatNumber(double amount, int precision, Locale locale) {
    NumberFormat nf = NumberFormat.getNumberInstance(locale);
    nf.setMinimumFractionDigits(precision);
    nf.setMaximumFractionDigits(precision);
    return nf.format(amount);
  }
}
```

| 2.14.1. | Number formatting helps make your numbers more readable. |
|---|---|
| 2.14.2. | Specifying Precision |
| 2.14.3. | Applied to strings, the precision specifier specifies the maximum field length |
| 2.14.4. | Illustrating the precision specifier |
| 2.14.5. | Add leading zeros to a number |
| 2.14.6. | NumberFormat.getInstance() |
| 2.14.7. | NumberFormat.getCurrencyInstance(Locale.ENGLISH) |
| 2.14.8. | NumberFormat: Minimum Integer Digits, Maximum/Minimum Fraction Digits |
| 2.14.9. | Number format with FieldPosition |
| 2.14.10. | NumberFormat.getPercentInstance(Locale.ENGLISH) |
| 2.14.11. | A number formatter for logarithmic values. This formatter does not support parsing. |
| 2.14.12. | Format a percentage for presentation to the user |
| 2.14.13. | Get Percent Value |
| 2.14.14. | Helper class for format number and currency |
