---
title: append hex digit
nav: append hex digit
description: // ------------------------------------------------------------------------
section: Imported - java2s Archive
order: 1143
source: https://web.archive.org/web/20091113022326/http://www.java2s.com:80/Code/Java/Data-Type/appendhexdigit.htm
---
```java title=Example.java
//
// Copyright 2004-2005 Mort Bay Consulting Pty. Ltd.
// ------------------------------------------------------------------------
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// http://www.apache.org/licenses/LICENSE-2.0
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
/**
 * Fast String Utilities.
 *
 * These string utilities provide both conveniance methods and performance
 * improvements over most standard library versions. The main aim of the
 * optimizations is to avoid object creation unless absolutely required.
 *
 * @author Greg Wilkins (gregw)
 */
public class Utils {
  /**
   *
   */
  public static void append(StringBuffer buf, byte b, int base) {
    int bi = 0xff & b;
    int c = '0' + (bi / base) % base;
    if (c > '9')
      c = 'a' + (c - '0' - 10);
    buf.append((char) c);
    c = '0' + bi % base;
    if (c > '9')
      c = 'a' + (c - '0' - 10);
    buf.append((char) c);
  }
  /* ------------------------------------------------------------ */
  public static void append2digits(StringBuffer buf, int i) {
    if (i < 100) {
      buf.append((char) (i / 10 + '0'));
      buf.append((char) (i % 10 + '0'));
    }
  }
}
```

1.  Convert Decimal to Hexadecimal
2.  Convert from decimal to hexadecimal
3.  Convert from Byte array to hexadecimal string
4.  Convert from decimal to hexadecimal with leading zeroes and uppercase
5.  Hex encoder and decoder.
6.  Decode hex string to a byte array
7.  Returns the hexadecimal value of the supplied byte array
8.  Convert byte array to Hex String
9.  Convert the bytes to a hex string representation of the bytes
10.  Hex decimal dump
11.  hex decoder
12.  Get Base64 From HEX
13.  Converts a hex string to a byte array.
14.  dump an array of bytes in hex form
15.  Get byte array from hex string
16.  Check if the current character is an Hex Char <hex> ::= [0x30-0x39]  [0x41-0x46]  [0x61-0x66]
17.  Helper function that returns a char from an hex
18.  Hex encoder/decoder implementation borrowed from BouncyCastle
