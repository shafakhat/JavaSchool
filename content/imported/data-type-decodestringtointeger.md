---
title: Decode string to integer
nav: Decode string to integer
description: Imported from the java2s.com archive: Decode string to integer
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Decodestringtointeger.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    String decimal = "10"; // Decimal
    String hexa = "0XFF"; // Hexa
    String octal = "077"; // Octal
Integer number = Integer.decode(decimal);
    System.out.println("String [" + decimal + "] = " + number);
    number = Integer.decode(hexa);
    System.out.println("String [" + hexa + "] = " + number);
    number = Integer.decode(octal);
    System.out.println("String [" + octal + "] = " + number);
  }
}
```
