---
title: Obtaining a Date Object From a String
nav: Obtaining a Date Object Fr...
description: DateFormat fmt = DateFormat.getDateInstance(DateFormat.FULL, Locale.US);
section: Imported - java2s Archive
order: 1240
source: https://web.archive.org/web/20140829090603/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ObtainingaDateObjectFromaString.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
public class MainClass {
  public static void main(String[] a) {
    Date aDate;
    DateFormat fmt = DateFormat.getDateInstance(DateFormat.FULL, Locale.US);
    try {
      aDate = fmt.parse("Saturday, July 4, 1998 ");
      System.out.println("The Date string is: " + fmt.format(aDate));
    } catch (java.text.ParseException e) {
      System.out.println(e);
    }
  }
}
java title=Example.java
The Date string is: Saturday, July 4, 1998
```

| 2.38.1. | The java.util.Date Class |
|---|---|
| 2.38.2. | Show date and time using only Date methods. |
| 2.38.3. | Obtaining a Date Object From a String |
| 2.38.4. | Convert from a java.util.Date Object to a java.sql.Date Object |
| 2.38.5. | Convert a String Date Such as 2003/01/10 into a java.util.Date Object |
| 2.38.6. | Create Yesterday's Date from a Date in the String Format of MM/DD/YYYY |
| 2.38.7. | Create a java.util.Date Object from a Year, Month, Day Format |
| 2.38.8. | Create a java.sql.Time Object from java.util.Date |
| 2.38.9. | Convert the Current Time to a java.sql.Date Object |
| 2.38.10. | Convert Date into milliseconds example |
| 2.38.11. | Create java Date from specific time example |
| 2.38.12. | Determine the Day of the Week from Today's Date |
| 2.38.13. | ISO 8601 date parsing utility. |
| 2.38.14. | Parses a string representing a date by trying a variety of different parsers. |
| 2.38.15. | Perform date validations |
