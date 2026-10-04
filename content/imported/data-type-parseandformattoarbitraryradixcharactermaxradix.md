---
title: Parse and format to arbitrary radix <= Character.MAX_RADIX
nav: Parse and format to arbitr...
description: Imported from the java2s.com archive: Parse and format to arbitrary radix <= Character.MAX_RADIX
section: Imported - java2s Archive
order: 1248
source: https://web.archive.org/web/20140316035036/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParseandformattoarbitraryradixCharacterMAXRADIX.htm
---
```java title=Example.java
import java.math.BigInteger;
public class Main {
  public static void main(String[] argv) throws Exception {
    int radix = 32;
    BigInteger bi = new BigInteger("vv", radix);
    String s = bi.toString(radix);
  }
}
```

| 2.45.1. | Create BigInteger via string |
|---|---|
| 2.45.2. | Create BigInteger via long type variable |
| 2.45.3. | Create BigInteger from byte array |
| 2.45.4. | Operating with Big Integer Values |
| 2.45.5. | Multiply one BigInteger to another BigInteger |
| 2.45.6. | Subtract one BigInteger from another BigInteger |
| 2.45.7. | Divide one BigInteger from another BigInteger |
| 2.45.8. | Negate a BigInteger |
| 2.45.9. | Calculate the power on a BigInteger |
| 2.45.10. | Performing Bitwise Operations with BigInteger |
| 2.45.11. | Get the value of a bit |
| 2.45.12. | Set a bit for BigInteger |
| 2.45.13. | Clear a bit in a BigInteger |
| 2.45.14. | Flip a bit in a BigInteger |
| 2.45.15. | Shift the bits in a BigInteger |
| 2.45.16. | Shift right in a BigInteger |
| 2.45.17. | xor a BigInteger |
| 2.45.18. | and operation on BigInteger |
| 2.45.19. | not operation for BigInteger |
| 2.45.20. | or operation for BigInteger |
| 2.45.21. | antNot operation on BigInteger |
| 2.45.22. | Retrieve the current bits in a byte array in twos-complement form. |
| 2.45.23. | Parse octal string to create BigInteger |
| 2.45.24. | Parse decimal string to create BigInteger |
| 2.45.25. | Parse hexadecimal string to create BigInteger |
| 2.45.26. | Parsing and Formatting a Big Integer into Binary |
| 2.45.27. | Parsing and Formatting a Big Integer into octal |
| 2.45.28. | Parsing and Formatting a Big Integer into decimal |
| 2.45.29. | Parsing and Formatting a Byte Array into Binary |
| 2.45.30. | Parsing and Formatting a Byte Array into Octal |
| 2.45.31. | Parsing and Formatting a Byte Array into decimal |
| 2.45.32. | Parsing and Formatting a Byte Array into Hexadecimal |
| 2.45.33. | Parse and format to hexadecimal |
| 2.45.34. | Parse and format to arbitrary radix < = Character.MAX_RADIX |
| 2.45.35. | Parse binary string |
| 2.45.36. | Convert BigInteger into another radix number |
| 2.45.37. | Do math operation for BigInteger |
| 2.45.38. | Operate with big integer values in code |
| 2.45.39. | Get byte array from BigInteger |
| 2.45.40. | BigInteger.isProbablePrime |
| 2.45.41. | performing the modular exponential |
| 2.45.42. | Use BigInteger |
| 2.45.43. | Get BigInteger from an object |
