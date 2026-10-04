---
title: Parse basic types
nav: Parse basic types
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1164
source: https://web.archive.org/web/20101009070948/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Parsebasictypes.htm
---
```java title=Example.java
/*
 * Copyright 2004, 2005, 2006 Odysseus Software GmbH
 *
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
import java.text.DateFormat;
import java.text.Format;
import java.text.ParseException;
import java.text.ParsePosition;
import java.util.Date;
import java.util.Locale;
import java.util.TimeZone;
import java.math.BigDecimal;
import java.math.BigInteger;
/**
 * Parse basic types.
 *
 * @author Christoph Beck
 */
public class ParseUtils {
  private static Locale locale = Locale.US;
  private static Object nullValue(Class type) {
    if (type.isPrimitive()) {
      if (type == boolean.class)
        return Boolean.FALSE;
      if (type == byte.class)
        return new Byte((byte)0);
      if (type == char.class)
        return new Character((char)0);
      if (type == short.class)
        return new Short((short)0);
      if (type == int.class)
        return new Integer(0);
      if (type == long.class)
        return new Long(0);
      if (type == float.class)
        return new Float(0);
      if (type == double.class)
        return new Double(0);
    }
    return null;
  }
  private static Class objectType(Class type) {
    if (type.isPrimitive()) {
      if (type == boolean.class)
        return Boolean.class;
      if (type == byte.class)
        return Byte.class;
      if (type == char.class)
        return Character.class;
      if (type == short.class)
        return Short.class;
      if (type == int.class)
        return Integer.class;
      if (type == long.class)
        return Long.class;
      if (type == float.class)
        return Float.class;
      if (type == double.class)
        return Double.class;
    }
    return type;
  }
  private static Object parse(Format format, String value) throws ParseException {
    ParsePosition pos = new ParsePosition(0);
    Object result = format.parseObject(value, pos);
    if (pos.getIndex() < value.length())
      throw new ParseException("Cannot parse " + value + " (garbage suffix)!", pos.getIndex());
    return result;
  }
  private static Date parseDate(String value) throws ParseException {
    DateFormat format = DateFormat.getDateInstance(DateFormat.SHORT, locale);
    format.setTimeZone(TimeZone.getTimeZone("GMT"));
    return (Date)parse(format, value);
  }
  private static Boolean parseBoolean(String value) throws ParseException {
    if ("true".equals(value)) {
      return Boolean.TRUE;
    } else if ("false".equals(value)) {
      return Boolean.FALSE;
    } else {
      throw new ParseException("Cannot parse '" + value + "' as boolean", 0);
    }
  }
  private static Character parseCharacter(String value) throws ParseException {
    if (value.length() != 1) {
      throw new ParseException("Cannot parse '" + value + "' as character", value.length());
    }
    return new Character(value.charAt(0));
  }
  /**
   * Parse value of specified type. The string value has to be in
   * standard notation for the specified type.
   */
  public static Object parse(Class type, String value) throws Exception {
    if (value == null) {
      return nullValue(type);
    } else if (value.length() == 0) {
      return type == String.class ? value : nullValue(type);
    }
    type = objectType(type);
    if (type == BigDecimal.class) {
      return new BigDecimal(value);
    } else if (type == BigInteger.class) {
      return new BigInteger(value);
    } else if (type == Boolean.class) {
      return parseBoolean(value);
    } else if (type == Byte.class) {
      return Byte.valueOf(value);
    } else if (type == Character.class) {
      return parseCharacter(value);
    } else if (type == Date.class) {
      return parseDate(value);
    } else if (type == Double.class) {
      return Double.valueOf(value);
    } else if (type == Float.class) {
      return Float.valueOf(value);
    } else if (type == Integer.class) {
      return Integer.valueOf(value);
    } else if (type == Long.class) {
      return Long.valueOf(value);
    } else if (type == Short.class) {
      return Short.valueOf(value);
    } else if (type == String.class) {
      return value;
    }
    throw new ParseException("Cannot parse type " + type, 0);
  }
}
///////////////////////
/*
 * Copyright 2004, 2005, 2006 Odysseus Software GmbH
 *
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
package de.odysseus.calyxo.base.util;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Date;
import junit.framework.TestCase;
/**
 * ParseUtils test case.
 *
 * @author Christoph Beck
 */
public class ParseUtilsTest extends TestCase {
  /**
   * Constructor for ParseUtilsTest.
   * @param arg0
   */
  public ParseUtilsTest(String arg0) {
    super(arg0);
  }
  public void testNullPrimitive() throws Exception {
    assertEquals(Boolean.FALSE, ParseUtils.parse(boolean.class, null));
    assertEquals(new Character((char)0), ParseUtils.parse(char.class, null));
    assertEquals(new Byte((byte)0), ParseUtils.parse(byte.class, null));
    assertEquals(new Short((short)0), ParseUtils.parse(short.class, null));
    assertEquals(new Integer(0), ParseUtils.parse(int.class, null));
    assertEquals(new Long(0), ParseUtils.parse(long.class, null));
    assertEquals(new Float(0), ParseUtils.parse(float.class, null));
    assertEquals(new Double(0), ParseUtils.parse(double.class, null));
  }
  public void testPrimitive() throws Exception {
    assertEquals(Boolean.TRUE, ParseUtils.parse(boolean.class, "true"));
    assertEquals(Boolean.FALSE, ParseUtils.parse(boolean.class, "false"));
    assertEquals(new Character((char)10), ParseUtils.parse(char.class, "\n"));
    assertEquals(new Byte((byte)10), ParseUtils.parse(byte.class, "10"));
    assertEquals(new Short((short)10), ParseUtils.parse(short.class, "10"));
    assertEquals(new Integer(10), ParseUtils.parse(int.class, "10"));
    assertEquals(new Long(10), ParseUtils.parse(long.class, "10"));
    assertEquals(new Float(10), ParseUtils.parse(float.class, "10"));
    assertEquals(new Double(10), ParseUtils.parse(double.class, "10"));
  }
  public void testNullObject() throws Exception {
    assertNull(ParseUtils.parse(Boolean.class, null));
    assertNull(ParseUtils.parse(Byte.class, null));
    assertNull(ParseUtils.parse(Character.class, null));
    assertNull(ParseUtils.parse(Short.class, null));
    assertNull(ParseUtils.parse(Integer.class, null));
    assertNull(ParseUtils.parse(Long.class, null));
    assertNull(ParseUtils.parse(Float.class, null));
    assertNull(ParseUtils.parse(Double.class, null));
    assertNull(ParseUtils.parse(BigInteger.class, null));
    assertNull(ParseUtils.parse(BigDecimal.class, null));
    assertNull(ParseUtils.parse(Date.class, null));
    assertNull(ParseUtils.parse(String.class, null));
  }
  public void testObject() throws Exception {
    assertEquals(Boolean.TRUE, ParseUtils.parse(Boolean.class, "true"));
    assertEquals(Boolean.FALSE, ParseUtils.parse(Boolean.class, "false"));
    assertEquals(new Character((char)10), ParseUtils.parse(Character.class, "\n"));
    assertEquals(new Byte((byte)10), ParseUtils.parse(Byte.class, "10"));
    assertEquals(new Short((short)10), ParseUtils.parse(Short.class, "10"));
    assertEquals(new Integer(10), ParseUtils.parse(Integer.class, "10"));
    assertEquals(new Long(10), ParseUtils.parse(Long.class, "10"));
    assertEquals(new Float(10), ParseUtils.parse(Float.class, "10"));
    assertEquals(new Double(10), ParseUtils.parse(Double.class, "10"));
    assertEquals(new BigInteger("10"), ParseUtils.parse(BigInteger.class, "10"));
    assertEquals(new BigDecimal(10), ParseUtils.parse(BigDecimal.class, "10"));
    assertEquals(new Date(0), ParseUtils.parse(Date.class, "1/1/70"));
    assertEquals("foo", ParseUtils.parse(String.class, "foo"));
  }
  public void testBadValues() throws Exception {
    try {
      ParseUtils.parse(Boolean.class, "no");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(Character.class, "10");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(Byte.class, "abc");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(Short.class, "abc");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(Integer.class, "abc");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(Long.class, "abc");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(Float.class, "abc");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(Double.class, "abc");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(BigInteger.class, "abc");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(BigDecimal.class, "abc");
      fail("Exception expected");
    } catch(Exception e) {}
    try {
      ParseUtils.parse(Date.class, "1.1.70");
      fail("Exception expected");
    } catch(Exception e) {}
  }
  public void testBadType() throws Exception {
    try {
      ParseUtils.parse(Cloneable.class, "dolly");
      fail("Exception expected");
    } catch(Exception e) {}
  }
  public static void main(String[] args) {
    junit.textui.TestRunner.run(ParseUtilsTest.class);
  }
}
```
