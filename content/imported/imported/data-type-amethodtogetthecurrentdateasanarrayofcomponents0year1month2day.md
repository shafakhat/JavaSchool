---
title: A method to get the current date as an array of components 0 = year, 1 = month, 2 = day
nav: A method to get the curren...
description: A method to get the current date as an array of components 0 = year, 1 = month, 2 = day
section: Imported - java2s Archive
order: 1127
source: https://web.archive.org/web/20111125120615/http://java2s.com/Code/Java/Data-Type/Amethodtogetthecurrentdateasanarrayofcomponents0year1month2day.htm
---
```java title=Example.java
/*
 * This file is part of the AusStage Utilities Package
 *
 * The AusStage Utilities Package is free software: you can redistribute
 * it and/or modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * The AusStage Utilities Package is distributed in the hope that it will
 * be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
 * of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with the AusStage Utilities Package.
 * If not, see <http://www.gnu.org/licenses/>.
*/
//package au.edu.ausstage.utils;
// import additional libraries
import java.util.GregorianCalendar;
import java.util.Calendar;
import java.text.DateFormat;
/**
 * A class of methods useful when processing dates in AusStage Services
 */
public class DateUtils {
  /**
   * A method to get the current date as an array of components
   * 0 = year, 1 = month, 2 = day
   *
   * @return an array of strings representing the current date
   */
  public static String[] getCurrentDateAsArray() {
    GregorianCalendar calendar = new GregorianCalendar();
    String[] fields = new String[3];
    fields[0] = Integer.toString(calendar.get(Calendar.YEAR));
    fields[1] = String.format("%02d", calendar.get(Calendar.MONTH) + 1);
    fields[2] = String.format("%02d", calendar.get(Calendar.DAY_OF_MONTH));
    return fields;
  }
}
```

1.  Date parser for ISO 8601 format
2.  Date Utils
3.  Date To String
4.  Perform date validations
5.  ISO 8601 date parsing utility.
6.  Parses a string representing a date by trying a variety of different parsers.
7.  Parses a time period into a long. Translates possible [msec  sec  min  h] suffixes
8.  ISO 8601 date parsing utility. Designed for parsing the ISO subset used in Dublin Core, RSS 1.0, and Atom.
9.  A simple XML parser that starts parsing right away and validates along the way.
