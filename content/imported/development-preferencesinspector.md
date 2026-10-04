---
title: Preferences Inspector
nav: Preferences Inspector
description: Preferences.userNodeForPackage(MainClass.class).addPreferenceChangeListener(this);
section: Imported - java2s Archive
order: 1852
source: https://web.archive.org/web/20140829081748/http://www.java2s.com/Tutorial/Java/0120__Development/PreferencesInspector.htm
---
```java title=Example.java
import java.util.prefs.PreferenceChangeEvent;
import java.util.prefs.PreferenceChangeListener;
import java.util.prefs.Preferences;
public class MainClass implements PreferenceChangeListener {
  private Preferences userPrefs;
  public static final String NAMEPREF = "name";
  public static final String EMAILPREF = "email";
  public static final String AGEPREF = "age";
  public static final String PHONEPREF = "phone";
  public static void main(String args[]) {
    new MainClass();
  }
  public MainClass() {
    userPrefs = Preferences.userNodeForPackage(MainClass.class);
    System.out.println(userPrefs.get(NAMEPREF, ""));
    System.out.println(userPrefs.get(EMAILPREF, ""));
    System.out.println(userPrefs.get(AGEPREF, ""));
    System.out.println(userPrefs.get(PHONEPREF, ""));
    userPrefs.put(NAMEPREF, "name");
    userPrefs.put(AGEPREF, "Text");
    userPrefs.put(EMAILPREF, "email");
    userPrefs.put(PHONEPREF, "phone");
    System.out.println("Preferences stored");
    Preferences.userNodeForPackage(MainClass.class).addPreferenceChangeListener(this);
  }
  public void preferenceChange(PreferenceChangeEvent evt) {
    String key = evt.getKey();
    String val = evt.getNewValue();
    if (key.equals(NAMEPREF)) {
      System.out.println(val);
    } else if (key.equals(EMAILPREF)) {
      System.out.println(val);
    } else if (key.equals(AGEPREF)) {
      System.out.println(val);
    } else if (key.equals(PHONEPREF)) {
      System.out.println(val);
    }
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
