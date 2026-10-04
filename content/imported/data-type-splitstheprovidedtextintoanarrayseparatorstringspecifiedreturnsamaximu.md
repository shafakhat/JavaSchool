---
title: Splits the provided text into an array, separator string specified. Returns a maximum of max substrings.
nav: Splits the provided text i...
description: * Splits the provided text into an array, separator string specified.
section: Imported - java2s Archive
order: 1177
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SplitstheprovidedtextintoanarrayseparatorstringspecifiedReturnsamaximumofmaxsubstrings.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.List;
public class Main {
  /**
   * Splits the provided text into an array, separator string specified.
   * Returns a maximum of <code>max</code> substrings.
   *
   * The separator(s) will not be included in the returned String array.
   * Adjacent separators are treated as one separator.
   *
   * A <code>null</code> input String returns <code>null</code>.
   * A <code>null</code> separator splits on whitespace.
   *
   * <pre>
   * StringUtils.splitByWholeSeparator(null, *, *)               = null
   * StringUtils.splitByWholeSeparator("", *, *)                 = []
   * StringUtils.splitByWholeSeparator("ab de fg", null, 0)      = ["ab", "de", "fg"]
   * StringUtils.splitByWholeSeparator("ab   de fg", null, 0)    = ["ab", "de", "fg"]
   * StringUtils.splitByWholeSeparator("ab:cd:ef", ":", 2)       = ["ab", "cd:ef"]
   * StringUtils.splitByWholeSeparator("ab-!-cd-!-ef", "-!-", 5) = ["ab", "cd", "ef"]
   * StringUtils.splitByWholeSeparator("ab-!-cd-!-ef", "-!-", 2) = ["ab", "cd-!-ef"]
   * </pre>
   *
   * @param str  the String to parse, may be null
   * @param separator  String containing the String to be used as a delimiter,
   *  <code>null</code> splits on whitespace
   * @param max  the maximum number of elements to include in the returned
   *  array. A zero or negative value implies no limit.
   * @return an array of parsed Strings, <code>null</code> if null String was input
   */ public static String[] splitByWholeSeparator( String str, String separator, int max ) {
      return splitByWholeSeparatorWorker(str, separator, max, false);
  }
  /**
   * Performs the logic for the <code>splitByWholeSeparatorPreserveAllTokens</code> methods.
   *
   * @param str  the String to parse, may be <code>null</code>
   * @param separator  String containing the String to be used as a delimiter,
   *  <code>null</code> splits on whitespace
   * @param max  the maximum number of elements to include in the returned
   *  array. A zero or negative value implies no limit.
   * @param preserveAllTokens if <code>true</code>, adjacent separators are
   * treated as empty token separators; if <code>false</code>, adjacent
   * separators are treated as one separator.
   * @return an array of parsed Strings, <code>null</code> if null String input
   * @since 2.4
   */ private static String[] splitByWholeSeparatorWorker(String str, String separator, int max,
                                                      boolean preserveAllTokens)
  {
      if (str == null) {
          return null;
      }
      int len = str.length();
      if (len == 0) {
          return new String[0];
      }
      if ((separator == null) || ("".equals(separator))) {
          // Split on whitespace.
 return splitWorker(str, null, max, preserveAllTokens);
      }
      int separatorLength = separator.length();
      ArrayList substrings = new ArrayList();
      int numberOfSubstrings = 0;
      int beg = 0;
      int end = 0;
      while (end < len) {
          end = str.indexOf(separator, beg);
          if (end > -1) {
              if (end > beg) {
                  numberOfSubstrings += 1;
                  if (numberOfSubstrings == max) {
                      end = len;
                      substrings.add(str.substring(beg));
                  } else {
                      // The following is OK, because String.substring( beg, end ) excludes
 // the character at the position 'end'.
                      substrings.add(str.substring(beg, end));
                      // Set the starting point for the next search.
 // The following is equivalent to beg = end + (separatorLength - 1) + 1,
 // which is the right calculation:
                      beg = end + separatorLength;
                  }
              } else {
                  // We found a consecutive occurrence of the separator, so skip it.
 if (preserveAllTokens) {
                      numberOfSubstrings += 1;
                      if (numberOfSubstrings == max) {
                          end = len;
                          substrings.add(str.substring(beg));
                      } else {
                          substrings.add("");
                      }
                  }
                  beg = end + separatorLength;
              }
          } else {
              // String.substring( beg ) goes from 'beg' to the end of the String.
              substrings.add(str.substring(beg));
              end = len;
          }
      }
      return (String[]) substrings.toArray(new String[substrings.size()]);
  }
  /**
   * Performs the logic for the <code>split</code> and
   * <code>splitPreserveAllTokens</code> methods that return a maximum array
   * length.
   *
   * @param str  the String to parse, may be <code>null</code>
   * @param separatorChars the separate character
   * @param max  the maximum number of elements to include in the
   *  array. A zero or negative value implies no limit.
   * @param preserveAllTokens if <code>true</code>, adjacent separators are
   * treated as empty token separators; if <code>false</code>, adjacent
   * separators are treated as one separator.
   * @return an array of parsed Strings, <code>null</code> if null String input
   */ private static String[] splitWorker(String str, String separatorChars, int max, boolean preserveAllTokens) {
      // Performance tuned for 2.0 (JDK1.4)
 // Direct code is quicker than StringTokenizer.
 // Also, StringTokenizer uses isSpace() not isWhitespace()
 if (str == null) {
          return null;
      }
      int len = str.length();
      if (len == 0) {
          return new String[0];
      }
      List list = new ArrayList();
      int sizePlus1 = 1;
      int i = 0, start = 0;
      boolean match = false;
      boolean lastMatch = false;
      if (separatorChars == null) {
          // Null separator means use whitespace
 while (i < len) {
              if (Character.isWhitespace(str.charAt(i))) {
                  if (match || preserveAllTokens) {
                      lastMatch = true;
                      if (sizePlus1++ == max) {
                          i = len;
                          lastMatch = false;
                      }
                      list.add(str.substring(start, i));
                      match = false;
                  }
                  start = ++i;
                  continue;
              }
              lastMatch = false;
              match = true;
              i++;
          }
      } else if (separatorChars.length() == 1) {
          // Optimise 1 character case
 char sep = separatorChars.charAt(0);
          while (i < len) {
              if (str.charAt(i) == sep) {
                  if (match || preserveAllTokens) {
                      lastMatch = true;
                      if (sizePlus1++ == max) {
                          i = len;
                          lastMatch = false;
                      }
                      list.add(str.substring(start, i));
                      match = false;
                  }
                  start = ++i;
                  continue;
              }
              lastMatch = false;
              match = true;
              i++;
          }
      } else {
          // standard case
 while (i < len) {
              if (separatorChars.indexOf(str.charAt(i)) >= 0) {
                  if (match || preserveAllTokens) {
                      lastMatch = true;
                      if (sizePlus1++ == max) {
                          i = len;
                          lastMatch = false;
                      }
                      list.add(str.substring(start, i));
                      match = false;
                  }
                  start = ++i;
                  continue;
              }
              lastMatch = false;
              match = true;
              i++;
          }
      }
      if (match || (preserveAllTokens && lastMatch)) {
          list.add(str.substring(start, i));
      }
      return (String[]) list.toArray(new String[list.size()]);
  }
}
```
