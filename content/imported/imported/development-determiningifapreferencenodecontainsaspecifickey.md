---
title: Determining If a Preference Node Contains a Specific Key
nav: Determining If a Preferenc...
description: // Returns true if node contains the specified key; false otherwise.
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20111105141039/http://java2s.com/Tutorial/Java/0120__Development/DeterminingIfaPreferenceNodeContainsaSpecificKey.htm
---
```java title=Example.java
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
  }
  // Returns true if node contains the specified key; false otherwise.
  public static boolean contains(Preferences node, String key) {
    return node.get(key, null) != null;
  }
}
```
