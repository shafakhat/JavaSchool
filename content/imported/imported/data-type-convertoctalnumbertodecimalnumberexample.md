---
title: Convert octal number to decimal number example
nav: Convert octal number to de...
description: Imported from the java2s.com archive: Convert octal number to decimal number example
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertoctalnumbertodecimalnumberexample.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    String strOctalNumber = "33";

    int decimalNumber = Integer.parseInt(strOctalNumber, 8);

    System.out.println(decimalNumber);
  }
}
//27
```
