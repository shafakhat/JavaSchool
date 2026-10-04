---
title: Use BigInteger
nav: Use BigInteger
description: Imported from the java2s.com archive: Use BigInteger
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UseBigInteger.htm
---
```java title=Example.java
import java.math.BigInteger;
publicclass MainClass {
  publicfinalstaticint pValue = 47;
  publicfinalstaticint gValue = 71;
  publicfinalstaticint XaValue = 9;
  publicfinalstaticint XbValue = 14;
  publicstaticvoid main(String[] args) throws Exception {
    BigInteger p = new BigInteger(Integer.toString(pValue));
    BigInteger g = new BigInteger(Integer.toString(gValue));
    System.out.println("p = " + p);
    System.out.println("g = " + g);
    BigInteger Xa = new BigInteger(Integer.toString(XaValue));
    BigInteger Xb = new BigInteger(Integer.toString(XbValue));
    System.out.println("Xa = " + Xa);
    System.out.println("Xb = " + Xb);
    BigInteger Ya = g.modPow(Xa, p);
    System.out.println("Ya = " + Ya);
    BigInteger Yb = g.modPow(Xb, p);
    System.out.println("Yb = " + Yb);
    BigInteger Ka = Ya.modPow(Xa, p);
    System.out.println("Users A, K = " + Ka);
    BigInteger Kb = Yb.modPow(Xb, p);
    System.out.println("Users B, K = " + Kb);
  }
}
```
