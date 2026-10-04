---
title: Return primitive type the passed in wrapper type corresponds to
nav: Return primitive type the ...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Returnprimitivetypethepassedinwrappertypecorrespondsto.htm
---
```java title=Example.java
import java.util.HashSet;
import java.util.List;
import java.util.Set;
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
public class Main {
  /**
   * @param wrapper
   *          a primitive wrapper type
   */
  public static Class getPrimitive(Class wrapper) {
    Class primitive;
    if (Integer.class == wrapper) {
      primitive = int.class;
    } else if (Long.class == wrapper) {
      primitive = long.class;
    } else if (Double.class == wrapper) {
      primitive = double.class;
    } else if (Boolean.class == wrapper) {
      primitive = boolean.class;
    } else if (Short.class == wrapper) {
      primitive = short.class;
    } else if (Float.class == wrapper) {
      primitive = float.class;
    } else if (Byte.class == wrapper) {
      primitive = byte.class;
    } else if (Character.class == wrapper) {
      primitive = char.class;
    } else {
      throw new IllegalArgumentException("The class is not a primitive wrapper type: " + wrapper);
    }
    return primitive;
  }
}
```
