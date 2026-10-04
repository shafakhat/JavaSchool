---
title: performing the modular exponential
nav: performing the modular exp...
description: BigInteger exponent = BigInteger.probablePrime(bitLength, rnd);
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/performingthemodularexponential.htm
---
```java title=Example.java
import java.math.BigInteger;
import java.security.SecureRandom;
publicclass MainClass {
  publicstaticvoid main(String[] args) throws Exception {
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
