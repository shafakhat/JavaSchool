---
title: Add hours, minutes or seconds to a date
nav: Add hours, minutes or seco...
description: Imported from the java2s.com archive: Add hours, minutes or seconds to a date
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Addhoursminutesorsecondstoadate.htm
---
```java title=Example.java
import java.util.Calendar;

publicclass DateAddHour {
    publicstaticvoid main(String[] args) {
        Calendar calendar = Calendar.getInstance();
        System.out.println("Original = " + calendar.getTime());

        // Substract 2 hour from the current time
        calendar.add(Calendar.HOUR, -2);

        // Add 30 minutes to the calendar time
        calendar.add(Calendar.MINUTE, 30);

        // Add 300 seconds to the calendar time
        calendar.add(Calendar.SECOND, 300);
        System.out.println("Updated  = " + calendar.getTime());
    }
}
```
