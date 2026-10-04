---
title: Compare two generic parameters
nav: Compare two generic parame...
description: } else if (arg1 instanceof Object[] && arg2 instanceof Object[]) {
section: Imported - java2s Archive
order: 1015
source: https://web.archive.org/web/20111124230651/http://java2s.com/Code/Java/Generics/Comparetwogenericparameters.htm
---
```java title=Example.java
//package com.webex.ta.hydra.util;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;
import java.util.Set;
/**
 * Created by Cisco WebEx.
 * User: vegaz
 * Date: 2010-10-20
 * Time: 15:18:50
 */
public class Comparing {
    private Comparing() {
    }
    public static <T> boolean equal(T arg1, T arg2) {
        if (arg1 == null || arg2 == null) {
            return arg1 == arg2;
        } else if (arg1 instanceof Object[] && arg2 instanceof Object[]) {
            Object[] arr1 = (Object[]) arg1;
            Object[] arr2 = (Object[]) arg2;
            return Arrays.equals(arr1, arr2);
        } else if (arg1 instanceof String && arg2 instanceof String) {
            return equal((String) arg1, (String) arg2, true);
        } else {
            return arg1.equals(arg2);
        }
    }
    public static <T> boolean equal(T[] arr1, T[] arr2) {
        if (arr1 == null || arr2 == null) {
            return arr1 == arr2;
        }
        return Arrays.equals(arr1, arr2);
    }
    public static boolean equal(String arg1, String arg2) {
        return equal(arg1, arg2, true);
    }
    public static boolean equal(String arg1, String arg2, boolean caseSensitive) {
        if (arg1 == null || arg2 == null) {
            return arg1 == arg2;
        } else {
            return caseSensitive ? arg1.equals(arg2) : arg1.equalsIgnoreCase(arg2);
        }
    }
    public static boolean strEqual(String arg1, String arg2) {
        return strEqual(arg1, arg2, true);
    }
    public static boolean strEqual(String arg1, String arg2, boolean caseSensitive) {
        return equal(arg1 == null ? "" : arg1, arg2 == null ? "" : arg2, caseSensitive);
    }
    public static <T> boolean haveEqualElements(Collection<T> a, Collection<T> b) {
        if (a.size() != b.size()) {
            return false;
        }
        Set<T> aSet = new HashSet<T>(a);
        for (T t : b) {
            if (!aSet.contains(t)) {
                return false;
            }
        }
        return true;
    }
    public static <T> boolean haveEqualElements(T[] a, T[] b) {
        if (a == null || b == null) {
            return a == b;
        }
        if (a.length != b.length) {
            return false;
        }
        Set<T> aSet = new HashSet<T>(Arrays.asList(a));
        for (T t : b) {
            if (!aSet.contains(t)) {
                return false;
            }
        }
        return true;
    }
    public static int hashcode(Object obj) {
        return obj == null ? 0 : obj.hashCode();
    }
    public static int hashcode(Object obj1, Object obj2) {
        return hashcode(obj1) ^ hashcode(obj2);
    }
    public static int compare(int name1, int name2) {
        return name1 < name2 ? -1 : name1 == name2 ? 0 : 1;
    }
    public static <T extends Comparable<T>> int compare(final T name1, final T name2) {
        if (name1 == null) return name2 == null ? 0 : -1;
        if (name2 == null) return 1;
        return name1.compareTo(name2);
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
10.  Default implementation of {@link java.lang.reflect.ParameterizedType}
11.  Get the Generic definition from a class for given class with given index.
