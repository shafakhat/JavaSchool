---
title: Putting test code in a nested class
nav: Putting test code in a nes...
description: Imported from the java2s.com archive: Putting test code in a nested class
section: Imported - java2s Archive
order: 1213
source: https://web.archive.org/web/20140829090808/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Puttingtestcodeinanestedclass.htm
---
```java title=Example.java
public class MainClass {
  public MainClass() {
  }
  public void f() {
    System.out.println("f()");
  }
  public static class Tester {
    public static void main(String[] args) {
      MainClass t = new MainClass();
      t.f();
    }
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
