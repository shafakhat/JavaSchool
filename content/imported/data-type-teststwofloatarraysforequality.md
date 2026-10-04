---
title: Tests two float arrays for equality.
nav: Tests two float arrays for...
description: * JCommon : a free general purpose class library for the Java(tm) platform
section: Imported - java2s Archive
order: 1100
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Teststwofloatarraysforequality.htm
---
```java title=Example.java
import java.util.Arrays;
/*
 * JCommon : a free general purpose class library for the Java(tm) platform
 *
 *
 * (C) Copyright 2000-2005, by Object Refinery Limited and Contributors.
 *
 * Project Info:  http://www.jfree.org/jcommon/index.html
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 2.1 of the License, or
 * (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
 * License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
 * USA.
 *
 * [Java is a trademark or registered trademark of Sun Microsystems, Inc.
 * in the United States and other countries.]
 *
 * -------------------
 * ArrayUtilities.java
 * -------------------
 * (C) Copyright 2003-2005, by Object Refinery Limited.
 *
 * Original Author:  David Gilbert (for Object Refinery Limited);
 * Contributor(s):   -;
 *
 * $Id: ArrayUtilities.java,v 1.7 2008/09/10 09:21:30 mungady Exp $
 *
 * Changes
 * -------
 * 21-Aug-2003 : Version 1 (DG);
 * 04-Oct-2004 : Renamed ArrayUtils --> ArrayUtilities (DG);
 *
 */public class Main {
  /**
   *
   * @param array1  the first array (<code>null</code> permitted).
   * @param array2  the second arrray (<code>null</code> permitted).
   *
   * @return A boolean.
   */ public static boolean equal(final float[][] array1,
                              final float[][] array2) {
      if (array1 == null) {
          return (array2 == null);
      }
      if (array2 == null) {
          return false;
      }
      if (array1.length != array2.length) {
          return false;
      }
      for (int i = 0; i < array1.length; i++) {
          if (!Arrays.equals(array1[i], array2[i])) {
              return false;
          }
      }
      return true;
  }
}
```
