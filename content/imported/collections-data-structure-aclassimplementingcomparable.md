---
title: A Class Implementing Comparable
nav: A Class Implementing Compa...
description: Imported from the java2s.com archive: A Class Implementing Comparable
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20060905011634/http://www.java2s.com:80/Code/Java/Collections-Data-Structure/AClassImplementingComparable.htm
---
```java title=Example.java
public class Time implements Comparable {
  private int hour, minute;
  public Time(int hh, int mm) {
    this.hour = hh;
    this.minute = mm;
  }
  public int compareTo(Object o) {
    Time t = (Time) o;
    return hour != t.hour ? hour - t.hour : minute - t.minute;
  }
  public boolean equals(Object o) {
    Time t = (Time) o;
    return hour == t.hour && minute == t.minute;
  }
  public int hashCode() {
    return 60 * hour + minute;
  }
}
```

Related examples in the same category
---
1. Creating a Comparable object
2. Writing Your own Comparator
3. Comparator for comparing strings ignoring first character
4. Customized Sort Test
5. List and Comparators
6. Sort backwards
7. Company and Employee
8. Search with a Comparator
9. Keep upper and lowercase letters together
10. Uses anonymous inner classes
11. Building the anonymous inner class in-place
