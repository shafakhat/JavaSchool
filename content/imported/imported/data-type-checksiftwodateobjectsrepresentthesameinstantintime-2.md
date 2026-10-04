---
title: Checks if two date objects represent the same instant in time
nav: Checks if two date objects...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Checksiftwodateobjectsrepresentthesameinstantintime.htm
---
```java title=Example.java
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Calendar;
import java.util.Date;

/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *//**
 * A suite of utilities surrounding the use of the
 * {@link java.util.Calendar} and {@link java.util.Date} object.
 *
 * DateUtils contains a lot of common methods considering manipulations
 * of Dates or Calendars. Some methods require some extra explanation.
 * The truncate and round methods could be considered the Math.floor(),
 * Math.ceil() or Math.round versions for dates
 * This way date-fields will be ignored in bottom-up order.
 * As a complement to these methods we've introduced some fragment-methods.
 * With these methods the Date-fields will be ignored in top-down order.
 * Since a date without a year is not a valid date, you have to decide in what
 * kind of date-field you want your result, for instance milliseconds or days.
 *
 *
 *
 *
 * @author <a href="mailto:sergek@lokitech.com">Serge Knystautas</a>
 * @author Stephen Colebourne
 * @author Janek Bogucki
 * @author <a href="mailto:ggregory@seagullsw.com">Gary Gregory</a>
 * @author Phil Steitz
 * @author Robert Scholte
 * @since 2.0
 * @version $Id: DateUtils.java 634096 2008-03-06 00:58:11Z niallp $
 */publicclass Main {

  //-----------------------------------------------------------------------
/**
   * Checks if two date objects represent the same instant in time.
   *
   * This method compares the long millisecond time of the two objects.
   *
   * @param date1  the first date, not altered, not null
   * @param date2  the second date, not altered, not null
   * @return true if they represent the same millisecond instant
   * @throws IllegalArgumentException if either date is <code>null</code>
   * @since 2.1
   */publicstaticboolean isSameInstant(Date date1, Date date2) {
      if (date1 == null || date2 == null) {
          thrownew IllegalArgumentException("The date must not be null");
      }
      return date1.getTime() == date2.getTime();
  }

  /**
   * Checks if two calendar objects represent the same instant in time.
   *
   * This method compares the long millisecond time of the two objects.
   *
   * @param cal1  the first calendar, not altered, not null
   * @param cal2  the second calendar, not altered, not null
   * @return true if they represent the same millisecond instant
   * @throws IllegalArgumentException if either date is <code>null</code>
   * @since 2.1
   */publicstaticboolean isSameInstant(Calendar cal1, Calendar cal2) {
      if (cal1 == null || cal2 == null) {
          thrownew IllegalArgumentException("The date must not be null");
      }
      return cal1.getTime().getTime() == cal2.getTime().getTime();
  }
}
```
