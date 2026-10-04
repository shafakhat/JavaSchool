---
title: Match Zip Codes
nav: Match Zip Codes
description: Imported from the java2s.com archive: Match Zip Codes
section: Imported - java2s Archive
order: 1165
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/MatchZipCodes.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] a) {
    String zip = "1234-123";
    String zipCodePattern = "\\d{5}(-\\d{4})?";
    boolean retval = zip.matches(zipCodePattern);
  }
}
```
