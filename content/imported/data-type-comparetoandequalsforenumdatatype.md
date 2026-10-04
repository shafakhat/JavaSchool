---
title: compareTo() and equals() for enum data type
nav: compareTo() and equals() f...
description: Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
section: Imported - java2s Archive
order: 1364
source: https://web.archive.org/web/20140829083859/http://www.java2s.com/Tutorial/Java/0040__Data-Type/compareToandequalsforenumdatatype.htm
---
```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
public class MainClass {
  public static void main(String args[]) {
    Week day1, day2, day3;
    day1 = Week.Monday;
    day2 = Week.Tuesday;
    day3 = Week.Friday;
    //
    if (day1.compareTo(day2) < 0)
      System.out.println(day1 + " comes before " + day2);
    if (day2.compareTo(day3) > 0)
      System.out.println(day2 + " comes before " + day3);
    if (day1.compareTo(day3) == 0)
      System.out.println(day1 + " equals " + day3);
  }
}
java title=Example.java
Monday comes before Tuesday
```

| 2.44.1. | Obtaining all ordinal values using ordinal() |
|---|---|
| 2.44.2. | compareTo() and equals() for enum data type |
| 2.44.3. | Using the built-in enumeration methods: values( ) |
| 2.44.4. | Using valueOf() |
| 2.44.5. | Switch statement with enum |
| 2.44.6. | Adding Members to an Enumeration Class |
| 2.44.7. | Use the built-in enumeration methods. |
| 2.44.8. | Use an enum constructor, instance variable, and method. |
| 2.44.9. | Demonstrate ordinal(), compareTo(), and equals(). |
