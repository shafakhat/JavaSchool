---
title: Trim off trailing blanks but not leading blanks
nav: Trim off trailing blanks b...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1008
source: https://web.archive.org/web/20100412211334/http://java2s.com:80/Tutorial/Java/0040__Data-Type/Trimofftrailingblanksbutnotleadingblanks.htm
---
```java title=Example.java
/*
 Derby - Class org.apache.derby.iapi.util.PropertyUtil
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to you under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */
public class Main {
  /**
   * Trim off trailing blanks but not leading blanks
   *
   * @param str
   *
   * @return The input with trailing blanks stipped off
   */
  public static String trimTrailing( String str)
  {
      if( str == null)
          return null;
      int len = str.length();
      for( ; len > 0; len--)
      {
          if( ! Character.isWhitespace( str.charAt( len - 1)))
              break;
      }
      return str.substring( 0, len);
  } // end of trimTrailing
}
```
