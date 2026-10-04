---
title: How do I mark method as deprecated?
nav: How do I mark method as de...
description: Imported from the java2s.com archive: How do I mark method as deprecated?
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0020__Language/HowdoImarkmethodasdeprecated.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Date;

publicclass Main {
  publicstaticvoid main(String[] args) {
    getDate();
    getMonthFromDate();
  }

  /**
   * Get current system date.
   *
   * @return current system date.
   * @deprecated This method will removed in the near future.
   */
  @Deprecated
  publicstatic Date getDate() {
    returnnew Date();
  }

  publicstaticint getMonthFromDate() {
    return Calendar.getInstance().get(Calendar.MONTH);
  }
}
```
