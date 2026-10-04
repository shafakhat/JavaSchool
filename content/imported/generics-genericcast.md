---
title: Generic cast
nav: Generic cast
description: * This library is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20100206220611/http://java2s.com/Code/Java/Generics/Genericcast.htm
---
```java title=Example.java
/*
 * Copyright (C) 2001-2003 Colin Bell
 * colbell@users.sourceforge.net
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */
import java.io.*;
import java.text.NumberFormat;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
/**
 * General purpose utilities functions.
 *
 * @author <A HREF="mailto:colbell@users.sourceforge.net">Colin Bell</A>
 */
public class Utilities
{
  /**
  * This is taken from Eammon McManus' blog:
  * http://weblogs.java.net/blog/emcmanus/archive/2007/03/getting_rid_of.html This prevents you from having
  * to place SuppressWarnings throughout your code.
  *
  * @param <T>
  *           the return type to cast the object to
  * @param x
  *           the object to cast.
  * @return a type-casted version of the specified object.
  */
 @SuppressWarnings("unchecked")
 public static <T> T cast(Object x) {
     return (T) x;
 }
}
```

1.  Java generic: Use a wildcard.
---  ---
2.  Java generic: Bounded Wildcard arguments
3.  Use a wildcard.
4.  Bounded Wildcard arguments.
