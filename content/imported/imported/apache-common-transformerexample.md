---
title: Transformer Example
nav: Transformer Example
description: Transformer transformer = TransformerUtils.invokerTransformer(
section: Imported - java2s Archive
order: 1070
source: https://web.archive.org/web/20061018180926/http://www.java2s.com/Code/Java/Apache-Common/TransformerExample.htm
---
Transformer Example

```java title=Example.java
import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.TransformerUtils;
public class TransformerExampleV1 {
  public static void main(String args[]) {
    Transformer transformer = TransformerUtils.invokerTransformer(
                               "append",
                               new Class[] {String.class},
                               new Object[] {" a Transformer?"});
    Object newObject =  transformer.transform(new StringBuffer("Are you"));
    System.err.println(newObject);
  }
}
```

Download: ApacheCommonTransformerExampleV1.zip ( 876 K )
Related examples in the same category
