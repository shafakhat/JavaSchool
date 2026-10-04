---
title: Collection BidiMap
nav: Collection BidiMap
description: import org.apache.commons.collections.bidimap.DualHashBidiMap;
section: Imported - java2s Archive
order: 1017
source: https://web.archive.org/web/20061018181032/http://www.java2s.com/Code/Java/Apache-Common/CollectionBidiMap.htm
---
Collection BidiMap

```java title=Example.java
import org.apache.commons.collections.BidiMap;
import org.apache.commons.collections.bidimap.DualHashBidiMap;
import org.apache.commons.collections.bidimap.UnmodifiableBidiMap;
public class BidiMapExample {
  public static void main(String args[]) {
    BidiMap agentToCode = new DualHashBidiMap();
    agentToCode.put("007", "Bond");
    agentToCode.put("006", "Joe");
    agentToCode = UnmodifiableBidiMap.decorate(agentToCode);
    agentToCode.put("002", "Fairbanks"); // throws Exception
    agentToCode.remove("007"); // throws Exception
    agentToCode.removeValue("Bond"); // throws Exception
  }
}
```

Download: ApacheCollectionBidiMapExample.zip ( 513 K )
Related examples in the same category
