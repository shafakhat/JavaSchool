---
title: Derived Class Constructors
nav: Derived Class Constructors
description: Imported from the java2s.com archive: Derived Class Constructors
section: Imported - java2s Archive
order: 1285
source: https://web.archive.org/web/20140829075145/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DerivedClassConstructorsCallingtheBaseClassConstructor.htm
---
```java title=Example.java
class Animal {
  public Animal(String aType) {
    type = new String(aType);
  }
  public String toString() {
    return "This is a " + type;
  }
  private String type;
}
class Dog extends Animal {
  public Dog(String aName) {
    super("Dog");
    name = aName;
    breed = "Unknown";
  }
  public Dog(String aName, String aBreed) {
    super("Dog");
    name = aName;
    breed = aBreed;
  }
  private String name;
  private String breed;
}
```
