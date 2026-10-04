---
title: Printing out weekday names
nav: Printing out weekday names
description: String[] weekdays = new DateFormatSymbols().getWeekdays(); // Get day names
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Printingoutweekdaynames.htm
---
```java title=Example.java
import java.text.DateFormatSymbols;
publicclass MainClass {
  publicstaticvoid main(String[] args) {
    String[] weekdays = new DateFormatSymbols().getWeekdays(); // Get day names
for(String s: weekdays){
      System.out.println(s);
    }
  }
}
```

```java title=Example.java
Sunday
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
```
