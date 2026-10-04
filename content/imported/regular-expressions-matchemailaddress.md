---
title: Match Email address
nav: Match Email address
description: int IndexOf = s.indexOf("@"); // returns an integer which tells the position of this substring "@" in the parent String "suraj.gupta@yahoo.com"
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20070611152055/http://www.java2s.com:80/Code/Java/Regular-Expressions/MatchEmailaddress.htm
---
```java title=Example.java
  /**
   * SubStringDemo.java separates domain name like "@yahoo.com"
   * from email id like "suraj.gupta@yahoo.com"
   *
   */
  public class SubStringDemo {
        /**
         * @author suraj.gupta
         */
     public static void main(String[] args) {
        String s = "suraj.gupta@yahoo.com"; // email id in a String
        int IndexOf = s.indexOf("@"); // returns an integer which tells the position of this substring "@" in the parent String "suraj.gupta@yahoo.com"
        String domainName = s.substring(IndexOf); //prints the String after that index
        System.out.println("Taking Domain name from an email id "+domainName);
     }
  }
```

Related examples in the same category
1. Match address regular expressions
