---
title: Returns a Date set just to Noon, to the closest possible millisecond of the day.
nav: Returns a Date set just to...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1090
source: https://web.archive.org/web/20100328231357/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ReturnsaDatesetjusttoNoontotheclosestpossiblemillisecondoftheday.htm
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
 */
import java.util.Calendar;
import java.util.Date;
public class Utils {
  /**
   * Returns a Date set just to Noon, to the closest possible millisecond
   * of the day. If a null day is passed in, a new Date is created.
   * nnoon (00m 12h 00s)
   */
  public static Date getNoonOfDay(Date day, Calendar cal) {
      if (day == null) day = new Date();
      cal.setTime(day);
      cal.set(Calendar.HOUR_OF_DAY, 12);
      cal.set(Calendar.MINUTE,      cal.getMinimum(Calendar.MINUTE));
      cal.set(Calendar.SECOND,      cal.getMinimum(Calendar.SECOND));
      cal.set(Calendar.MILLISECOND, cal.getMinimum(Calendar.MILLISECOND));
      return cal.getTime();
  }
}
```
