---
title: Check if given string is number with dot separator and two decimals
nav: Check if given string is n...
description: Check if given string is number with dot separator and two decimals
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20090530100207/http://www.java2s.com:80/Code/Java/Regular-Expressions/Checkifgivenstringisnumberwithdotseparatorandtwodecimals.htm
---
```java title=Example.java
public class Main {
  public static boolean isNumberWith2Decimals(String string) {
    return string.matches("^\\d+\\.\\d{2}$");
  }
  public static void main(String[] args) {
  sysout isNumberWith2Decimals("1234.123")
  }
}
```

1.  Check if given string is a number (digits only)
---  ---
2.  Check if given string is numeric (-+0..9(.)0...9)
3.  Match number
4.  Match a single digit
5.  Matcher Pattern number
