---
title: Enum type field
nav: Enum type field
description: Imported from the java2s.com archive: Enum type field
section: Imported - java2s Archive
order: 1035
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Enumtypefield.htm
---
```java title=Example.java
publicclass ShirtTest {
  publicstaticvoid main(String[] args) {
    Shirt shirt1 = new Shirt();
    shirt1.setName("new name");
    shirt1.setBid(23.5);
    shirt1.setSize(Size.M);
    System.out.println(shirt1);
  }
}
class Shirt {
  private String name;
  privatedouble bid;
  private Size size;
  public Shirt() {
  }
  publicvoid setName(String name) {
    this.name = name;
  }
  public String getName() {
    return name;
  }
  publicvoid setBid(double bid) {
    this.bid = bid;
  }
  publicdouble getBid() {
    return bid;
  }
  publicvoid setSize(Size size) {
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
