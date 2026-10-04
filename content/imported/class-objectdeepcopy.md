---
title: Object Deep copy
nav: Object Deep copy
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1049
source: https://web.archive.org/web/20111014011125/http://www.java2s.com:80/Code/Java/Class/ObjectDeepcopy.htm
---
Object Deep copy

```java title=Example.java
/*
 * Copyright 2009-2010 junithelper.org.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
 * either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
 */
//package org.junithelper.core.util;
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.List;
public final class ObjectUtil {
    private ObjectUtil() {
    }
    @SuppressWarnings("unchecked")
    public static <T> T deepCopy(T obj) {
        try {
            if (obj == null) {
                return null;
            }
            Class<?> clazz = obj.getClass();
            T clone = (T) clazz.newInstance();
            Field[] fields = clazz.getDeclaredFields();
            for (int i = 0; i < fields.length; i++) {
                Field field = fields[i];
                field.setAccessible(true);
                if (!Modifier.isFinal(field.getModifiers())) {
                    if (field.get(obj) instanceof List<?>) {
                        List<?> copiedList = deepCopyList((List<?>) field.get(obj));
                        field.set(clone, copiedList);
                    } else {
                        field.set(clone, field.get(obj));
                    }
                }
            }
            while (true) {
                if (Object.class.equals(clazz)) {
                    break;
                }
                clazz = clazz.getSuperclass();
                Field[] sFields = clazz.getDeclaredFields();
                for (int i = 0; i < sFields.length; i++) {
                    Field field = sFields[i];
                    field.setAccessible(true);
                    if (!Modifier.isFinal(field.getModifiers())) {
                        if (field.get(obj) instanceof List<?>) {
                            List<?> copiedList = deepCopyList((List<?>) field.get(obj));
                            field.set(clone, copiedList);
                        } else {
                            field.set(clone, field.get(obj));
                        }
                    }
                }
            }
            return clone;
        } catch (InstantiationException e) {
            return null;
        } catch (IllegalAccessException e) {
            return null;
        }
    }
    public static <T> List<T> deepCopyList(List<T> arg) {
        if (arg == null) {
            return null;
        }
        List<T> retList = new ArrayList<T>();
        for (T each : arg) {
            retList.add(deepCopy(each));
        }
        return retList;
    }
}
/*
package org.junithelper.core.util;
import org.junit.Test;
import org.junithelper.core.meta.ArgTypeMeta;
import org.junithelper.core.meta.MethodMeta;
import java.util.ArrayList;
import java.util.List;
import static org.junit.Assert.*;
public class ObjectUtilTest {
    @Test
    public void deepCopy_A$T_paramNull() throws Exception {
        Object arg = null;
        Object res = ObjectUtil.deepCopy(arg);
        assertNull(res);
        assertNull(arg);
    }
    @Test
    public void deepCopy_A$T_paramObject() throws Exception {
        Object arg = new Object();
        Object res = ObjectUtil.deepCopy(arg);
        assertNotSame(res, arg);
    }
    @Test
    public void deepCopy_A$T_paramClass() throws Exception {
        Object arg = new Object();
        Object res = ObjectUtil.deepCopy(arg);
        assertNotSame(res, arg);
    }
    @Test
    public void deepCopy_A$T_MethodInfo() throws Exception {
        MethodMeta arg = new MethodMeta();
        arg.argTypes.add(new ArgTypeMeta());
        arg.isStatic = true;
        arg.name = "hogehoge";
        MethodMeta res = ObjectUtil.deepCopy(arg);
        assertNotSame(arg.argTypes, res.argTypes);
        assertNotSame(arg.argTypes.get(0), res.argTypes.get(0));
        assertEquals(arg.isStatic, res.isStatic);
        assertEquals(arg.name, res.name);
    }
    @Test
    public void deepCopyList_A$List_List() throws Exception {
        List<Object> arg = new ArrayList<Object>();
        arg.add(new Object());
        arg.add(new Object());
        List<Object> result = ObjectUtil.deepCopyList(arg);
        assertNotSame(result, arg);
        assertNotSame(result.get(0), arg.get(0));
        assertNotSame(result.get(0), arg.get(0));
    }
    @Test
    public void deepCopyList_A$List_empty() throws Exception {
        List<Object> arg = new ArrayList<Object>();
        List<Object> result = ObjectUtil.deepCopyList(arg);
        assertNotSame(result, arg);
    }
    @Test
    public void deepCopyList_A$List_null() throws Exception {
        List<Object> arg = null;
        List<Object> result = ObjectUtil.deepCopyList(arg);
        assertSame(result, arg);
    }
    @Test
    public void type() throws Exception {
        assertNotNull(ObjectUtil.class);
    }
    @Test
    public void deepCopy_A$Object_null() throws Exception {
        // given
        Object obj = null;
        // when
        Object actual = ObjectUtil.deepCopy(obj);
        // then
        Object expected = null;
        assertEquals(expected, actual);
    }
    @Test
    public void deepCopy_A$Object_notNull() throws Exception {
        // given
        Object obj = new ObjectUtilTest();
        // when
        Object actual = ObjectUtil.deepCopy(obj);
        // then
        Object expected = obj;
        assertFalse(expected == actual);
    }
}
*/
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
31.  Deep-copies the values from one object to the other
