---
title: Getting the Roots of the Preference Trees
nav: Getting the Roots of the P...
description: Imported from java2s.com: Getting the Roots of the Preference Trees
section: Imported
order: 20038
source: http://java2s.com/Tutorial/Java/0120__Development/GettingtheRootsofthePreferenceTrees.htm
---
```java title=Example.java
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Get the system root
    Preferences prefs = Preferences.systemRoot();
    // Get the user root
    prefs = Preferences.userRoot();
    // The name of a root is ""
    String name = prefs.name();
    // The parent of a root is null
    Preferences parent = prefs.parent();
    // The absolute path of a root is "/"
    String path = prefs.absolutePath();
  }
}
```
