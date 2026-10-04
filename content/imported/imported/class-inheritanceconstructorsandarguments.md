---
title: Inheritance, constructors and arguments
nav: Inheritance, constructors ...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20081230140546/http://www.java2s.com:80/Code/Java/Class/Inheritanceconstructorsandarguments.htm
---
```java title=Example.java
// : c06:Chess.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Game {
  Game(int i) {
    System.out.println("Game constructor");
  }
}
class BoardGame extends Game {
  BoardGame(int i) {
    super(i);
    System.out.println("BoardGame constructor");
  }
}
public class Chess extends BoardGame {
  Chess() {
    super(11);
    System.out.println("Chess constructor");
  }
  public static void main(String[] args) {
    Chess x = new Chess();
  }
} ///:~
```

1.  Combining composition and inheritance
---  ---
2.  Inheritance syntax and properties
3.  Composition for code reuse
4.  Cleanup and inheritance
5.  Proper inheritance of an inner class
6.  Extending an interface with inheritance
7.  Inheriting an inner class
