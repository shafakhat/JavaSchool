---
title: Return a string padded with the given string for the given count.
nav: Return a string padded wit...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1085
source: https://web.archive.org/web/20140829080837/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Returnastringpaddedwiththegivenstringforthegivencount.htm
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
  */
public class Main{
  /////////////////////////////////////////////////////////////////////////
  //                            Padding Methods                          //
  /////////////////////////////////////////////////////////////////////////
  /**
   *
   * @param buff       String buffer used for padding (buffer is not reset).
   * @param string     Pad element.
   * @param count      Pad count.
   * @return           Padded string.
   */
  public static String pad(final StringBuffer buff, final String string,
     final int count)
  {
     for (int i = 0; i < count; i++)
     {
        buff.append(string);
     }
     return buff.toString();
  }
  /**
   *
   * @param string     Pad element.
   * @param count      Pad count.
   * @return           Padded string.
   */
  public static String pad(final String string, final int count)
  {
     return pad(new StringBuffer(), string, count);
  }
  /**
   * Return a string padded with the given string value of an object
   * for the given count.
   *
   * @param obj     Object to convert to a string.
   * @param count   Pad count.
   * @return        Padded string.
   */
  public static String pad(final Object obj, final int count)
  {
     return pad(new StringBuffer(), String.valueOf(obj), count);
  }
}
```
