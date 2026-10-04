---
title: Combining both statements into one
nav: Combining both statements ...
description: System.out.println(new Animal("a").getClass().getName()); // Output the
section: Imported - java2s Archive
order: 1058
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/Combiningbothstatementsintoone.htm
---
```java title=Example.java
class Animal {
  public Animal(String aType) {
    type = aType;
  }
  public String toString() {
    return"This is a " + type;
  }
  private String type;
}
publicclass MainClass {
  publicstaticvoid main(String[] a) {
    System.out.println(new Animal("a").getClass().getName()); // Output the
// class name
  }
}
```

```java title=Example.java
Animal
```
