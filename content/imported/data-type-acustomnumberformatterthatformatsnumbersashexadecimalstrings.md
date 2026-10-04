---
title: A custom number formatter that formats numbers as hexadecimal strings.
nav: A custom number formatter ...
description: * JFreeChart : a free chart library for the Java(tm) platform
section: Imported - java2s Archive
order: 1276
source: https://web.archive.org/web/20140829091644/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Acustomnumberformatterthatformatsnumbersashexadecimalstrings.htm
---
```java title=Example.java
/*
 * JFreeChart : a free chart library for the Java(tm) platform
 *
 *
 * (C) Copyright 2000-2008, by Object Refinery Limited and Contributors.
 *
 * Project Info:  http://www.jfree.org/jfreechart/index.html
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 2.1 of the License, or
 * (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
 * License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
 * USA.
 *
 * [Java is a trademark or registered trademark of Sun Microsystems, Inc.
 * in the United States and other countries.]
 *
 * --------------------
 * HexNumberFormat.java
 * --------------------
 * (C) Copyright 2007, 2008, by Richard West and Contributors.
 *
 * Original Author:  Richard West, Advanced Micro Devices, Inc.;
 * Contributor(s):   David Gilbert (for Object Refinery Limited);
 *
 * Changes:
 * --------
 * 14-Jun-2007 : Version 1 (RW);
 *
 */
import java.text.FieldPosition;
import java.text.NumberFormat;
import java.text.ParsePosition;
/**
 * There are some limitations, so be careful using this class.
 *
 * @since 1.0.6
 */
public class HexNumberFormat extends NumberFormat {
    /** Number of hexadecimal digits for a byte. */
    public static final int BYTE = 2;
    /** Number of hexadecimal digits for a word. */
    public static final int WORD = 4;
    /** Number of hexadecimal digits for a double word. */
    public static final int DWORD = 8;
    /** Number of hexadecimal digits for a quad word. */
    public static final int QWORD = 16;
    /** The number of digits (shorter strings will be left padded). */
    private int m_numDigits = DWORD;
    /**
     * Creates a new instance with 8 digits.
     */
    public HexNumberFormat() {
        this(DWORD);
    }
    /**
     * Creates a new instance with the specified number of digits.
     * @param digits  the digits.
     */
    public HexNumberFormat(int digits) {
        super();
        this.m_numDigits = digits;
    }
    /**
     * Returns the number of digits.
     *
     * @return The number of digits.
     */
    public final int getNumberOfDigits() {
        return this.m_numDigits;
    }
    /**
     * Sets the number of digits.
     *
     * @param digits  the number of digits.
     */
    public void setNumberOfDigits(int digits) {
        this.m_numDigits = digits;
    }
    /**
     * Formats the specified number as a hexadecimal string.  The decimal
     * fraction is ignored.
     *
     * @param number  the number to format.
     * @param toAppendTo  the buffer to append to (ignored here).
     * @param pos  the field position (ignored here).
     *
     * @return The string buffer.
     */
    public StringBuffer format(double number, StringBuffer toAppendTo,
            FieldPosition pos) {
        return format((long) number, toAppendTo, pos);
    }
    /**
     * Formats the specified number as a hexadecimal string.  The decimal
     * fraction is ignored.
     *
     * @param number  the number to format.
     * @param toAppendTo  the buffer to append to (ignored here).
     * @param pos  the field position (ignored here).
     *
     * @return The string buffer.
     */
    public StringBuffer format(long number, StringBuffer toAppendTo,
            FieldPosition pos) {
        String l_hex = Long.toHexString(number).toUpperCase();
        int l_pad = this.m_numDigits - l_hex.length();
        l_pad = (0 < l_pad) ? l_pad : 0;
        StringBuffer l_extended = new StringBuffer("0x");
        for (int i = 0; i < l_pad; i++) {
            l_extended.append(0);
        }
        l_extended.append(l_hex);
        return l_extended;
    }
    /**
     * Parsing is not implemented, so this method always returns
     * <code>null</code>.
     *
     * @param source  ignored.
     * @param parsePosition  ignored.
     *
     * @return Always <code>null</code>.
     */
    public Number parse (String source, ParsePosition parsePosition) {
        return null; // don't bother with parsing
    }
}
```

| 2.9.1. | Hexadecimal integer literal |
|---|---|
| 2.9.2. | A hexadecimal literal of type long |
| 2.9.3. | Defining integer literals as octal values |
| 2.9.4. | Decode string to integer |
| 2.9.5. | Convert octal number to decimal number example |
| 2.9.6. | Convert decimal integer to octal number example |
| 2.9.7. | Convert decimal integer to hexadecimal number example |
| 2.9.8. | Parsing and Formatting a Number into Binary |
| 2.9.9. | Convert byte array to Hex String |
| 2.9.10. | Convert the bytes to a hex string representation of the bytes |
| 2.9.11. | Converting hexadecimal strings |
| 2.9.12. | Dumps data in hexadecimal format |
| 2.9.13. | Given a hexstring this will return the byte array corresponding to string |
| 2.9.14. | Hex encoder/decoder implementation borrowed from BouncyCastle |
| 2.9.15. | Returns the hexadecimal value of the supplied byte array |
| 2.9.16. | A custom number formatter that formats numbers as hexadecimal strings. |
| 2.9.17. | Decodes Hex data into octects |
| 2.9.18. | Decodes Base64 data into octects |
| 2.9.19. | Helper function that returns a char from an hex |
| 2.9.20. | Encodes hex octects into Base64 |
| 2.9.21. | Hex encoder and decoder. |
| 2.9.22. | Helper function that dump an array of bytes in hex pair form, without '0x' and space chars |
| 2.9.23. | dump an array of bytes in hex form |
| 2.9.24. | Decode byte array |
