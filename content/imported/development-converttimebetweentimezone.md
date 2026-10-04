---
title: Convert time between timezone
nav: Convert time between timez...
description: System.out.printf("Local time : %02d:%02d:%02d\n", hour, minute, second);
section: Imported - java2s Archive
order: 1761
source: https://web.archive.org/web/20140829084043/http://www.java2s.com/Tutorial/Java/0120__Development/Converttimebetweentimezone.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.TimeZone;
public class Main {
  public static void main(String[] args) {
    Calendar localTime = Calendar.getInstance();
    localTime.set(Calendar.HOUR, 17);
    localTime.set(Calendar.MINUTE, 15);
    localTime.set(Calendar.SECOND, 20);
    int hour = localTime.get(Calendar.HOUR);
    int minute = localTime.get(Calendar.MINUTE);
    int second = localTime.get(Calendar.SECOND);
    System.out.printf("Local time  : %02d:%02d:%02d\n", hour, minute, second);
    Calendar germanyTime = new GregorianCalendar(TimeZone.getTimeZone("Germany"));
    germanyTime.setTimeInMillis(localTime.getTimeInMillis());
    hour = germanyTime.get(Calendar.HOUR);
    minute = germanyTime.get(Calendar.MINUTE);
    second = germanyTime.get(Calendar.SECOND);
    System.out.printf("Germany time: %02d:%02d:%02d\n", hour, minute, second);
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
