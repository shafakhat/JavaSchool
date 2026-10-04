---
title: Convert a byte array to a String with a hexidecimal format.
nav: Convert a byte array to a ...
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertabytearraytoaStringwithahexidecimalformat.htm
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
  Convert a byte array to a String with a hexidecimal format.
  The String may be converted back to a byte array using fromHexString.
  <BR>
  For each byte (b) two characaters are generated, the first character
  represents the high nibble (4 bits) in hexidecimal (<code>b & 0xf0</code>), the second character
  represents the low nibble (<code>b & 0x0f</code>).
  <BR>
  The byte at <code>data[offset]</code> is represented by the first two characters in the returned String.

  @param  data  byte array
  @param  offset  starting byte (zero based) to convert.
  @param  length  number of bytes to convert.

  @return the String (with hexidecimal format) form of the byte array
*/publicstatic String toHexString(byte[] data, int offset, int length)
{
  StringBuffer s = new StringBuffer(length*2);
  int end = offset+length;

  for (int i = offset; i < end; i++)
  {
    int high_nibble = (data[i] & 0xf0) >>> 4;
    int low_nibble = (data[i] & 0x0f);
    s.append(hex_table[high_nibble]);
    s.append(hex_table[low_nibble]);
  }

  return s.toString();
}

}
```
