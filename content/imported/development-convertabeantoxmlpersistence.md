---
title: Convert a bean to XML persistence
nav: Convert a bean to XML pers...
description: XMLEncoder encoder = new XMLEncoder(new BufferedOutputStream(new FileOutputStream("Bean.xml")));
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20100624051647/http://www.java2s.com:80/Tutorial/Java/0120__Development/ConvertabeantoXMLpersistence.htm
---
```java title=Example.java
import java.beans.XMLEncoder;
import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
public class Main {
  public static void main(String[] args) throws Exception {
    Item bean = new Item();
    bean.setId(new Long(1));
    bean.setItemName("a");
    bean.setItemColour("Red");
    bean.setItemQuantities(new Integer(100));
    XMLEncoder encoder = new XMLEncoder(new BufferedOutputStream(new FileOutputStream("Bean.xml")));
    encoder.writeObject(bean);
    encoder.close();
  }
}
class Item {
  private Long id;
  private String itemName;
  private String itemColour;
  private Integer itemQuantities;
  public Long getId() {
    return id;
  }
  public void setId(Long id) {
    this.id = id;
  }
  public String getItemName() {
    return itemName;
  }
  public void setItemName(String itemName) {
    this.itemName = itemName;
  }
  public String getItemColour() {
    return itemColour;
  }
  public void setItemColour(String itemColour) {
    this.itemColour = itemColour;
  }
  public Integer getItemQuantities() {
    return itemQuantities;
  }
  public void setItemQuantities(Integer itemQuantities) {
    this.itemQuantities = itemQuantities;
  }
}
```
