---
title: Get the Generic definition from a class for given class with given index.
nav: Get the Generic definition...
description: Get the Generic definition from a class for given class with given index.
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/20111124225431/http://java2s.com/Code/Java/Generics/GettheGenericdefinitionfromaclassforgivenclasswithgivenindex.htm
---
Get the Generic definition from a class for given class with given index.

```java title=Example.java
/**
 * Copyright (C) 2010 altuure <altuure [AT] gmail [DOT] com> http://www.altuure.com/projects/yagdao
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *         http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
//package com.altuure.yagdao.common;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
/**
 * Created by IntelliJ IDEA.
 * User: makkan
 * Date: 04-Dec-2010
 * Time: 20:14:55
 * To change this template use File | Settings | File Templates.
 */
public class GenericUtils {
    /**
     * Get the Generic definition from a class for given class with given index.
     * @param clz Implementing class
     * @param class1 class with generic definition
     * @param index generic index
     * @return null if not found
     */
    public static Type getGenericDefiniton(Class clz, Class class1, int index) {
        Type[] t = getGenericDefinitons(clz, class1);
        if (t != null && t.length > index)
            return t[index];
        return null;
    }
    /**
     * Get the Generic definitions from a class for given class .
     * @param clz Implementing class
     * @param class1 class with generic definition
     * @return null if not found
     */
    public static Type[] getGenericDefinitons(Class clz, Class class1) {
        Type[] t = null;
        while (clz != null) {
            t = getGenericDefinitonsThis(clz, class1);
            if (t != null)
                return t;
            Class[] interfaces = clz.getInterfaces();
            for (Class class2 : interfaces) {
                t = getGenericDefinitonsThis(class2, class1);
                if (t != null)
                    return t;
            }
            clz = clz.getSuperclass();
        }
        return t;
    }
    /**
     * Get the Generic definitions from a class for given class without looking
     * super classes.
     * @param classFrom Implementing class
     * @param interfaceClz class with generic definition
     * @return null if not found
     */
    @SuppressWarnings("unchecked")
    public static Type[] getGenericDefinitonsThis(Class classFrom, Class interfaceClz) {
        Type[] genericInterfaces = classFrom.getGenericInterfaces();
        for (Type type : genericInterfaces) {
            if (type instanceof ParameterizedType) {
                ParameterizedType pt = (ParameterizedType) type;
                if (interfaceClz.isAssignableFrom((Class) pt.getRawType())) {
                    return pt.getActualTypeArguments();
                }
            }
        }
        // check if it if available on generic super class
        Type genericSuperclass = classFrom.getGenericSuperclass();
        if (genericSuperclass instanceof ParameterizedType) {
            ParameterizedType pt = (ParameterizedType) genericSuperclass;
            if (interfaceClz.equals(pt.getRawType())) {
                return pt.getActualTypeArguments();
            }
        }
        return null;
    }
}
```

1.  A simple generic class with two type parameters: T and V.
---  ---
2.  Java generic: Hierarchy argument
3.  Boxing Generic Example
4.  Demonstrate a raw generic type.
5.  T is a type parameter that will be replaced by a real type when an object of type Gen is created.
6.  Create a generic class that can compute the average of an array of numbers of any given type.
7.  the type argument for T must be either Number, or a class derived from Number.
8.  Demonstrate a raw type.
9.  A subclass can add its own type parameters.
10.  Compare two generic parameters
11.  Default implementation of {@link java.lang.reflect.ParameterizedType}
