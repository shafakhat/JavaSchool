---
title: Match Address
nav: Match Address
description: Match Address: mixing numbers and characters : Match Address « Regular Expressions « Java
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20090914064643/http://www.java2s.com:80/Code/Java/Regular-Expressions/MatchAddressmixingnumbersandcharacters.htm
---
Match Address: mixing numbers and characters : Match Address « Regular Expressions « Java
Match Address: mixing numbers and characters

```java title=Example.java
public class Main {
  public static void main(String args[]) {
    String addr = "street 124 a0a";
    String nameToken = "\\p{Upper}(\\p{Lower}+\\s?)";
    String namePattern = "(" + nameToken + "){2,3}";
    String zipCodePattern = "\\d{5}(-\\d{4})?";
    String addressPattern = "^" + namePattern + "\\w+ .*, \\w+ " + zipCodePattern + "$";
    System.out.println(addr.matches(addressPattern));
  }
}
```

1.  Match Email address
2.  Match address regular expressions
