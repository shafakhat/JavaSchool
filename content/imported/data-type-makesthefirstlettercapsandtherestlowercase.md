---
title: Makes the first letter caps and the rest lowercase.
nav: Makes the first letter cap...
description: * For example <code>fooBar</code> becomes <code>Foobar</code>.
section: Imported - java2s Archive
order: 1061
source: https://web.archive.org/web/20100412210713/http://java2s.com:80/Tutorial/Java/0040__Data-Type/Makesthefirstlettercapsandtherestlowercase.htm
---
```java title=Example.java
public class Main {
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
   */
  static public String firstLetterCaps ( String data )
  {
      String firstLetter = data.substring(0,1).toUpperCase();
      String restLetters = data.substring(1).toLowerCase();
      return firstLetter + restLetters;
  }
}
```
