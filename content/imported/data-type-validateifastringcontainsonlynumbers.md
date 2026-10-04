---
title: Validate if a String contains only numbers
nav: Validate if a String conta...
description: Imported from the java2s.com archive: Validate if a String contains only numbers
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20140829083344/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ValidateifaStringcontainsonlynumbers.htm
---
```java title=Example.java
public class Main {
  public static boolean containsOnlyNumbers(String str) {
    for (int i = 0; i < str.length(); i++) {
      if (!Character.isDigit(str.charAt(i)))
        return false;
    }
    return true;
  }
  public static void main(String[] args) {
    System.out.println(containsOnlyNumbers("123456"));
    System.out.println(containsOnlyNumbers("123abc456"));
  }
}
/*
true
false
*/
```
