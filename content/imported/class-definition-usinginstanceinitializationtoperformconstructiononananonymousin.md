---
title: Using 'instance initialization' to perform construction on an anonymous inner class
nav: Using 'instance initializa...
description: Imported from the java2s.com archive: Using 'instance initialization' to perform construction on an anonymous inner class
section: Imported - java2s Archive
order: 1103
source: https://web.archive.org/web/20140829083044/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Usinginstanceinitializationtoperformconstructiononananonymousinnerclass.htm
---
```java title=Example.java
public class MainClass {
  public A dest(final String dest, final float price) {
    return new A() {
      private int cost;
      {
        cost = 100;
        System.out.println("Over budget!");
      }
      private String label = dest;
      public String readLabel() {
        return label;
      }
    };
  }
  public static void main(String[] args) {
    MainClass p = new MainClass();
    A d = p.dest("A", 101.395F);
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
