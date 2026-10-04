---
title: Create an instance a Bean
nav: Create an instance a Bean
description: Main bean = (Main) Beans.instantiate(ClassLoader.getSystemClassLoader(),
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20100624051658/http://www.java2s.com:80/Tutorial/Java/0120__Development/CreateaninstanceaBean.htm
---
```java title=Example.java
import java.beans.Beans;
import java.io.Serializable;
public class Main implements Serializable {
  private Long id;
  private String name;
  public Main() {
  }
  public static void main(String[] args) throws Exception {
    Main bean = (Main) Beans.instantiate(ClassLoader.getSystemClassLoader(),
        "Main");
    System.out.println("The Bean = " + bean);
  }
  public Long getId() {
    return id;
  }
  public void setId(Long id) {
    this.id = id;
  }
  public String getName() {
    return name;
  }
  public void setName(String name) {
    this.name = name;
  }
  @Override
  public String toString() {
    return "[id=" + id + "; name=" + name + "]";
  }
}
```
