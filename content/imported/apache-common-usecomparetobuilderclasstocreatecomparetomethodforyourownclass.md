---
title: Use CompareToBuilder class to create compareTo method for your own class
nav: Use CompareToBuilder class...
description: Use CompareToBuilder class to create compareTo method for your own class
section: Imported - java2s Archive
order: 1072
source: https://web.archive.org/web/20100213232503/http://java2s.com/Code/Java/Apache-Common/UseCompareToBuilderclasstocreatecompareTomethodforyourownclass.htm
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

1.  Implement hashCode using commons-lang
---  ---
2.  Use Reflection To build toString method
3.  Implement equals method using commons-lang
4.  Jakarta Commons toString Builder
