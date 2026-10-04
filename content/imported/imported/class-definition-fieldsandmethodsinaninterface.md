---
title: Fields and Methods in an Interface
nav: Fields and Methods in an I...
description: Imported from the java2s.com archive: Fields and Methods in an Interface
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20070430093442/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/FieldsandMethodsinanInterface.htm
---
- Fields in an interface must be initialized and are implicitly public, static, and final.
- You declare methods in an interface just as you would in a class.
- Methods in an interface do not have a body.
- All methods are implicitly public and abstract

```java title=Example.java
interface Conversions{
  double inchesToMillimeters(double inches);
}
```
