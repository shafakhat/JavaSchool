---
title: The protected keyword
nav: The protected keyword
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1081
source: https://web.archive.org/web/20090411121732/http://www.java2s.com:80/Code/Java/Class/Theprotectedkeyword.htm
---
The protected keyword

```java title=Example.java
// : c06:Orc.java
// The protected keyword.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Villain {
  private String name;
  protected void set(String nm) {
    name = nm;
  }
  public Villain(String name) {
    this.name = name;
  }
  public String toString() {
    return "I'm a Villain and my name is " + name;
  }
}
public class Orc extends Villain {
  private int orcNumber;
  public Orc(String name, int orcNumber) {
    super(name);
    this.orcNumber = orcNumber;
  }
  public void change(String name, int orcNumber) {
    set(name); // Available because it's protected
    this.orcNumber = orcNumber;
  }
  public String toString() {
    return "Orc " + orcNumber + ": " + super.toString();
  }
  public static void main(String[] args) {
    Orc orc = new Orc("Limburger", 12);
    System.out.println(orc);
    orc.change("Bob", 19);
    System.out.println(orc);
  }
} ///:~
```

1.  Visibility
2.  Composition with public objects
