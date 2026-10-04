---
title: Thansform an array of ASCII bytes to a string. the byte array should contains only values in [0, 127].
nav: Thansform an array of ASCI...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ThansformanarrayofASCIIbytestoastringthebytearrayshouldcontainsonlyvaluesin0127.htm
---
```java title=Example.java
import java.io.UnsupportedEncodingException;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
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
   * Thansform an array of ASCII bytes to a string. the byte array should contains
   * only values in [0, 127].
   *
   * @param bytes The byte array to transform
   * @return The resulting string
   */publicstatic String asciiBytesToString( byte[] bytes )
  {
      if ( (bytes == null) || (bytes.length == 0 ) )
      {
          return"";
      }
      char[] result = newchar[bytes.length];
      for ( int i = 0; i < bytes.length; i++ )
      {
          result[i] = (char)bytes[i];
      }
      returnnew String( result );
  }
}
```
