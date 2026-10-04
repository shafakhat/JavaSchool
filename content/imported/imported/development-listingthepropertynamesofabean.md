---
title: Listing the Property Names of a Bean
nav: Listing the Property Names...
description: Imported from java2s.com: Listing the Property Names of a Bean
section: Imported
order: 20059
source: http://www.java2s.com:80/Tutorial/Java/0120__Development/ListingthePropertyNamesofaBean.htm
---
```java title=Example.java
import java.beans.BeanInfo;
import java.beans.Introspector;
import java.beans.PropertyDescriptor;
public class Main {
  public static void main(String[] argv) throws Exception {
    BeanInfo bi = Introspector.getBeanInfo(MyBean.class);
    PropertyDescriptor[] pds = bi.getPropertyDescriptors();
    for (int i = 0; i < pds.length; i++) {
      String propName = pds[i].getDisplayName();
      System.out.println(propName);
    }
  }
}
class MyBean {
  public String getProp1() {
    return null;
  }
  public void setProp1(String s) {
  }
  public int getProp2() {
    return 0;
  }
  public void setProp2(int i) {
  }
  public byte[] getPROP3() {
    return null;
  }
  public void setPROP3(byte[] bytes) {
  }
}
```
