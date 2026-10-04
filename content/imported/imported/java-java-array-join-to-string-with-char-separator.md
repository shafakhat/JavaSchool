---
title: Java array join to String with char separator
nav: Java array join to String ...
description: Object[] array = newString[] { "CSS", "HTML", "Java", null, "demo2s.com", "Javascript 123" };
section: Imported
order: 20003
source: http://www.java2s.com/ref/java/java-array-join-to-string-with-char-separator.html
---
- Java Basic
- Java Language Basics Java Language Data Types Operator Statement String enum Array Autobox class Method interface Generics Exception Javadoc Lambda package import Java Features Algorithms Byte Array Data Structures Design Patterns Directory Network Regular Expression Text File OCA OCP Exam OCA OCP Exam 1 OCA OCP Exam 2 OCA OCP Exam 3 OCA OCP Exam 4 OCA OCP Exam 5 OCA OCP Exam 6 OCA OCP Exam 7 OCA OCP Exam 8 OCA OCP Exam 9 OCA OCP Exam 10 OCA OCP Exam 11 OCA OCP Exam 12 OCA OCP Exam 13 OCA OCP Exam 14 OCA OCP Exam 15 OCA OCP Exam 16 OCA OCP Exam 17 OCA OCP Exam 18 OCA OCP Exam 19 OCA OCP Exam 20 OCA OCP Exam 21 OCA OCP Exam 22 OCA OCP Exam 23 OCA OCP Exam 24 OCA OCP Exam 25 OCA OCP Exam 26 OCA OCP Exam 27 OCA OCP Exam 28 OCA OCP Exam 29 OCA OCP Exam 30 OCA OCP Exam 31 OCA OCP Exam 32 OCA OCP Exam 33

## Description

Java array join to String with char separator

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] argv) throwsException {
    Object[] array = newString[] { "CSS", "HTML", "Java", null, "demo2s.com", "Javascript 123" };
    System.out.println(join(array, ' '));
  }//fromwww.java2s.com/**
   * <p>
   * Joins the elements of the provided array into a single String containing the
   * provided list of elements.
   * </p>
   *
   * <p>
   * No delimiter is added before or after the list. Null objects or empty strings
   * within the array are represented by empty strings.
   * </p>
   *
   * <pre>
   * StringUtil.join(null, *)               = null
   * StringUtil.join([], *)                 = ""
   * StringUtil.join([null], *)             = ""
   * StringUtil.join(["a", "b", "c"], ';')  = "a;b;c"
   * StringUtil.join(["a", "b", "c"], null) = "abc"
   * StringUtil.join([null, "", "a"], ';')  = ";;a"
   * </pre>
   *
   * @param array
   *          the array of values to join together, may be null
   * @param separator
   *          the separator character to use
   * @return the joined String, <code>null</code> if null array input
   * @since 2.0
   */publicstaticString join(Object[] array, char separator) {
    if (array == null) {
      return null;
    }

    return join(array, separator, 0, array.length);
  }

  /**
   * <p>
   * Joins the elements of the provided array into a single String containing the
   * provided list of elements.
   * </p>
   *
   * <p>
   * No delimiter is added before or after the list. Null objects or empty strings
   * within the array are represented by empty strings.
   * </p>
   *
   * <pre>
   * StringUtil.join(null, *)               = null
   * StringUtil.join([], *)                 = ""
   * StringUtil.join([null], *)             = ""
   * StringUtil.join(["a", "b", "c"], ';')  = "a;b;c"
   * StringUtil.join(["a", "b", "c"], null) = "abc"
   * StringUtil.join([null, "", "a"], ';')  = ";;a"
   * </pre>
   *
   * @param array
   *          the array of values to join together, may be null
   * @param separator
   *          the separator character to use
   * @param startIndex
   *          the first index to start joining from. It is an error to pass in an
   *          end index past the end of the array
   * @param endIndex
   *          the index to stop joining from (exclusive). It is an error to pass
   *          in an end index past the end of the array
   * @return the joined String, <code>null</code> if null array input
   * @since 2.0
   */publicstaticString join(Object[] array, char separator, int startIndex, int endIndex) {
    if (array == null) {
      return null;
    }
    int bufSize = (endIndex - startIndex);
    if (bufSize <= 0) {
      return EMPTY;
    }

    bufSize *= ((array[startIndex] == null ? 16 : array[startIndex].toString().length()) + 1);
    StringBuffer buf = newStringBuffer(bufSize);

    for (int i = startIndex; i < endIndex; i++) {
      if (i > startIndex) {
        buf.append(separator);
      }
      if (array[i] != null) {
        buf.append(array[i]);
      }
    }
    return buf.toString();
  }

  publicstaticfinalString EMPTY = "";
}

/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
```

PreviousNext

## Related

- Java array join int[] array to String
- Java array join long[] array to String
- Java array join String[] array to String
- Java array join to String with String separator
- Java array length double
