---
title: A method used to build a date for use Marker XML and KML data
nav: A method used to build a d...
description: A method used to build a date for use Marker XML and KML data
section: Imported - java2s Archive
order: 1130
source: https://web.archive.org/web/20111125123828/http://java2s.com/Code/Java/Data-Type/AmethodusedtobuildadateforuseMarkerXMLandKMLdata.htm
---
A method used to build a date for use Marker XML and KML data

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
   * A method used to build a date for use Marker XML and KML data
   *
   * @param year  the year component of the date
   * @param month the month component of the date
   * @param day   the day component of the month
   *
   * @return      a string containing the finalised date
   */
  public static String buildDate(String year, String month, String day) {
    // check for at least a year
    if(year != null) {
      String date = year + "-" + month + "-" + day;
       date = date.replace("-null","");
      date = date.replace("null","");
      return date;
    } else {
      return "";
    }
  } // end buildDate method
}
```

1.  Cast a float or double to an integral value
---  ---
2.  A simple casting demo
3.  Casting Demo
4.  Get the minimum and maximum value of a primitive data types?
5.  Class with methods for type conversion
6.  Data type conversion
7.  Data type Conversion Util
8.  Convert Byte array to Int
9.  Convert Number To Target Class
10.  Convert byte array to Long
11.  Convert long to Bytes
12.  Conversion utilities
13.  Get Time From Date
14.  Get String From Date
15.  A method used to build a date for display in line with existing formatting rules
