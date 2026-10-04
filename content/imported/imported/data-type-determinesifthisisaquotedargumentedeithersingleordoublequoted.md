---
title: Determines if this is a quoted argumented - either single or double quoted.
nav: Determines if this is a qu...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1086
source: https://web.archive.org/web/20111105131245/http://java2s.com/Tutorial/Java/0040__Data-Type/Determinesifthisisaquotedargumentedeithersingleordoublequoted.htm
---
```java title=Example.java
import java.io.File;
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *@author <a href="mailto:siegfried.goeschl@it20one.at">Siegfried Goeschl</a>
 */
public class Main {
  private static final String SINGLE_QUOTE = "\'";
  private static final String DOUBLE_QUOTE = "\"";
  private static final char SLASH_CHAR = '/';
  private static final char BACKSLASH_CHAR = '\\';
  /**
   * Determines if this is a quoted argumented - either single or
   * double quoted.
   *
   * @param argument the argument to check
   * @return true when the argument is quoted
   */
  public static boolean isQuoted(final String argument) {
      return ( argument.startsWith( SINGLE_QUOTE ) || argument.startsWith( DOUBLE_QUOTE ) ) &&
          ( argument.endsWith( SINGLE_QUOTE ) || argument.endsWith( DOUBLE_QUOTE ) );
  }
}
```
