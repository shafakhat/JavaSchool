---
title: Inside main( ), the static method callme( ) and the static variable b are accessed outside of their class.
nav: Inside main( ), the static...
description: Imported from the java2s.com archive: Inside main( ), the static method callme( ) and the static variable b are accessed outside of their class.
section: Imported - java2s Archive
order: 1216
source: https://web.archive.org/web/20140829082530/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Insidemainthestaticmethodcallmeandthestaticvariablebareaccessedoutsideoftheirclass.htm
---
```java title=Example.java
class StaticDemo {
  static int a = 42;
  static int b = 99;
  static void callme() {
    System.out.println("a = " + a);
  }
}
class StaticByName {
  public static void main(String args[]) {
    StaticDemo.callme();
    System.out.println("b = " + StaticDemo.b);
  }
}
```

| 5.12.1. | Static Members |
|---|---|
| 5.12.2. | Define the static member |
| 5.12.3. | Demonstrate static variables, methods, and blocks. |
| 5.12.4. | Inside main( ), the static method callme( ) and the static variable b are accessed outside of their class. |
| 5.12.5. | reference static field after declaration |
| 5.12.6. | static section of Initializer |
| 5.12.7. | static section Initializer and logic |
| 5.12.8. | Initializer for final static field |
| 5.12.9. | Demonstrates Static nested Classes |
| 5.12.10. | Reference inner static class |
| 5.12.11. | Static field, constructor and exception |
