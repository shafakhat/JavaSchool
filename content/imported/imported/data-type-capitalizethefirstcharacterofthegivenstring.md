---
title: Capitalize the first character of the given string
nav: Capitalize the first chara...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20100412210652/http://java2s.com:80/Tutorial/Java/0040__Data-Type/Capitalizethefirstcharacterofthegivenstring.htm
---
```java title=Example.java
import java.util.Map;
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
  /**
   * Capitalize the first character of the given string.
   *
   * @param string     String to capitalize.
   * @return           Capitalized string.
   *
   * @throws IllegalArgumentException    String is <kk>null</kk> or empty.
   */
  public static String capitalize(final String string)
  {
     if (string == null)
        throw new NullPointerException("string");
     if (string.equals(""))
        throw new NullPointerException("string");
     return Character.toUpperCase(string.charAt(0)) + string.substring(1);
  }
}
```
