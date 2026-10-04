---
title: Gets a hex string from byte array.
nav: Gets a hex string from byt...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Getsahexstringfrombytearray.htm
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
  /**
   *
   * @param res
   *            the byte array
   * @return the hex string representing the binary values in the array
   */ public static final String toHexString( byte[] res )
  {
      StringBuffer buf = new StringBuffer( res.length << 1 );
      for ( int ii = 0; ii < res.length; ii++ )
      {
          String digit = Integer.toHexString( 0xFF & res[ii] );
          if ( digit.length() == 1 )
          {
              digit = '0' + digit;
          }
          buf.append( digit );
      }
      return buf.toString().toUpperCase();
  }
}
```
