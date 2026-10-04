---
title: A method to get the current date to use in a timestamp
nav: A method to get the curren...
description: * The AusStage Utilities Package is free software: you can redistribute
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20111003002924/http://www.java2s.com:80/Code/Java/Database-SQL-JDBC/Amethodtogetthecurrentdatetouseinatimestamp.htm
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
   *
   * @return  a string containing the timestamp
   */
  public static String getCurrentDate() {
     GregorianCalendar calendar = new GregorianCalendar();
     DateFormat formatter = DateFormat.getDateInstance(DateFormat.FULL);
    return formatter.format(calendar.getTime());
  } // end getCurrentDate method
}
```

1.  Convert java.sql.Timestamp to long for easy compare
---  ---
2.  Get Date From MySql
3.  Get java.sql.Timestamp fro current time
4.  Get date from Oracle
5.  Insert Date, time and date time data to Oracle
6.  Construct java.sql.Timestamp from string
7.  Demo PreparedStatement Set Time
8.  Demo PreparedStatement Set Timestamp
9.  Demo PreparedStatement Set Date
10.  Compare two times
11.  Convert an Object to a DateTime, without an Exception
12.  Convert an Object to a Timestamp, without an Exception
13.  Convert an Object to a java.sql.Time
14.  Timestamp parse
15.  Parse date and time
16.  convert Strings to Dates and Timestamps and vice versa.
17.  Convert into java.sql.Time (or into java.util.Calendar)
18.  A method to get the current date and time to use in a timestamp
19.  Get today's Timestamp
20.  Convert String To Timestamp
21.  Format Timestamp
22.  Convert a timestamp (= millisecs) to a concise string
23.  Get Date stamp
