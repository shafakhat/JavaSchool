---
title: Pattern helper
nav: Pattern helper
description: * This program is free software; you can redistribute it and/or modify
section: Imported - java2s Archive
order: 2232
source: https://web.archive.org/web/20140829090638/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Patternhelper.htm
---
```java title=Example.java
/*
 * Static String formatting and query routines.
 * Copyright (C) 2001-2005 Stephen Ostermiller
 * http://ostermiller.org/contact.pl?regarding=Java+Utilities
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * See COPYING.TXT for details.
 */
import java.util.HashMap;
import java.util.regex.Pattern;
/**
 * Utilities for String formatting, manipulation, and queries.
 * More information about this class is available from <a target="_top" href=
 * "http://ostermiller.org/utils/StringHelper.html">ostermiller.org</a>.
 *
 * @author Stephen Ostermiller http://ostermiller.org/contact.pl?regarding=Java+Utilities
 * @since ostermillerutils 1.00.00
 */
public class StringHelper {
  /**
   * Build a regular expression that is each of the terms or'd together.
   *
   * @param terms a list of search terms.
   * @param sb place to build the regular expression.
   * @throws IllegalArgumentException if the length of terms is zero.
   *
   * @since ostermillerutils 1.02.25
   */
  private static void buildFindAnyPattern(String[] terms, StringBuffer sb){
    if (terms.length == 0) throw new IllegalArgumentException("There must be at least one term to find.");
    sb.append("(?:");
    for (int i=0; i<terms.length; i++){
      if (i>0) sb.append("|");
      sb.append("(?:");
      sb.append(escapeRegularExpressionLiteral(terms[i]));
      sb.append(")");
    }
    sb.append(")");
  }
  /**
   * Compile a pattern that can will match a string if the string
   * contains any of the given terms.
   *
   * Usage:<br>
   * <code>boolean b = getContainsAnyPattern(terms).matcher(s).matches();</code>
   *
   * If multiple strings are matched against the same set of terms,
   * it is more efficient to reuse the pattern returned by this function.
   *
   * @param terms Array of search strings.
   * @return Compiled pattern that can be used to match a string to see if it contains any of the terms.
   *
   * @since ostermillerutils 1.02.25
   */
  public static Pattern getContainsAnyPattern(String[] terms){
    StringBuffer sb = new StringBuffer();
    sb.append("(?s).*");
    buildFindAnyPattern(terms, sb);
    sb.append(".*");
    return Pattern.compile(sb.toString());
  }
  /**
   * Compile a pattern that can will match a string if the string
   * equals any of the given terms.
   *
   * Usage:<br>
   * <code>boolean b = getEqualsAnyPattern(terms).matcher(s).matches();</code>
   *
   * If multiple strings are matched against the same set of terms,
   * it is more efficient to reuse the pattern returned by this function.
   *
   * @param terms Array of search strings.
   * @return Compiled pattern that can be used to match a string to see if it equals any of the terms.
   *
   * @since ostermillerutils 1.02.25
   */
   public static Pattern getEqualsAnyPattern(String[] terms){
    StringBuffer sb = new StringBuffer();
    sb.append("(?s)\\A");
    buildFindAnyPattern(terms, sb);
    sb.append("\\z");
    return Pattern.compile(sb.toString());
  }
  /**
   * Compile a pattern that can will match a string if the string
   * starts with any of the given terms.
   *
   * Usage:<br>
   * <code>boolean b = getStartsWithAnyPattern(terms).matcher(s).matches();</code>
   *
   * If multiple strings are matched against the same set of terms,
   * it is more efficient to reuse the pattern returned by this function.
   *
   * @param terms Array of search strings.
   * @return Compiled pattern that can be used to match a string to see if it starts with any of the terms.
   *
   * @since ostermillerutils 1.02.25
   */
   public static Pattern getStartsWithAnyPattern(String[] terms){
    StringBuffer sb = new StringBuffer();
    sb.append("(?s)\\A");
    buildFindAnyPattern(terms, sb);
    sb.append(".*");
    return Pattern.compile(sb.toString());
  }
  /**
   * Compile a pattern that can will match a string if the string
   * ends with any of the given terms.
   *
   * Usage:<br>
   * <code>boolean b = getEndsWithAnyPattern(terms).matcher(s).matches();</code>
   *
   * If multiple strings are matched against the same set of terms,
   * it is more efficient to reuse the pattern returned by this function.
   *
   * @param terms Array of search strings.
   * @return Compiled pattern that can be used to match a string to see if it ends with any of the terms.
   *
   * @since ostermillerutils 1.02.25
   */
  public static Pattern getEndsWithAnyPattern(String[] terms){
    StringBuffer sb = new StringBuffer();
    sb.append("(?s).*");
    buildFindAnyPattern(terms, sb);
    sb.append("\\z");
    return Pattern.compile(sb.toString());
  }
  /**
   * Compile a pattern that can will match a string if the string
   * contains any of the given terms.
   *
   * Case is ignored when matching using Unicode case rules.
   *
   * Usage:<br>
   * <code>boolean b = getContainsAnyPattern(terms).matcher(s).matches();</code>
   *
   * If multiple strings are matched against the same set of terms,
   * it is more efficient to reuse the pattern returned by this function.
   *
   * @param terms Array of search strings.
   * @return Compiled pattern that can be used to match a string to see if it contains any of the terms.
   *
   * @since ostermillerutils 1.02.25
   */
  public static Pattern getContainsAnyIgnoreCasePattern(String[] terms){
    StringBuffer sb = new StringBuffer();
    sb.append("(?i)(?u)(?s).*");
    buildFindAnyPattern(terms, sb);
    sb.append(".*");
    return Pattern.compile(sb.toString());
  }
  /**
   * Compile a pattern that can will match a string if the string
   * equals any of the given terms.
   *
   * Case is ignored when matching using Unicode case rules.
   *
   * Usage:<br>
   * <code>boolean b = getEqualsAnyPattern(terms).matcher(s).matches();</code>
   *
   * If multiple strings are matched against the same set of terms,
   * it is more efficient to reuse the pattern returned by this function.
   *
   * @param terms Array of search strings.
   * @return Compiled pattern that can be used to match a string to see if it equals any of the terms.
   *
   * @since ostermillerutils 1.02.25
   */
   public static Pattern getEqualsAnyIgnoreCasePattern(String[] terms){
    StringBuffer sb = new StringBuffer();
    sb.append("(?i)(?u)(?s)\\A");
    buildFindAnyPattern(terms, sb);
    sb.append("\\z");
    return Pattern.compile(sb.toString());
  }
  /**
   * Compile a pattern that can will match a string if the string
   * starts with any of the given terms.
   *
   * Case is ignored when matching using Unicode case rules.
   *
   * Usage:<br>
   * <code>boolean b = getStartsWithAnyPattern(terms).matcher(s).matches();</code>
   *
   * If multiple strings are matched against the same set of terms,
   * it is more efficient to reuse the pattern returned by this function.
   *
   * @param terms Array of search strings.
   * @return Compiled pattern that can be used to match a string to see if it starts with any of the terms.
   *
   * @since ostermillerutils 1.02.25
   */
   public static Pattern getStartsWithAnyIgnoreCasePattern(String[] terms){
    StringBuffer sb = new StringBuffer();
    sb.append("(?i)(?u)(?s)\\A");
    buildFindAnyPattern(terms, sb);
    sb.append(".*");
    return Pattern.compile(sb.toString());
  }
  /**
   * Compile a pattern that can will match a string if the string
   * ends with any of the given terms.
   *
   * Case is ignored when matching using Unicode case rules.
   *
   * Usage:<br>
   * <code>boolean b = getEndsWithAnyPattern(terms).matcher(s).matches();</code>
   *
   * If multiple strings are matched against the same set of terms,
   * it is more efficient to reuse the pattern returned by this function.
   *
   * @param terms Array of search strings.
   * @return Compiled pattern that can be used to match a string to see if it ends with any of the terms.
   *
   * @since ostermillerutils 1.02.25
   */
  public static Pattern getEndsWithAnyIgnoreCasePattern(String[] terms){
    StringBuffer sb = new StringBuffer();
    sb.append("(?i)(?u)(?s).*");
    buildFindAnyPattern(terms, sb);
    sb.append("\\z");
    return Pattern.compile(sb.toString());
  }
  /**
   * Tests to see if the given string contains any of the given terms.
   *
   * This implementation is more efficient than the brute force approach
   * of testing the string against each of the terms.  It instead compiles
   * a single regular expression that can test all the terms at once, and
   * uses that expression against the string.
   *
   * This is a convenience method.  If multiple strings are tested against
   * the same set of terms, it is more efficient not to compile the regular
   * expression multiple times.
   * @see #getContainsAnyPattern(String[])
   *
   * @param s String that may contain any of the given terms.
   * @param terms list of substrings that may be contained in the given string.
   * @return true iff one of the terms is a substring of the given string.
   *
   * @since ostermillerutils 1.02.25
   */
  public static boolean containsAny(String s, String[] terms){
    return getContainsAnyPattern(terms).matcher(s).matches();
  }
  /**
   * Tests to see if the given string equals any of the given terms.
   *
   * This implementation is more efficient than the brute force approach
   * of testing the string against each of the terms.  It instead compiles
   * a single regular expression that can test all the terms at once, and
   * uses that expression against the string.
   *
   * This is a convenience method.  If multiple strings are tested against
   * the same set of terms, it is more efficient not to compile the regular
   * expression multiple times.
   * @see #getEqualsAnyPattern(String[])
   *
   * @param s String that may equal any of the given terms.
   * @param terms list of strings that may equal the given string.
   * @return true iff one of the terms is equal to the given string.
   *
   * @since ostermillerutils 1.02.25
   */
  public static boolean equalsAny(String s, String[] terms){
    return getEqualsAnyPattern(terms).matcher(s).matches();
  }
  /**
   * Tests to see if the given string starts with any of the given terms.
   *
   * This implementation is more efficient than the brute force approach
   * of testing the string against each of the terms.  It instead compiles
   * a single regular expression that can test all the terms at once, and
   * uses that expression against the string.
   *
   * This is a convenience method.  If multiple strings are tested against
   * the same set of terms, it is more efficient not to compile the regular
   * expression multiple times.
   * @see #getStartsWithAnyPattern(String[])
   *
   * @param s String that may start with any of the given terms.
   * @param terms list of strings that may start with the given string.
   * @return true iff the given string starts with one of the given terms.
   *
   * @since ostermillerutils 1.02.25
   */
  public static boolean startsWithAny(String s, String[] terms){
    return getStartsWithAnyPattern(terms).matcher(s).matches();
  }
  /**
   * Tests to see if the given string ends with any of the given terms.
   *
   * This implementation is more efficient than the brute force approach
   * of testing the string against each of the terms.  It instead compiles
   * a single regular expression that can test all the terms at once, and
   * uses that expression against the string.
   *
   * This is a convenience method.  If multiple strings are tested against
   * the same set of terms, it is more efficient not to compile the regular
   * expression multiple times.
   * @see #getEndsWithAnyPattern(String[])
   *
   * @param s String that may end with any of the given terms.
   * @param terms list of strings that may end with the given string.
   * @return true iff the given string ends with one of the given terms.
   *
   * @since ostermillerutils 1.02.25
   */
  public static boolean endsWithAny(String s, String[] terms){
    return getEndsWithAnyPattern(terms).matcher(s).matches();
  }
  /**
   * Tests to see if the given string contains any of the given terms.
   *
   * Case is ignored when matching using Unicode case rules.
   *
   * This implementation is more efficient than the brute force approach
   * of testing the string against each of the terms.  It instead compiles
   * a single regular expression that can test all the terms at once, and
   * uses that expression against the string.
   *
   * This is a convenience method.  If multiple strings are tested against
   * the same set of terms, it is more efficient not to compile the regular
   * expression multiple times.
   * @see #getContainsAnyIgnoreCasePattern(String[])
   *
   * @param s String that may contain any of the given terms.
   * @param terms list of substrings that may be contained in the given string.
   * @return true iff one of the terms is a substring of the given string.
   *
   * @since ostermillerutils 1.02.25
   */
  public static boolean containsAnyIgnoreCase(String s, String[] terms){
    return getContainsAnyIgnoreCasePattern(terms).matcher(s).matches();
  }
  /**
   * Tests to see if the given string equals any of the given terms.
   *
   * Case is ignored when matching using Unicode case rules.
   *
   * This implementation is more efficient than the brute force approach
   * of testing the string against each of the terms.  It instead compiles
   * a single regular expression that can test all the terms at once, and
   * uses that expression against the string.
   *
   * This is a convenience method.  If multiple strings are tested against
   * the same set of terms, it is more efficient not to compile the regular
   * expression multiple times.
   * @see #getEqualsAnyIgnoreCasePattern(String[])
   *
   * @param s String that may equal any of the given terms.
   * @param terms list of strings that may equal the given string.
   * @return true iff one of the terms is equal to the given string.
   *
   * @since ostermillerutils 1.02.25
   */
  public static boolean equalsAnyIgnoreCase(String s, String[] terms){
    return getEqualsAnyIgnoreCasePattern(terms).matcher(s).matches();
  }
  /**
   * Tests to see if the given string starts with any of the given terms.
   *
   * Case is ignored when matching using Unicode case rules.
   *
   * This implementation is more efficient than the brute force approach
   * of testing the string against each of the terms.  It instead compiles
   * a single regular expression that can test all the terms at once, and
   * uses that expression against the string.
   *
   * This is a convenience method.  If multiple strings are tested against
   * the same set of terms, it is more efficient not to compile the regular
   * expression multiple times.
   * @see #getStartsWithAnyIgnoreCasePattern(String[])
   *
   * @param s String that may start with any of the given terms.
   * @param terms list of strings that may start with the given string.
   * @return true iff the given string starts with one of the given terms.
   *
   * @since ostermillerutils 1.02.25
   */
  public static boolean startsWithAnyIgnoreCase(String s, String[] terms){
    return getStartsWithAnyIgnoreCasePattern(terms).matcher(s).matches();
  }
  /**
   * Tests to see if the given string ends with any of the given terms.
   *
   * Case is ignored when matching using Unicode case rules.
   *
   * This implementation is more efficient than the brute force approach
   * of testing the string against each of the terms.  It instead compiles
   * a single regular expression that can test all the terms at once, and
   * uses that expression against the string.
   *
   * This is a convenience method.  If multiple strings are tested against
   * the same set of terms, it is more efficient not to compile the regular
   * expression multiple times.
   * @see #getEndsWithAnyIgnoreCasePattern(String[])
   *
   * @param s String that may end with any of the given terms.
   * @param terms list of strings that may end with the given string.
   * @return true iff the given string ends with one of the given terms.
   *
   * @since ostermillerutils 1.02.25
   */
  public static boolean endsWithAnyIgnoreCase(String s, String[] terms){
    return getEndsWithAnyIgnoreCasePattern(terms).matcher(s).matches();
  }
  /**
   * Escapes characters that have special meaning to
   * regular expressions
   *
   * @param s String to be escaped
   * @return escaped String
   * @throws NullPointerException if s is null.
   *
   * @since ostermillerutils 1.02.25
   */
  public static String escapeRegularExpressionLiteral(String s){
    // According to the documentation in the Pattern class:
    //
    // The backslash character ('\') serves to introduce escaped constructs,
    // as defined in the table above, as well as to quote characters that
    // otherwise would be interpreted as unescaped constructs. Thus the
    // expression \\ matches a single backslash and \{ matches a left brace.
    //
    // It is an error to use a backslash prior to any alphabetic character
    // that does not denote an escaped construct; these are reserved for future
    // extensions to the regular-expression language. A backslash may be used
    // prior to a non-alphabetic character regardless of whether that character
    // is part of an unescaped construct.
    //
    // As a result, escape everything except [0-9a-zA-Z]
    int length = s.length();
    int newLength = length;
    // first check for characters that might
    // be dangerous and calculate a length
    // of the string that has escapes.
    for (int i=0; i<length; i++){
      char c = s.charAt(i);
      if (!((c>='0' && c<='9') || (c>='A' && c<='Z') || (c>='a' && c<='z'))){
        newLength += 1;
      }
    }
    if (length == newLength){
      // nothing to escape in the string
      return s;
    }
    StringBuffer sb = new StringBuffer(newLength);
    for (int i=0; i<length; i++){
      char c = s.charAt(i);
      if (!((c>='0' && c<='9') || (c>='A' && c<='Z') || (c>='a' && c<='z'))){
        sb.append('\\');
      }
      sb.append(c);
    }
    return sb.toString();
  }
}
```

| 8.1.1. | Meta-characters predefined to match specific characters. |
|---|---|
| 8.1.2. | Meta-characters to match against certain string boundaries. |
| 8.1.3. | Regular expression languages also have character classes. |
| 8.1.4. | POSIX character classes and Java character classes |
| 8.1.5. | Java Character Class |
| 8.1.6. | Match a particular character a specified number of times. |
| 8.1.7. | Read regular expression from console |
| 8.1.8. | Regex Test Harness |
| 8.1.9. | Match Java source file and file and class name |
| 8.1.10. | Finding all words that start with an 'a' |
| 8.1.11. | Simple validation using the Pattern and Matcher objects |
| 8.1.12. | A possessive qualifier |
| 8.1.13. | Find the starting point of the second 'Bond' |
| 8.1.14. | A negative look ahead |
| 8.1.15. | A negative behind ahead |
| 8.1.16. | A positive look ahead |
| 8.1.17. | Pattern helper |
| 8.1.18. | Escapes characters that have special meaning to regular expressions |
