---
title: Convert string to uppercase
nav: Convert string to uppercase
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1064
source: https://web.archive.org/web/20100412210109/http://java2s.com:80/Tutorial/Java/0040__Data-Type/Convertstringtouppercase.htm
---
```java title=Example.java
import java.io.IOException;
import java.io.InputStream;
import java.util.Enumeration;
import java.util.Locale;
import java.util.Properties;
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
 */
public class Main {
  /** Convert string to uppercase
   * Always use the java.util.ENGLISH locale
   * @param s   string to uppercase
   * @return uppercased string
   */
  public static String SQLToUpperCase(String s)
  {
      return s.toUpperCase(Locale.ENGLISH);
  }
}
```
