---
title: Use Class.forName to load a class
nav: Use Class.forName to load ...
description: Imported from the java2s.com archive: Use Class.forName to load a class
section: Imported - java2s Archive
order: 2216
source: https://web.archive.org/web/20140829075648/http://www.java2s.com/Tutorial/Java/0125__Reflection/UseClassforNametoloadaclass.htm
---
```java title=Example.java
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
public class Main{
  public static void main(String args[]) throws Exception {
    Class c = Class.forName("MyClass");
  }
}
class MyClass {
  private int count;
  MyClass(int c) {
    count = c;
  }
  MyClass() {
    count = 0;
  }
  void setCount(int c) {
    count = c;
  }
  int getCount() {
    return count;
  }
  void showcount() {
    System.out.println("count is " + count);
  }
}
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
