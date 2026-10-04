---
title: Test the equality of two object arrays
nav: Test the equality of two o...
description: * Copyright 2005, JBoss Inc., and individual contributors as indicated
section: Imported - java2s Archive
order: 1077
source: https://web.archive.org/web/20091120144733/http://www.java2s.com:80/Code/Java/Class/Testtheequalityoftwoobjectarrays.htm
---
Test the equality of two object arrays

```java title=Example.java
import java.lang.reflect.Array;
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
public class Main {
  /**
   * Test the equality of two object arrays.
   *
   * @param a       The first array.
   * @param b       The second array.
   * @param deep    True to traverse elements which are arrays.
   * @return        True if arrays are equal.
   */
  public static boolean equals(final Object[] a, final Object[] b,
                               final boolean deep)
  {
     if (a == b) return true;
     if (a == null || b == null) return false;
     if (a.length != b.length) return false;
     for (int i=0; i<a.length; i++) {
        Object x = a[i];
        Object y = b[i];
        if (x != y) return false;
        if (x == null || y == null) return false;
        if (deep) {
           if (x instanceof Object[] && y instanceof Object[]) {
              if (! equals((Object[])x, (Object[])y, true)) return false;
           }
           else {
              return false;
           }
        }
        if (! x.equals(y)) return false;
     }
     return true;
  }
  /**
   * Test the equality of two object arrays.
   *
   * @param a    The first array.
   * @param b    The second array.
   * @return     True if arrays are equal.
   */
  public static boolean equals(final Object[] a, final Object[] b) {
     return equals(a, b, true);
  }
}
```

1.  Equals(Equal) Method
---  ---
2.  Equals Method
3.  Equivalence
4.  If the given objects are equal
5.  Equivalence ClassSet
6.  Compares two objects for equality, where either one or both objects may be null
