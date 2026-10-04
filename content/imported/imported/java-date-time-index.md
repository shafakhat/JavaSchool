---
title: Java Date Time Introduction
nav: Java Date Time Introduction
description: Java 8 introduced a new Date-Time API based on IS0-8601 date-time standards.
section: Imported - java2s Archive
order: 50050
source: https://www.java2s.com/Tutorials/Java/Java_Date_Time/index.html
---
Java 8 introduced a new Date-Time API based on IS0-8601 date-time standards.

The Date-Time API uses the calendar system defined in ISO-8601 as the default calendar. This calendar is based on the Gregorian calendar system

The LocalDateTime, ZonedDateTime, and OffsetDateTime in the Date-Time API are all using ISO calendar system.

The Date-Time API uses the Unicode Common Locale Data Repository (CLDR) for the locale data.

The Date-Time API uses the Time-Zone Database (TZDB) for information about time zone.

## Date-Time API Design Principles

The methods in the API are well defined

The Date-Time API provides a fluent interface which makes the code easy to read. Method calls can be chained together. For example we can use the following code to create new date.

```java title=Example.java

LocalDate aDay = LocalDate.now().with(TemporalAdjusters.lastDayOfMonth()).minusDays(2);
```

The Java Date-Time API consists of mostly immutable classes. After the object is created, it cannot be modified. To change its value, a new object must be created as a modified copy of the original.

The Date-Time API is thread-safe.

Methods used to create date or time objects are prefixed with of, from, or with, rather than constructors. There are no set methods. For example:

```java title=Example.java

LocalDate dateOfBirth = LocalDate.of(2014, Month.MAY, 14);
```

The Date-Time API is extensible wherever possible.

Java Date-Time API has a separate set of classes to deal with machine-based time and calendar-based human time.

## Date-Time Packages

Java Date-Time API consists of the primary package, java.time, and four subpackages:

- java.time contains the core of the API for representing date and time. It includes classes for date, time, date and time combined, time zones, instants, duration, and clocks. LocalDate, LocalTime, LocalDateTime, ZonedDateTime, Period, Duration, and Instant classes are in this package. Classes in this package are based on ISO-8601 standards.
- java.time.chrono contains the API for representing calendar systems other than the default ISO-8601. For example, Hijrah calendar, ThaiBuddhist calendar, etc.
- java.time.format contains classes for formatting and parsing dates and times.
- java.time.temporal contains API allowing interoperations between the date and time classes, querying, and adjustment. For example, TemporalField and ChronoField and TemporalUnit and ChronoUnit.
- java.time.zone contains classes that support time zones, offsets from time zones, and time zone rules. For example, ZonedDateTime, and ZoneId or ZoneOffset.
