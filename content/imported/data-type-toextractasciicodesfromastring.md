---
title: To extract Ascii codes from a String
nav: To extract Ascii codes fro...
description: Imported from the java2s.com archive: To extract Ascii codes from a String
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20140829082904/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ToextractAsciicodesfromaString.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) throws Exception {
    String test = "ABCD";
    for (int i = 0; i < test.length(); ++i) {
      char c = test.charAt(i);
      System.out.println((int) c);
    }
  }
}
/*
65
66
67
68
*/
```
