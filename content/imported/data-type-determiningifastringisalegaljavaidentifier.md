---
title: Determining If a String Is a Legal Java Identifier
nav: Determining If a String Is...
description: if (s.length() == 0 || !Character.isJavaIdentifierStart(s.charAt(0))) {
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DeterminingIfaStringIsaLegalJavaIdentifier.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    boolean b = isJavaIdentifier("my_var");
  }
  publicstaticboolean isJavaIdentifier(String s) {
    if (s.length() == 0 || !Character.isJavaIdentifierStart(s.charAt(0))) {
      return false;
    }
    for (int i = 1; i < s.length(); i++) {
      if (!Character.isJavaIdentifierPart(s.charAt(i))) {
        return false;
      }
    }
    return true;
  }
}
```
