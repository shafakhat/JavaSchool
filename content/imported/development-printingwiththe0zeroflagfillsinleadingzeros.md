---
title: Printing with the 0 (zero) flag fills in leading zeros
nav: Printing with the 0 (zero)...
description: Imported from the java2s.com archive: Printing with the 0 (zero) flag fills in leading zeros
section: Imported - java2s Archive
order: 1622
source: https://web.archive.org/web/20140829080633/http://www.java2s.com/Tutorial/Java/0120__Development/Printingwiththe0zeroflagfillsinleadingzeros.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      System.out.printf( "%+09d\n", 452 );
      System.out.printf( "%09d\n", 452 );
      System.out.printf( "% 9d\n", 452 );
   }
}
java title=Example.java
+00000452
000000452
      452
```

| 6.14.1. | Using Java's printf( ) Method |
|---|---|
| 6.14.2. | Demonstrate printf() |
| 6.14.3. | printf to command line summary |
| 6.14.4. | Formatting Numerical Data: |
| 6.14.5. | Specifying the Width and Precision |
| 6.14.6. | Formatting Characters and Strings |
| 6.14.7. | output a % character |
| 6.14.8. | Formatting Data into a String |
| 6.14.9. | Formatting a string and Ouputing to console |
| 6.14.10. | Formated System.out.printf |
| 6.14.11. | localized day name: %tA/%TA |
| 6.14.12. | localized, abbreviated day: %ta/%Ta |
| 6.14.13. | two-digit century: %tC/%TC |
| 6.14.14. | four digit year: %tY/%TY |
| 6.14.15. | two-digit year: %ty/%Ty |
| 6.14.16. | three-digit day of the year: %tj/%Tj |
| 6.14.17. | two-digit month: %tm/%Tm |
| 6.14.18. | two-digit day of the month: %td/%Td |
| 6.14.19. | a one-or-two-digit day of the month: %te/%Te |
| 6.14.20. | hours and minutes on a 24-hour clock: %tR/%TR |
| 6.14.21. | hours, minutes, and seconds on a 24-hour clock: %tT/%TT |
| 6.14.22. | hours, minutes, and seconds on a 12-hour clock: %tr/%Tr |
| 6.14.23. | month/day/year: %tD/%TD |
| 6.14.24. | ISO 8601 standard date: %tF/%TF |
| 6.14.25. | Unix date format: %tc/%Tc |
| 6.14.26. | Decimal: %f |
| 6.14.27. | Scientific notation: %e (lower case e) |
| 6.14.28. | Scientific notation: %E (upper case E) |
| 6.14.29. | Decimal/Scientific: %g (lower case g) |
| 6.14.30. | Decimal/Scientific: %G (upper case G) |
| 6.14.31. | Lowercase Hexadecimal: %a |
| 6.14.32. | Uppercase Hexadecimal: %A |
| 6.14.33. | Decimal: %d |
| 6.14.34. | Octal: %o |
| 6.14.35. | Lowercase hexadecimal: %x |
| 6.14.36. | Uppercase hexadecimal: %X |
| 6.14.37. | Output URL: %b (lower case b) |
| 6.14.38. | Output URL: %B (upper case B) |
| 6.14.39. | Hashcode: %h (lower case h) |
| 6.14.40. | HASHCODE: %H (upper case H) |
| 6.14.41. | STRING: %S (upper case S) |
| 6.14.42. | string: %s (lower case s) |
| 6.14.43. | Using the integral conversion characters |
| 6.14.44. | Using floating-point conversion characters |
| 6.14.45. | Using character and string conversion characters. |
| 6.14.46. | Conversion characters for date/time compositions |
| 6.14.47. | Conversion characters for date |
| 6.14.48. | Conversion characters for time |
| 6.14.49. | Using the b, B, h, H, % and n conversion characters. |
| 6.14.50. | Right justifying integers in fields: Field Width |
| 6.14.51. | Using precision for floating-point numbers and strings |
| 6.14.52. | Right justifying and left justifying values |
| 6.14.53. | Printing numbers with and without the + flag |
| 6.14.54. | Printing a space before non-negative values |
| 6.14.55. | Using the # flag with conversion characters o and x |
| 6.14.56. | Printing with the 0 (zero) flag fills in leading zeros |
| 6.14.57. | Using the comma (,) flag to display numbers with thousands separator |
| 6.14.58. | Using the ( flag to place parentheses around negative numbers |
| 6.14.59. | Reordering output with argument indices. |
| 6.14.60. | Two digit hour on a 24-hour clock: %tH/%TH |
| 6.14.61. | two digit hour on a 12-hour clock: %tI/%TI |
| 6.14.62. | one-or-two digit hour on a 24-hour clock: %tk/%Tk |
| 6.14.63. | one-or-two digit hour on a 12-hour: %tl/%Tl |
| 6.14.64. | two digit minutes ranging from 00 to 59: %tH / %TH |
| 6.14.65. | two digit seconds ranging from 00 to 60 : %tS/%TS |
| 6.14.66. | milliseconds: %tL/%TL |
| 6.14.67. | nanoseconds: %tN/%TN |
| 6.14.68. | Locale-specific morning/afternoon indicator: %tp/%Tp |
| 6.14.69. | RFC 822 numeric time zone indicator: %tz/%Tz |
| 6.14.70. | Time zone abbreviation: %tZ/%TZ |
| 6.14.71. | seconds since the epoch: %ts/%Ts |
| 6.14.72. | milliseconds since the epoch: %TQ |
| 6.14.73. | localized month name: %tB/%TB |
| 6.14.74. | localized, abbreviated month: %tb/%Tb |
| 6.14.75. | localized, abbreviated month: %th/%Th |
