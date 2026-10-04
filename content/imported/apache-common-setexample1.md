---
title: Set Example 1
nav: Set Example 1
description: Imported from the java2s.com archive: Set Example 1
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20061018181036/http://www.java2s.com/Code/Java/Apache-Common/SetExample1.htm
---
Set Example 1

```java title=Example.java
import org.apache.commons.collections.set.MapBackedSet;
import java.util.Map;
import java.util.Set;
import java.util.HashMap;
import java.util.Iterator;
public class SetExampleV1 {
  public static void main(String args[]) {
    // create a Map
    Map map = new HashMap();
    map.put("Key1", "Value1");
    // create the decoration
    Set set = MapBackedSet.decorate(map);
    map.put("Key2", "Any dummy value");
    set.add("Key3");
    Iterator itr = set.iterator();
    while(itr.hasNext()) {
      System.err.println(itr.next());
    }
  }
}
```

Download: ApacheCommonSetExampleV1.zip ( 513 K )
Related examples in the same category
