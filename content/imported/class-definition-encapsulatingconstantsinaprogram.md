---
title: Encapsulating Constants in a Program
nav: Encapsulating Constants in...
description: Imported from the java2s.com archive: Encapsulating Constants in a Program
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20070430052401/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/EncapsulatingConstantsinaProgram.htm
---
```java title=Example.java
interface ConversionFactors {
  double INCH_TO_MM = 25.4;
  double OUNCE_TO_GRAM = 28.349523125;
  double POUND_TO_GRAM = 453.5924;
  double HP_TO_WATT = 745.7;
  double WATT_TO_HP = 1.0 / HP_TO_WATT;
}
```

```java title=Example.java
public class MainClass {
  public static void main(String[] a) {
    System.out.println(ConversionFactors.INCH_TO_MM);
  }
}
```

```java title=Example.java
25.4
```
