---
title: Removes spaces (char <= 32) from end of this String with escape, handling null by returning null
nav: Removes spaces (char <= 32...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1284
source: https://web.archive.org/web/20140828212241/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Removesspacescharlt32fromendofthisStringwithescapehandlingnullbyreturningnull.htm
---
```java title=Example.java
/*
 *  Licensed to the Apache Software Foundation (ASF) under one
 *  or more contributor license agreements.  See the NOTICE file
 *  distributed with this work for additional information
 *  regarding copyright ownership.  The ASF licenses this file
 *  to you under the Apache License, Version 2.0 (the
 *  "License"); you may not use this file except in compliance
 *  with the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an
 *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 *  KIND, either express or implied.  See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 *
 */
/**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */
public class Main {
  /**
   *
   * Removes spaces (char &lt;= 32) from end of this String, handling
   * <code>null</code> by returning <code>null</code>.
   *
   * Trim removes start characters &lt;= 32.
   *
   * <pre>
   *  StringUtils.trimRight(null)          = null
   *  StringUtils.trimRight(&quot;&quot;)            = &quot;&quot;
   *  StringUtils.trimRight(&quot;     &quot;)       = &quot;&quot;
   *  StringUtils.trimRight(&quot;abc&quot;)         = &quot;abc&quot;
   *  StringUtils.trimRight(&quot;    abc    &quot;) = &quot;    abc&quot;
   * </pre>
   *
   * @param str the String to be trimmed, may be null
   * @param escapedSpace The last escaped space, if any
   * @return the trimmed string, <code>null</code> if null String input
   */
  public static final String trimRight( String str, int escapedSpace )
  {
      if ( isEmpty( str ) )
      {
          return "";
      }
      int length = str.length();
      int end = length;
      while ( ( end > 0 ) && ( str.charAt( end - 1 ) == ' ' ) && ( end > escapedSpace ) )
      {
          if ( ( end > 1 ) && ( str.charAt(  end - 2 ) == '\\' ) )
          {
              break;
          }
          end--;
      }
      return ( end == length ? str : str.substring( 0, end ) );
  }
  /**
   *
   * Checks if a String is empty ("") or null.
   *
   *
   * <pre>
   *  StringUtils.isEmpty(null)      = true
   *  StringUtils.isEmpty(&quot;&quot;)        = true
   *  StringUtils.isEmpty(&quot; &quot;)       = false
   *  StringUtils.isEmpty(&quot;bob&quot;)     = false
   *  StringUtils.isEmpty(&quot;  bob  &quot;) = false
   * </pre>
   *
   *
   * NOTE: This method changed in Lang version 2.0. It no longer trims the
   * String. That functionality is available in isBlank().
   *
   *
   * @param str
   *            the String to check, may be null
   * @return <code>true</code> if the String is empty or null
   */
  public static final boolean isEmpty( String str )
  {
      return str == null || str.length() == 0;
  }
}
```

| 2.28.1. | Demonstrates the charAt and getChars |
|---|---|
| 2.28.2. | Converting Char array to String |
| 2.28.3. | Creating Character Arrays From String Objects |
| 2.28.4. | Copy characters from string into char Array |
| 2.28.5. | Creating String Objects From Character Arrays |
| 2.28.6. | new String(textArray, 9, 3): Creating String Objects From certain part of a character Array |
| 2.28.7. | Creating String Objects From Character Arrays using String.copyValueOf() |
| 2.28.8. | Creating a string from a subset of the array elements |
| 2.28.9. | Extracting a substring as an array of characters using the method getChars() |
| 2.28.10. | Using the Collection-Based for Loop with a String: Counting all vowels in a string |
| 2.28.11. | Construct one String from another. |
| 2.28.12. | demonstrates getChars( ): |
| 2.28.13. | implements CharSequence |
| 2.28.14. | Removes spaces (char <= 32) from end of this String with escape, handling null by returning null |
| 2.28.15. | Removes spaces (char <= 32) from end of this String, handling null by returning null |
| 2.28.16. | Swaps the case of a String changing upper and title case to lower case, and lower case to upper case. |
| 2.28.17. | Deletes all whitespaces from a String as defined by Character.isWhitespace(char). |
| 2.28.18. | Checks whether the String contains only digit characters. |
| 2.28.19. | Checks that the String does not contain certain characters. |
