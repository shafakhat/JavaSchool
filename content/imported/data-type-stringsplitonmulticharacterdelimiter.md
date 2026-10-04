---
title: String split on multicharacter delimiter
nav: String split on multichara...
description: /**************************************************************************************
section: Imported - java2s Archive
order: 1160
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Stringsplitonmulticharacterdelimiter.htm
---
```java title=Example.java
/**************************************************************************************
 * Copyright (c) Jonas Bonr, Alexandre Vasseur. All rights reserved.                 *
 * http://aspectwerkz.codehaus.org                                                    *
 * ---------------------------------------------------------------------------------- *
 * The software in this package is published under the terms of the LGPL license      *
 * a copy of which has been included with this distribution in the license.txt file.  *
 **************************************************************************************/import java.util.List;
import java.util.ArrayList;
/**
 * Utility methods for strings.
 *
 * @author <a href="mailto:jboner@codehaus.org">Jonas Bonr </a>
 */public class Strings {
  /**
   * String split on multicharacter delimiter. <p/>Written by Tim Quinn (tim.quinn@honeywell.com)
   *
   * @param stringToSplit
   * @param delimiter
   * @return
   */ public static final String[] splitString(String stringToSplit, String delimiter) {
      String[] aRet;
      int iLast;
      int iFrom;
      int iFound;
      int iRecords;
      // return Blank Array if stringToSplit == "")
 if (stringToSplit.equals("")) {
          return new String[0];
      }
      // count Field Entries
      iFrom = 0;
      iRecords = 0;
      while (true) {
          iFound = stringToSplit.indexOf(delimiter, iFrom);
          if (iFound == -1) {
              break;
          }
          iRecords++;
          iFrom = iFound + delimiter.length();
      }
      iRecords = iRecords + 1;
      // populate aRet[]
      aRet = new String[iRecords];
      if (iRecords == 1) {
          aRet[0] = stringToSplit;
      } else {
          iLast = 0;
          iFrom = 0;
          iFound = 0;
          for (int i = 0; i < iRecords; i++) {
              iFound = stringToSplit.indexOf(delimiter, iFrom);
              if (iFound == -1) { // at End
                  aRet[i] = stringToSplit.substring(iLast + delimiter.length(), stringToSplit.length());
              } else if (iFound == 0) { // at Beginning
                  aRet[i] = "";
              } else { // somewhere in middle
                  aRet[i] = stringToSplit.substring(iFrom, iFound);
              }
              iLast = iFound;
              iFrom = iFound + delimiter.length();
          }
      }
      return aRet;
  }
}
```
