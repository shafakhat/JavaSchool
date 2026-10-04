---
title: Unaccent letters
nav: Unaccent letters
description: Imported from the java2s.com archive: Unaccent letters
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Unaccentletters.htm
---
```java title=Example.java
import java.text.Normalizer;
publicclass Main {
  publicstaticvoid main(String args[]) throws Exception {
    System.out.println(formatString(""));
  }
  publicstatic String formatString(String s) {
    String temp = Normalizer.normalize(s, Normalizer.Form.NFD);
    return temp.replaceAll("[^\\p{ASCII}]", "");
  }
}
```
