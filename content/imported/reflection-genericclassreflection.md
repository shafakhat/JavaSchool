---
title: Generic class Reflection
nav: Generic class Reflection
description: Imported from the java2s.com archive: Generic class Reflection
section: Imported - java2s Archive
order: 2172
source: https://web.archive.org/web/20140829081835/http://www.java2s.com/Tutorial/Java/0125__Reflection/GenericclassReflection.htm
---
```java title=Example.java
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.lang.reflect.TypeVariable;
import java.util.ArrayList;
import java.util.List;
public class GenericReflect {
  public static void main(String[] args) {
    TypeVariable[] tv = List.class.getTypeParameters();
    System.out.println(tv[0].getName()); // E
    class StringList extends ArrayList<String> {
    }
    Type type = StringList.class.getGenericSuperclass();
    System.out.println(type);
    ParameterizedType pt = (ParameterizedType) type;
    System.out.println(pt.getActualTypeArguments()[0]);
  }
}
```

7.10.1.  Generic class Reflection
