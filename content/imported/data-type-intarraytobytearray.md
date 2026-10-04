---
title: int array to byte array
nav: int array to byte array
description: * Permission is hereby granted, free of charge, to any person obtaining a copy of
section: Imported - java2s Archive
order: 1189
source: https://web.archive.org/web/20140829091945/http://www.java2s.com/Tutorial/Java/0040__Data-Type/intarraytobytearray.htm
---
```java title=Example.java
/*
 * Permission is hereby granted, free of charge, to any person obtaining a copy of
 * this software and associated documentation files (the "Software"), to deal in
 * the Software without restriction, including without limitation the rights to
 * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is furnished to do
 * so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
public class ArrayCopy {
  public static byte[] int2byte(int[]src) {
    int srcLength = src.length;
    byte[]dst = new byte[srcLength << 2];
    for (int i=0; i<srcLength; i++) {
        int x = src[i];
        int j = i << 2;
        dst[j++] = (byte) ((x >>> 0) & 0xff);
        dst[j++] = (byte) ((x >>> 8) & 0xff);
        dst[j++] = (byte) ((x >>> 16) & 0xff);
        dst[j++] = (byte) ((x >>> 24) & 0xff);
    }
    return dst;
}
}
```

| 2.3.1. | Integer Data Types in Java: memory and length |
|---|---|
| 2.3.2. | Integer Calculations |
| 2.3.3. | Add two integers, checking for overflow. |
| 2.3.4. | Multiply two integers, checking for overflow. |
| 2.3.5. | Subtract two integers, checking for overflow. |
| 2.3.6. | Binary and Decimal value table |
| 2.3.7. | Min and Max values of datatype int |
| 2.3.8. | Hexadecimal Numbers and its corresponding Decimal and binary value |
| 2.3.9. | Gets the maximum of three int values. |
| 2.3.10. | Gets the minimum of three int values. |
| 2.3.11. | Given an integer, return a string that is in an approximate, but human readable format |
| 2.3.12. | int array to byte array |
