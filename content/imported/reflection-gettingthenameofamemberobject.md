---
title: Getting the Name of a Member Object
nav: Getting the Name of a Memb...
description: Imported from the java2s.com archive: Getting the Name of a Member Object
section: Imported - java2s Archive
order: 2204
source: https://web.archive.org/web/20140829075348/http://www.java2s.com/Tutorial/Java/0125__Reflection/GettingtheNameofaMemberObject.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
public class Main {
  public static void main(String[] argv) throws Exception {
    Class cls = java.lang.String.class;
    Method method = cls.getMethods()[0];
    Field field = cls.getFields()[0];
    Constructor constructor = cls.getConstructors()[0];
    String name;
    name = cls.getName();
    System.out.println(name);
    name = cls.getName() + "." + field.getName();
    System.out.println(name);
    name = constructor.getName();
    System.out.println(name);
    name = cls.getName() + "." + method.getName();
    System.out.println(name);
  }
}
/*
java.lang.String
java.lang.String.CASE_INSENSITIVE_ORDER
java.lang.String
java.lang.String.hashCode
*/
```

| 7.14.1. | Getting the Name of a Member Object |
|---|---|
| 7.14.2. | Unqualified names |
| 7.14.3. | Get full class name |
| 7.14.4. | Get the name of a class |
| 7.14.5. | Get the name of an array |
| 7.14.6. | Get the name of void |
| 7.14.7. | Get the unqualified name of a class |
| 7.14.8. | Get the fully-qualified name of a class |
| 7.14.9. | Get the fully-qualified name of a inner class |
| 7.14.10. | Use Class.forName to load a class |
| 7.14.11. | Get the class name in a static method |
