---
title: Jakarta Commons toString Builder
nav: Jakarta Commons toString B...
description: return new ToStringBuilder(this, ToStringStyle.MULTI_LINE_STYLE).append("id", id).append(
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20090629063905/http://www.java2s.com:80/Code/Java/Apache-Common/JakartaCommonstoStringBuilder.htm
---
```java title=Example.java
import org.apache.commons.lang.builder.ToStringBuilder;
import org.apache.commons.lang.builder.ToStringStyle;
public class Main {
  private String id;
  private String firstName;
  private String lastName;
  public Main() {
  }
  public String toString() {
    return new ToStringBuilder(this, ToStringStyle.MULTI_LINE_STYLE).append("id", id).append(
        "firstName", firstName).append("lastName", lastName).toString();
  }
  public static void main(String[] args) {
    Main example = new Main();
    example.id = "1";
    example.firstName = "First Name";
    example.lastName = "Last Name";
    System.out.println("example = " + example);
  }
}
```

1.  Implement hashCode using commons-lang
---  ---
2.  Use CompareToBuilder class to create compareTo method for your own class
3.  Use Reflection To build toString method
4.  Implement equals method using commons-lang
