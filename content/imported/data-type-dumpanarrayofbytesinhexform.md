---
title: dump an array of bytes in hex form
nav: dump an array of bytes in ...
description: * Licensed to the Apache Software Foundation (ASF) under one
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/20100706223525/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/dumpanarrayofbytesinhexform.htm
---
```java title=Example.java
import java.io.File;
import java.io.FileFilter;
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
 */
/**
 * Various string manipulation methods that are more efficient then chaining
 * string operations: all is done in the same buffer without creating a bunch of
 * string objects.
 *
 * @author <a href="mailto:dev@labs.apache.org">Dungeon Project</a>
 */
public class Main {
  /** Hex chars */
  private static final byte[] HEX_CHAR = new byte[]
      { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' };
  /**
   * Helper function that dump an array of bytes in hex form
   *
   * @param buffer
   *            The bytes array to dump
   * @return A string representation of the array of bytes
   */
  public static final String dumpBytes( byte[] buffer )
  {
      if ( buffer == null )
      {
          return "";
      }
      StringBuffer sb = new StringBuffer();
      for ( int i = 0; i < buffer.length; i++ )
      {
          sb.append( "0x" ).append( ( char ) ( HEX_CHAR[( buffer[i] & 0x00F0 ) >> 4] ) ).append(
              ( char ) ( HEX_CHAR[buffer[i] & 0x000F] ) ).append( " " );
      }
      return sb.toString();
  }
}
```
