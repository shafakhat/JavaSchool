---
title: Get the unqualified name of a class
nav: Get the unqualified name o...
description: name = name.substring(name.lastIndexOf('.') + 1); // Map$Entry
section: Imported - java2s Archive
order: 2223
source: https://web.archive.org/web/20140829075619/http://www.java2s.com/Tutorial/Java/0125__Reflection/Gettheunqualifiednameofaclass.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] argv) throws Exception {
    Class cls = java.util.Map.Entry.class;
    String name = cls.getName();
    if (name.lastIndexOf('.') > 0) {
      name = name.substring(name.lastIndexOf('.') + 1); // Map$Entry
      name = name.replace('$', '.');      // Map.Entry
    }
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
