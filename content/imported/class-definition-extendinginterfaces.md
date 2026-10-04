---
title: Extending Interfaces
nav: Extending Interfaces
description: Imported from the java2s.com archive: Extending Interfaces
section: Imported - java2s Archive
order: 1227
source: https://web.archive.org/web/2020/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/ExtendingInterfaces.htm
---
```java title=Example.java
interface ConversionFactors {
  double INCH_TO_MM = 25.4;
}
interface Conversions extends ConversionFactors {
  double inchesToMillimeters(double inches);
}
```

| 5.29.1. | Interfaces and Abstract Classes |
|---|---|
| 5.29.2. | Fields and Methods in an Interface |
| 5.29.3. | To implement an interface: use the implements keyword after the class declaration |
| 5.29.4. | A Partial Interface Implementation |
| 5.29.5. | Extending Interfaces |
| 5.29.6. | Interfaces and Multiple Inheritance |
| 5.29.7. | Interfaces and Polymorphism: Using Multiple Interfaces |
| 5.29.8. | Nesting Classes in an Interface Definition |
| 5.29.9. | Encapsulating Constants in a Program |
| 5.29.10. | Multiple interfaces |
| 5.29.11. | Initializing interface fields with non-constant initializers |
