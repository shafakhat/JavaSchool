---
title: Splits a string around matches of the given delimiter character.
nav: Splits a string around mat...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1188
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Splitsastringaroundmatchesofthegivendelimitercharacter.htm
---
```java title=Example.java
import java.util.StringTokenizer;
/*
 Derby - Class org.apache.derby.iapi.util.PropertyUtil
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to you under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */public class Main {
  /**
   *
   * Where applicable, this method can be used as a substitute for
   * <code>String.split(String regex)</code>, which is not available
   * on a JSR169/Java ME platform.
   *
   * @param str the string to be split
   * @param delim the delimiter
   * @throws NullPointerException if str is null
   */ static public String[] split(String str, char delim)
  {
      if (str == null) {
          throw new NullPointerException("str can't be null");
      }
      // Note the javadoc on StringTokenizer:
 //     StringTokenizer is a legacy class that is retained for
 //     compatibility reasons although its use is discouraged in
 //     new code.
 // In other words, if StringTokenizer is ever removed from the JDK,
 // we need to have a look at String.split() (or java.util.regex)
 // if it is supported on a JSR169/Java ME platform by then.
      StringTokenizer st = new StringTokenizer(str, String.valueOf(delim));
      int n = st.countTokens();
      String[] s = new String[n];
      for (int i = 0; i < n; i++) {
          s[i] = st.nextToken();
      }
      return s;
  }
}
```
