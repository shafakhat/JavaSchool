---
title: Returns true if endDate is after startDate or if startDate equals endDate.
nav: Returns true if endDate is...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1102
source: https://web.archive.org/web/20100328232700/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/ReturnstrueifendDateisafterstartDateorifstartDateequalsendDate.htm
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
import java.util.Date;
public class Utils {
  /**
   * Returns false if either value is null.  If equalOK, returns true if the
   * dates are equal.
   **/
  public static boolean isValidDateRange(Date startDate, Date endDate, boolean equalOK) {
      // false if either value is null
      if (startDate == null || endDate == null) { return false; }
      if (equalOK) {
          // true if they are equal
          if (startDate.equals(endDate)) { return true; }
      }
      // true if endDate after startDate
      if (endDate.after(startDate)) { return true; }
      return false;
  }
}
```
