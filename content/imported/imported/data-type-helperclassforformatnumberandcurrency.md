---
title: Helper class for format number and currency
nav: Helper class for format nu...
description: /* Copyright 2004 Sun Microsystems, Inc. All rights reserved. You may not modify, use, reproduce, or distribute this software except in compliance with the terms of the
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Helperclassforformatnumberandcurrency.htm
---
```java title=Example.java
/* Copyright 2004 Sun Microsystems, Inc.  All rights reserved.  You may not modify, use, reproduce, or distribute this software except in compliance with the terms of the License at:
 http://adventurebuilder.dev.java.net/LICENSE.txt
 $Id: I18nUtil.java,v 1.2 2004/05/26 00:07:34 inder Exp $ */import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Locale;

/**
 * This utility class for internationalization. This class provides a central
 * location to do specialized formatting in both a default and a locale specfic
 * manner.
 */publicclass Main {

  publicstatic String formatCurrency(double amount, int precision, String pattern, Locale locale) {
    NumberFormat nf = NumberFormat.getCurrencyInstance(locale);
    DecimalFormat df = (DecimalFormat) nf;
    df.setMinimumFractionDigits(precision);
    df.setMaximumFractionDigits(precision);
    df.setDecimalSeparatorAlwaysShown(true);
    df.applyPattern(pattern);
    return df.format(amount);
  }

  publicstatic String formatNumber(double amount, int precision, String pattern, Locale locale) {
    NumberFormat nf = NumberFormat.getNumberInstance(locale);
    DecimalFormat df = (DecimalFormat) nf;
    df.setMinimumFractionDigits(precision);
    df.setMaximumFractionDigits(precision);
    df.setDecimalSeparatorAlwaysShown(true);
    df.applyPattern(pattern);
    return df.format(amount);
  }

  publicstatic String formatCurrency(double amount, int precision, Locale locale) {
    NumberFormat nf = NumberFormat.getCurrencyInstance(locale);
    nf.setMinimumFractionDigits(precision);
    nf.setMaximumFractionDigits(precision);
    return nf.format(amount);
  }

  publicstatic String formatNumber(double amount, int precision, Locale locale) {
    NumberFormat nf = NumberFormat.getNumberInstance(locale);
    nf.setMinimumFractionDigits(precision);
    nf.setMaximumFractionDigits(precision);
    return nf.format(amount);
  }
}
```
