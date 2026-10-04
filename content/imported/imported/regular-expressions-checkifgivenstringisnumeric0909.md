---
title: Check if given string is numeric (-+0..9(.)0...9)
nav: Check if given string is n...
description: 2. Check if given string is number with dot separator and two decimals
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20090531212025/http://www.java2s.com:80/Code/Java/Regular-Expressions/Checkifgivenstringisnumeric0909.htm
---
```java title=Example.java
public class Main {
  public static boolean isNumeric(String string) {
      return string.matches("^[-+]?\\d+(\\.\\d+)?$");
  }
  public static void main(String[] args) {
sysout isNumeric("123.123")
  }
}
```

1.  Check if given string is a number (digits only)
---  ---
2.  Check if given string is number with dot separator and two decimals
3.  Match number
4.  Match a single digit
5.  Matcher Pattern number
