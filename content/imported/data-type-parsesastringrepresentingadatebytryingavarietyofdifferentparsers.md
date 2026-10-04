---
title: Parses a string representing a date by trying a variety of different parsers.
nav: Parses a string representi...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1272
source: https://web.archive.org/web/20140829090916/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Parsesastringrepresentingadatebytryingavarietyofdifferentparsers.htm
---
```java title=Example.java
import java.math.BigDecimal;
import java.math.BigInteger;
import java.text.ParseException;
import java.text.ParsePosition;
import java.text.SimpleDateFormat;
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
 */
/**
 * <p>A suite of utilities surrounding the use of the
 * {@link java.util.Calendar} and {@link java.util.Date} object.</p>
 *
 * <p>DateUtils contains a lot of common methods considering manipulations
 * of Dates or Calendars. Some methods require some extra explanation.
 * The truncate and round methods could be considered the Math.floor(),
 * Math.ceil() or Math.round versions for dates
 * This way date-fields will be ignored in bottom-up order.
 * As a complement to these methods we've introduced some fragment-methods.
 * With these methods the Date-fields will be ignored in top-down order.
 * Since a date without a year is not a valid date, you have to decide in what
 * kind of date-field you want your result, for instance milliseconds or days.
 * </p>
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
 */
public class Main {
  //-----------------------------------------------------------------------
  /**
   * <p>Parses a string representing a date by trying a variety of different parsers.</p>
   *
   * <p>The parse will try each parse pattern in turn.
   * A parse is only deemed sucessful if it parses the whole of the input string.
   * If no parse patterns match, a ParseException is thrown.</p>
   *
   * @param str  the date to parse, not null
   * @param parsePatterns  the date format patterns to use, see SimpleDateFormat, not null
   * @return the parsed date
   * @throws IllegalArgumentException if the date string or pattern array is null
   * @throws ParseException if none of the date patterns were suitable
   */
  public static Date parseDate(String str, String[] parsePatterns) throws ParseException {
      if (str == null || parsePatterns == null) {
          throw new IllegalArgumentException("Date and Patterns must not be null");
      }
      SimpleDateFormat parser = null;
      ParsePosition pos = new ParsePosition(0);
      for (int i = 0; i < parsePatterns.length; i++) {
          if (i == 0) {
              parser = new SimpleDateFormat(parsePatterns[0]);
          } else {
              parser.applyPattern(parsePatterns[i]);
          }
          pos.setIndex(0);
          Date date = parser.parse(str, pos);
          if (date != null && pos.getIndex() == str.length()) {
              return date;
          }
      }
      throw new ParseException("Unable to parse the date: " + str, -1);
  }
}
```

| 2.38.1. | The java.util.Date Class |
|---|---|
| 2.38.2. | Show date and time using only Date methods. |
| 2.38.3. | Obtaining a Date Object From a String |
| 2.38.4. | Convert from a java.util.Date Object to a java.sql.Date Object |
| 2.38.5. | Convert a String Date Such as 2003/01/10 into a java.util.Date Object |
| 2.38.6. | Create Yesterday's Date from a Date in the String Format of MM/DD/YYYY |
| 2.38.7. | Create a java.util.Date Object from a Year, Month, Day Format |
| 2.38.8. | Create a java.sql.Time Object from java.util.Date |
| 2.38.9. | Convert the Current Time to a java.sql.Date Object |
| 2.38.10. | Convert Date into milliseconds example |
| 2.38.11. | Create java Date from specific time example |
| 2.38.12. | Determine the Day of the Week from Today's Date |
| 2.38.13. | ISO 8601 date parsing utility. |
| 2.38.14. | Parses a string representing a date by trying a variety of different parsers. |
| 2.38.15. | Perform date validations |
