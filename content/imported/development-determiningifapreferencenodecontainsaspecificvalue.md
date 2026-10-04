---
title: Determining If a Preference Node Contains a Specific Value
nav: Determining If a Preferenc...
description: public static String containsValue(Preferences node, String value) {
section: Imported - java2s Archive
order: 1043
source: https://web.archive.org/web/20111105140832/http://java2s.com/Tutorial/Java/0120__Development/DeterminingIfaPreferenceNodeContainsaSpecificValue.htm
---
```java title=Example.java
import java.util.prefs.BackingStoreException;
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
  }
  public static String containsValue(Preferences node, String value) {
    try {
      String[] keys = node.keys();
      for (int i = 0; i < keys.length; i++) {
        if (value.equals(node.get(keys[i], null))) {
          return keys[i];
        }
      }
    } catch (BackingStoreException e) {
    }
    return null;
  }
}
```
