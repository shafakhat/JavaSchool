---
title: Get the class name in a static method
nav: Get the class name in a st...
description: System.out.println("in " + new CurrentClassGetter().getClassName() + " class");
section: Imported - java2s Archive
order: 2214
source: https://web.archive.org/web/20140829075242/http://www.java2s.com/Tutorial/Java/0125__Reflection/Gettheclassnameinastaticmethod.htm
---
```java title=Example.java
public class Main{
  public static void main(java.lang.String[] args) {
    System.out.println("in " + new CurrentClassGetter().getClassName() + " class");
  }
}
 class CurrentClassGetter extends SecurityManager {
  public String getClassName() {
    return getClassContext()[1].getName();
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
