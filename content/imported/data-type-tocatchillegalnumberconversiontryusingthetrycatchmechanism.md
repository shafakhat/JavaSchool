---
title: To catch illegal number conversion, try using the try/catch mechanism.
nav: To catch illegal number co...
description: Imported from the java2s.com archive: To catch illegal number conversion, try using the try/catch mechanism.
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20140316034850/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Tocatchillegalnumberconversiontryusingthetrycatchmechanism.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) throws Exception {
    try {
      int i = Integer.parseInt("asdf");
    } catch (NumberFormatException e) {
      ;
    }
  }
}
```
