---
title: Implement equals method using commons-lang
nav: Implement equals method us...
description: return new EqualsBuilder().append(this.id, book.id).append(this.title, book.title).append(
section: Imported - java2s Archive
order: 1091
source: https://web.archive.org/web/20140829083846/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Implementequalsmethodusingcommonslang.htm
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

| 5.19.1. | Comparing Objects |
|---|---|
| 5.19.2. | Implement equals method using commons-lang |
| 5.19.3. | Use CompareToBuilder class to create compareTo method for your own class |
| 5.19.4. | Define your own equals method |
