---
title: Appends a whitespace-normalized form of the specified character sequence into the specified string buffer.
nav: Appends a whitespace-norma...
description: Appends a whitespace-normalized form of the specified character sequence into the specified string buffer.
section: Imported - java2s Archive
order: 1144
source: https://web.archive.org/web/20111031020808/http://www.java2s.com:80/Code/Java/Data-Type/Appendsawhitespacenormalizedformofthespecifiedcharactersequenceintothespecifiedstringbuffer.htm
---
```java title=Example.java
/*
 * LingPipe v. 3.9
 * Copyright (C) 2003-2010 Alias-i
 *
 * This program is licensed under the Alias-i Royalty Free License
 * Version 1 WITHOUT ANY WARRANTY, without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the Alias-i
 * Royalty Free License Version 1 for more details.
 *
 * You should have received a copy of the Alias-i Royalty Free License
 * Version 1 along with this program; if not, visit
 * http://alias-i.com/lingpipe/licenses/lingpipe-license-1.txt or contact
 * Alias-i, Inc. at 181 North 11th Street, Suite 401, Brooklyn, NY 11211,
 * +1 (718) 290-9170.
 */
//package com.aliasi.util;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.text.DecimalFormat;
/**
 * Static utility methods for processing strings, characters and
 * string buffers.
 *
 * @author  Bob Carpenter
 * @version 4.0.1
 * @since   LingPipe1.0
 * @see     java.lang.Character
 * @see     java.lang.String
 * @see     java.lang.StringBuilder
 */
public class Strings {
    /**
     * Appends a whitespace-normalized form of the specified character
     * sequence into the specified string buffer.  Initial and final
     * whitespaces are not appended, and every other maximal sequence
     * of contiguous whitespace is replaced with a single whitespace
     * character.  For instance, <code>&quot; a\tb\n&quot;</code>
     * would append the following characters to <code>&quot;a
     * b&quot;</code>.
     *
     * <P>This command is useful for text inputs for web or GUI
     * applications.
     *
     * @param cs Character sequence whose normalization is appended to
     * the buffer.
     * @param sb String buffer to which the normalized character
     * sequence is appended.
     */
    public static void normalizeWhitespace(CharSequence cs, StringBuilder sb) {
        int i = 0;
        int length = cs.length();
        while (length > 0 && isWhitespace(cs.charAt(length-1)))
            --length;
        while (i < length && isWhitespace(cs.charAt(i)))
            ++i;
        boolean inWhiteSpace = false;
        for ( ; i < length; ++i) {
            char nextChar = cs.charAt(i);
            if (isWhitespace(nextChar)) {
                if (!inWhiteSpace) {
                    sb.append(' ');
                    inWhiteSpace = true;
                }
            } else {
                inWhiteSpace = false;
                sb.append(nextChar);
            }
        }
    }
    /**
     * Returns a whitespace-normalized version of the specified
     * character sequence.  See {@link
     * #normalizeWhitespace(CharSequence,StringBuilder)} for
     * information on the normalization procedure.
     *
     * @param cs Character sequence to normalize.
     * @return Normalized version of character sequence.
     */
    public static String normalizeWhitespace(CharSequence cs) {
        StringBuilder sb = new StringBuilder();
        normalizeWhitespace(cs,sb);
        return sb.toString();
    }
    /**
     * Returns <code>true</code> if the specified buffer contains
     * only whitespace characters.
     *
     * @param sb String buffer to test for whitespace.
     * @return <code>true</code> if the specified buffer contains only
     * whitespace characters.
     */
    public static boolean allWhitespace(StringBuilder sb) {
        return allWhitespace(sb.toString());
    }
    /**
     * Returns <code>true</code> if the specified string contains
     * only whitespace characters.
     *
     * @param s Stirng to test for whitespace.
     * @return <code>true</code> if the specified string contains only
     * whitespace characters.
     */
    public static boolean allWhitespace(String s) {
        return allWhitespace(s.toCharArray(),0,s.length());
    }
    /**
     * Returns <code>true</code> if the specified range of the
     * specified character array only whitespace characters, as defined for
     * characters by {@link #isWhitespace(char c)}.
     *
     * @param ch Character array to test for whitespace characters in range.
     * @param start Beginning of range to test.
     * @param length Number of characters to test.
     * @return <code>true</code> if the specified string contains only
     * whitespace characters.
     */
    public static boolean allWhitespace(char[] ch, int start, int length) {
        for (int i = start; i < start+length; ++i)
            if (!isWhitespace(ch[i])) return false;
        return true;
    }
    /**
     * Returns true if specified character is a whitespace character.
     * The definition in {@link
     * java.lang.Character#isWhitespace(char)} is extended to include
     * the unicode non-breakable space character (unicode 160).
     *
     * @param c Character to test.
     * @return <code>true</code> if specified character is a
     * whitespace.
     * @see java.lang.Character#isWhitespace(char)
     */
    public static boolean isWhitespace(char c) {
        return Character.isWhitespace(c) || c == NBSP_CHAR;
    }
    /**
     * The non-breakable space character.
     */
    public static char NBSP_CHAR = (char)160;
}
```

1.  StrCharAt - show String.charAt()
---  ---
2.  Basic tab-character handling stuff
3.  Convert Characters to Lower Case
4.  Convert Characters to Upper Case
5.  Replace Characters in a String
6.  Character array to String conversion
7.  Convert String to character array
8.  Last occurrence of a character
9.  Extract Ascii codes from a String
10.  To remove a character
11.  Removes specified chars from a string
12.  Checks if a String is not empty (""), not null and not whitespace only.
13.  Checks if a String is whitespace, empty ("") or null.
14.  Checks if the String contains any character in the given set of characters.
15.  Checks if the String contains only certain characters.
16.  Checks if the String contains only whitespace.
17.  Checks if the string contains only ASCII printable characters.
18.  Checks that the String does not contain certain characters.
19.  The character array based string
20.  Checks whether the String contains only digit characters.
21.  Remove char from a string
22.  Remove whitespace from the ends as well as excessive whitespace within the inside of the string between non-whitespace characters.
23.  Removes any hypens ( - ) from the given string
24.  Returns a new string with all the whitespace removed
25.  Is char a white space character
26.  Simple scanner that allows to navigate over the characters of a string.
27.  Returns a string with size of count and all characters initialized with ch.
28.  Returns a string that contains all characters of the given string in reverse order.
29.  Returns a string that is equivalent to the specified string with its first character converted to uppercase
30.  Count the number of occurrences of character c in a string.
31.  A fast way to convert character arrays into Strings.
32.  XML utilities that pertain to character handling (markup or character data), without use of any XML libraries.
33.  Check whether the given String contains any whitespace characters.
34.  Character utilities.
35.  Provides a number of static methods which interact with java.nio.charset.Charset to analyze and transform the strings identifing character encodings.
36.  Operations on char primitives and Character objects.
37.  Cleans strings of illegal characters with respect to the XML specification.
38.  Return the result of adding the specified character to the specified sorted character array.
39.  Return a displayable version of the character sequence, followed by integer positions at various powers of 10.
40.  Returns the string constructed from the specified character sequence by deaccenting each of its characters.
41.  Returns a hash code for a character sequence that is equivalent to the hash code generated for a its string yield.
42.  Return true if the two character sequences have the same length and the same characters.
43.  Returns an array of substrings of the specified string, in order, with divisions before and after any instance of the specified character.
44.  Returns true if specified character is a punctuation character.
45.  Determine whether characters may appear in certain roles in XML documents.
46.  Advanced navigation over the underlying string.
47.  Compare two char sequences
48.  Contents As CharSequence
