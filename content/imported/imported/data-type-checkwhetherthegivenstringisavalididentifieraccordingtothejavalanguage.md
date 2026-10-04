---
title: Check whether the given String is a valid identifier according to the Java Language specifications.
nav: Check whether the given St...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckwhetherthegivenStringisavalididentifieraccordingtotheJavaLanguagespecifications.htm
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
  */publicclass Main{
  /**
   * Check whether the given String is a valid identifier according
   * to the Java Language specifications.
   *
   * See The Java Language Specification Second Edition, Section 3.8
   * for the definition of what is a valid identifier.
   *
   * @param s String to check
   *
   * @return <code>true</code> if the given String is a valid Java
   *         identifier, <code>false</code> otherwise.
   */publicfinalstaticboolean isValidJavaIdentifier(String s)
  {
     // an empty or null string cannot be a valid identifier
if (s == null || s.length() == 0)
     {
        return false;
     }

     char[] c = s.toCharArray();
     if (!Character.isJavaIdentifierStart(c[0]))
     {
        return false;
     }

     for (int i = 1; i < c.length; i++)
     {
        if (!Character.isJavaIdentifierPart(c[i]))
        {
           return false;
        }
     }

     return true;
  }

}
```
