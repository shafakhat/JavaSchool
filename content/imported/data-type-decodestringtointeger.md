---
title: Decode string to integer
nav: Decode string to integer
description: Imported from the java2s.com archive: Decode string to integer
section: Imported - java2s Archive
order: 1121
source: https://web.archive.org/web/20140829091117/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Decodestringtointeger.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String decimal = "10"; // Decimal
    String hexa = "0XFF"; // Hexa
    String octal = "077"; // Octal
    Integer number = Integer.decode(decimal);
    System.out.println("String [" + decimal + "] = " + number);
    number = Integer.decode(hexa);
    System.out.println("String [" + hexa + "] = " + number);
    number = Integer.decode(octal);
    System.out.println("String [" + octal + "] = " + number);
  }
}
```

| 2.9.1. | Hexadecimal integer literal |
|---|---|
| 2.9.2. | A hexadecimal literal of type long |
| 2.9.3. | Defining integer literals as octal values |
| 2.9.4. | Decode string to integer |
| 2.9.5. | Convert octal number to decimal number example |
| 2.9.6. | Convert decimal integer to octal number example |
| 2.9.7. | Convert decimal integer to hexadecimal number example |
| 2.9.8. | Parsing and Formatting a Number into Binary |
| 2.9.9. | Convert byte array to Hex String |
| 2.9.10. | Convert the bytes to a hex string representation of the bytes |
| 2.9.11. | Converting hexadecimal strings |
| 2.9.12. | Dumps data in hexadecimal format |
| 2.9.13. | Given a hexstring this will return the byte array corresponding to string |
| 2.9.14. | Hex encoder/decoder implementation borrowed from BouncyCastle |
| 2.9.15. | Returns the hexadecimal value of the supplied byte array |
| 2.9.16. | A custom number formatter that formats numbers as hexadecimal strings. |
| 2.9.17. | Decodes Hex data into octects |
| 2.9.18. | Decodes Base64 data into octects |
| 2.9.19. | Helper function that returns a char from an hex |
| 2.9.20. | Encodes hex octects into Base64 |
| 2.9.21. | Hex encoder and decoder. |
| 2.9.22. | Helper function that dump an array of bytes in hex pair form, without '0x' and space chars |
| 2.9.23. | dump an array of bytes in hex form |
| 2.9.24. | Decode byte array |
