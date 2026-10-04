---
title: Convert a String to int
nav: Convert a String to int
description: Imported from the java2s.com archive: Convert a String to int
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertaStringtoint.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) {
    String sValue = "5";
    try {
      int iValue = Integer.parseInt(sValue);
      System.out.println(iValue);
    } catch (NumberFormatException ex) {
      ex.printStackTrace();
    }
  }
}
```
