---
title: Exporting the Preferences in a Preference Node
nav: Exporting the Preferences ...
description: Preferences prefs = Preferences.userNodeForPackage(String.class);
section: Imported
order: 20004
source: http://java2s.com/Tutorial/Java/0120__Development/ExportingthePreferencesinaPreferenceNode.htm
---
```java title=Example.java
import java.io.FileOutputStream;
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
    Preferences prefs = Preferences.userNodeForPackage(String.class);
    // Save some values
    prefs.put("myString", "a string"); // String
    prefs.putBoolean("myBoolean", true); // boolean
    prefs.putInt("myInt", 123); // int
    prefs.putLong("myLong", 123L); // long
    prefs.putFloat("myFloat", 12.3F); // float
    prefs.putDouble("myDouble", 12.3); // double
    byte[] bytes = new byte[10];
    prefs.putByteArray("myByteArray", bytes); // byte[]
    // Export the node to a file
    prefs.exportNode(new FileOutputStream("output.xml"));
  }
}
```
