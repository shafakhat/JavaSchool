---
title: Deriving a Class
nav: Deriving a Class
description: Imported from the java2s.com archive: Deriving a Class
section: Imported - java2s Archive
order: 1203
source: https://web.archive.org/web/20140829075310/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/DerivingaClass.htm
---
```java title=Example.java
class Animal {
  public Animal(String aType) {
    type = aType;
  }
  public String toString() {
    return "This is a " + type;
  }
  private String type;
}
class Dog extends Animal {
  public Dog(String name){
    super(name);
  }
  private String breed;
}
```

| 5.22.1. | Inheritance |
|---|---|
| 5.22.2. | Accessibility |
| 5.22.3. | Method Overriding |
| 5.22.4. | The extends Keyword |
| 5.22.5. | Deriving a Class |
| 5.22.6. | The keyword super represents an instance of the direct superclass of the current object. |
| 5.22.7. | Derived Class Constructors: Calling the Base Class Constructor |
| 5.22.8. | Overriding a Base Class Method |
| 5.22.9. | Type Casting |
| 5.22.10. | Inheritance, constructors and arguments |
| 5.22.11. | Combining composition and inheritance |
| 5.22.12. | Inheritance and upcasting. |
| 5.22.13. | Overloading a base-class method name in a derived class does not hide the base-class versions. |
| 5.22.14. | Cleanup and inheritance |
| 5.22.15. | Creating a Multilevel Hierarchy |
| 5.22.16. | Demonstrate when constructors are called in a Multilevel Hierarchy |
