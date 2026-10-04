---
title: Enumeration Fundamentals
nav: Enumeration Fundamentals
description: Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20070428112248/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/EnumerationFundamentals.htm
---
An enumeration is created using the new enum keyword.

```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
```

- The identifiers Monday, Tuesday, and so on, are called enumeration constants.
- Each is implicitly declared as a public, static member of Week.
- Their type is the type of the enumeration in which they are declared.
- These constants are called self-typed.

You declare and use an enumeration variable in much the same way as the primitive types.

```java title=Example.java
Week aWeekDay;
```

Because aWeekDay is of type Week, the only values that it can be assigned (or contain) are those defined by the enumeration.

```java title=Example.java
enum Week {
  Monday, Tuesday, Wednesday, Thursday, Friday, Saturaday, Sunday
}
public class MainClass {
  public static void main(String args[]) {
    Week aWeekDay;
    aWeekDay = Week.Monday;
    // Output an enum value.
    System.out.println("Value of aWeekDay: " + aWeekDay);
    System.out.println();
  }
}
java title=Example.java
Value of aWeekDay: Monday
```
