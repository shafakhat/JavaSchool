---
title: Java Format - Java Date Format Class
nav: Java Format - Java Date Fo...
description: Java 8 has new Date-Time API to work with dates and times. We should use the new Java 8 Date-Time API to format and parse date time value.
section: Imported - java2s Archive
order: 50387
source: https://www.java2s.com/Tutorials/Java/Java_Format/0020__Java_Date_Format_Class.html
---
```java title=Example.java
```

Java 8 has new Date-Time API to work with dates and times. We should use the new Java 8 Date-Time API to format and parse date time value.

If we are writing new code related to dates and times, we should be using the new Date-Time API.

Format date and time using new Java 8 Date-Time API.

This section is for you to work with legacy code that uses old Date and Calendar classes.

## Class

The Java library provides two classes to format dates:

- java.text.DateFormat
- java.text.SimpleDateFormat

DateFormat class is an abstract class and we can use the DateFormat class to format dates with a predefined format.

Since it is abstract, so we cannot create an instance of DateFormat class using the new operator.

We have to use one of its getXxxInstance() methods to create new instance. Xxx can be Date, DateTime, or Time.

To format a date time value we use the format() method of the DateFormat class.

The formatted text from DateFormat class depends on two things:

- style
- locale

The style of formatting determines how much datetime information is included in the formatted text

The locale determines which locale to use.

## Formatting Style

The DateFormat class defines five styles as constants:

- DateFormat.DEFAULT
- DateFormat.SHORT
- DateFormat.MEDIUM
- DateFormat.LONG
- DateFormat.FULL

The DEFAULT format is the same as MEDIUM. getInstance() uses SHORT.

The following table shows the same date formatted in different styles for a US locale.

Style  Formatted Date
---  ---
DEFAULT  Mar 27, 2014
SHORT  3/27/14
MEDIUM  Mar 26, 2014
LONG  March 26, 2014
FULL  Sunday, November 2, 2014

## Example

The following code shows how to display dates in short and medium formats for locales as default, France, and Germany.

```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
publicclass Main {
  publicstaticvoid main(String[] args) {
    Date today = new Date();
    // Print date in the default locale format
    Locale defaultLocale = Locale.getDefault();
    printLocaleDetails(defaultLocale);
    printDate(defaultLocale, today);
    // Print date in French format
    printLocaleDetails(Locale.FRANCE);
    printDate(Locale.FRANCE, today);
    // Print date in German format. We could also use Locale.GERMANY
// instead of new Locale ("de", "DE").
    Locale germanLocale = new Locale("de", "DE");
    printLocaleDetails(germanLocale);
    printDate(germanLocale, today);
  }
  publicstaticvoid printLocaleDetails(Locale locale) {
    String languageCode = locale.getLanguage();
    String languageName = locale.getDisplayLanguage();
    String countryCode = locale.getCountry();
    String countryName = locale.getDisplayCountry();
    // Print the locale info
    System.out.println("Language: " + languageName + "(" + languageCode + "); "
        + "Country: " + countryName + "(" + countryCode + ")");
  }
  publicstaticvoid printDate(Locale locale, Date date) {
    DateFormat formatter = DateFormat.getDateInstance(DateFormat.SHORT, locale);
    String formattedDate = formatter.format(date);
    System.out.println("SHORT: " + formattedDate);
    formatter = DateFormat.getDateInstance(DateFormat.MEDIUM, locale);
    formattedDate = formatter.format(date);
    System.out.println("MEDIUM: " + formattedDate+"\n");
  }
}
```

The code above generates the following result.

The java.util.Locale class contains constants for common locales.

We can use the Locale.getDefault() method to get the default Locale for your system.

## SimpleDateFormat Class

To create custom date formats, we can use the SimpleDateFormat class.

SimpleDateFormat class is locale-sensitive.

Its default constructor creates a formatter with default date format for default locale.

format() method from the SimpleDateFormat class does the date format.

## Example 2

To change the date format for subsequent formatting, you can use the applyPattern() method by passing the new date format as an argument.

```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] args) {
    SimpleDateFormat simpleFormatter = new SimpleDateFormat("dd/MM/yyyy");
    Date today = new Date();
    String formattedDate = simpleFormatter.format(today);
    System.out.println("Today is (dd/MM/yyyy):  " + formattedDate);
    simpleFormatter.applyPattern("MMMM dd, yyyy");
    formattedDate = simpleFormatter.format(today);
    System.out.println("Today is  (MMMM dd, yyyy): " + formattedDate);
  }
}
```

The code above generates the following result.

- « Previous
