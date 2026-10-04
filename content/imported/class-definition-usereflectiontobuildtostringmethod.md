---
title: Use Reflection To build toString method
nav: Use Reflection To build to...
description: import org.apache.commons.lang.builder.ReflectionToStringBuilder;
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20101106001915/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/UseReflectionTobuildtoStringmethod.htm
---
```java title=Example.java
import org.apache.commons.lang.builder.ReflectionToStringBuilder;
import org.apache.commons.lang.builder.ToStringStyle;
public class Main {
  private Integer id;
  private String name;
  private String description;
  public static final String KEY = "APP-KEY";
  private transient String secretKey;
  public Main(Integer id, String name, String description, String secretKey) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.secretKey = secretKey;
  }
  public String toString() {
    return ReflectionToStringBuilder.toString(this, ToStringStyle.SIMPLE_STYLE, true, true);
  }
  public static void main(String[] args) {
    Main demo = new Main (1, "A", "B", "C");
    System.out.println("Demo = " + demo);
  }
}
```
