---
title: Getting the Current Time in Another Time Zone
nav: Getting the Current Time i...
description: Calendar cal = new GregorianCalendar(TimeZone.getTimeZone("Hongkong"));
section: Imported - java2s Archive
order: 1762
source: https://web.archive.org/web/20140829082624/http://www.java2s.com/Tutorial/Java/0120__Development/GettingtheCurrentTimeinAnotherTimeZone.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.TimeZone;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Get the current time in Hong Kong
    Calendar cal = new GregorianCalendar(TimeZone.getTimeZone("Hongkong"));
    int hour12 = cal.get(Calendar.HOUR); // 0..11
    int minutes = cal.get(Calendar.MINUTE); // 0..59
    int seconds = cal.get(Calendar.SECOND); // 0..59
    boolean am = cal.get(Calendar.AM_PM) == Calendar.AM;
    // Get the current hour-of-day at GMT
    cal.setTimeZone(TimeZone.getTimeZone("GMT"));
    int hour24 = cal.get(Calendar.HOUR_OF_DAY); // 0..23
    // Get the current local hour-of-day
    cal.setTimeZone(TimeZone.getDefault());
    hour24 = cal.get(Calendar.HOUR_OF_DAY); // 0..23
  }
}
```

| 6.21.1. | To obtain a reference to a TimeZone object corresponding to a given time zone ID |
|---|---|
| 6.21.2. | TimeZone.getTimeZone('America/New_York') |
| 6.21.3. | TimeZone.getTimeZone('Europe/Paris') |
| 6.21.4. | TimeZone.getTimeZone('Asia/Tokyo') |
| 6.21.5. | Get current TimeZone using Java Calendar |
| 6.21.6. | Convert time between timezone |
| 6.21.7. | Getting the Current Time in Another Time Zone |
| 6.21.8. | Converting Times Between Time Zones |
| 6.21.9. | Create an instance using Japan's time zone and set it with the local UTC |
| 6.21.10. | Get the foreign time |
| 6.21.11. | Given a time of 10am in Japan, get the local time |
| 6.21.12. | Create a Calendar object with the local time zone and set the UTC from japanCal |
| 6.21.13. | Get the time in the local time zone |
| 6.21.14. | Getting all the time zones IDs |
| 6.21.15. | Timezone conversion routines |
