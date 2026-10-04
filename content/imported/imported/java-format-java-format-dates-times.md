---
title: Java Format - Java printf Date/Time Format
nav: Java Format - Java printf ...
description: Java printf Date/time formatting deals with date, time, and datetime values.
section: Imported - java2s Archive
order: 50396
source: https://www.java2s.com/Tutorials/Java/Java_Format/0120__Java_Format_Dates_Times.html
---
```java title=Example.java
« Previous
```

- Next »

Java printf Date/time formatting deals with date, time, and datetime values.

Java printf Date/time formatting can be applied to format values of long, Long, java.util.Calendar, java.util.Date, and java.time.temporal.TemporalAccessor types.

The value in a long type is interpreted as the milliseconds passed since January 1, 1970 midnight UTC.

The t uppercase variant T conversion characters are used to format date/time values.

The general syntax for date/time formatting is as follows:

```java title=Example.java

%<argument_index$><flags><width><conversion>
```

Precision is not applicable to date/time formatting.

For date/time formatting, the conversion is a two-character sequence. The first character is always 't' or 'T'. The second character, which is called the conversion suffix, determines the format of the date/time argument.

The following table contains the suffix characters for Time Formatting

Suffix  Meaning
---  ---
H  Format time as two-digit hour of the day for the 24-hour clock. The valid values are 00 to 23. 00 is used for midnight.
I  Format a two-digit hour of the day for the 12-hour clock. The valid values are 01 to 12.
k  Format time the same as the H suffix except that it does not add a leading zero to the output. Valid values are 0 to 23.
l  Format time the same as 'I' suffix except that it does not add a leading zero. Valid values are 1 to 12.
M  A two-digit minute within an hour. Valid values are 00 to 59.
S  A two-digit second. Valid values are 00 to 60.
L  A three-digit millisecond. Valid values are 000 to 999.
N  A nine-digit nanosecond. The valid values are 000000000 to 999999999.
p  Format a locale-specific morning or afternoon string in lowercase. For US locale, "am" or "pm". To get "AM" and "PM", use the uppercase variant 'T' as the conversion character.
z  Output the numeric time zone offset from GMT (e.g., +0530).
Z  Output a string abbreviation of the time zone (e.g., CST, EST, IST, etc).
s  Output seconds since January 1, 1970 midnight UTC.
Q  Output milliseconds since January 1, 1970 midnight UTC.

The following table list of suffix characters for Date Formatting

Letter  Meaning
---  ---
B  Output locale-specific full name of the month, such as "January", "February", in US locale.
b  Output locale-specific abbreviated month name, such as "Jan", "Feb", in US locale.
h  Same as 'b'. Output locale-specific abbreviated month name, such as "Jan", "Feb", in US locale.
A  Output locale-specific full name for the day of the week, such as "Sunday", "Monday" for US locale.
a  Output locale-specific short name of the day of the week, such as "Sun", "Mon" for US locale.
C  Divide the four-digit year by 100 and formats the result as two digits. It adds a leading zero if the resulting number is one digit. Valid values are 00 to 99. For example, if the four-digit year is 2014, it will output 20.
Y  Output a four-digit year with leading zeros if the year contains less than four digits.
y  Output the last two digits of the year and adds leading zero if necessary. 2011 will output 11
j  A three-digit day of the year. Valid values are 000 to 366.
m  A two-digit month. Valid values are 01 to 13. The special value of 13 is required to support lunar calendar.
d  A two-digit day of the month. Valid values are 01 to 31.
e  Day of the month. Valid values are 1 to 31.

The following table lists of Suffix Characters for Date/Time Formatting

Format  Description
---  ---
R  Output time in 24-hour clock format as "hour:minute". It outputs the same as %tH:%tM. Examples: 11:23
T  Output time in 24-hour clock in "hour:minute:second" format. It outputs the same as "%tH:%tM:%tS". Examples 11:23:10
r  Output time in 12-hour clock format as "hour:minute:second morning/afternoon marker". It outputs the same as "%tI:%tM:%tS %Tp". Example, 09:23:45 AM
D  Output the date as "%tm/%td/%ty", such as "01/19/14"
F  Output the date as "%tY-%tm-%td", such as "2014-01-19".
c  Output the date and time as "%ta %tb %td %tT %tZ %tY", such as "Wed Jan 20 12:22:06 CST 2014".

## Example

The following code shows how to use the date time formatter. It uses '<' flag in the format specifier to reuse the value from argument.

```java title=Example.java
import java.time.LocalDateTime;
import java.time.Month;
import java.util.Locale;
//fromwww.java2s.compublicclass Main {
  publicstaticvoid main(String[] args) {
    Locale englishUS = Locale.US;
    LocalDateTime ldt = LocalDateTime.of(2014, Month.JANUARY, 25, 11, 48, 16);
    System.out.printf(englishUS, "US: %tB %<te,  %<tY  %<tT %<Tp%n", ldt);
  }
}
```

The code above generates the following result.

## Example 2

The following code formats the current date and time in the default locale. It uses a ZonedDateTime argument that holds the current date/time with time zone.

```java title=Example.java
import java.time.ZonedDateTime;
/*fromwww.java2s.com*/publicclass Main {
  publicstaticvoid main(String[] args) {
    ZonedDateTime currentTime = ZonedDateTime.now();
    System.out.printf("%tA %<tB  %<te,  %<tY  %n", currentTime);
    System.out.printf("%TA %<TB  %<te,  %<tY  %n", currentTime);
    System.out.printf("%tD %n", currentTime);
    System.out.printf("%tF %n", currentTime);
    System.out.printf("%tc %n", currentTime);
    System.out.printf("%Tc %n", currentTime);
  }
}
```

The code above generates the following result.

- Next »
- « Previous
