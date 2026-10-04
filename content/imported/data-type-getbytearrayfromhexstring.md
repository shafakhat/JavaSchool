---
title: Get byte array from hex string
nav: Get byte array from hex st...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getbytearrayfromhexstring.htm
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
 */public class Main {
  /** lowerCase = 'a' .. 'z', '0'..'9', '-' */ private static final char[] LOWER_CASE =
      {
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0, '-',   0,   0,
          '0', '1', '2', '3', '4', '5', '6', '7',
          '8', '9',   0,   0,   0,   0,   0,   0,
            0, 'a', 'b', 'c', 'd', 'e', 'f', 'g',
          'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
          'x', 'y', 'z',   0,   0,   0,   0,   0,
            0, 'a', 'b', 'c', 'd', 'e', 'f', 'g',
          'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
          'x', 'y', 'z',   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0,
            0,   0,   0,   0,   0,   0,   0,   0
      };
  /**
   *
   * @param hexString
   *            the hex string to convert to a byte array
   * @return the byte form of the hex string.
   */ public static final byte[] toByteArray( String hexString )
  {
      int arrLength = hexString.length() >> 1;
      byte buf[] = new byte[arrLength];
      for ( int ii = 0; ii < arrLength; ii++ )
      {
          int index = ii << 1;
          String l_digit = hexString.substring( index, index + 2 );
          buf[ii] = ( byte ) Integer.parseInt( l_digit, 16 );
      }
      return buf;
  }
}
```
