---
title: how to use reflection to print the names and values of all nonstatic fields of an object
nav: how to use reflection to p...
description: public static void main(String[] args) throws IllegalAccessException {
section: Imported - java2s Archive
order: 2138
source: https://web.archive.org/web/20140829075702/http://www.java2s.com/Tutorial/Java/0125__Reflection/howtousereflectiontoprintthenamesandvaluesofallnonstaticfieldsofanobject.htm
---
```java title=Example.java
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.Random;
public class Main {
  public static void main(String[] args) throws IllegalAccessException {
    Random r = new Random();
    System.out.print(spyFields(r));
    r.nextInt();
    System.out.println("\nAfter calling nextInt:\n");
    System.out.print(spyFields(r));
  }
  public static String spyFields(Object obj) throws IllegalAccessException {
    StringBuffer buffer = new StringBuffer();
    Field[] fields = obj.getClass().getDeclaredFields();
    for (Field f : fields) {
      if (!Modifier.isStatic(f.getModifiers())) {
        f.setAccessible(true);
        Object value = f.get(obj);
        buffer.append(f.getType().getName());
        buffer.append(" ");
        buffer.append(f.getName());
        buffer.append("=");
        buffer.append("" + value);
        buffer.append("\n");
      }
    }
    return buffer.toString();
  }
}
```

| 7.7.1. | URL class loader |
|---|---|
| 7.7.2. | extends URLClassLoader |
| 7.7.3. | Load classes |
| 7.7.4. | how to use reflection to print the names and values of all nonstatic fields of an object |
| 7.7.5. | Runs a jar application from any url |
| 7.7.6. | BufferedReader reflection |
| 7.7.7. | Get the class By way of an object |
| 7.7.8. | Get the class By way of a string |
| 7.7.9. | Get the class By way of .class |
| 7.7.10. | Catch InvocationTargetException |
| 7.7.11. | Determining from Where a Class Was Loaded |
| 7.7.12. | Dynamically Reloading a Modified Class |
| 7.7.13. | Creating an Object Using a Constructor Object |
| 7.7.14. | Create an object from a string |
| 7.7.15. | Using the forName() method |
| 7.7.16. | Context ClassLoader |
| 7.7.17. | A tree structure that maps inheritance hierarchies of classes |
| 7.7.18. | Analyze ClassLoader hierarchy for any given object or class loader |
| 7.7.19. | Instantiate unknown class at runtime and call the object's methods |
| 7.7.20. | Load Class |
