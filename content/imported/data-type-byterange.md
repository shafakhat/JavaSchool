---
title: Byte Range
nav: Byte Range
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1345
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ByteRange.htm
---
```java title=Example.java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *//**
 * @version $Id: ByteRange.java 587751 2007-10-24 02:41:36Z vgritsenko $
 */final public class ByteRange {
    private final long start;
    private final long end;
    public ByteRange(long start, long end) {
        this.start = start;
        this.end = end;
    }
    public ByteRange(String string) throws NumberFormatException {
        string = string.trim();
        int dashPos = string.indexOf('-');
        int length = string.length();
        if (string.indexOf(',') != -1) {
            throw new NumberFormatException("Simple ByteRange String contains a comma.");
        }
        if (dashPos > 0) {
            this.start = Integer.parseInt(string.substring(0, dashPos));
        } else {
            this.start = Long.MIN_VALUE;
        }
        if (dashPos < length - 1) {
            this.end = Integer.parseInt(string.substring(dashPos + 1, length));
        } else {
            this.end = Long.MAX_VALUE;
        }
        if (this.start > this.end) {
            throw new NumberFormatException("Start value is greater than end value.");
        }
    }
    public long getStart() {
        return this.start;
    }
    public long getEnd() {
        return this.end;
    }
    public long length() {
        return this.end - this.start + 1;
    }
    public ByteRange intersection(ByteRange range) {
        if (range.end < this.start || this.end < range.start) {
            return null;
        } else {
            long start = (this.start > range.start) ? this.start : range.start;
            long end = (this.end < range.end) ? this.end : range.end;
            return new ByteRange(start, end);
        }
    }
    public String toString() {
        return this.start + "-" + this.end;
    }
}
```

| 2.4.1. | Java byte: byte is smallest Java integer type.byte is 8 bit signed type ranges from –128 to 127. |
|---|---|
| 2.4.2. | Using byte data type |
| 2.4.3. | Convert byte to String: Using the static toString method of the Byte class |
| 2.4.4. | Convert byte to String: Using simple concatenation with an empty String |
| 2.4.5. | Convert byte to String: Creating a byte array and passing it to the String constructor |
| 2.4.6. | Convert String to byte |
| 2.4.7. | Use toString method of Byte class to convert Byte into String |
| 2.4.8. | Use Byte constructor to convert byte primitive type to Byte object |
| 2.4.9. | Compare Two Java byte Arrays Example |
| 2.4.10. | Convert an UNSIGNED byte to a JAVA type |
| 2.4.11. | To convert a byte to it's hexadecimal equivalent |
| 2.4.12. | byte Array To Hex String |
| 2.4.13. | hex String To Byte Array |
| 2.4.14. | Convert byte[ ] array to String |
| 2.4.15. | Convert String to byte array |
| 2.4.16. | Convert Byte to numeric primitive data types example |
| 2.4.17. | Min and Max values of datatype byte |
| 2.4.18. | Byte Range |
