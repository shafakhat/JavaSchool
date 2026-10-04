---
title: Initializing interface fields with non-constant initializers
nav: Initializing interface fie...
description: Imported from the java2s.com archive: Initializing interface fields with non-constant initializers
section: Imported - java2s Archive
order: 1156
source: https://web.archive.org/web/20140829085312/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Initializinginterfacefieldswithnonconstantinitializers.htm
---
```java title=Example.java
import java.util.Random;
public class MainClass {
  public static void main(String[] args) {
    System.out.println(RandVals.randomInt);
    System.out.println(RandVals.randomLong);
    System.out.println(RandVals.randomFloat);
    System.out.println(RandVals.randomDouble);
  }
}
interface RandVals {
  Random rand = new Random();
  int randomInt = rand.nextInt(10);
  long randomLong = rand.nextLong() * 10;
  float randomFloat = rand.nextLong() * 10;
  double randomDouble = rand.nextDouble() * 10;
}
java title=Example.java
3
-6942612165866507216
-8.1946244E18
5.045338828500432
```

| 5.29.1. | Interfaces and Abstract Classes |
|---|---|
| 5.29.2. | Fields and Methods in an Interface |
| 5.29.3. | To implement an interface: use the implements keyword after the class declaration |
| 5.29.4. | A Partial Interface Implementation |
| 5.29.5. | Extending Interfaces |
| 5.29.6. | Interfaces and Multiple Inheritance |
| 5.29.7. | Interfaces and Polymorphism: Using Multiple Interfaces |
| 5.29.8. | Nesting Classes in an Interface Definition |
| 5.29.9. | Encapsulating Constants in a Program |
| 5.29.10. | Multiple interfaces |
| 5.29.11. | Initializing interface fields with non-constant initializers |
