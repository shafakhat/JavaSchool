---
title: With concrete or abstract classes, inner classes are the only way to produce the effect of multiple implementation inheritance.
nav: With concrete or abstract ...
description: Imported from the java2s.com archive: With concrete or abstract classes, inner classes are the only way to produce the effect of multiple implementation inheritance.
section: Imported - java2s Archive
order: 1222
source: https://web.archive.org/web/20140829090900/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Withconcreteorabstractclassesinnerclassesaretheonlywaytoproducetheeffectofmultipleimplementationinheritance.htm
---
```java title=Example.java
class D {
}
abstract class E {
}
class Z extends D {
  E makeE() {
    return new E() {
    };
  }
}
public class MainClass {
  static void takesD(D d) {
  }
  static void takesE(E e) {
  }
  public static void main(String[] args) {
    Z z = new Z();
    takesD(z);
    takesE(z.makeE());
  }
}
```

| 5.14.1. | Creating instances of inner classes |
|---|---|
| 5.14.2. | Nested Classes |
| 5.14.3. | Creating a new nested object outside |
| 5.14.4. | Static Nested Classes |
| 5.14.5. | Creating inner classes |
| 5.14.6. | Defining references to inner classes |
| 5.14.7. | Nesting a class within a method |
| 5.14.8. | Nesting a class within a scope. |
| 5.14.9. | Nested classes (static inner classes) |
| 5.14.10. | An inner class cannot be overriden like a method |
| 5.14.11. | Two ways that a class can implement multiple interfaces |
| 5.14.12. | Nested classes can access all members of all levels of the classes they are nested within |
| 5.14.13. | Proper inheritance of an inner class. |
| 5.14.14. | Using inner classes for callbacks |
| 5.14.15. | Returning a reference to an inner class |
| 5.14.16. | Putting test code in a nested class |
| 5.14.17. | With concrete or abstract classes, inner classes are the only way to produce the effect of multiple implementation inheritance. |
| 5.14.18. | Local inner class can have a constructor |
