---
title: Create an instance using Japan's time zone and set it with the local UTC
nav: Create an instance using J...
description: Calendar japanCal = new GregorianCalendar(TimeZone.getTimeZone("Japan"));
section: Imported - java2s Archive
order: 1765
source: https://web.archive.org/web/20140829082956/http://www.java2s.com/Tutorial/Java/0120__Development/CreateaninstanceusingJapanstimezoneandsetitwiththelocalUTC.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.TimeZone;
public class Main {
  public static void main(String[] argv) throws Exception {
    Calendar local = Calendar.getInstance();
    Calendar japanCal = new GregorianCalendar(TimeZone.getTimeZone("Japan"));
    japanCal.setTimeInMillis(local.getTimeInMillis());
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
