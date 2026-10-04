---
title: Join an array of strings into one delimited string
nav: Join an array of strings i...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Joinanarrayofstringsintoonedelimitedstring.htm
---
```java title=Example.java
/*
  * JBoss, Home of Professional Open Source
  * Copyright 2005, JBoss Inc., and individual contributors as indicated
  * by the @authors tag. See the copyright.txt in the distribution for a
  * full listing of individual contributors.
  *
  * This is free software; you can redistribute it and/or modify it
  * under the terms of the GNU Lesser General Public License as
  * published by the Free Software Foundation; either version 2.1 of
  * the License, or (at your option) any later version.
  *
  * This software is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  * Lesser General Public License for more details.
  *
  * You should have received a copy of the GNU Lesser General Public
  * License along with this software; if not, write to the Free
  * Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
  * 02110-1301 USA, or see the FSF site: http://www.fsf.org.
  */public class Main{
  /////////////////////////////////////////////////////////////////////////
 //                    Joining/Concatenation Methods                    //
 /////////////////////////////////////////////////////////////////////////
 /**
   *
   * @param buff    String buffered used for join (buffer is not reset).
   * @param array   Array of objects to join as strings.
   * @param delim   Delimiter to join strings with or <i>null</i>.
   * @return        Joined string.
   */ public static String join(final StringBuffer buff, final Object array[],
     final String delim)
  {
     boolean haveDelim = (delim != null);
     for (int i = 0; i < array.length; i++)
     {
        buff.append(array[i]);
        // if this is the last element then don't append delim
 if (haveDelim && (i + 1) < array.length)
        {
           buff.append(delim);
        }
     }
     return buff.toString();
  }
  /**
   *
   * @param array   Array of objects to join as strings.
   * @param delim   Delimiter to join strings with or <i>null</i>.
   * @return        Joined string.
   */ public static String join(final Object array[], final String delim)
  {
     return join(new StringBuffer(), array, delim);
  }
  /**
   * Convert and join an array of objects into one string.
   *
   * @param array   Array of objects to join as strings.
   * @return        Converted and joined objects.
   */ public static String join(final Object array[])
  {
     return join(array, null);
  }
  /**
   * Convert and join an array of bytes into one string.
   *
   * @param array   Array of objects to join as strings.
   * @return        Converted and joined objects.
   */ public static String join(final byte array[])
  {
     Byte bytes[] = new Byte[array.length];
     for (int i = 0; i < bytes.length; i++)
     {
        bytes[i] = new Byte(array[i]);
     }
     return join(bytes, null);
  }
  /**
   * Return a string composed of the given array.
   *
   * @param buff       Buffer used to construct string value (not reset).
   * @param array      Array of objects.
   * @param prefix     String prefix.
   * @param separator  Element sepearator.
   * @param suffix     String suffix.
   * @return           String in the format of:
   *                   prefix + n ( + separator + n+i)* + suffix.
   */ public static String join(final StringBuffer buff, final Object[] array,
     final String prefix, final String separator,
     final String suffix)
  {
     buff.append(prefix);
     join(buff, array, separator);
     buff.append(suffix);
     return buff.toString();
  }
  /**
   * Return a string composed of the given array.
   *
   * @param array      Array of objects.
   * @param prefix     String prefix.
   * @param separator  Element sepearator.
   * @param suffix     String suffix.
   * @return           String in the format of:
   *                   prefix + n ( + separator + n+i)* + suffix.
   */ public static String join(final Object[] array, final String prefix,
     final String separator, final String suffix)
  {
     return join(new StringBuffer(), array, prefix, separator, suffix);
  }
}
```
