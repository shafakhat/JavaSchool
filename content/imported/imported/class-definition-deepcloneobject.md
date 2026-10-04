---
title: Deep clone Object
nav: Deep clone Object
description: * This library is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 1016
source: https://web.archive.org/web/20100529044445/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/DeepcloneObject.htm
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
   * Creates a clone of any serializable object. Collections and arrays
   * may be cloned if the entries are serializable.
   *
   * Caution super class members are not cloned if a super class is not serializable.
   */
  public static Object cloneObject(Object toClone, final ClassLoader classLoader)
  {
     if(null == toClone)
     {
        return null;
     }
     else
     {
        try
        {
           ByteArrayOutputStream bOut = new ByteArrayOutputStream();
           ObjectOutputStream oOut = new ObjectOutputStream(bOut);
           oOut.writeObject(toClone);
           oOut.close();
           ByteArrayInputStream bIn = new ByteArrayInputStream(bOut.toByteArray());
           bOut.close();
           ObjectInputStream oIn = new ObjectInputStream(bIn)
           {
              protected Class<?> resolveClass(ObjectStreamClass desc) throws IOException, ClassNotFoundException
              {
                return Class.forName(desc.getName(), false, classLoader);
              }
           };
           bIn.close();
           Object copy = oIn.readObject();
           oIn.close();
           return copy;
        }
        catch (Exception e)
        {
           throw new RuntimeException(e);
        }
     }
  }
}
```
