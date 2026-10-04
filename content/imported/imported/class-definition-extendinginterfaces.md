---
title: Extending Interfaces
nav: Extending Interfaces
description: Imported from the java2s.com archive: Extending Interfaces
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20070430052202/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/ExtendingInterfaces.htm
---
```java title=Example.java
interface ConversionFactors {
  double INCH_TO_MM = 25.4;
}
interface Conversions extends ConversionFactors {
  double inchesToMillimeters(double inches);
}
```
