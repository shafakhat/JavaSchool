---
title: Check if a string is present at the current position in another string.
nav: Check if a string is prese...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1168
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Checkifastringispresentatthecurrentpositioninanotherstring.htm
---
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
 *//**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */public class Main {
  /**
   * Check if a text is present at the current position in another string.
   *
   * @param string
   *            The string which contains the data
   * @param index
   *            Current position in the string
   * @param text
   *            The text we want to check
   * @return <code>true</code> if the string contains the text.
   */ public static final boolean areEquals( String string, int index, String text )
  {
      if ( ( string == null ) || ( text == null ) )
      {
          return false;
      }
      int length1 = string.length();
      int length2 = text.length();
      if ( ( length1 == 0 ) || ( length1 <= index ) || ( index < 0 )
          || ( text == null ) || ( length2 == 0 )
          || ( length2 > ( length1 + index ) ) )
      {
          return false;
      }
      else
      {
          return string.substring( index ).startsWith( text );
      }
  }
}
```
