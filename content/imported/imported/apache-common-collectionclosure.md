---
title: Collection Closure
nav: Collection Closure
description: Imported from the java2s.com archive: Collection Closure
section: Imported - java2s Archive
order: 1019
source: https://web.archive.org/web/20061018180952/http://www.java2s.com/Code/Java/Apache-Common/CollectionClosure.htm
---
```java title=Example.java
import org.apache.commons.collections.Closure;
import org.apache.commons.collections.ClosureUtils;
import org.apache.commons.collections.PredicateUtils;
public class ClosureExample {
  public static void main(String args[]) {
    Closure ifClosure = ClosureUtils.ifClosure(
                       PredicateUtils.equalPredicate(new Integer(20)),
                       ClosureUtils.nopClosure(),
                       ClosureUtils.exceptionClosure());
    ifClosure.execute(new Integer(20));
//    ifClosure.execute(new Integer(30));
  }
}
```

Download: ApacheCollectionClosureExample.zip ( 513 K )
Related examples in the same category
