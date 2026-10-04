---
title: Copying Objects implements Cloneable
nav: Copying Objects implements...
description: return super.toString() + "\nIt's " + name + " the " + species;
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20070225115345/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/CopyingObjectsimplementsCloneable.htm
---
```java title=Example.java
class Flea implements Cloneable {
  public Flea() {
  }
  public void setName(String aName) {
    name = aName;
  }
  public String getName() {
    return name;
  }
  public String getSpecies() {
    return species;
  }
  public void sound() {
    System.out.println("Psst");
  }
  public String toString() {
    return super.toString() + "\nIt's " + name + " the " + species;
  }
  public Object clone() throws CloneNotSupportedException {
    return super.clone();
  }
  private String name;
  private String species;
}
public class MainClass {
  public static void main(String[] args) {
    try {
      Flea myPet = new Flea();
      myPet.setName("my name");
      Flea yourPet = (Flea) myPet.clone();
      yourPet.setName("Gnasher");
      System.out.println("\nYour pet details:\n" + yourPet);
      System.out.println("\nMy pet details:\n" + myPet);
    } catch (CloneNotSupportedException e) {
      e.printStackTrace(System.err);
    }
  }
}
java title=Example.java
Your pet details:
Flea@360be0
It's Gnasher the null
My pet details:
Flea@45a877
It's my name the null
```
