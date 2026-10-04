---
title: Match a single digit
nav: Match a single digit
description: 3. Check if given string is number with dot separator and two decimals
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20090531215201/http://www.java2s.com:80/Code/Java/Regular-Expressions/Matchasingledigit.htm
---
Match a single digit

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String args[]) {
    // match a single digit
    Pattern p = Pattern.compile("\\d");
    Matcher matcher = p.matcher("5");
    boolean isOk = matcher.matches();
    System.out.println("original pattern matches " + isOk);
    // recycle the pattern
    String tmp = p.pattern();
    Pattern p2 = Pattern.compile(tmp);
    matcher = p.matcher("5");
    isOk = matcher.matches();
    System.out.println("second pattern matches " + isOk);
  }
}
```

1.  Check if given string is a number (digits only)
---  ---
2.  Check if given string is numeric (-+0..9(.)0...9)
3.  Check if given string is number with dot separator and two decimals
4.  Match number
5.  Matcher Pattern number
