---
title: Returns a new string with all the whitespace removed
nav: Returns a new string with ...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1096
source: https://web.archive.org/web/20100131052538/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Returnsanewstringwithallthewhitespaceremoved.htm
---
```java title=Example.java
import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.net.URLDecoder;
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
   * Returns a new string with all the whitespace removed
   *
   * @param s the source string
   * @return the string without whitespace or null
   */
  public static String removeWhiteSpace(String s)
  {
     String retn = null;
     if (s != null)
     {
        int len = s.length();
        StringBuffer sbuf = new StringBuffer(len);
        for (int i = 0; i < len; i++)
        {
           char c = s.charAt(i);
           if (!Character.isWhitespace(c))
               sbuf.append(c);
        }
        retn = sbuf.toString();
     }
     return retn;
  }
}
```
