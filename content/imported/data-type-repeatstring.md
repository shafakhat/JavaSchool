---
title: Repeat String
nav: Repeat String
description: * A simple routine which just repeates the arguments. This is useful
section: Imported - java2s Archive
order: 1087
source: https://web.archive.org/web/20100627080007/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/RepeatString.htm
---
```java title=Example.java
/*
    JSPWiki - a JSP-based WikiWiki clone.
    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 */
import java.security.SecureRandom;
import java.util.Random;
public class StringUtils
{
  /**
   *  A simple routine which just repeates the arguments.  This is useful
   *  for creating something like a line or something.
   *
   *  @param what String to repeat
   *  @param times How many times to repeat the string.
   *  @return Guess what?
   *  @since 2.1.98.
   */
  public static String repeatString( String what, int times )
  {
      StringBuffer sb = new StringBuffer();
      for( int i = 0; i < times; i++ )
      {
          sb.append( what );
      }
      return sb.toString();
  }
}
```
