---
title: Get First Not Empty String in a String list
nav: Get First Not Empty String...
description: Get First Not Empty String in a String list : String Operation « Regular Expressions « Java
section: Imported - java2s Archive
order: 1036
source: https://web.archive.org/web/20090828181247/http://www.java2s.com:80/Code/Java/Regular-Expressions/GetFirstNotEmptyStringinaStringlist.htm
---
Get First Not Empty String in a String list : String Operation « Regular Expressions « Java
Get First Not Empty String in a String list

```java title=Example.java
/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Utils {
  public static String getFirstNotEmpty(List<String> list) {
    if (isEmpty(list)) {
      return null;
    }
    for (String item : list) {
      if (!isEmpty(item)) {
        return item;
      }
    }
    return null;
  }
  public static List<String> getFound(String contents, String regex) {
    if (isEmpty(regex) || isEmpty(contents)) {
      return null;
    }
    List<String> results = new ArrayList<String>();
    Pattern pattern = Pattern.compile(regex, Pattern.UNICODE_CASE);
    Matcher matcher = pattern.matcher(contents);
    while (matcher.find()) {
      if (matcher.groupCount() > 0) {
        results.add(matcher.group(1));
      } else {
        results.add(matcher.group());
      }
    }
    return results;
  }
  public static boolean isEmpty(List<String> list) {
    if (list == null || list.size() == 0) {
      return true;
    }
    if (list.size() == 1 && isEmpty(list.get(0))) {
      return true;
    }
    return false;
  }
  public static boolean isEmpty(String str) {
    if (str != null && str.trim().length() > 0) {
      return false;
    }
    return true;
  }
}
```

1.  Regular expression: Split Demo
---  ---
2.  Replacing String Tokenizer
3.  String replace
4.  String split
5.  Simple split
6.  Calculating Word Frequencies with Regular Expressions
7.  Print all the strings that match a given pattern from a file
8.  Quick demo of Regular Expressions substitution
9.  Parse an Apache log file with StringTokenizer
10.  StringConvenience -- demonstrate java.lang.String convenience routine
11.  Split a String into a Java Array of Strings divided by an Regular Expressions
12.  Regular Expression Replace
13.  Java Regular Expression : Split text
14.  Java Regular Expression :split 2
15.  Get all digits from a string
16.  Strip extra spaces in a XML string
17.  Remove trailing white space from a string
18.  Create a string search and replace using regex
19.  Split-up string using regular expression
20.  Apply proper uppercase and lowercase on a String
21.  Regular Expression Search and Replace Program
22.  Searching and Replacing with Nonconstant Values Using a Regular Expression
23.  Use Matcher.appendReplacement() to match [a-zA-Z]+[0-9]+
24.  Ignore case differences when searching for or replacing substrings.
25.  Use replaceAll() to ignore case when replacing one substring with another
26.  Extract a substring by matching a regular expression.
27.  Match string ends
28.  Match words
29.  Match punct
30.  Match space
31.  Determining If a String Matches a Pattern Exactly
32.  Removing Duplicate Whitespace in a String
33.  Split the supplied content into lines, returning each line as an element in the returned list.
34.  Get First Found regex
35.  Get Found regex
