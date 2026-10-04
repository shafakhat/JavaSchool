---
title: Combining composition and inheritance
nav: Combining composition and ...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1145
source: https://web.archive.org/web/20081230140536/http://www.java2s.com:80/Code/Java/Class/Combiningcompositionandinheritance.htm
---
```java title=Example.java
// : c06:PlaceSetting.java
// Combining composition & inheritance.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Plate {
  Plate(int i) {
    System.out.println("Plate constructor");
  }
}
class DinnerPlate extends Plate {
  DinnerPlate(int i) {
    super(i);
    System.out.println("DinnerPlate constructor");
  }
}
class Utensil {
  Utensil(int i) {
    System.out.println("Utensil constructor");
  }
}
class Spoon extends Utensil {
  Spoon(int i) {
    super(i);
    System.out.println("Spoon constructor");
  }
}
class Fork extends Utensil {
  Fork(int i) {
    super(i);
    System.out.println("Fork constructor");
  }
}
class Knife extends Utensil {
  Knife(int i) {
    super(i);
    System.out.println("Knife constructor");
  }
}
// A cultural way of doing something:
class Custom {
  Custom(int i) {
    System.out.println("Custom constructor");
  }
}
public class PlaceSetting extends Custom {
  private Spoon sp;
  private Fork frk;
  private Knife kn;
  private DinnerPlate pl;
  public PlaceSetting(int i) {
    super(i + 1);
    sp = new Spoon(i + 2);
    frk = new Fork(i + 3);
    kn = new Knife(i + 4);
    pl = new DinnerPlate(i + 5);
    System.out.println("PlaceSetting constructor");
  }
  public static void main(String[] args) {
    PlaceSetting x = new PlaceSetting(9);
  }
} ///:~
```

1.  Inheritance, constructors and arguments
---  ---
2.  Inheritance syntax and properties
3.  Composition for code reuse
4.  Cleanup and inheritance
5.  Proper inheritance of an inner class
6.  Extending an interface with inheritance
7.  Inheriting an inner class
