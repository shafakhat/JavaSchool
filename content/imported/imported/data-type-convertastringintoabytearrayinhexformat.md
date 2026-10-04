---
title: Convert a string into a byte array in hex format.
nav: Convert a string into a by...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Convertastringintoabytearrayinhexformat.htm
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

 */publicclass Main {

  privatestaticchar[] hex_table = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f'
};

  /**

      Convert a string into a byte array in hex format.
      <BR>
      For each character (b) two bytes are generated, the first byte
      represents the high nibble (4 bits) in hexidecimal (<code>b & 0xf0</code>),
      the second byte represents the low nibble (<code>b & 0x0f</code>).
      <BR>
      The character at <code>str.charAt(0)</code> is represented by the first two bytes
      in the returned String.

      @param  str string
      @param  offset  starting character (zero based) to convert.
      @param  length  number of characters to convert.

      @return the byte[]  (with hexidecimal format) form of the string (str)
  */publicstaticbyte[] toHexByte(String str, int offset, int length)
  {
      byte[] data = newbyte[(length - offset) * 2];
      int end = offset+length;

      for (int i = offset; i < end; i++)
      {
          char ch = str.charAt(i);
          int high_nibble = (ch & 0xf0) >>> 4;
          int low_nibble = (ch & 0x0f);
          data[i] = (byte)high_nibble;
          data[i+1] = (byte)low_nibble;
      }
      return data;
  }

}
```
