---
title: Check if given string is a number (digits only)
nav: Check if given string is a...
description: 2. Check if given string is number with dot separator and two decimals
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20090530095730/http://www.java2s.com:80/Code/Java/Regular-Expressions/Checkifgivenstringisanumberdigitsonly.htm
---
Check if given string is a number (digits only)

```java title=Example.java
public class Main {
  public static boolean isNumber(String string) {
    return string.matches("^\\d+$");
  }
  public static void main(String[] args) {
    System.out.println(isNumber("123"));
  }
}
```

1.  Check if given string is numeric (-+0..9(.)0...9)
---  ---
2.  Check if given string is number with dot separator and two decimals
3.  Match number
4.  Match a single digit
5.  Matcher Pattern number
