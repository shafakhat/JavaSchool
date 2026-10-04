---
title: Returns a Date set to the last possible millisecond of the minute.
nav: Returns a Date set to the ...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1094
source: https://web.archive.org/web/20100328232644/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ReturnsaDatesettothelastpossiblemillisecondoftheminute.htm
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
   * Returns a Date set to the last possible millisecond of the minute.
   * If a null day is passed in, a new Date is created.
   */
  public static Date getEndOfMinute(Date day) {
      return getEndOfMinute(day, Calendar.getInstance());
  }
  public static Date getEndOfMinute(Date day, Calendar cal) {
      if (day == null || cal == null) {
          return day;
      }
      cal.setTime(day);
      cal.set(Calendar.SECOND,      cal.getMaximum(Calendar.SECOND));
      cal.set(Calendar.MILLISECOND, cal.getMaximum(Calendar.MILLISECOND));
      return cal.getTime();
  }
}
```
