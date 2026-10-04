---
title: A Partial Interface Implementation
nav: A Partial Interface Implem...
description: Imported from the java2s.com archive: A Partial Interface Implementation
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20070430090228/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/APartialInterfaceImplementation.htm
---
```java title=Example.java
interface Conversions {
  double INCH_TO_MM = 25.4;
  double OUNCE_TO_GRAM = 28.349523125;
  double POUND_TO_GRAM = 453.5924;
  double HP_TO_WATT = 745.7;
  double WATT_TO_HP = 1.0 / HP_TO_WATT;
  public double inchesToMillimeters(double inches);
  public double ouncesToGrams(double ounces);
}
java title=Example.java
public abstract class MainClass implements Conversions {
  public double inchesToMillimeters(double inches) {
    return inches * INCH_TO_MM;
  }
  public double ouncesToGrams(double ounces) {
    return ounces * OUNCE_TO_GRAM;
  }
}
```
