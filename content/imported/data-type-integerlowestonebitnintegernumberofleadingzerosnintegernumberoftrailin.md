---
title: Integer.lowestOneBit(n), Integer.numberOfLeadingZeros(n), Integer.numberOfTrailingZeros(n)
nav: Integer.lowestOneBit(n), I...
description: System.out.println("Lowest one bit: " + Integer.lowestOneBit(n));
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20070319193213/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/IntegerlowestOneBitnIntegernumberOfLeadingZerosnIntegernumberOfTrailingZerosn.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int n = 170;
    System.out.println("Lowest one bit: " + Integer.lowestOneBit(n));
    System.out.println("Number of leading zeros : " + Integer.numberOfLeadingZeros(n));
    System.out.println("Number of trailing zeros : " + Integer.numberOfTrailingZeros(n));
    System.out.println("\nBeginning with the value 1, " + "rotate left 16 times.");
  }
}
```

```java title=Example.java
Lowest one bit: 2
Number of leading zeros : 24
Number of trailing zeros : 1
Beginning with the value 1, rotate left 16 times.
```
