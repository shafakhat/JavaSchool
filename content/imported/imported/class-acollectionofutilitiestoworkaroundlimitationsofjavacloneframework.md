---
title: A collection of utilities to workaround limitations of Java clone framework
nav: A collection of utilities ...
description: A collection of utilities to workaround limitations of Java clone framework
section: Imported - java2s Archive
order: 1126
source: https://web.archive.org/web/20100212194927/http://java2s.com/Code/Java/Class/AcollectionofutilitiestoworkaroundlimitationsofJavacloneframework.htm
---
```java title=Example.java
/*
 * $HeadURL$
 * $Revision$
 * $Date$
 *
 *
 *
 *  Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 *
 *
 * This software consists of voluntary contributions made by many
 * individuals on behalf of the Apache Software Foundation.  For more
 * information on the Apache Software Foundation, please see
 * <http://www.apache.org/>.
 *
 */
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
/**
 */
public class CloneUtils {
    public static Object clone(final Object obj) throws CloneNotSupportedException {
        if (obj == null) {
            return null;
        }
        if (obj instanceof Cloneable) {
            Class<?> clazz = obj.getClass ();
            Method m;
            try {
                m = clazz.getMethod("clone", (Class[]) null);
            } catch (NoSuchMethodException ex) {
                throw new NoSuchMethodError(ex.getMessage());
            }
            try {
                return m.invoke(obj, (Object []) null);
            } catch (InvocationTargetException ex) {
                Throwable cause = ex.getCause();
                if (cause instanceof CloneNotSupportedException) {
                    throw ((CloneNotSupportedException) cause);
                } else {
                    throw new Error("Unexpected exception", cause);
                }
            } catch (IllegalAccessException ex) {
                throw new IllegalAccessError(ex.getMessage());
            }
        } else {
            throw new CloneNotSupportedException();
        }
    }
    /**
     * This class should not be instantiated.
     */
    private CloneUtils() {
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
