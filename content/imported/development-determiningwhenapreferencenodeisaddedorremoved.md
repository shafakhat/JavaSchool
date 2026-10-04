---
title: Determining When a Preference Node Is Added or Removed
nav: Determining When a Prefere...
description: Preferences prefs = Preferences.userNodeForPackage(String.class);
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/20111105134549/http://java2s.com/Tutorial/Java/0120__Development/DeterminingWhenaPreferenceNodeIsAddedorRemoved.htm
---
```java title=Example.java
import java.util.prefs.NodeChangeEvent;
import java.util.prefs.NodeChangeListener;
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
    Preferences prefs = Preferences.userNodeForPackage(String.class);
    prefs.addNodeChangeListener(new NodeChangeListener() {
      public void childAdded(NodeChangeEvent evt) {
        Preferences parent = evt.getParent();
        Preferences child = evt.getChild();
      }
      public void childRemoved(NodeChangeEvent evt) {
        Preferences parent = evt.getParent();
        Preferences child = evt.getChild();
      }
    });
    Preferences child = prefs.node("new node");
    child.removeNode();
    prefs.removeNode();
  }
}
```
