---
title: Factory Example 1
nav: Factory Example 1
description: Factory bufferFactory = FactoryUtils.instantiateFactory(StringBuffer.class,
section: Imported - java2s Archive
order: 1031
source: https://web.archive.org/web/20061018180945/http://www.java2s.com/Code/Java/Apache-Common/FactoryExample1.htm
---
```java title=Example.java
import org.apache.commons.collections.Factory;
import org.apache.commons.collections.FactoryUtils;
public class FactoryExampleV1 {
  public static void main(String args[]) {
    Factory bufferFactory = FactoryUtils.instantiateFactory(StringBuffer.class,
                          new Class[] {String.class},
                          new Object[] {"a string"});
    System.err.println(bufferFactory.create());
  }
}
```

Download: ApacheCollectionFactoryExampleV1.zip ( 513 K )
Related examples in the same category
