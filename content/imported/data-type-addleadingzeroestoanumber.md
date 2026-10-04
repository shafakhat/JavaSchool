---
title: Add leading zeroes to a number
nav: Add leading zeroes to a nu...
description: System.out.println("Number with leading zeros: " + formatted);
section: Imported - java2s Archive
order: 1110
source: https://web.archive.org/web/20091129091529/http://www.java2s.com:80/Code/Java/Data-Type/Addleadingzeroestoanumber.htm
---
Add leading zeroes to a number

```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int number = 1500;
    String formatted = String.format("%07d", number);
    System.out.println("Number with leading zeros: " + formatted);
  }
}
```

1.  The Uppercase Option
---  ---
2.  Using the Format Flags
3.  The Format Specifiers
4.  NumberFormat with Constant Locale Usage
5.  Number Format by locale
6.  demonstrates the %n and %% format specifiers:
7.  demonstrates the minimum field-width specifier by applying it to the %f conversion:
8.  Create a table of squares and cubes.
9.  precision modifier: Format 4 decimal places
10.  precision modifier: Format to 2 decimal places in a 16 character field
11.  precision modifier: Display at most 15 characters in a string
12.  left justification: Right justify by default
13.  left justification: left justify
14.  Demonstrate the space format specifiers.
15.  Using an Argument Index
16.  the NumberFormat object is created once when the program starts.
17.  Default rounding mode
18.  RoundingMode.HALF_DOWN
19.  RoundingMode.FLOOR
20.  RoundingMode.CEILING
21.  Format a number our way and the default way
22.  Number Format Test
23.  Format a number to currency
24.  Number Format with Locale
25.  Decimal Format Demo
26.  Parse number with NumberFormat and Locale
27.  Formatting and Parsing a Locale-Specific Percentage
28.  Format a number with DecimalFormat
29.  Parse a number with NumberFormat and Locale.CANADA
30.  Format a number with leading zeroes
31.  Format a number for a locale
32.  Formatting and Parsing a Number for a Locale
33.  Display numbers in scientific notation
34.  Format for GERMAN locale
35.  Format for the default locale
36.  Displaying numbers with commas
37.  Formatting a Number in Exponential Notation
38.  Using only 0's to the left of E forces no decimal point
39.  Parse a GERMAN number
40.  Formatting and Parsing Locale-Specific Currency
41.  Parse a number for a locale
42.  Use grouping to display a number
43.  Number format viewer
44.  A number formatter for logarithmic values. This formatter does not support parsing.
45.  A custom number formatter that formats numbers as hexadecimal strings.
46.  NumberFormat and locale
