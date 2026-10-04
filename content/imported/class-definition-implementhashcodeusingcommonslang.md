---
title: Implement hashCode using commons-lang
nav: Implement hashCode using c...
description: return new HashCodeBuilder().append(id).append(title).append(author).toHashCode();
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20100312140716/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/ImplementhashCodeusingcommonslang.htm
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
