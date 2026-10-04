---
title: Pair of template arguments
nav: Pair of template arguments
description: * Copyright (C) 2006-2007 DSRG, Charles University in Prague
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20090926133732/http://www.java2s.com:80/Code/Java/Generics/Pairoftemplatearguments.htm
---
Pair of template arguments

```java title=Example.java
/* $Id$
 *
 * Behavior Protocols Tools - Parsers, Transformations
 * Copyright (C) 2006-2007  DSRG, Charles University in Prague
 *                          http://dsrg.mff.cuni.cz/
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
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301 USA
 *
 */
package org.ow2.dsrg.fm.bptools.util;
/**
 * Keeps pair of values whose type is given by template arguments
 * @author thorm
 */
public class Pair<T1, T2> {
    /**
     * Creates a new instance of Pair
     * @param first first value
     * @param second second value
     */
    public Pair(T1 first, T2 second) {
        this.first = first;
        this.second = second;
    }
    public boolean equals(Object obj) {
        if (obj instanceof Pair) {
            Pair other = (Pair)obj;
             return (other.first == null ? this.first == null : other.first.equals(this.first)) &&
                     (other.second == null ? this.second == null : other.second.equals(this.second));
        }
        else
            return false;
    }
    public String toString(){
        return first.toString() +"::"+second.toString() ;
    }
    /**
     * first value
     */
    public T1 first;
    /**
     * second value
     */
    public T2 second;
}
```

1.  A simple generic class.
---  ---
2.  Demonstrate the non generic class
3.  Stats attempts (unsuccessfully) to create a generic class
4.  A simple generic class hierarchy.
5.  A nongeneric class can be the superclass of a generic subclass.
6.  Use the instanceof operator with a generic class hierarchy.
7.  Java hierarchy generic class
8.  Custom Generic Object Tester
