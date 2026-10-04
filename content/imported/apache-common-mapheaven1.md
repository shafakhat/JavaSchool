---
title: MapHeaven 1
nav: MapHeaven 1
description: import org.apache.commons.collections.map.CaseInsensitiveMap;
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20061018180935/http://www.java2s.com/Code/Java/Apache-Common/MapHeaven1.htm
---
MapHeaven 1

```java title=Example.java
import java.util.Map;
import java.util.Date;
import java.util.HashMap;
import org.apache.commons.collections.map.LazyMap;
import org.apache.commons.collections.FactoryUtils;
import org.apache.commons.collections.map.IdentityMap;
import org.apache.commons.collections.map.CaseInsensitiveMap;
public class MapHeavenV1 {
  public static void main(String args[]) {
    MapHeavenV1 instance = new MapHeavenV1();
    instance.createMaps();
    instance.testMaps();
  }
  private void testMaps() {
    cIMap.put("key1", "value1");
    cIMap.put("key2", "value2");
    cIMap.put("KeY1", "value3");
    System.err.println("Value of key1: " + cIMap.get("key1")); // value3 because it is case insensitive
    Integer identRef = new Integer(1);
    Integer identRef2 = new Integer(1);
    identMap.put(identRef, "value1");
    identMap.put(identRef2, "value3");
    System.err.println("Value of identRef2: " + identMap.get(identRef2)); // value 3 even though both identRef and identRef2 are equal
    System.err.println(lazyMap); // only creates elements when they are accessed
    lazyMap.get("EmptyBuffer");
    System.err.println(lazyMap);
  }
  private void createMaps() {
    cIMap = new CaseInsensitiveMap();
    identMap = new IdentityMap();
    lazyMap = LazyMap.decorate(
      new HashMap(),
      FactoryUtils.instantiateFactory(StringBuffer.class));
  }
  private CaseInsensitiveMap cIMap;
  private IdentityMap identMap;
  private Map lazyMap;
}
```

Download: ApacheCommonMapHeavenV1.zip ( 514 K )
Related examples in the same category
