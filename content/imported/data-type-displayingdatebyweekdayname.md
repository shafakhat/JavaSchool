---
title: Displaying Date by weekday name
nav: Displaying Date by weekday...
description: GregorianCalendar birthdate = new GregorianCalendar(1999, 1, 1);
section: Imported - java2s Archive
order: 1236
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DisplayingDatebyweekdayname.htm
---
```java title=Example.java
import static java.util.Calendar.DATE;
import static java.util.Calendar.DAY_OF_WEEK;
import static java.util.Calendar.MONTH;
import static java.util.Calendar.YEAR;
import java.text.DateFormatSymbols;
import java.util.GregorianCalendar;
public class MainClass {
  public static void main(String[] args) {
    GregorianCalendar birthdate = new GregorianCalendar(1999, 1, 1);
    GregorianCalendar today = new GregorianCalendar(); // Today's date
    GregorianCalendar birthday = new GregorianCalendar(today.get(YEAR), birthdate.get(MONTH),
        birthdate.get(DATE));
    int age = today.get(today.YEAR) - birthdate.get(YEAR);
    String[] weekdays = new DateFormatSymbols().getWeekdays(); // Get day names
    System.out.println("You were born on a " + weekdays[birthdate.get(DAY_OF_WEEK)]);
    System.out.println("This year you " + (birthday.after(today) ? " will be " : "are ") + age
        + " years old.");
    System.out.println("In " + today.get(YEAR) + " your birthday "
        + (today.before(birthday) ? "will be" : "was") + " on a "
        + weekdays[birthday.get(DAY_OF_WEEK)] + ".");
  }
}
java title=Example.java
You were born on a Monday
This year you  will be 8 years old.
In 2007 your birthday will be on a Thursday.
```
