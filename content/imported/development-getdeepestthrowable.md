---
title: Get Deepest Throwable
nav: Get Deepest Throwable
description: * This library is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20101102012947/http://www.java2s.com:80/Tutorial/Java/0120__Development/GetDeepestThrowable.htm
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
  public static Throwable getDeepestThrowable(Throwable t)
  {
     Throwable parent = t;
     Throwable child = t.getCause();
     while(null != child)
     {
        parent = child;
        child = parent.getCause();
     }
     return parent;
  }
}
```
