---
title: Chop i characters off the end of a string.
nav: Chop i characters off the ...
description: * or more contributor license agreements. See the NOTICE file
section: Imported - java2s Archive
order: 1358
source: https://web.archive.org/web/20140829083121/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Chopicharactersofftheendofastring.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
import java.util.StringTokenizer;
/**
 *
 *  @author <a href="mailto:jvanzyl@apache.org">Jason van Zyl</a>
 *  @author <a href="mailto:dlr@finemaltcoding.com">Daniel Rall</a>
 *  @version $Id: StringUtils.java 685685 2008-08-13 21:43:27Z nbubna $
 */
public class Main {
  /**
   * Line separator for the OS we are operating on.
   */
  private static final String EOL = System.getProperty("line.separator");
  /**
   * This method assumes that any EOL characters in String s
   * and the platform EOL will be the same.
   * A 2 character EOL will count as 1 character.
   *
   * @param s String to chop.
   * @param i Number of characters to chop.
   * @return String with processed answer.
   */
  public static String chop(String s, int i)
  {
      return chop(s, i, EOL);
  }
  /**
   * A 2 character EOL will count as 1 character.
   *
   * @param s String to chop.
   * @param i Number of characters to chop.
   * @param eol A String representing the EOL (end of line).
   * @return String with processed answer.
   */
  public static String chop(String s, int i, String eol)
  {
      if ( i == 0 || s == null || eol == null )
      {
         return s;
      }
      int length = s.length();
      /*
       * if it is a 2 char EOL and the string ends with
       * it, nip it off.  The EOL in this case is treated like 1 character
       */
      if ( eol.length() == 2 && s.endsWith(eol ))
      {
          length -= 2;
          i -= 1;
      }
      if ( i > 0)
      {
          length -= i;
      }
      if ( length < 0)
      {
          length = 0;
      }
      return s.substring( 0, length);
  }
}
```

| 2.20.1. | Checking the Start of a String |
|---|---|
| 2.20.2. | Checking the End of a String |
| 2.20.3. | Accessing String Characters |
| 2.20.4. | Chop i characters off the end of a string. |
| 2.20.5. | Removes separator from the end of str if it's there, otherwise leave it alone. |
| 2.20.6. | Remove the last character from a String. |
