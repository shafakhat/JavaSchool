---
title: Split up a string into multiple strings based on a delimiter
nav: Split up a string into mul...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1143
source: https://web.archive.org/web/20140829090417/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Splitupastringintomultiplestringsbasedonadelimiter.htm
---
```java title=Example.java
/*
  * JBoss, Home of Professional Open Source
  * Copyright 2005, JBoss Inc., and individual contributors as indicated
  * by the @authors tag. See the copyright.txt in the distribution for a
  * full listing of individual contributors.
  *
  * This is free software; you can redistribute it and/or modify it
  * under the terms of the GNU Lesser General Public License as
  * published by the Free Software Foundation; either version 2.1 of
  * the License, or (at your option) any later version.
  *
  * This software is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  * Lesser General Public License for more details.
  *
  * You should have received a copy of the GNU Lesser General Public
  * License along with this software; if not, write to the Free
  * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
  * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
  */
public class Main{
  /** An empty string constant */
  public static final String EMPTY = "";
  /////////////////////////////////////////////////////////////////////////
  //                           Spliting Methods                          //
  /////////////////////////////////////////////////////////////////////////
  /**
   *
   * @param string  String to split up.
   * @param delim   Delimiter.
   * @param limit   Limit the number of strings to split into
   *                (-1 for no limit).
   * @return        Array of strings.
   */
  public static String[] split(final String string, final String delim,
     final int limit)
  {
     // get the count of delim in string, if count is > limit
     // then use limit for count.  The number of delimiters is less by one
     // than the number of elements, so add one to count.
     int count = count(string, delim) + 1;
     if (limit > 0 && count > limit)
     {
        count = limit;
     }
     String strings[] = new String[count];
     int begin = 0;
     for (int i = 0; i < count; i++)
     {
        // get the next index of delim
        int end = string.indexOf(delim, begin);
        // if the end index is -1 or if this is the last element
        // then use the string's length for the end index
        if (end == -1 || i + 1 == count)
           end = string.length();
        // if end is 0, then the first element is empty
        if (end == 0)
           strings[i] = EMPTY;
        else
           strings[i] = string.substring(begin, end);
        // update the begining index
        begin = end + 1;
     }
     return strings;
  }
  /**
   *
   * @param string  String to split up.
   * @param delim   Delimiter.
   * @return        Array of strings.
   */
  public static String[] split(final String string, final String delim)
  {
     return split(string, delim, -1);
  }
  /////////////////////////////////////////////////////////////////////////
  //                          Counting Methods                           //
  /////////////////////////////////////////////////////////////////////////
  /**
   * Count the number of instances of substring within a string.
   *
   * @param string     String to look for substring in.
   * @param substring  Sub-string to look for.
   * @return           Count of substrings in string.
   */
  public static int count(final String string, final String substring)
  {
     int count = 0;
     int idx = 0;
     while ((idx = string.indexOf(substring, idx)) != -1)
     {
        idx++;
        count++;
     }
     return count;
  }
  /**
   * Count the number of instances of character within a string.
   *
   * @param string     String to look for substring in.
   * @param c          Character to look for.
   * @return           Count of substrings in string.
   */
  public static int count(final String string, final char c)
  {
     return count(string, String.valueOf(c));
  }
}
```
