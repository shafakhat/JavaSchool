---
title: Utility methods for ASCII character checking.
nav: Utility methods for ASCII ...
description: * Checks whether the supplied character is a letter or number.
section: Imported - java2s Archive
order: 1060
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UtilitymethodsforASCIIcharacterchecking.htm
---
```java title=Example.java
/**
 */publicclass ASCIIUtil {
  /**
   * Checks whether the supplied character is a letter or number.
   */publicstaticboolean isLetterOrNumber(int c) {
    return isLetter(c) || isNumber(c);
  }
  /**
   * Checks whether the supplied character is a letter.
   */publicstaticboolean isLetter(int c) {
    return isUpperCaseLetter(c) || isLowerCaseLetter(c);
  }
  /**
   * Checks whether the supplied character is an upper-case letter.
   */publicstaticboolean isUpperCaseLetter(int c) {
    return (c >= 65 && c <= 90); // A - Z
  }
  /**
   * Checks whether the supplied character is an lower-case letter.
   */publicstaticboolean isLowerCaseLetter(int c) {
    return (c >= 97 && c <= 122);  // a - z
  }
  /**
   * Checks whether the supplied character is a number
   */publicstaticboolean isNumber(int c) {
    return (c >= 48 && c <= 57); // 0 - 9
  }
}
```
