---
title: Put quotes around the given String if necessary.
nav: Put quotes around the give...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/PutquotesaroundthegivenStringifnecessary.htm
---
```java title=Example.java
import java.io.File;
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *@author <a href="mailto:siegfried.goeschl@it20one.at">Siegfried Goeschl</a>
 */publicclass Main {
  privatestaticfinal String SINGLE_QUOTE = "\'";
  privatestaticfinal String DOUBLE_QUOTE = "\"";
  privatestaticfinalchar SLASH_CHAR = '/';
  privatestaticfinalchar BACKSLASH_CHAR = '\\';
  /**
   *
   * If the argument doesn't include spaces or quotes, return it as is. If it
   * contains double quotes, use single quotes - else surround the argument by
   * double quotes.
   *
   *
   * @param argument the argument to be quoted
   * @return the quoted argument
   * @throws IllegalArgumentException If argument contains both types of quotes
   */publicstatic String quoteArgument(final String argument) {
      String cleanedArgument = argument.trim();
      while(cleanedArgument.startsWith(SINGLE_QUOTE) || cleanedArgument.startsWith(DOUBLE_QUOTE)) {
          cleanedArgument = cleanedArgument.substring(1);
      }
      while(cleanedArgument.endsWith(SINGLE_QUOTE) || cleanedArgument.endsWith(DOUBLE_QUOTE)) {
          cleanedArgument = cleanedArgument.substring(0, cleanedArgument.length() - 1);
      }
      final StringBuffer buf = new StringBuffer();
      if (cleanedArgument.indexOf(DOUBLE_QUOTE) > -1) {
          if (cleanedArgument.indexOf(SINGLE_QUOTE) > -1) {
              thrownew IllegalArgumentException(
                      "Can't handle single and double quotes in same argument");
          } else {
              return buf.append(SINGLE_QUOTE).append(cleanedArgument).append(
                      SINGLE_QUOTE).toString();
          }
      } elseif (cleanedArgument.indexOf(SINGLE_QUOTE) > -1
              || cleanedArgument.indexOf(" ") > -1) {
          return buf.append(DOUBLE_QUOTE).append(cleanedArgument).append(
                  DOUBLE_QUOTE).toString();
      } else {
          return cleanedArgument;
      }
  }
}
```
