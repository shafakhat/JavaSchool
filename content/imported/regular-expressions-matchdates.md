---
title: Match Dates
nav: Match Dates
description: Imported from the java2s.com archive: Match Dates
section: Imported - java2s Archive
order: 1052
source: https://web.archive.org/web/20091106064007/http://www.java2s.com:80/Code/Java/Regular-Expressions/MatchDates.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    boolean retval = false;
    String date = "12/12/1212";
    String datePattern = "\\d{1,2}-\\d{1,2}-\\d{4}";
    retval = date.matches(datePattern);
  }
}
```
