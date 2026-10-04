---
title: An anonymous inner class that performs initialization
nav: An anonymous inner class t...
description: Imported from the java2s.com archive: An anonymous inner class that performs initialization
section: Imported - java2s Archive
order: 1106
source: https://web.archive.org/web/20140829083240/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Ananonymousinnerclassthatperformsinitialization.htm
---
```java title=Example.java
public class MainClass {
  public A dest(final String dest) {
    return new A() {
      private String label = dest;
      public String readLabel() {
        return label;
      }
    };
  }
  public static void main(String[] args) {
    MainClass p = new MainClass();
    A d = p.dest("A");
  }
}
interface A {
  String readLabel();
}
```

| 5.15.1. | Demonstrate an inner class. |
|---|---|
| 5.15.2. | Define an inner class within a for loop. |
| 5.15.3. | Use anonymous inner classes |
| 5.15.4. | Building the anonymous inner class in-place |
| 5.15.5. | Anonymous inner class cannot have a named constructor, only an instance initializer |
| 5.15.6. | Creating a constructor for an anonymous inner class |
| 5.15.7. | Using 'instance initialization' to perform construction on an anonymous inner class |
| 5.15.8. | Argument must be final to use inside anonymous inner class |
| 5.15.9. | A method that returns an anonymous inner class |
| 5.15.10. | An anonymous inner class that calls the base-class constructor |
| 5.15.11. | An anonymous inner class that performs initialization |
| 5.15.12. | Demonstrates method-scoped inner classes |
| 5.15.13. | Demonstrates anonymous classes |
| 5.15.14. | Demonstration of some static nested classes |
| 5.15.15. | Access inner class from outside |
| 5.15.16. | Accessing its enclosing instance from an inner class |
