---
title: Use CompareToBuilder class to create compareTo method for your own class
nav: Use CompareToBuilder class...
description: System.out.println(orange.getName() + " == " + watermelon.getName());
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20140829084035/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/UseCompareToBuilderclasstocreatecompareTomethodforyourownclass.htm
---
```java title=Example.java
import org.apache.commons.lang.builder.CompareToBuilder;
public class Main {
  public static void main(String[] args) {
    Fruit orange = new Fruit("A", "B");
    Fruit watermelon = new Fruit("C", "D");
    if (orange.compareTo(watermelon) == 0) {
      System.out.println(orange.getName() + " == " + watermelon.getName());
    } else {
      System.out.println(orange.getName() + " != " + watermelon.getName());
    }
  }
}
class Fruit {
  private String name;
  private String colour;
  public Fruit(String name, String colour) {
    this.name = name;
    this.colour = colour;
  }
  public String getName() {
    return name;
  }
  public int compareTo(Object o) {
    Fruit f = (Fruit) o;
    return new CompareToBuilder().append(this.name, f.name).append(this.colour, f.colour)
        .toComparison();
  }
}
```

| 5.19.1. | Comparing Objects |
|---|---|
| 5.19.2. | Implement equals method using commons-lang |
| 5.19.3. | Use CompareToBuilder class to create compareTo method for your own class |
| 5.19.4. | Define your own equals method |
