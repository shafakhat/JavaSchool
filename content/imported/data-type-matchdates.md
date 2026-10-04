---
title: Match Dates
nav: Match Dates
description: Imported from the java2s.com archive: Match Dates
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/MatchDates.htm
---
```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    boolean retval = false;
    String date = "12/12/1212";
    String datePattern = "\\d{1,2}-\\d{1,2}-\\d{4}";
    retval = date.matches(datePattern);
  }
}
```
