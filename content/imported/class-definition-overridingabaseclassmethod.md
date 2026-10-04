---
title: Overriding a Base Class Method
nav: Overriding a Base Class Me...
description: Imported from the java2s.com archive: Overriding a Base Class Method
section: Imported - java2s Archive
order: 1286
source: https://web.archive.org/web/20140829075157/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/OverridingaBaseClassMethod.htm
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
  public String toString() {
    return "It's " + name + " the " + breed;
  }
  private String name;
  private String breed;
}
```
