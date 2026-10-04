---
title: To obtain a reference to a TimeZone object corresponding to a given time zone ID
nav: To obtain a reference to a...
description: GregorianCalendar calendar = new GregorianCalendar(TimeZone.getTimeZone("America/Chicago"));
section: Imported - java2s Archive
order: 1756
source: https://web.archive.org/web/20140829082757/http://www.java2s.com/Tutorial/Java/0120__Development/ToobtainareferencetoaTimeZoneobjectcorrespondingtoagiventimezoneID.htm
---
```java title=Example.java
import java.util.GregorianCalendar;
import java.util.TimeZone;
public class MainClass {
  public static void main(String[] a) {
    GregorianCalendar calendar = new GregorianCalendar(TimeZone.getTimeZone("America/Chicago"));
    System.out.println(calendar);
  }
}
java title=Example.java
java.util.GregorianCalendar[
time=1168970797636,
areFieldsSet=true,
areAllFieldsSet=true,
lenient=true,
zone=sun.util.calendar.ZoneInfo[id="America/Chicago",
                                offset=-21600000,
                                dstSavings=3600000,
                                useDaylight=true,
                                transitions=235,
                                lastRule=java.util.SimpleTimeZone[id=America/Chicago,
                                                                  offset=-21600000,
                                                                  dstSavings=3600000,
                                                                  useDaylight=true,
                                                                  startYear=0,
                                                                  startMode=3,
                                                                  startMonth=3,
                                                                  startDay=1,
                                                                  startDayOfWeek=1,
                                                                  startTime=7200000,
                                                                  startTimeMode=0,
                                                                  endMode=2,
                                                                  endMonth=9,
                                                                  endDay=-1,
                                                                  endDayOfWeek=1,
                                                                  endTime=7200000,
                                                                  endTimeMode=0]
                               ],
firstDayOfWeek=1,
minimalDaysInFirstWeek=1,
ERA=1,
YEAR=2007,
MONTH=0,
WEEK_OF_YEAR=3,
WEEK_OF_MONTH=3,
DAY_OF_MONTH=16,
DAY_OF_YEAR=16,
DAY_OF_WEEK=3,
DAY_OF_WEEK_IN_MONTH=3,
AM_PM=1,
HOUR=0,
HOUR_OF_DAY=12,
MINUTE=6,
SECOND=37,
MILLISECOND=636,
ZONE_OFFSET=-21600000,
DST_OFFSET=0]
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
