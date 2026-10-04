---
title: Returns a Date set to the last possible millisecond of the month, just before midnight.
nav: Returns a Date set to the ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ReturnsaDatesettothelastpossiblemillisecondofthemonthjustbeforemidnight.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  The ASF licenses this file to You
 * under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.  For additional information regarding
 * copyright in this work, please see the NOTICE file in the top level
 * directory of this distribution.
 */import java.util.Calendar;
import java.util.Date;
publicclass Utils {
  /**
   * Returns a Date set to the last possible millisecond of the month, just
   * before midnight. If a null day is passed in, a new Date is created.
   * midnight (00m 00h 00s)
   */publicstatic Date getEndOfMonth(Date day) {
      return getEndOfMonth(day, Calendar.getInstance());
  }
  publicstatic Date getEndOfMonth(Date day,Calendar cal) {
      if (day == null) day = new Date();
      cal.setTime(day);
      // set time to end of day
      cal.set(Calendar.HOUR_OF_DAY, cal.getMaximum(Calendar.HOUR_OF_DAY));
      cal.set(Calendar.MINUTE,      cal.getMaximum(Calendar.MINUTE));
      cal.set(Calendar.SECOND,      cal.getMaximum(Calendar.SECOND));
      cal.set(Calendar.MILLISECOND, cal.getMaximum(Calendar.MILLISECOND));
      // set time to first day of month
      cal.set(Calendar.DAY_OF_MONTH, 1);
      // add one month
      cal.add(Calendar.MONTH, 1);
      // back up one day
      cal.add(Calendar.DAY_OF_MONTH, -1);
      return cal.getTime();
  }
}
```
