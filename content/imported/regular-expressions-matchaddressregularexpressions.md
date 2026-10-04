---
title: Match address regular expressions
nav: Match address regular expr...
description: Match address regular expressions : Java examples (example source code) » Regular Expressions » Match Address
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20060513094134/http://www.java2s.com/Code/Java/Regular-Expressions/Matchaddressregularexpressions.htm
---
Match address regular expressions : Java examples (example source code) » Regular Expressions » Match Address

Match address regular expressions

```java title=Example.java
public class MatchAddress {
  public static void main(String args[]) {
    isAddressValid("John Smith 888 Luck Street,NY 64332");
    isAddressValid("John A. Smith 888 Luck Street, NY 64332-4453");
    isAddressValid("John Allen Smith 888 Luck Street, NY 64332-4453");
    isAddressValid("888 Luck Street, NY 64332");
    isAddressValid("P.O. BOX 888 Luck Street, NY 64332-4453");
    isAddressValid("John Allen Smith 888 Luck st., NY");
  }
  public static boolean isAddressValid(String addr) {
    boolean retval = false;
    String nameToken = "\\p{Upper}(\\p{Lower}+\\s?)";
    String namePattern = "(" + nameToken + "){2,3}";
    String zipCodePattern = "\\d{5}(-\\d{4})?";
    String addressPattern = "^" + namePattern + "\\w+ .*, \\w+ "
        + zipCodePattern + "$";
    retval = addr.matches(addressPattern);
    String msg = "NO MATCH\npattern:\n " + addr + "\nregexLength:\n "
        + addressPattern;
    if (retval) {
      msg = "MATCH\npattern:\n " + addr + "\nregexLength:\n "
          + addressPattern;
    }
    System.out.println(msg + "\r\n");
    return retval;
  }
}
```

Related examples in the same category
