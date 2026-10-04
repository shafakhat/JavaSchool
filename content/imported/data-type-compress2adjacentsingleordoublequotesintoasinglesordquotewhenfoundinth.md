---
title: Compress 2 adjacent (single or double) quotes into a single (s or d) quote when found in the middle of a String.
nav: Compress 2 adjacent (singl...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20100831125911/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Compress2adjacentsingleordoublequotesintoasinglesordquotewhenfoundinthemiddleofaString.htm
---
```java title=Example.java
import java.io.IOException;
import java.io.InputStream;
import java.util.Enumeration;
import java.util.Properties;
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
   * Compress 2 adjacent (single or double) quotes into a single (s or d)
   * quote when found in the middle of a String.
   *
   * NOTE:  """" or '''' will be compressed into "" or ''.
   * This function assumes that the leading and trailing quote from a
   * string or delimited identifier have already been removed.
   * @param source string to be compressed
   * @param quotes string containing two single or double quotes.
   * @return String where quotes have been compressed
   */
  public static String compressQuotes(String source, String quotes)
  {
    String  result = source;
    int   index;
    /* Find the first occurrence of adjacent quotes. */
    index = result.indexOf(quotes);
    /* Replace each occurrence with a single quote and begin the
     * search for the next occurrence from where we left off.
     */
    while (index != -1) {
      result = result.substring(0, index + 1) +
           result.substring(index + 2);
      index = result.indexOf(quotes, index + 1);
    }
    return result;
  }
}
```
