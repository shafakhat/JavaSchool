---
title: Getting and Setting Java Type Values in a Preference
nav: Getting and Setting Java T...
description: Preferences prefs = Preferences.userNodeForPackage(Main.class);
section: Imported
order: 20039
source: http://java2s.com/Tutorial/Java/0120__Development/GettingandSettingJavaTypeValuesinaPreference.htm
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
