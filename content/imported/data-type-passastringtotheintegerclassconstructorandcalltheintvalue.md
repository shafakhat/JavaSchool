---
title: Pass a string to the Integer class constructor and call the intValue()
nav: Pass a string to the Integ...
description: Imported from the java2s.com archive: Pass a string to the Integer class constructor and call the intValue()
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/PassastringtotheIntegerclassconstructorandcalltheintValue.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) {
    String sValue = "5";
    try {
      int iValue = newInteger(sValue).intValue();
    } catch (NumberFormatException ex) {
      ex.printStackTrace();
    }
  }
}
```
