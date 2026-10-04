---
title: Parse and format a number to octal
nav: Parse and format a number ...
description: Imported from the java2s.com archive: Parse and format a number to octal
section: Imported - java2s Archive
order: 1247
source: https://web.archive.org/web/20140316035031/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Parseandformatanumbertooctal.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    int i = Integer.parseInt("1000", 8);
    String s = Integer.toString(i, 8);
    System.out.println(s);
  }
}
```

| 2.6.1. | Java int:int is 32 bit signed type ranges from –2,147,483,648 to 2,147,483,647. |
|---|---|
| 2.6.2. | Integer: MAX, MIN VALUE |
| 2.6.3. | The number of bits used to represent an int value in two's complement binary form. |
| 2.6.4. | Bit manipulation methods in Integer: bitCount |
| 2.6.5. | Highest one bit: 128 |
| 2.6.6. | Create an Integer object |
| 2.6.7. | Integer.lowestOneBit(n), Integer.numberOfLeadingZeros(n), Integer.numberOfTrailingZeros(n) |
| 2.6.8. | Integer: rotate Left |
| 2.6.9. | Integer signum() returns |
| 2.6.10. | Integer.reverseBytes( ) reverses the order of the bytes in num and returns the result |
| 2.6.11. | Read Integers from console and calculate |
| 2.6.12. | Compare integers using if statements, relational operators and equality operators |
| 2.6.13. | Shifted and scaled random integers |
| 2.6.14. | Equals Method |
| 2.6.15. | Equivalence |
| 2.6.16. | Convert an int value to String: Integer.toString(i) |
| 2.6.17. | Convert an int value to String: new Integer(i).toString() |
| 2.6.18. | Convert a String to int |
| 2.6.19. | Convert an int value to String: concatenate string to an int value |
| 2.6.20. | Convert hexadecimal number to decimal number |
| 2.6.21. | Convert octal number to decimal number |
| 2.6.22. | Convert binary number to decimal number |
| 2.6.23. | Convert decimal integer to octal number |
| 2.6.24. | Convert decimal integer to hexadecimal number |
| 2.6.25. | Convert from integer to String |
| 2.6.26. | Convert from String to integer |
| 2.6.27. | Convert from decimal to binary |
| 2.6.28. | Convert from decimal to hexadecimal |
| 2.6.29. | Convert from decimal to hexadecimal with leading zeroes and uppercase |
| 2.6.30. | Convert from Byte array to hexadecimal string |
| 2.6.31. | Convert a byte array to a Hex string |
| 2.6.32. | Convert Decimal to Hexadecimal |
| 2.6.33. | Convert Decimal to Octal |
| 2.6.34. | Convert Decimal to Binary |
| 2.6.35. | Convert string to an integer or number |
| 2.6.36. | Parse and format a number to octal |
| 2.6.37. | Parse and format a number to decimal |
| 2.6.38. | Parse and format to hexadecimal |
| 2.6.39. | Parse and format to arbitrary radix < = Character.MAX_RADIX |
| 2.6.40. | To catch illegal number conversion, try using the try/catch mechanism. |
| 2.6.41. | Pass an integer by reference |
| 2.6.42. | Compare Two Java int Arrays |
| 2.6.43. | Reverse an Integer |
