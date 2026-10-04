---
title: ASCII character handling functions
nav: ASCII character handling f...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1294
source: https://web.archive.org/web/20140829083102/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ASCIIcharacterhandlingfunctions.htm
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
 */
/**
 * This class implements some basic ASCII character handling functions.
 *
 * @author dac@eng.sun.com
 * @author James Todd [gonzo@eng.sun.com]
 */
public final class Ascii {
    /*
     * Character translation tables.
     */
    private static final byte[] toUpper = new byte[256];
    private static final byte[] toLower = new byte[256];
    /*
     * Character type tables.
     */
    private static final boolean[] isAlpha = new boolean[256];
    private static final boolean[] isUpper = new boolean[256];
    private static final boolean[] isLower = new boolean[256];
    private static final boolean[] isWhite = new boolean[256];
    private static final boolean[] isDigit = new boolean[256];
    /*
     * Initialize character translation and type tables.
     */
    static {
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
     */
    public static int toUpper(int c) {
        return toUpper[c & 0xff] & 0xff;
    }
    /**
     * Returns the lower case equivalent of the specified ASCII character.
     */
    public static int toLower(int c) {
        return toLower[c & 0xff] & 0xff;
    }
    /**
     * Returns true if the specified ASCII character is upper or lower case.
     */
    public static boolean isAlpha(int c) {
        return isAlpha[c & 0xff];
    }
    /**
     * Returns true if the specified ASCII character is upper case.
     */
    public static boolean isUpper(int c) {
        return isUpper[c & 0xff];
    }
    /**
     * Returns true if the specified ASCII character is lower case.
     */
    public static boolean isLower(int c) {
        return isLower[c & 0xff];
    }
    /**
     * Returns true if the specified ASCII character is white space.
     */
    public static boolean isWhite(int c) {
        return isWhite[c & 0xff];
    }
    /**
     * Returns true if the specified ASCII character is a digit.
     */
    public static boolean isDigit(int c) {
        return isDigit[c & 0xff];
    }
    /**
     * Parses an unsigned integer from the specified subarray of bytes.
     * @param b the bytes to parse
     * @param off the start offset of the bytes
     * @param len the length of the bytes
     * @exception NumberFormatException if the integer format was invalid
     */
    public static int parseInt(byte[] b, int off, int len)
        throws NumberFormatException
    {
        int c;
        if (b == null || len <= 0 || !isDigit(c = b[off++])) {
            throw new NumberFormatException();
        }
        int n = c - '0';
        while (--len > 0) {
            if (!isDigit(c = b[off++])) {
                throw new NumberFormatException();
            }
            n = n * 10 + c - '0';
        }
        return n;
    }
    public static int parseInt(char[] b, int off, int len)
        throws NumberFormatException
    {
        int c;
        if (b == null || len <= 0 || !isDigit(c = b[off++])) {
            throw new NumberFormatException();
        }
        int n = c - '0';
        while (--len > 0) {
            if (!isDigit(c = b[off++])) {
                throw new NumberFormatException();
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
     */
    public static long parseLong(byte[] b, int off, int len)
        throws NumberFormatException
    {
        int c;
        if (b == null || len <= 0 || !isDigit(c = b[off++])) {
            throw new NumberFormatException();
        }
        long n = c - '0';
        long m;
        while (--len > 0) {
            if (!isDigit(c = b[off++])) {
                throw new NumberFormatException();
            }
            m = n * 10 + c - '0';
            if (m < n) {
                // Overflow
                throw new NumberFormatException();
            } else {
                n = m;
            }
        }
        return n;
    }
    public static long parseLong(char[] b, int off, int len)
        throws NumberFormatException
    {
        int c;
        if (b == null || len <= 0 || !isDigit(c = b[off++])) {
            throw new NumberFormatException();
        }
        long n = c - '0';
        long m;
        while (--len > 0) {
            if (!isDigit(c = b[off++])) {
                throw new NumberFormatException();
            }
            m = n * 10 + c - '0';
            if (m < n) {
                // Overflow
                throw new NumberFormatException();
            } else {
                n = m;
            }
        }
        return n;
    }
}
```

| 2.7.1. | Java char: char is 16 bit type and used to represent Unicode characters. Range of char is 0 to 65,536. |
|---|---|
| 2.7.2. | Escape Sequence Characters |
| 2.7.3. | Storing Characters |
| 2.7.4. | Assign int value to char variable |
| 2.7.5. | char variables behave like integers |
| 2.7.6. | Display printable Characters |
| 2.7.7. | Character: is Upper Case |
| 2.7.8. | Character: is Lower Case |
| 2.7.9. | isDigit(): true if the argument is a digit (0 to 9), and false otherwise. |
| 2.7.10. | Validate if a String contains only numbers |
| 2.7.11. | isLetter(): true if the argument is a letter, and false otherwise. |
| 2.7.12. | Count letters in a String |
| 2.7.13. | isLetterOrDigit(): true if the argument is a letter or a digit, and false otherwise. |
| 2.7.14. | is White space |
| 2.7.15. | Is character a digit, letter, white space, lower case or upper case character |
| 2.7.16. | Convert character to digit with Character.digit |
| 2.7.17. | Demonstrate several Is... methods. |
| 2.7.18. | Convert from ASCII code to String |
| 2.7.19. | Convert from integer to ASCII code (byte) |
| 2.7.20. | To extract Ascii codes from a String |
| 2.7.21. | Copy char array to string |
| 2.7.22. | Store unicode in a char variable |
| 2.7.23. | Determining a Character's Unicode Block |
| 2.7.24. | Plus one to char variable |
| 2.7.25. | Convert string to char array |
| 2.7.26. | Compare Two Java char Arrays |
| 2.7.27. | Max and Min values of datatype char |
| 2.7.28. | Determining If a String Is a Legal Java Identifier |
| 2.7.29. | compare two objects of Character |
| 2.7.30. | ASCII character handling functions |
| 2.7.31. | Checks if the string contains only ASCII printable characters. |
| 2.7.32. | Checks whether the character is ASCII 7 bit alphabetic lower case. |
| 2.7.33. | Checks whether the character is ASCII 7 bit alphabetic upper case. |
| 2.7.34. | Checks whether the character is ASCII 7 bit alphabetic. |
| 2.7.35. | Checks whether the character is ASCII 7 bit control. |
| 2.7.36. | Checks whether the character is ASCII 7 bit numeric and character. |
| 2.7.37. | Checks whether the character is ASCII 7 bit numeric. |
| 2.7.38. | Checks whether the character is ASCII 7 bit printable. |
| 2.7.39. | Checks whether the character is ASCII 7 bit. |
| 2.7.40. | Determines if the specified string is permissible as a Java identifier. |
| 2.7.41. | Thansform an array of ASCII bytes to a string. the byte array should contains only values in [0, 127]. |
| 2.7.42. | Utility methods for ASCII character checking. |
