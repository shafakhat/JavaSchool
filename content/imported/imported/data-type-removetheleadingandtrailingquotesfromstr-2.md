---
title: Remove the leading and trailing quotes from str.
nav: Remove the leading and tra...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1177
source: https://web.archive.org/web/20100323054526/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Removetheleadingandtrailingquotesfromstr.htm
---
```java title=Example.java
/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * Contains useful helper methods for classes within this package.
 *
 * @author John Keyes (john at integralsource.com)
 * @version $Revision: 680644 $, $Date: 2008-07-29 01:13:48 -0700 (Tue, 29 Jul 2008) $
 */
public class Main {
  /**
   * Remove the leading and trailing quotes from <code>str</code>.
   * E.g. if str is '"one two"', then 'one two' is returned.
   *
   * @param str The string from which the leading and trailing quotes
   * should be removed.
   *
   * @return The string without the leading and trailing quotes.
   */
  static String stripLeadingAndTrailingQuotes(String str)
  {
      if (str.startsWith("\""))
      {
          str = str.substring(1, str.length());
      }
      if (str.endsWith("\""))
      {
          str = str.substring(0, str.length() - 1);
      }
      return str;
  }
}
```
