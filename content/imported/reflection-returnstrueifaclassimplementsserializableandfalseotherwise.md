---
title: Returns true if a class implements Serializable and false otherwise.
nav: Returns true if a class im...
description: * JCommon : a free general purpose class library for the Java(tm) platform
section: Imported - java2s Archive
order: 2061
source: https://web.archive.org/web/20140829083640/http://www.java2s.com/Tutorial/Java/0125__Reflection/ReturnstrueifaclassimplementsSerializableandfalseotherwise.htm
---
```java title=Example.java
import java.io.Serializable;
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
 * ------------
 * IOUtils.java
 * ------------
 * (C)opyright 2002-2004, by Thomas Morgner and Contributors.
 *
 * Original Author:  Thomas Morgner;
 * Contributor(s):   David Gilbert (for Object Refinery Limited);
 *
 * $Id: IOUtils.java,v 1.8 2009/01/22 08:34:58 taqua Exp $
 *
 * Changes
 * -------
 * 26-Jan-2003 : Initial version
 * 23-Feb-2003 : Documentation
 * 25-Feb-2003 : Fixed Checkstyle issues (DG);
 * 29-Apr-2003 : Moved to jcommon
 * 04-Jan-2004 : Fixed JDK 1.2.2 issues with createRelativeURL;
 *               added support for query strings within these urls (TM);
 */
public class Main {
  /**
   * Returns <code>true</code> if a class implements <code>Serializable</code>
   * and <code>false</code> otherwise.
   *
   * @param c  the class.
   *
   * @return A boolean.
   */
  public static boolean isSerializable(final Class c) {
      /**
      final Class[] interfaces = c.getInterfaces();
      for (int i = 0; i < interfaces.length; i++) {
          if (interfaces[i].equals(Serializable.class)) {
              return true;
          }
      }
      Class cc = c.getSuperclass();
      if (cc != null) {
          return isSerializable(cc);
      }
       */
      return (Serializable.class.isAssignableFrom(c));
  }
}
```

| 7.2.1. | The superclass of interfaces is always null |
|---|---|
| 7.2.2. | Listing the Interfaces That an Interface Extends |
| 7.2.3. | Checking whether String is an interface or class |
| 7.2.4. | If a class object is an interface or a class |
| 7.2.5. | Listing the Interfaces That a Class Implements |
| 7.2.6. | Although the type of o2 is an interface, getSuperclass() returns the object's superclass |
| 7.2.7. | The interfaces for a primitive type is an empty array |
| 7.2.8. | Return Returns true if type is implementing Map |
| 7.2.9. | Returns true if a class implements Serializable and false otherwise. |
| 7.2.10. | Get Super Interfaces |
| 7.2.11. | Get all interface and object classes that are generalizations of the provided class |
