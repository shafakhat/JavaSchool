---
title: CharSet Example
nav: CharSet Example
description: Imported from the java2s.com archive: CharSet Example
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20080128152702/http://www.java2s.com:80/Code/Java/Apache-Common/CharSetExample.htm
---
CharSet Example

```java title=Example.java
import org.apache.commons.lang.CharSet;
import org.apache.commons.lang.CharRange;
import org.apache.commons.lang.ArrayUtils;
public class CharSetExampleV1 {
  public static void main(String args[]) {
    CharSet set = CharSet.getInstance("the apprentice");
    System.err.println(set.contains('q'));
    CharRange[] range = set.getCharRanges();
    System.err.println(ArrayUtils.toString(range));
  }
}
```

BeanUtilsCharSetExampleV1.zip( 877 k)
