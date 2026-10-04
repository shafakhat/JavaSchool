---
title: Default implementation of {@link java.lang.reflect.ParameterizedType}
nav: Default implementation of ...
description: Default implementation of {@link java.lang.reflect.ParameterizedType}
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20111124225913/http://java2s.com/Code/Java/Generics/DefaultimplementationoflinkjavalangreflectParameterizedType.htm
---
Default implementation of {@link java.lang.reflect.ParameterizedType}

```java title=Example.java
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
//package org.bridj.util;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
/**
 * Default implementation of {@link java.lang.reflect.ParameterizedType}
 *
 * @author Olivier
 */
public class DefaultParameterizedType implements ParameterizedType {
  private final Type[] actualTypeArguments;
  private final Type ownerType;
  private final Type rawType;
  public DefaultParameterizedType(Type ownerType, Type rawType,
      Type[] actualTypeArguments) {
    this.ownerType = ownerType;
    this.actualTypeArguments = actualTypeArguments;
    this.rawType = rawType;
  }
  public DefaultParameterizedType(Type rawType, Type... actualTypeArguments) {
    this(null, rawType, actualTypeArguments);
  }
  public static Type paramType(Type rawType, Type... actualTypeArguments) {
    return new DefaultParameterizedType(rawType, actualTypeArguments);
  }
  @Override
  public Type[] getActualTypeArguments() {
    return actualTypeArguments.clone();
  }
  @Override
  public java.lang.reflect.Type getOwnerType() {
    return ownerType;
  }
  @Override
  public java.lang.reflect.Type getRawType() {
    return rawType;
  }
  @Override
  public int hashCode() {
    int h = getRawType().hashCode();
    if (getOwnerType() != null)
      h ^= getOwnerType().hashCode();
    for (int i = 0, n = actualTypeArguments.length; i < n; i++)
      h ^= actualTypeArguments[i].hashCode();
    return h;
  }
  static boolean eq(Object a, Object b) {
    if ((a == null) != (b == null))
      return false;
    if (a != null && !a.equals(b))
      return false;
    return true;
  }
  @Override
  public boolean equals(Object o) {
    if (o == null || !(o instanceof DefaultParameterizedType))
      return false;
    DefaultParameterizedType t = (DefaultParameterizedType) o;
    if (!eq(getRawType(), t.getRawType()))
      return false;
    if (!eq(getOwnerType(), t.getOwnerType()))
      return false;
    Object[] tp = t.actualTypeArguments;
    if (actualTypeArguments.length != tp.length)
      return false;
    for (int i = 0, n = actualTypeArguments.length; i < n; i++)
      if (!eq(actualTypeArguments[i], tp[i]))
        return false;
    return true;
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
11.  Get the Generic definition from a class for given class with given index.
