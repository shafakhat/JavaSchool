---
title: Match Address
nav: Match Address
description: String addressPattern = "^" + namePattern + "\\w+ .*, \\w+ " + zipCodePattern + "$";
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20090504061127/http://www.java2s.com:80/Code/Java/Regular-Expressions/MatchAddressmixingnumnersandcharacters.htm
---
Match Address: mixing numners and characters

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
