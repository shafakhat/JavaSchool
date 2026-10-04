---
title: Implement equals method using commons-lang
nav: Implement equals method us...
description: return new EqualsBuilder().append(this.id, book.id).append(this.title, book.title).append(
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20100213232647/http://java2s.com/Code/Java/Apache-Common/Implementequalsmethodusingcommonslang.htm
---
```java title=Example.java
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.EqualsBuilder;
import java.io.Serializable;
public class Main implements Serializable {
  private Long id;
  private String title;
  private String author;
  public boolean equals(Object object) {
    if (!(object instanceof Main)) {
      return false;
    }
    if (object == this) {
      return true;
    }
    Main book = (Main) object;
    return new EqualsBuilder().append(this.id, book.id).append(this.title, book.title).append(
        this.author, book.author).isEquals();
    // return EqualsBuilder.reflectionEquals(this, book);
  }
}
```

1.  Implement hashCode using commons-lang
---  ---
2.  Use CompareToBuilder class to create compareTo method for your own class
3.  Use Reflection To build toString method
4.  Jakarta Commons toString Builder
