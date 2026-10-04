---
title: Create a Singleton Object
nav: Create a Singleton Object
description: Imported from the java2s.com archive: Create a Singleton Object
section: Imported - java2s Archive
order: 1155
source: https://web.archive.org/web/20090530095635/http://www.java2s.com:80/Code/Java/Class/CreateaSingletonObject.htm
---
```java title=Example.java
class MySingleton {
  // the static singleton object
  private static MySingleton theObject;
  private MySingleton() {
  }
  public static MySingleton createMySingleton() {
    if (theObject == null)
      theObject = new MySingleton();
    return theObject;
  }
}
public class Main {
  public static void main(String[] args) {
    MySingleton ms1 = MySingleton.createMySingleton();
    MySingleton ms2 = MySingleton.createMySingleton();
    System.out.println(ms1 == ms2);
  }
}
```

1.  Visibility
---  ---
2.  Composition with public objects
3.  The protected keyword
