---
title: Deep clone Object
nav: Deep clone Object
description: * This library is free software; you can redistribute it and/or
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20100208014149/http://java2s.com/Code/Java/Class/DeepcloneObject.htm
---
Deep clone Object

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

1.  A Cloning Example
---  ---
2.  Class is declared to be cloneable.
3.  Arrays are automatically cloneable
4.  Clone objects
5.  Creating a Deep Copy
6.  Shallow Copy Test
7.  Deep Copy Test
8.  Uses serialization to perform deep copy cloning.
9.  Tests cloning to see if destination of references are also cloned
10.  Creating local copies with clone
11.  You can insert Cloneability at any level of inheritance
12.  Cloning a composed object
13.  Serializable and clone
14.  Go through a few gyrations to add cloning to your own class
15.  Checking to see if a reference can be cloned
16.  The clone operation works for only a few items in the standard Java library
17.  Demonstration of cloning
18.  Simple demo of avoiding side-effects by using Object.clone
19.  Clone an object with clone method from parent
20.  Manipulate properties after clone operation
21.  Serializable Clone
22.  Utility for object cloning
23.  Clone Via Serialization
24.  Clone demo
25.  Deep clone serializing/de-serializng Clone
26.  Implements a pool of internalized objects
27.  A collection of utilities to workaround limitations of Java clone framework
