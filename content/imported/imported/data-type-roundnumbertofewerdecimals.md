---
title: Round number to fewer decimals
nav: Round number to fewer deci...
description: System.out.println("Rounded number = " + df.format(numberToRound));
section: Imported - java2s Archive
order: 1198
source: https://web.archive.org/web/20100525043630/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Roundnumbertofewerdecimals.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] args) {
    double numberToRound = 12345.6789;
    DecimalFormat df = new DecimalFormat("0.000");
    System.out.println("Rounded number = " + df.format(numberToRound));
    System.out.println(String.format("Rounded number = %.3f", numberToRound));
  }
}
/*
Rounded number = 12345.679
Rounded number = 12345.679
*/
```
