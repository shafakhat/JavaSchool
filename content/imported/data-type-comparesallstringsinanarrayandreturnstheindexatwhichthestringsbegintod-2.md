---
title: Compares all Strings in an array and returns the index at which the Strings begin to differ.
nav: Compares all Strings in an...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ComparesallStringsinanarrayandreturnstheindexatwhichtheStringsbegintodiffer.htm
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
 */publicclass Main {
  /**
   * Compares all Strings in an array and returns the index at which the
   * Strings begin to differ.
   *
   * For example,
   * <code>indexOfDifference(new String[] {"i am a machine", "i am a robot"}) -> 7</code>
   *
   * <pre>
   * StringUtils.indexOfDifference(null) = -1
   * StringUtils.indexOfDifference(new String[] {}) = -1
   * StringUtils.indexOfDifference(new String[] {"abc"}) = -1
   * StringUtils.indexOfDifference(new String[] {null, null}) = -1
   * StringUtils.indexOfDifference(new String[] {"", ""}) = -1
   * StringUtils.indexOfDifference(new String[] {"", null}) = 0
   * StringUtils.indexOfDifference(new String[] {"abc", null, null}) = 0
   * StringUtils.indexOfDifference(new String[] {null, null, "abc"}) = 0
   * StringUtils.indexOfDifference(new String[] {"", "abc"}) = 0
   * StringUtils.indexOfDifference(new String[] {"abc", ""}) = 0
   * StringUtils.indexOfDifference(new String[] {"abc", "abc"}) = -1
   * StringUtils.indexOfDifference(new String[] {"abc", "a"}) = 1
   * StringUtils.indexOfDifference(new String[] {"ab", "abxyz"}) = 2
   * StringUtils.indexOfDifference(new String[] {"abcde", "abxyz"}) = 2
   * StringUtils.indexOfDifference(new String[] {"abcde", "xyz"}) = 0
   * StringUtils.indexOfDifference(new String[] {"xyz", "abcde"}) = 0
   * StringUtils.indexOfDifference(new String[] {"i am a machine", "i am a robot"}) = 7
   * </pre>
   *
   * @param strs  array of strings, entries may be null
   * @return the index where the strings begin to differ; -1 if they are all equal
   * @since 2.4
   */publicstaticint indexOfDifference(String[] strs) {
      if (strs == null || strs.length <= 1) {
          return -1;
      }
      boolean anyStringNull = false;
      boolean allStringsNull = true;
      int arrayLen = strs.length;
      int shortestStrLen = Integer.MAX_VALUE;
      int longestStrLen = 0;
      // find the min and max string lengths; this avoids checking to make
// sure we are not exceeding the length of the string each time through
// the bottom loop.
for (int i = 0; i < arrayLen; i++) {
          if (strs[i] == null) {
              anyStringNull = true;
              shortestStrLen = 0;
          } else {
              allStringsNull = false;
              shortestStrLen = Math.min(strs[i].length(), shortestStrLen);
              longestStrLen = Math.max(strs[i].length(), longestStrLen);
          }
      }
      // handle lists containing all nulls or all empty strings
if (allStringsNull || (longestStrLen == 0 && !anyStringNull)) {
          return -1;
      }
      // handle lists containing some nulls or some empty strings
if (shortestStrLen == 0) {
          return 0;
      }
      // find the position with the first difference across all strings
int firstDiff = -1;
      for (int stringPos = 0; stringPos < shortestStrLen; stringPos++) {
          char comparisonChar = strs[0].charAt(stringPos);
          for (int arrayPos = 1; arrayPos < arrayLen; arrayPos++) {
              if (strs[arrayPos].charAt(stringPos) != comparisonChar) {
                  firstDiff = stringPos;
                  break;
              }
          }
          if (firstDiff != -1) {
              break;
          }
      }
      if (firstDiff == -1 && shortestStrLen != longestStrLen) {
          // we compared all of the characters up to the length of the
// shortest string and didn't find a match, but the string lengths
// vary, so return the length of the shortest string.
return shortestStrLen;
      }
      return firstDiff;
  }
}
```
