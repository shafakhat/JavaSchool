---
title: Getting and Setting Java Type Values in a Preference
nav: Getting and Setting Java T...
description: Preferences prefs = Preferences.userNodeForPackage(Main.class);
section: Imported - java2s Archive
order: 1846
source: https://web.archive.org/web/20140829081827/http://www.java2s.com/Tutorial/Java/0120__Development/GettingandSettingJavaTypeValuesinaPreference.htm
---
```java title=Example.java
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
    Preferences prefs = Preferences.userNodeForPackage(Main.class);
    // Preference key name
    final String PREF_NAME = "name_of_preference";
    // Save
    prefs.put(PREF_NAME, "a string"); // String
    prefs.putBoolean(PREF_NAME, true); // boolean
    prefs.putInt(PREF_NAME, 123); // int
    prefs.putLong(PREF_NAME, 123L); // long
    prefs.putFloat(PREF_NAME, 12.3F); // float
    prefs.putDouble(PREF_NAME, 12.3); // double
    byte[] bytes = new byte[1024];
    prefs.putByteArray(PREF_NAME, bytes); // byte[]
    // Retrieve
    String s = prefs.get(PREF_NAME, "a string"); // String
    boolean b = prefs.getBoolean(PREF_NAME, true); // boolean
    int i = prefs.getInt(PREF_NAME, 123); // int
    long l = prefs.getLong(PREF_NAME, 123L); // long
    float f = prefs.getFloat(PREF_NAME, 12.3F); // float
    double d = prefs.getDouble(PREF_NAME, 12.3); // double
    bytes = prefs.getByteArray(PREF_NAME, bytes); // byte[]
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
