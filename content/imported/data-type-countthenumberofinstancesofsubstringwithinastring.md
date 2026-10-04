---
title: Count the number of instances of substring within a string
nav: Count the number of instan...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1473
source: https://web.archive.org/web/20140829081737/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Countthenumberofinstancesofsubstringwithinastring.htm
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
  /////////////////////////////////////////////////////////////////////////
  //                          Counting Methods                           //
  /////////////////////////////////////////////////////////////////////////
  /**
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

| 2.34.1. | Get the difference between two strings |
|---|---|
| 2.34.2. | Gets a substring from the specified String avoiding exceptions. |
| 2.34.3. | Gets len characters from the middle of a String. |
| 2.34.4. | Gets the String that is nested in between two Strings. Only the first match is returned. |
| 2.34.5. | Gets the String that is nested in between two instances of the same String. |
| 2.34.6. | Gets the leftmost len characters of a String |
| 2.34.7. | Gets the rightmost len characters of a String. |
| 2.34.8. | Gets the substring after the first occurrence of a separator. The separator is not returned. |
| 2.34.9. | Gets the substring before the last occurrence of a separator. The separator is not returned. |
| 2.34.10. | Removes a substring only if it is at the begining of a source string, otherwise returns the source string. |
| 2.34.11. | Removes a substring only if it is at the end of a source string, otherwise returns the source string. |
| 2.34.12. | Substitute sub-strings in side of a string |
| 2.34.13. | Searches a String for substrings delimited by a start and end tag, returning all matching substrings in an array. |
| 2.34.14. | Counts how many times the substring appears in the larger String. |
| 2.34.15. | Count the number of instances of substring within a string |
