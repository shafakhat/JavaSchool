---
title: Count the number of instances of substring within a string
nav: Count the number of instan...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Countthenumberofinstancesofsubstringwithinastring.htm
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
  */publicclass Main{
  /////////////////////////////////////////////////////////////////////////
//                          Counting Methods                           //
/////////////////////////////////////////////////////////////////////////
/**
   *
   * @param string     String to look for substring in.
   * @param substring  Sub-string to look for.
   * @return           Count of substrings in string.
   */publicstaticint count(final String string, final String substring)
  {
     int count = 0;
     int idx = 0;
     while ((idx = string.indexOf(substring, idx)) != -1)
     {
        idx++;
        count++;
     }
     return count;
  }
  /**
   * Count the number of instances of character within a string.
   *
   * @param string     String to look for substring in.
   * @param c          Character to look for.
   * @return           Count of substrings in string.
   */publicstaticint count(final String string, finalchar c)
  {
     return count(string, String.valueOf(c));
  }
}
```
