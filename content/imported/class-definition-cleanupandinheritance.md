---
title: Cleanup and inheritance
nav: Cleanup and inheritance
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1292
source: https://web.archive.org/web/20140829075333/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Cleanupandinheritance.htm
---
```java title=Example.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Characteristic {
  private String s;
  Characteristic(String s) {
    this.s = s;
    System.out.println("Creating Characteristic " + s);
  }
  protected void dispose() {
    System.out.println("finalizing Characteristic " + s);
  }
}
class Description {
  private String s;
  Description(String s) {
    this.s = s;
    System.out.println("Creating Description " + s);
  }
  protected void dispose() {
    System.out.println("finalizing Description " + s);
  }
}
class LivingCreature {
  private Characteristic p = new Characteristic("is alive");
  private Description t = new Description("Basic Living Creature");
  LivingCreature() {
    System.out.println("LivingCreature()");
  }
  protected void dispose() {
    System.out.println("LivingCreature dispose");
    t.dispose();
    p.dispose();
  }
}
class Animal extends LivingCreature {
  private Characteristic p = new Characteristic("has heart");
  private Description t = new Description("Animal not Vegetable");
  Animal() {
    System.out.println("Animal()");
  }
  protected void dispose() {
    System.out.println("Animal dispose");
    t.dispose();
    p.dispose();
    super.dispose();
  }
}
class Amphibian extends Animal {
  private Characteristic p = new Characteristic("can live in water");
  private Description t = new Description("Both water and land");
  Amphibian() {
    System.out.println("Amphibian()");
  }
  protected void dispose() {
    System.out.println("Amphibian dispose");
    t.dispose();
    p.dispose();
    super.dispose();
  }
}
class Frog extends Amphibian {
  private Characteristic p = new Characteristic("Croaks");
  private Description t = new Description("Eats Bugs");
  public Frog() {
    System.out.println("Frog()");
  }
  protected void dispose() {
    System.out.println("Frog dispose");
    t.dispose();
    p.dispose();
    super.dispose();
  }
}
public class MainClass {
  public static void main(String[] args) {
    Frog frog = new Frog();
    System.out.println("Bye!");
    frog.dispose();
  }
}
java title=Example.java
Creating Characteristic is alive
Creating Description Basic Living Creature
LivingCreature()
Creating Characteristic has heart
Creating Description Animal not Vegetable
Animal()
Creating Characteristic can live in water
Creating Description Both water and land
Amphibian()
Creating Characteristic Croaks
Creating Description Eats Bugs
Frog()
Bye!
Frog dispose
finalizing Description Eats Bugs
finalizing Characteristic Croaks
Amphibian dispose
finalizing Description Both water and land
finalizing Characteristic can live in water
Animal dispose
finalizing Description Animal not Vegetable
finalizing Characteristic has heart
LivingCreature dispose
finalizing Description Basic Living Creature
finalizing Characteristic is alive
```
