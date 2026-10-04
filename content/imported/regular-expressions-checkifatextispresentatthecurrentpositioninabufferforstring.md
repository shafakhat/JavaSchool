---
title: Check if a text is present at the current position in a buffer for string
nav: Check if a text is present...
description: Check if a text is present at the current position in a buffer for string
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20100213065034/http://java2s.com/Code/Java/Regular-Expressions/Checkifatextispresentatthecurrentpositioninabufferforstring.htm
---
Check if a text is present at the current position in a buffer for string

```java title=Example.java
import java.io.File;
import java.io.FileFilter;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;
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
   * Check if a text is present at the current position in a buffer.
   *
   * @param byteArray
   *            The buffer which contains the data
   * @param index
   *            Current position in the buffer
   * @param text
   *            The text we want to check
   * @return <code>true</code> if the buffer contains the text.
   */
  public static final int areEquals( byte[] byteArray, int index, String text )
  {
      if ( ( byteArray == null ) || ( byteArray.length == 0 ) || ( byteArray.length <= index ) || ( index < 0 )
          || ( text == null ) )
      {
          return -1;
      }
      else
      {
          try
          {
              byte[] data = text.getBytes( "UTF-8" );
              return areEquals( byteArray, index, data );
          }
          catch ( UnsupportedEncodingException uee )
          {
              return -1;
          }
      }
  }
  /**
   * Check if a text is present at the current position in a buffer.
   *
   * @param byteArray
   *            The buffer which contains the data
   * @param index
   *            Current position in the buffer
   * @param byteArray2
   *            The text we want to check
   * @return <code>true</code> if the buffer contains the text.
   */
  public static final int areEquals( byte[] byteArray, int index, byte[] byteArray2 )
  {
      if ( ( byteArray == null ) || ( byteArray.length == 0 ) || ( byteArray.length <= index ) || ( index < 0 )
          || ( byteArray2 == null ) || ( byteArray2.length == 0 )
          || ( byteArray2.length > ( byteArray.length + index ) ) )
      {
          return -1;
      }
      else
      {
          for ( int i = 0; i < byteArray2.length; i++ )
          {
              if ( byteArray[index++] != byteArray2[i] )
              {
                  return -1;
              }
          }
          return index;
      }
  }
}
```

1.  Matcher: Find Demo
---  ---
2.  Matcher Reset
3.  Matcher Pattern
4.  Another Matcher reset
5.  Matcher start
6.  Matcher start with parameter
7.  Matcher end
8.  Matcher end with parameter
9.  Matcher group
10.  Matcher group with parameter
11.  Matcher group count
12.  Matcher match
13.  Matcher find
14.  Matcher find with parameter
15.  Matcher LookingAt
16.  Matcher appendReplacement
17.  Matcher replaceAll
18.  Matcher replaceFirst
19.  Matcher group 2
20.  Matcher group with parameter 2
21.  Matcher ground count
22.  Matcher replaceAll 2
23.  Matcher find group
24.  Another Matcher find and group
25.  Pattern compile
26.  Show line ending matching using Regular Expressions class
27.  Matcher Groups
28.  Matches Looking
29.  Match Name Formats
30.  Checks whether a string matches a given wildcard pattern
31.  Replace all occurances of the target text with the provided replacement text
