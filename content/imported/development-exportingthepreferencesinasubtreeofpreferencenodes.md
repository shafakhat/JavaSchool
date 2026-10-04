---
title: Exporting the Preferences in a Subtree of Preference Nodes
nav: Exporting the Preferences ...
description: Preferences prefs = Preferences.userNodeForPackage(String.class);
section: Imported - java2s Archive
order: 1861
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0120__Development/ExportingthePreferencesinaSubtreeofPreferenceNodes.htm
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
 // Save some values in the parent node
    prefs = prefs.parent();
    prefs.putFloat("myFloat", 12.3F); // float
    prefs.putDouble("myDouble", 12.3); // double
 byte[] bytes = new byte[10];
    prefs.putByteArray("myByteArray", bytes); // byte[]
    prefs.exportSubtree(new FileOutputStream("output.xml"));
  }
}
```

| 6.36.1. | Put key value pair to Preference |
|---|---|
| 6.36.2. | Get childrenNames from Preferences |
| 6.36.3. | Get keys from Preferences |
| 6.36.4. | Get name and parent from Preference |
| 6.36.5. | Get node from Preference |
| 6.36.6. | Get value from Preferences |
| 6.36.7. | Getting and Setting Java Type Values in a Preference |
| 6.36.8. | Getting the Maximum Size of a Preference Key and Value |
| 6.36.9. | Getting the Roots of the Preference Trees |
| 6.36.10. | Removing a Preference from a Preference Node |
| 6.36.11. | Export Preferences to XML file |
| 6.36.12. | Preference save and load |
| 6.36.13. | Preferences Inspector |
| 6.36.14. | Removing a Preference Node |
| 6.36.15. | Determining If a Preference Node Exists |
| 6.36.16. | Determining If a Preference Node Contains a Specific Key |
| 6.36.17. | Determining If a Preference Node Contains a Specific Value |
| 6.36.18. | Read / write data in Windows registry |
| 6.36.19. | Retrieving the Parent and Child Nodes of a Preference Node |
| 6.36.20. | Exporting the Preferences in a Preference Node |
| 6.36.21. | Exporting the Preferences in a Subtree of Preference Nodes |
| 6.36.22. | Listening for Changes to Preference Values in a Preference Node |
| 6.36.23. | Determining When a Preference Node Is Added or Removed |
| 6.36.24. | Get the desired look and feel from a per-user preference |
