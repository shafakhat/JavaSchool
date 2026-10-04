---
title: Java Format - Java Date Format Pattern
nav: Java Format - Java Date Fo...
description: SimpleDateFormat Date and time formats are specified by date and time pattern strings.
section: Imported - java2s Archive
order: 50388
source: https://www.java2s.com/Tutorials/Java/Java_Format/0030__Java_Date_Format_Symbol.html
---
```java title=Example.java
```

SimpleDateFormat Date and time formats are specified by date and time pattern strings.

Within format strings, unquoted letters from 'A' to 'Z' and from 'a' to 'z' are treated as format letters representing the components of a date or time string.

Text can be quoted using single quotes (') to avoid interpretation. '' represents a single quote. All other characters are not interpreted and will be simply copied into the output string.

## Pattern

The following pattern letters are defined:

Letter  Date or Time Component  Examples
---  ---  ---
G  Era designator  AD
y  Year  2014 ; 14
Y  Week year  2014 ; 14
M  Month in year (context sensitive)  July ; Jul ; 07
L  Month in year (standalone form)  July ; Jul ; 07
w  Week in year  27
W  Week in month  2
D  Day in year  189
d  Day in month  10
F  Day of week in month  2
E  Day name in week  Tuesday ; Tue
u  Day number of week (1 = Monday, ..., 7 = Sunday)  1
a  Am/pm marker  PM
H  Hour in day (0-23)  0
k  Hour in day (1-24)  24
K  Hour in am/pm (0-11)  0
h  Hour in am/pm (1-12)  12
m  Minute in hour  30
s  Second in minute  55
S  Millisecond  978
z  Time zone  Pacific Standard Time ; PST ; GMT-08:00
Z  Time zone  -0800
X  Time zone  -08 ; -0800 ; -08:00

## Example

The following table has some example format string and its result.

Date and Time Pattern  Result
---  ---
"yyyy.MM.dd G 'at' HH:mm:ss z"  2014.08.04 AD at 12:08:56 PDT
"EEE, MMM d, ''yy"  Wed, Jul 4, '01
"h:mm a"  11:08 PM
"hh 'o''clock' a, zzzz"  12 o'clock PM, Pacific Daylight Time
"K:mm a, z"  0:08 PM, PDT
"yyyyy.MMMMM.dd GGG hh:mm aaa"  02014.July.04 AD 12:08 PM
"EEE, d MMM yyyy HH:mm:ss Z"  Wed, 4 Jul 2001 12:08:56 -0700
"yyMMddHHmmssZ"  020704120856-0700
"yyyy-MM-dd'T'HH:mm:ss.SSSZ"  2014-07-04T12:08:56.235-0700
"yyyy-MM-dd'T'HH:mm:ss.SSSXXX"  2014-07-04T12:08:56.235-07:00
"YYYY-'W'ww-u"  2014-W27-3

## Example 2

We can embed literals inside formatted dates.

We need to place them inside single quotes to treat them as literals.

```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
publicclass Main {
  publicstaticvoid main(String[] args) {
    GregorianCalendar gc  = new GregorianCalendar(2010, Calendar.SEPTEMBER,9);
    Date  birthDate = gc.getTime();
    String pattern = "'I was born on the day' dd 'of the month 'MMMM 'in' yyyy";
    SimpleDateFormat simpleFormatter  = new SimpleDateFormat(pattern);
    System.out.println(simpleFormatter.format(birthDate));
  }
}
```

The code above generates the following result.

## Parse String to Date

We can convert String value to date time value by using the parse() method of the SimpleDateFormat class.

The signature of the parse() method is as follows:

```java title=Example.java
public Date parse(String text, ParsePosition startPos)
```

The parse() method takes two arguments. text is the string to parse, startPos sets the starting position of the character in the text from where you want to start parsing.

## Example 3

The following code shows how parse a string to a date value.

```java title=Example.java
import java.text.ParsePosition;
import java.text.SimpleDateFormat;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String text = "09/19/2014";
    // Create a pattern for the date text "09/19/2014"
    String pattern = "MM/dd/yyyy";
    SimpleDateFormat simpleFormatter = new SimpleDateFormat(pattern);
    // a ParsePosition object with value zero
    ParsePosition startPos = new ParsePosition(0);
    // Parse the text
    Date parsedDate = simpleFormatter.parse(text, startPos);
    System.out.println(parsedDate);
  }
}
```

The code above generates the following result.

## Example 4

The following code parses two date values from a single string.

```java title=Example.java
import java.text.ParsePosition;
import java.text.SimpleDateFormat;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String text = "ab01/01/1999cd12/31/2000ef";
    String pattern = "MM/dd/yyyy";
    SimpleDateFormat simpleFormatter  = new SimpleDateFormat(pattern);
    // Set  the   start index   at 2
    ParsePosition startPos  = new ParsePosition(2);
    // Parse the   text to get   the   first date (January 1,  1999)
    Date  firstDate = simpleFormatter.parse(text, startPos);
    System.out.println(firstDate);
   //Now, startPos has  its index set after the last  character of the first date parsed.
int  currentIndex = startPos.getIndex();
    System.out.println(currentIndex);
    // To set its index   to the   next   date increment its index   by  2.
int  nextIndex = currentIndex + 2;
    startPos.setIndex  (nextIndex);
    // Parse the   text to get   the   second  date (December  31,   2000)
    Date  secondDate = simpleFormatter.parse(text, startPos);
    System.out.println(secondDate);
  }
}
```

The code above generates the following result.

## Example 5

The following code shows how to parse a Timestamp to Get Its Time Parts

```java title=Example.java
import java.text.ParsePosition;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
publicclass Main {
  publicstaticvoid main(String[] args) {
    String input = "2014-05-04 09:10:40.321";
    // Prepare the pattern
    String pattern = "yyyy-MM-dd HH:mm:ss.SSS";
    SimpleDateFormat sdf = new SimpleDateFormat(pattern);
    // Parse the text into a Date object
    Date dt = sdf.parse(input, new ParsePosition(0));
    System.out.println(dt);
    // Get the Calendar instance
    Calendar cal = Calendar.getInstance();
    cal.setTime(dt);
    // Print time parts
    System.out.println("Hour:" + cal.get(Calendar.HOUR));
    System.out.println("Minute:" + cal.get(Calendar.MINUTE));
    System.out.println("Second:" + cal.get(Calendar.SECOND));
    System.out.println("Millisecond:" + cal.get(Calendar.MILLISECOND));
  }
}
```

The code above generates the following result.

- « Previous
