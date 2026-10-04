---
title: Splits the provided text into an array, using whitespace as the separator, preserving all tokens, including empty tokens created by adjacent separators.
nav: Splits the provided text i...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1147
source: https://web.archive.org/web/20140829090202/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Splitstheprovidedtextintoanarrayusingwhitespaceastheseparatorpreservingalltokensincludingemptytokenscreatedbyadjacentseparators.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.util.ArrayList;
import java.util.List;
public class Main {
  // -----------------------------------------------------------------------
  /**
   * Splits the provided text into an array, using whitespace as the
   * separator, preserving all tokens, including empty tokens created by
   * adjacent separators. This is an alternative to using StringTokenizer.
   * Whitespace is defined by {@link Character#isWhitespace(char)}.
   *
   * The separator is not included in the returned String array.
   * Adjacent separators are treated as separators for empty tokens.
   * For more control over the split use the StrTokenizer class.
   *
   * A <code>null</code> input String returns <code>null</code>.
   *
   * <pre>
   * StringUtils.splitPreserveAllTokens(null)       = null
   * StringUtils.splitPreserveAllTokens("")         = []
   * StringUtils.splitPreserveAllTokens("abc def")  = ["abc", "def"]
   * StringUtils.splitPreserveAllTokens("abc  def") = ["abc", "", "def"]
   * StringUtils.splitPreserveAllTokens(" abc ")    = ["", "abc", ""]
   * </pre>
   *
   * @param str  the String to parse, may be <code>null</code>
   * @return an array of parsed Strings, <code>null</code> if null String input
   * @since 2.1
   */
  public static String[] splitPreserveAllTokens(String str) {
      return splitWorker(str, null, -1, true);
  }
  /**
   * Performs the logic for the <code>split</code> and
   * <code>splitPreserveAllTokens</code> methods that return a maximum array
   * length.
   *
   * @param str  the String to parse, may be <code>null</code>
   * @param separatorChars the separate character
   * @param max  the maximum number of elements to include in the
   *  array. A zero or negative value implies no limit.
   * @param preserveAllTokens if <code>true</code>, adjacent separators are
   * treated as empty token separators; if <code>false</code>, adjacent
   * separators are treated as one separator.
   * @return an array of parsed Strings, <code>null</code> if null String input
   */
  private static String[] splitWorker(String str, String separatorChars, int max, boolean preserveAllTokens) {
      // Performance tuned for 2.0 (JDK1.4)
      // Direct code is quicker than StringTokenizer.
      // Also, StringTokenizer uses isSpace() not isWhitespace()
      if (str == null) {
          return null;
      }
      int len = str.length();
      if (len == 0) {
          return new String[0];
      }
      List list = new ArrayList();
      int sizePlus1 = 1;
      int i = 0, start = 0;
      boolean match = false;
      boolean lastMatch = false;
      if (separatorChars == null) {
          // Null separator means use whitespace
          while (i < len) {
              if (Character.isWhitespace(str.charAt(i))) {
                  if (match || preserveAllTokens) {
                      lastMatch = true;
                      if (sizePlus1++ == max) {
                          i = len;
                          lastMatch = false;
                      }
                      list.add(str.substring(start, i));
                      match = false;
                  }
                  start = ++i;
                  continue;
              }
              lastMatch = false;
              match = true;
              i++;
          }
      } else if (separatorChars.length() == 1) {
          // Optimise 1 character case
          char sep = separatorChars.charAt(0);
          while (i < len) {
              if (str.charAt(i) == sep) {
                  if (match || preserveAllTokens) {
                      lastMatch = true;
                      if (sizePlus1++ == max) {
                          i = len;
                          lastMatch = false;
                      }
                      list.add(str.substring(start, i));
                      match = false;
                  }
                  start = ++i;
                  continue;
              }
              lastMatch = false;
              match = true;
              i++;
          }
      } else {
          // standard case
          while (i < len) {
              if (separatorChars.indexOf(str.charAt(i)) >= 0) {
                  if (match || preserveAllTokens) {
                      lastMatch = true;
                      if (sizePlus1++ == max) {
                          i = len;
                          lastMatch = false;
                      }
                      list.add(str.substring(start, i));
                      match = false;
                  }
                  start = ++i;
                  continue;
              }
              lastMatch = false;
              match = true;
              i++;
          }
      }
      if (match || (preserveAllTokens && lastMatch)) {
          list.add(str.substring(start, i));
      }
      return (String[]) list.toArray(new String[list.size()]);
  }
}
```
