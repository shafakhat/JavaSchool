---
title: Removes spaces (char <= 32) from end of this String, handling null by returning null
nav: Removes spaces (char <= 32...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Removesspacescharlt32fromendofthisStringhandlingnullbyreturningnull.htm
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
 *//**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */publicclass Main {
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
   * @param str
   *            the String to be trimmed, may be null
   * @return the trimmed string, <code>null</code> if null String input
   */publicstaticfinal String trimRight( String str )
  {
      if ( isEmpty( str ) )
      {
          return"";
      }
      int length = str.length();
      int end = length;
      while ( ( end > 0 ) && ( str.charAt( end - 1 ) == ' ' ) )
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
   * Removes spaces (char &lt;= 32) from start of this String, handling
   * <code>null</code> by returning <code>null</code>.
   *
   * Trim removes start characters &lt;= 32.
   *
   * <pre>
   *  StringUtils.trimLeft(null)          = null
   *  StringUtils.trimLeft(&quot;&quot;)            = &quot;&quot;
   *  StringUtils.trimLeft(&quot;     &quot;)       = &quot;&quot;
   *  StringUtils.trimLeft(&quot;abc&quot;)         = &quot;abc&quot;
   *  StringUtils.trimLeft(&quot;    abc    &quot;) = &quot;abc    &quot;
   * </pre>
   *
   * @param str
   *            the String to be trimmed, may be null
   * @return the trimmed string, <code>null</code> if null String input
   */publicstaticfinal String trimLeft( String str )
  {
      if ( isEmpty( str ) )
      {
          return"";
      }
      int start = 0;
      int end = str.length();
      while ( ( start < end ) && ( str.charAt( start ) == ' ' ) )
      {
          start++;
      }
      return ( start == 0 ? str : str.substring( start ) );
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
   */publicstaticfinalboolean isEmpty( String str )
  {
      return str == null || str.length() == 0;
  }
}
```
