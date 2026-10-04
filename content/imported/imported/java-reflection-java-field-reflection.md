---
title: Java Reflection - Java Field Reflection
nav: Java Reflection - Java Fie...
description: We can use java.lang.reflect.Field class to get information about a field in a class.
section: Imported - java2s Archive
order: 50404
source: https://www.java2s.com/Tutorials/Java/Java_Reflection/0040__Java_Field_Reflection.html
---
```java title=Example.java
```

We can use java.lang.reflect.Field class to get information about a field in a class.

The following four methods in the Class class can return Field object about the fields.

```java title=Example.java

Field[] getFields()
Field[] getDeclaredFields()
Field getField(String name)
Field getDeclaredField(String name)
```

The getFields() method returns all the accessible public fields declared in the class or inherited from the superclass.

The getDeclaredFields() method returns all the fields that appear in the declaration of the class only(not from inherited fields).

getField(String name) and getDeclaredField(String name) get the Field object by the field name.

## Example

```java title=Example.java
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
/*www.java2s.com*/class MySuperClass {
  publicint super_id = -1;
  public String super_name = "Unknown";
}
class MyClass extends MySuperClass{
  publicint id = -1;
  public String name = "Unknown";
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    Class<MyClass> c = MyClass.class;
    // Print declared fields
    ArrayList<String> fieldsDesciption = getDeclaredFieldsList(c);
    System.out.println("Declared Fields for " + c.getName());
    for (String desc : fieldsDesciption) {
      System.out.println(desc);
    }
    fieldsDesciption = getFieldsList(c);
    System.out.println("\nAccessible Fields for " + c.getName());
    for (String desc : fieldsDesciption) {
      System.out.println(desc);
    }
  }
  publicstatic ArrayList<String> getFieldsList(Class c) {
    Field[] fields = c.getFields();
    ArrayList<String> fieldsList = getFieldsDesciption(fields);
    return fieldsList;
  }
  publicstatic ArrayList<String> getDeclaredFieldsList(Class c) {
    Field[] fields = c.getDeclaredFields();
    ArrayList<String> fieldsList = getFieldsDesciption(fields);
    return fieldsList;
  }
  publicstatic ArrayList<String> getFieldsDesciption(Field[] fields) {
    ArrayList<String> fieldList = new ArrayList<>();
    for (Field f : fields) {
      int mod = f.getModifiers() & Modifier.fieldModifiers();
      String modifiers = Modifier.toString(mod);
      Class<?> type = f.getType();
      String typeName = type.getSimpleName();
      String fieldName = f.getName();
      fieldList.add(modifiers + "  " + typeName + "  " + fieldName);
    }
    return fieldList;
  }
}
```

The code above generates the following result.

- « Previous
