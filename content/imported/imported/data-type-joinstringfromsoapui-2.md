---
title: Join string from soapUI
nav: Join string from soapUI
description: * soapUI is free software; you can redistribute it and/or modify it under the
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/20100604104940/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/JoinstringfromsoapUI.htm
---
```java title=Example.java
/*
 *  soapUI, copyright (C) 2004-2009 eviware.com
 *
 *  soapUI is free software; you can redistribute it and/or modify it under the
 *  terms of version 2.1 of the GNU Lesser General Public License as published by
 *  the Free Software Foundation.
 *
 *  soapUI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 *  even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 *  See the GNU Lesser General Public License for more details at gnu.org.
 */
public class Utils {
  public static String join( String[] array, String separator )
  {
    StringBuffer buf = new StringBuffer();
    for( int i = 0; i < array.length; i++ )
    {
      if( i > 0 )
        buf.append( separator );
      buf.append( array[i] );
    }
    return buf.toString();
  }
}
```
