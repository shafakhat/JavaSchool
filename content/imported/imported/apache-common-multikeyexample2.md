---
title: MultiKey Example 2
nav: MultiKey Example 2
description: Imported from the java2s.com archive: MultiKey Example 2
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20061018181040/http://www.java2s.com/Code/Java/Apache-Common/MultiKeyExample2.htm
---
```java title=Example.java
import java.util.HashMap;
import org.apache.commons.collections.keyvalue.MultiKey;
public class MultiKeyExampleV2 {
  private static HashMap codeAndLangToText;
  public static void main(String args[]) {
    codeAndLangToText = new HashMap();
    addMultiKeyAndValue("en", "GM", "Good Morning");
    addMultiKeyAndValue("en", "GE", "Good Evening");
    addMultiKeyAndValue("en", "GN", "Good Night");
    addMultiKeyAndValue("de", "GM", "Guten Morgen");
    addMultiKeyAndValue("de", "GE", "Guten Abend");
    addMultiKeyAndValue("de", "GN", "Guten Nacht");
    System.err.println("Good Evening in English: " +
      codeAndLangToText.get(new MultiKey("en", "GE")));
    System.err.println("Good Night in German: " +
      codeAndLangToText.get(new MultiKey("de", "GN")));
  }
  private static void addMultiKeyAndValue(
    Object key1, Object key2, Object value) {
    MultiKey key = new MultiKey(key1, key2);
    codeAndLangToText.put(key, value);
  }
}
```

Download: ApacheCommonMultiKeyExampleV2.zip ( 514 K )
Related examples in the same category
