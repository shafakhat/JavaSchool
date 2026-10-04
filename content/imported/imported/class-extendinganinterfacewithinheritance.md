---
title: Extending an interface with inheritance
nav: Extending an interface wit...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20081230150644/http://www.java2s.com:80/Code/Java/Class/Extendinganinterfacewithinheritance.htm
---
```java title=Example.java
// : c08:HorrorShow.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
interface Monster {
  void menace();
}
interface DangerousMonster extends Monster {
  void destroy();
}
interface Lethal {
  void kill();
}
class DragonZilla implements DangerousMonster {
  public void menace() {
  }
  public void destroy() {
  }
}
interface Vampire extends DangerousMonster, Lethal {
  void drinkBlood();
}
class VeryBadVampire implements Vampire {
  public void menace() {
  }
  public void destroy() {
  }
  public void kill() {
  }
  public void drinkBlood() {
  }
}
public class HorrorShow {
  static void u(Monster b) {
    b.menace();
  }
  static void v(DangerousMonster d) {
    d.menace();
    d.destroy();
  }
  static void w(Lethal l) {
    l.kill();
  }
  public static void main(String[] args) {
    DangerousMonster barney = new DragonZilla();
    u(barney);
    v(barney);
    Vampire vlad = new VeryBadVampire();
    u(vlad);
    v(vlad);
    w(vlad);
  }
} ///:~
```

1.  Combining composition and inheritance
---  ---
2.  Inheritance, constructors and arguments
3.  Inheritance syntax and properties
4.  Composition for code reuse
5.  Cleanup and inheritance
6.  Proper inheritance of an inner class
7.  Inheriting an inner class
