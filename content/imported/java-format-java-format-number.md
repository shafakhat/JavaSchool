---
title: Java Format - Java printf Numeric Format
nav: Java Format - Java printf ...
description: It can format values of byte, Byte, short, Short, int, Integer, long, Long and BigInteger.
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/2016/https://www.java2s.com/Tutorials/Java/Java_Format/0110__Java_Format_Number.html
---
Java printf supports two types of numeric formatting:

- Integral number formatting
- Floating-point number formatting

## Integral Number Formatting

The integral number formatting formats the whole numbers.

It can format values of byte, Byte, short, Short, int, Integer, long, Long and BigInteger.

The following list explains the format characters.

- d Format the argument in locale-specific decimal integer. The '#' flag cannot be used with this conversion.
- o Format the argument as a base-8 integer. If '#' flag is used, the output begins with 0 . The '(', '+', ' ', and ' ,' flags cannot be used with this conversion.
- x or Uppercase variant X Format the argument as a base-16 integer. If '#' flag is used, the output begins with a "0x". If 'X' is used with '#' flag, the output begins with "0X". The '(', '+', ' ', and ',' flags cannot be used with an argument of byte, Byte, short, Short, int, Integer, long, and Long data types. The ',' flag cannot be used with an argument of BigInteger data type.

The general syntax for a format specifier for integral number formatting is as follows:

```java title=Example.java
%<argument_index$><flags><width><conversion>
```

The precision in a format specifier is not applicable to integral number formatting.

The following code demonstrates the use of the 'd' conversion with various flags to format integers:

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.printf("'%d' %n", 1234);
    System.out.printf("'%6d' %n", 1234);
    System.out.printf("'%-6d' %n", 1234);
    System.out.printf("'%06d' %n", 1234);
    System.out.printf("'%(d' %n", 1234);
    System.out.printf("'%(d' %n", -1234);
    System.out.printf("'% d'  %n", 1234);
    System.out.printf("'% d'  %n", -1234);
    System.out.printf("'%+d' %n", 1234);
    System.out.printf("'%+d' %n", -1234);
  }
}
```

The code above generates the following result.

## Example

When o and x are used with a negative argument of byte, Byte, short, Short, int, Integer, long, and Long data types, the argument value is first converted to an unsigned number by adding a number 2N to it, where N is the number of bits of the value. The conversions do not transform the negative BigInteger argument.

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    byte b1 = 1;
    byte b2 = -2;
    System.out.printf("%o\n", b1);
    System.out.printf("%o", b2);
  }
}
```

## Example 2

The following snippet of code shows some more examples of 'o' and 'x' conversions for int and BigInteger argument types:

```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] args) {
    System.out.printf("%o %n", 1234);
    System.out.printf("%o %n", -1234);
    System.out.printf("%o %n", new BigInteger("1234"));
    System.out.printf("%o %n", new BigInteger("-1234"));
    System.out.printf("%x %n", 1234);
    System.out.printf("%x %n", -1234);
    System.out.printf("%x %n", new BigInteger("1234"));
    System.out.printf("%x %n", new BigInteger("-1234"));
    System.out.printf("%#o %n", 1234);
    System.out.printf("%#x %n", 1234);
    System.out.printf("%#o %n", new BigInteger("1234"));
    System.out.printf("%#x %n", new BigInteger("1234"));
  }
}
```

The code above generates the following result.

## Floating-Point Number Formatting

Floating-point number formatting deals a whole number part and a fraction part for a number.

Floating-point number formatting can be applied to format values of float, Float, double, Double, and BigDecimal data types.

The following list contains conversions used for formatting floating-point number.

- e and Uppercase Variant E Format the argument in a locale-specific scientific notation. The output has one digit followed by a decimal separator and exponent part. For example, 1234.567 will be formatted as 1.234567e+03 if the precision is 6. Precision sets the number of digits after the decimal separator. The group separator flag ' ,' cannot be used with this conversion.
- g and Uppercase Variant G Format the argument in a locale-specific general scientific notation. The formatting can act as e or f conversion. If the value after rounding is greater than or equal to 10 -4 but less than 10 precision , it formats the value as f conversion. If the value after rounding is less than 10 -4 or greater than or equal to 10 precision , it formats the value as 'e' conversion. By default, precision of 6 is used.
- f Format the argument in a locale-specific decimal format. Precision is the number of digits after the decimal separator. The value is rounded according to the precision.
- a and Uppercase Variant A Format the argument in hexadecimal exponential form. This conversion is not applicable to the BigDecimal type.

The general syntax for floating-point number formatting is

```java title=Example.java
%<argument_index$><flags><width><.precision><conversion>
```

The precision has different meanings depend on the conversion character.

- By default, the value of precision is 6.
- For 'e' and 'f' conversions, the precision is the number of digits after the decimal separator.
- For the 'g' conversion, the precision is the total number of digits in the resulting magnitude after rounding.
- Precision is not applicable to the 'a' conversion.

The following snippet of code shows how to format floating-point numbers with the default precision, which is 6:

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.printf("%e %n", 10.2);
    System.out.printf("%f %n", 10.2);
    System.out.printf("%g %n", 10.2);
    System.out.printf("%e %n", 0.000001234);
    System.out.printf("%f %n", 0.000001234);
    System.out.printf("%g %n", 0.000001234);
    System.out.printf("%a %n", 0.000001234);
  }
}
```

The code above generates the following result.

## Example 4

The following code shows the effects of using width and precision in floating-point number formatting:

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.printf("%.2e %n", 123456.789);
    System.out.printf("%.2f %n", 123456.789);
    System.out.printf("%.2g %n", 123456.789);
    System.out.printf("'%8.2e' %n", 123456.789);
    System.out.printf("'%8.2f' %n", 123456.789);
    System.out.printf("'%8.2g' %n", 123456.789);
    System.out.printf("'%10.2e' %n", 123456.789);
    System.out.printf("'%10.2f' %n", 123456.789);
    System.out.printf("'%10.2g' %n", 123456.789);
    System.out.printf("'%-10.2e' %n", 123456.789);
    System.out.printf("'%-10.2f' %n", 123456.789);
    System.out.printf("'%-10.2g' %n", 123456.789);
    System.out.printf("'%010.2e' %n", 123456.789);
    System.out.printf("'%010.2f' %n", 123456.789);
    System.out.printf("'%010.2g' %n", 123456.789);
  }
}
```

The code above generates the following result.

## Example 5

If the argument value for a floating-point conversion is NaN or Infinity, the output contains the strings "NaN" and "Infinity", respectively.

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    System.out.printf("%.2e %n", Double.NaN);
    System.out.printf("%.2f %n", Double.POSITIVE_INFINITY);
    System.out.printf("%.2g %n", Double.NEGATIVE_INFINITY);
    System.out.printf("%(f %n", Double.POSITIVE_INFINITY);
    System.out.printf("%(f %n", Double.NEGATIVE_INFINITY);
  }
}
```

The code above generates the following result.

- « Previous
