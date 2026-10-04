---
title: Multi Key Example 1
nav: Multi Key Example 1
description: Imported from the java2s.com archive: Multi Key Example 1
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20061018180941/http://www.java2s.com/Code/Java/Apache-Common/MultiKeyExample1.htm
---
```java title=Example.java
import java.util.HashMap;
public class MultiKeyExampleV1 {
  public static void main(String args[]) {
    HashMap codeToText_en = new HashMap();
    codeToText_en.put("GM", "Good Morning");
    codeToText_en.put("GN", "Good Night");
    codeToText_en.put("GE", "Good Evening");
    HashMap codeToText_de = new HashMap();
    codeToText_de.put("GM", "Guten Morgen");
    codeToText_de.put("GE", "Guten Abend");
    codeToText_de.put("GN", "Guten Nacht");
    HashMap langToMap = new HashMap();
    langToMap.put("en", codeToText_en);
    langToMap.put("de", codeToText_de);
    System.err.println("Good Evening in English: " +
      ((HashMap)langToMap.get("en")).get("GE"));
    System.err.println("Good Night in German: " +
      ((HashMap)langToMap.get("de")).get("GN"));
  }
}
```

Download: ApacheCommonMultiKeyExampleV1.zip ( 514 K )
Related examples in the same category
