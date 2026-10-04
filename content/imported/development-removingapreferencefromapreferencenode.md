---
title: Removing a Preference from a Preference Node
nav: Removing a Preference from...
description: Preferences prefs = Preferences.userNodeForPackage(String.class);
section: Imported - java2s Archive
order: 1849
source: https://web.archive.org/web/20140829081644/http://www.java2s.com/Tutorial/Java/0120__Development/RemovingaPreferencefromaPreferenceNode.htm
---
```java title=Example.java
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Get the user preference node for java.lang
    Preferences prefs = Preferences.userNodeForPackage(String.class);
    // Remove a preference in the node
    final String PREF_NAME = "name_of_preference";
    prefs.remove(PREF_NAME);
    // Remove all preferences in the node
    prefs.clear();
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
