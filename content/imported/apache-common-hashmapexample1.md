---
title: HashMap Example 1
nav: HashMap Example 1
description: import org.apache.commons.collections.bidimap.DualHashBidiMap;
section: Imported - java2s Archive
order: 1039
source: https://web.archive.org/web/20061018180931/http://www.java2s.com/Code/Java/Apache-Common/HashMapExample1.htm
---
```java title=Example.java
import org.apache.commons.collections.BidiMap;
import org.apache.commons.collections.bidimap.DualHashBidiMap;
public class HashMapExampleV1 {
  public static void main(String args[]) {
    BidiMap agentToCode = new DualHashBidiMap();
    agentToCode.put("007", "Bond");
    agentToCode.put("006", "Trevelyan");
    agentToCode.put("002", "Fairbanks");
    System.err.println("Agent name from code: " + agentToCode.get("007"));
    System.err.println("Code from Agent name: " + agentToCode.getKey("Bond"));
  }
}
```

Download: ApacheCollectionHashMapExampleV1.zip ( 514 K )
Related examples in the same category
