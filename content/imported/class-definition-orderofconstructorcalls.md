---
title: Order of constructor calls
nav: Order of constructor calls
description: Imported from the java2s.com archive: Order of constructor calls
section: Imported - java2s Archive
order: 1090
source: https://web.archive.org/web/20140829082830/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Orderofconstructorcalls.htm
---
```java title=Example.java
class Meal {
  Meal() {
    System.out.println("Meal()");
  }
}
class Bread {
  Bread() {
    System.out.println("Bread()");
  }
}
class Cheese {
  Cheese() {
    System.out.println("Cheese()");
  }
}
class Lettuce {
  Lettuce() {
    System.out.println("Lettuce()");
  }
}
class Lunch extends Meal {
  Lunch() {
    System.out.println("Lunch()");
  }
}
class PortableLunch extends Lunch {
  PortableLunch() {
    System.out.println("PortableLunch()");
  }
}
class Sandwich extends PortableLunch {
  private Bread b = new Bread();
  private Cheese c = new Cheese();
  private Lettuce l = new Lettuce();
  public Sandwich() {
    System.out.println("Sandwich()");
  }
}
public class MainClass {
  public static void main(String[] args) {
    new Sandwich();
  }
}
java title=Example.java
Meal()
Lunch()
PortableLunch()
Bread()
Cheese()
Lettuce()
Sandwich()
```

| 5.2.1. | Using Constructors |
|---|---|
| 5.2.2. | The Default Constructor |
| 5.2.3. | Multiple Constructors |
| 5.2.4. | Calling a Constructor From a Constructor |
| 5.2.5. | Duplicating Objects using a Constructor |
| 5.2.6. | Class Initializer: during declaration |
| 5.2.7. | Order of constructor calls |
