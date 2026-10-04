---
title: Convert an XML persistence to bean
nav: Convert an XML persistence...
description: XMLDecoder decoder = new XMLDecoder(new BufferedInputStream(new FileInputStream("Bean.xml")));
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/20100624051652/http://www.java2s.com:80/Tutorial/Java/0120__Development/ConvertanXMLpersistencetobean.htm
---
```java title=Example.java
import java.beans.XMLDecoder;
import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.Serializable;
public class Main {
  public static void main(String[] argv) throws Exception {
    XMLDecoder decoder = new XMLDecoder(new BufferedInputStream(new FileInputStream("Bean.xml")));
    Bean bean = (Bean) decoder.readObject();
    decoder.close();
    System.out.println("ID = " + bean.getId());
  }
}
class Bean implements Serializable {
  private Long id;
  public Long getId() {
    return id;
  }
  public void setId(Long id) {
    this.id = id;
  }
}
Here is our Bean.xml persistence file:
<?xml version="1.0" encoding="UTF-8"?>
<java version="1.6.0_02" class="java.beans.XMLDecoder">
 <object class="org.username.example.bean.BeanToXML">
  <void property="id">
   <long>1</long>
  </void>
 </object>
</java>
```
