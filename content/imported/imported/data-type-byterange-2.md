---
title: Byte Range
nav: Byte Range
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ByteRange.htm
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
 */finalpublicclass ByteRange {

    privatefinallong start;
    privatefinallong end;

    public ByteRange(long start, long end) {
        this.start = start;
        this.end = end;
    }

    public ByteRange(String string) throws NumberFormatException {
        string = string.trim();
        int dashPos = string.indexOf('-');
        int length = string.length();
        if (string.indexOf(',') != -1) {
            thrownew NumberFormatException("Simple ByteRange String contains a comma.");
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
            thrownew NumberFormatException("Start value is greater than end value.");
        }
    }

    publiclong getStart() {
        return this.start;
    }

    publiclong getEnd() {
        return this.end;
    }

    publiclong length() {
        return this.end - this.start + 1;
    }

    public ByteRange intersection(ByteRange range) {
        if (range.end < this.start || this.end < range.start) {
            return null;
        } else {
            long start = (this.start > range.start) ? this.start : range.start;
            long end = (this.end < range.end) ? this.end : range.end;
            returnnew ByteRange(start, end);
        }
    }

    public String toString() {
        return this.start + "-" + this.end;
    }

}
```
