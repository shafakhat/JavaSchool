---
title: Implement hashCode using commons-lang
nav: Implement hashCode using c...
description: return new HashCodeBuilder().append(id).append(title).append(author).toHashCode();
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20100213232448/http://java2s.com/Code/Java/Apache-Common/ImplementhashCodeusingcommonslang.htm
---
```java title=Example.java
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.EqualsBuilder;
import java.io.Serializable;
public class Main implements Serializable {
  private Long id;
  private String title;
  private String author;
  public int hashCode() {
    return new HashCodeBuilder().append(id).append(title).append(author).toHashCode();
    // return HashCodeBuilder.reflectionHashCode(this);
  }
}
```

1.  Use CompareToBuilder class to create compareTo method for your own class
---  ---
2.  Use Reflection To build toString method
3.  Implement equals method using commons-lang
4.  Jakarta Commons toString Builder
