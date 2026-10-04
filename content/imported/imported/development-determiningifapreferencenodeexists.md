---
title: Determining If a Preference Node Exists
nav: Determining If a Preferenc...
description: boolean exists = Preferences.userRoot().nodeExists("/yourValue"); // false
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20111105141619/http://java2s.com/Tutorial/Java/0120__Development/DeterminingIfaPreferenceNodeExists.htm
---
```java title=Example.java
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
    boolean exists = Preferences.userRoot().nodeExists("/yourValue"); // false
    Preferences.userRoot().node("/yourValue");
    exists = Preferences.userRoot().nodeExists("/yourValue"); // true
    Preferences prefs = Preferences.userRoot().node("/yourValue");
    prefs.removeNode();
    // exists = prefs.nodeExists("/yourValue");
    exists = prefs.nodeExists(""); // false
  }
}
```
