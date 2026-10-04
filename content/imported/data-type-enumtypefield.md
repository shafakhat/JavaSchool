---
title: Enum type field
nav: Enum type field
description: Imported from the java2s.com archive: Enum type field
section: Imported - java2s Archive
order: 1150
source: https://web.archive.org/web/20140829075748/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Enumtypefield.htm
---
```java title=Example.java
public class ShirtTest {
  public static void main(String[] args) {
    Shirt shirt1 = new Shirt();
    shirt1.setName("new name");
    shirt1.setBid(23.5);
    shirt1.setSize(Size.M);
    System.out.println(shirt1);
  }
}
class Shirt {
  private String name;
  private double bid;
  private Size size;
  public Shirt() {
  }
  public void setName(String name) {
    this.name = name;
  }
  public String getName() {
    return name;
  }
  public void setBid(double bid) {
    this.bid = bid;
  }
  public double getBid() {
    return bid;
  }
  public void setSize(Size size) {
    this.size = size;
  }
  public Size getSize() {
    return size;
  }
  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append(" Name: " + this.getName() + ",");
    sb.append(" Bid: " + this.getBid() + " Dollar,");
    sb.append(" Size: " + this.getSize());
    return sb.toString();
  }
}
enum Size {
  S, M, L, XL, XXL, XXXL;
}
```

| 2.43.1. | Enumeration Fundamentals |
|---|---|
| 2.43.2. | How to define an enumeration |
| 2.43.3. | Enums in a Class |
| 2.43.4. | equals and = operator for enum data type |
| 2.43.5. | Comparing Enumeration Values |
| 2.43.6. | Two enumeration constants can be compared for equality by using the == relational operator |
| 2.43.7. | uses an enum, rather than interface variables, to represent the answers. |
| 2.43.8. | enum type with its own method |
| 2.43.9. | Enum type field |
| 2.43.10. | enum with switch |
