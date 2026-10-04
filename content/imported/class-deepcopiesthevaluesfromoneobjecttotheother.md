---
title: Deep-copies the values from one object to the other
nav: Deep-copies the values fro...
description: return c.isPrimitive() || c == String.class || c == Boolean.class
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20111014030733/http://www.java2s.com:80/Code/Java/Class/Deepcopiesthevaluesfromoneobjecttotheother.htm
---
```java title=Example.java
//package com.ryanm.util;
import java.lang.reflect.Field;
import java.util.Random;
/**
 * I can't think of anywhere else to put them
 *
 * @author ryanm
 */
public class Util
{
  /**
   *
   * @param <T>
   * @param from
   *           the source of the copied data
   * @param to
   *           The destination of the copied data
   */
  public static <T> void copyFields( T from, T to )
  {
    for( Field f : from.getClass().getFields() )
    {
      try
      {
        if( isPrimitivish( f.getType() ) )
        {
          f.set( to, f.get( from ) );
        }
        else
        {
          copyFields( f.get( from ), f.get( to ) );
        }
      }
      catch( IllegalArgumentException e )
      {
        e.printStackTrace();
      }
      catch( IllegalAccessException e )
      {
        e.printStackTrace();
      }
    }
  }
  private static boolean isPrimitivish( Class c )
  {
    return c.isPrimitive() || c == String.class || c == Boolean.class
        || c == Byte.class || c == Short.class || c == Character.class
        || c == Integer.class || c == Float.class || c == Double.class
        || c == Long.class;
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
21.  Deep clone Object
22.  Serializable Clone
23.  Utility for object cloning
24.  Clone Via Serialization
25.  Clone demo
26.  Deep clone serializing/de-serializng Clone
27.  Implements a pool of internalized objects
28.  A collection of utilities to workaround limitations of Java clone framework
29.  This program demonstrates cloning
30.  Returns a copy of the object, or null if the object cannot be serialized.
31.  Object Deep copy
