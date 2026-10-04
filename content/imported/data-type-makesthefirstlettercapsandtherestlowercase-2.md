---
title: Makes the first letter caps and the rest lowercase.
nav: Makes the first letter cap...
description: * For example <code>fooBar</code> becomes <code>Foobar</code>.
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Makesthefirstlettercapsandtherestlowercase.htm
---
```java title=Example.java
publicclass Main {
  /**
   *
   *
   *
   *
   *  For example <code>fooBar</code> becomes <code>Foobar</code>.
   *
   *
   * @param data capitalize this
   * @return String
   */staticpublic String firstLetterCaps ( String data )
  {
      String firstLetter = data.substring(0,1).toUpperCase();
      String restLetters = data.substring(1).toLowerCase();
      return firstLetter + restLetters;
  }
}
```
