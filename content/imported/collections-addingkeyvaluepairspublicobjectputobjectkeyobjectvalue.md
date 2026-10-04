---
title: Adding Key-Value Pairs
nav: Adding Key-Value Pairs
description: Imported from the java2s.com archive: Adding Key-Value Pairs
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20070705212324/http://www.java2s.com:80/Tutorial/Java/0140__Collections/AddingKeyValuePairspublicObjectputObjectkeyObjectvalue.htm
---
```java title=Example.java
import java.util.HashMap;
import java.util.Map;
public class MainClass {
  public static void main(String[] a) {
    Map map = new HashMap();
    map.put("key1", "value1");
    map.put("key2", "value2");
    map.put("key3", "value3");
    System.out.println(map);
  }
}
```

```java title=Example.java
{key1=value1, key3=value3, key2=value2}
```
