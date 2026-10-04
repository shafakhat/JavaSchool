---
title: Get Generic Parameter
nav: Get Generic Parameter
description: * Licensed under the Apache License, Version 2.0 (the "License");
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20111009070801/http://java2s.com:80/Code/Java/Generics/GetGenericParameter.htm
---
Get Generic Parameter

```java title=Example.java
/*
 * Copyright 2008-2010 the T2 Project ant the Others.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
//package org.t2framework.commons.util;
import java.lang.reflect.Array;
import java.lang.reflect.GenericArrayType;
import java.lang.reflect.GenericDeclaration;
import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.lang.reflect.TypeVariable;
import java.util.Collection;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
public class GenericsUtil {
  public static Type[] getGenericParameter(final Type type) {
    if (ParameterizedType.class.isInstance(type)) {
      return ParameterizedType.class.cast(type).getActualTypeArguments();
    } else if (GenericArrayType.class.isInstance(type)) {
      final Type genericComponentType = GenericArrayType.class.cast(type)
          .getGenericComponentType();
      return getGenericParameter(genericComponentType);
    } else if (Class.class.isInstance(type)) {
      return Class.class.cast(type).getTypeParameters();
    } else {
      return null;
    }
  }
  public static Type getGenericParameter(final Type type, final int index) {
    if (ParameterizedType.class.isInstance(type) == false) {
      return null;
    }
    final Type[] genericParameter = getGenericParameter(type);
    if (genericParameter == null) {
      return null;
    }
    return genericParameter[index];
  }
}
```

1.  Generic Reflection Test
