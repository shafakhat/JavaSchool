---
title: Parse Comma Delimited List
nav: Parse Comma Delimited List
description: * The contents of this file are subject to the Sapient Public License
section: Imported - java2s Archive
order: 1250
source: https://web.archive.org/web/20140829093225/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ParseCommaDelimitedList.htm
---
```java title=Example.java
/*
 * The contents of this file are subject to the Sapient Public License
 * Version 1.0 (the "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 * http://carbon.sf.net/License.html.
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
 * the specific language governing rights and limitations under the License.
 *
 * The Original Code is The Carbon Component Framework.
 *
 * The Initial Developer of the Original Code is Sapient Corporation
 *
 * Copyright (C) 2003 Sapient Corporation. All Rights Reserved.
 */
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;
/**
 * Utilities for strings.
 *
 *
 * Copyright 2002 Sapient
 * @since carbon 1.0
 * @author Greg Hinkle, May 2002
 * @version $Revision: 1.5 $($Author: dvoet $ / $Date: 2003/05/05 21:21:24 $)
 */
public class StringUtil {
  /**
   * Parses a comma-separated list into an array of Strings
   * Values can contain whitespace, but whitespace at the beginning and
   * end of each value is trimmed.
   * @return array of Strings
   * @param csvList a string of comma seperated values
   */
  public static String[] parseCommaDelimitedList(String csvList) {
      String[] result = parseList(csvList, ",");
      for (int i = 0; i < result.length; i++) {
          result[i] = result[i].trim();
      }
      return result;
  }
  /**
   * Parses a whitepsace-separated list into an array of Strings
   * @return array of Strings
   * @param wsvList a string of white space seperated values
   */
  public static String[] parseWhitespaceDelimitedList(String wsvList) {
      return parseList(wsvList, "\t ");
  }
  /**
   * Parses a list according to the specified delimiter into an
   * array of Strings.
   * @see java.util.StringTokenizer
   * @param list a string of token seperated values
   * @param delim the delimiter character(s).  Each character in the string is a
   * single delimeter.
   * @return an array of strings
   */
  public static String[] parseList(String list, String delim) {
      List result = new ArrayList();
      StringTokenizer tokenizer = new StringTokenizer(list, delim);
      while (tokenizer.hasMoreTokens()) {
          result.add(tokenizer.nextToken());
      }
      return (String[]) result.toArray(new String[0]);
  }
}
```

| 2.24.1. | Tokenizing a String |
|---|---|
| 2.24.2. | Delimiters are comma, space, or period: '[, .]' |
| 2.24.3. | Parse Comma Delimited List |
