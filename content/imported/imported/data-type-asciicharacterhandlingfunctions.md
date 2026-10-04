---
title: ASCII character handling functions
nav: ASCII character handling f...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ASCIIcharacterhandlingfunctions.htm
---
```java title=Example.java
/*
 *  Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *//**
 * This class implements some basic ASCII character handling functions.
 *
 * @author dac@eng.sun.com
 * @author James Todd [gonzo@eng.sun.com]
 */publicfinalclass Ascii {
    /*
     * Character translation tables.
     */privatestaticfinalbyte[] toUpper = newbyte[256];
    privatestaticfinalbyte[] toLower = newbyte[256];

    /*
     * Character type tables.
     */privatestaticfinalboolean[] isAlpha = newboolean[256];
    privatestaticfinalboolean[] isUpper = newboolean[256];
    privatestaticfinalboolean[] isLower = newboolean[256];
    privatestaticfinalboolean[] isWhite = newboolean[256];
    privatestaticfinalboolean[] isDigit = newboolean[256];

    /*
     * Initialize character translation and type tables.
     */static {
        for (int i = 0; i < 256; i++) {
            toUpper[i] = (byte)i;
            toLower[i] = (byte)i;
        }

        for (int lc = 'a'; lc <= 'z'; lc++) {
            int uc = lc + 'A' - 'a';

            toUpper[lc] = (byte)uc;
            toLower[uc] = (byte)lc;
            isAlpha[lc] = true;
            isAlpha[uc] = true;
            isLower[lc] = true;
            isUpper[uc] = true;
        }

        isWhite[ ' '] = true;
        isWhite['\t'] = true;
        isWhite['\r'] = true;
        isWhite['\n'] = true;
        isWhite['\f'] = true;
        isWhite['\b'] = true;

        for (int d = '0'; d <= '9'; d++) {
            isDigit[d] = true;
        }
    }

    /**
     * Returns the upper case equivalent of the specified ASCII character.
     */publicstaticint toUpper(int c) {
        return toUpper[c & 0xff] & 0xff;
    }

    /**
     * Returns the lower case equivalent of the specified ASCII character.
     */publicstaticint toLower(int c) {
        return toLower[c & 0xff] & 0xff;
    }

    /**
     * Returns true if the specified ASCII character is upper or lower case.
     */publicstaticboolean isAlpha(int c) {
        return isAlpha[c & 0xff];
    }

    /**
     * Returns true if the specified ASCII character is upper case.
     */publicstaticboolean isUpper(int c) {
        return isUpper[c & 0xff];
    }

    /**
     * Returns true if the specified ASCII character is lower case.
     */publicstaticboolean isLower(int c) {
        return isLower[c & 0xff];
    }

    /**
     * Returns true if the specified ASCII character is white space.
     */publicstaticboolean isWhite(int c) {
        return isWhite[c & 0xff];
    }

    /**
     * Returns true if the specified ASCII character is a digit.
     */publicstaticboolean isDigit(int c) {
        return isDigit[c & 0xff];
    }

    /**
     * Parses an unsigned integer from the specified subarray of bytes.
     * @param b the bytes to parse
     * @param off the start offset of the bytes
     * @param len the length of the bytes
     * @exception NumberFormatException if the integer format was invalid
     */publicstaticint parseInt(byte[] b, int off, int len)
        throws NumberFormatException
    {
        int c;

        if (b == null || len <= 0 || !isDigit(c = b[off++])) {
            thrownew NumberFormatException();
        }

        int n = c - '0';

        while (--len > 0) {
            if (!isDigit(c = b[off++])) {
                thrownew NumberFormatException();
            }
            n = n * 10 + c - '0';
        }

        return n;
    }

    publicstaticint parseInt(char[] b, int off, int len)
        throws NumberFormatException
    {
        int c;

        if (b == null || len <= 0 || !isDigit(c = b[off++])) {
            thrownew NumberFormatException();
        }

        int n = c - '0';

        while (--len > 0) {
            if (!isDigit(c = b[off++])) {
                thrownew NumberFormatException();
            }
            n = n * 10 + c - '0';
        }

        return n;
    }

    /**
     * Parses an unsigned long from the specified subarray of bytes.
     * @param b the bytes to parse
     * @param off the start offset of the bytes
     * @param len the length of the bytes
     * @exception NumberFormatException if the long format was invalid
     */publicstaticlong parseLong(byte[] b, int off, int len)
        throws NumberFormatException
    {
        int c;

        if (b == null || len <= 0 || !isDigit(c = b[off++])) {
            thrownew NumberFormatException();
        }

        long n = c - '0';
        long m;

        while (--len > 0) {
            if (!isDigit(c = b[off++])) {
                thrownew NumberFormatException();
            }
            m = n * 10 + c - '0';

            if (m < n) {
                // Overflow
thrownew NumberFormatException();
            } else {
                n = m;
            }
        }

        return n;
    }

    publicstaticlong parseLong(char[] b, int off, int len)
        throws NumberFormatException
    {
        int c;

        if (b == null || len <= 0 || !isDigit(c = b[off++])) {
            thrownew NumberFormatException();
        }

        long n = c - '0';
        long m;

        while (--len > 0) {
            if (!isDigit(c = b[off++])) {
                thrownew NumberFormatException();
            }
            m = n * 10 + c - '0';

            if (m < n) {
                // Overflow
thrownew NumberFormatException();
            } else {
                n = m;
            }
        }

        return n;
    }

}
```
