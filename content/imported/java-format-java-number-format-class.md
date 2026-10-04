---
title: Java Format - Java Number Format Class
nav: Java Format - Java Number ...
description: The following two classes can be used to format and parse numbers:
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Format/0040__Java_Number_Format_Class.html
---
The following two classes can be used to format and parse numbers:

- java.text.NumberFormat
- java.text.DecimalFormat

The NumberFormat class can format a number in a particular locale's predefined format.

The DecimalFormat class can format a number in a customized format for a particular locale.

A getXXXInstance() method of the NumberFormat class returns the instance of a formatter object.

The XXX can be replaced by Number, Currency, Integer, or Percent, or just getInstance(). And these methods are overloaded.

If you call them without argument, they return a formatter object for the default locale.

Call the format() method with the number argument to get the formatted number as a string.

```java title=Example.java
import java.text.NumberFormat;
public class Main {
  public static void main(String[] args) {
    NumberFormat formatter;
    // Get number formatter for default locale
    formatter = NumberFormat.getInstance();
    System.out.println(formatter.format(12312.123123));
  }
}
```

The code above generates the following result.

## Example

The following code illustrates how to format numbers in default format for the current locale, French locale, and German locale.

```java title=Example.java
import java.text.NumberFormat;
import java.util.Locale;
public class Main {
  public static void main(String[] args) {
    double value = 123456789.9876543;
    // Default locale
    printFormatted(Locale.getDefault(), value);
    // Indian locale
    Locale indianLocale = new Locale("en", "IN");
    printFormatted(indianLocale, value);
  }
  public static void printFormatted(Locale locale, double value) {
    // Get number and currency formatter
    NumberFormat nf = NumberFormat.getInstance(locale);
    NumberFormat cf = NumberFormat.getCurrencyInstance(locale);
    System.out.println("Format value: " + value + "  for locale: " + locale);
    System.out.println("Number: " + nf.format(value));
    System.out.println("Currency: " + cf.format(value));
  }
}
```

The code above generates the following result.

## DecimalFormat class

To perform more advanced formatting, we can use the DecimalFormat class.

DecimalFormat class allows us to supply our own format pattern. The following table shows the pattern and its usage.

Symbol  Location  Meaning
---  ---  ---
0  Number  Represent digit
##  Number  Digit, zero shows as absent
.  Number  Decimal separator or monetary decimal separator
-  Number  Minus sign
,  Number  Grouping separator
E  Number  Separates mantissa and exponent in scientific notation.
;  Subpattern boundary  Separates positive and negative subpatterns
%  Prefix or suffix  Multiply by 100 and show as percentage
\u2030  Prefix or suffix  Multiply by 1000 and show as per mille value

Once we create an object of the DecimalFormat class, you can change the format pattern using its applyPattern() method.

```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  private static DecimalFormat formatter = new DecimalFormat();
  public static void main(String[] args) {
    formatNumber("##.##", 12.345);
    formatNumber("##.##", 12.345);
    formatNumber("0000.0000", 12.345);
    formatNumber("#.##", -12.345);
    // Positive and negative number format
    formatNumber("#.##;(#.##)", -12.735);
  }
  public static void formatNumber(String pattern, double value) {
    // Apply the pattern formatter.applyPattern ( pattern );
    String formattedNumber = formatter.format(value);
    System.out.println("Number:" + value + ", Pattern:" + pattern
        + ", Formatted Number:" + formattedNumber);
  }
}
```

The code above generates the following result.

## Parse

We can also parse a string to a number using the parse() method. The parse() method returns an object of the java.lang.Number class.

We can use xxxValue() methods from java.lang.Number class to get the primitive value, where xxx can be byte, double, float, int, long, and short.

```java title=Example.java
import java.text.DecimalFormat;
import java.text.ParsePosition;
public class Main {
  private static DecimalFormat formatter = new DecimalFormat();
  public static void main(String[] args) {
    // Parse a string to decimal number
    String str = "qq1,234.567";
    String pattern = "#,###.###";
    formatter.applyPattern(pattern);
    // Create a ParsePosition object to specify the first digit of
 // number in the string. It is 1 in "qq1,234.567"
 // with the index 2.
    ParsePosition pp = new ParsePosition(2);
    Number numberObject = formatter.parse(str, pp);
    double value = numberObject.doubleValue();
    System.out.println("Parsed Value  is " + value);
  }
}
```

The code above generates the following result.

- « Previous
