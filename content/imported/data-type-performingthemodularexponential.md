---
title: performing the modular exponential
nav: performing the modular exp...
description: BigInteger exponent = BigInteger.probablePrime(bitLength, rnd);
section: Imported - java2s Archive
order: 1277
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/performingthemodularexponential.htm
---
```java title=Example.java
import java.math.BigInteger;
import java.security.SecureRandom;
public class MainClass {
  public static void main(String[] args) throws Exception {
    int bitLength = 512; // 512 bits
    SecureRandom rnd = new SecureRandom();
    int certainty = 90; // 1 - 1/2(90) certainty
    System.out.println("BitLength : " + bitLength);
    BigInteger mod = new BigInteger(bitLength, certainty, rnd);
    BigInteger exponent = BigInteger.probablePrime(bitLength, rnd);
    BigInteger n = BigInteger.probablePrime(bitLength, rnd);
    BigInteger result = n.modPow(exponent, mod);
    System.out.println("Number ^ Exponent MOD Modulus = Result");
    System.out.println("Number");
    System.out.println(n);
    System.out.println("Exponent");
    System.out.println(exponent);
    System.out.println("Modulus");
    System.out.println(mod);
    System.out.println("Result");
    System.out.println(result);
  }
}
/*BitLength : 512
Number ^ Exponent MOD Modulus = Result
Number
12429010321466148979282045876615924104266625036004424072013594464398465860901924701756511994455904802521087513832503046348373547015122338773846757329693089
Exponent
7960165959547365392190891717471267683026232484827038749061088628549083772881870434293423234456457412681666128278442829496431230428387587660778678814696147
Modulus
10339566307708626815760173877230355067432306461489808819560490502837798859869280782572410563219404567771359973589211641725154894564515306242543575863832237
Result
4664677700053277466905242082951352345941397508884099204138151141886794649976135281786429283508499942760627515243676288735812526509264162843510761720483915
*/
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
