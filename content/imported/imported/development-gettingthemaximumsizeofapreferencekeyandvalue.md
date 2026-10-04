---
title: Getting the Maximum Size of a Preference Key and Value
nav: Getting the Maximum Size o...
description: Imported from java2s.com: Getting the Maximum Size of a Preference Key and Value
section: Imported
order: 20040
source: http://java2s.com/Tutorial/Java/0120__Development/GettingtheMaximumSizeofaPreferenceKeyandValue.htm
---
```java title=Example.java
import java.util.prefs.Preferences;
public class Main {
  public static void main(String[] argv) throws Exception {
    // Get maximum key length
    int keyMax = Preferences.MAX_KEY_LENGTH;
    // Get maximum value length
    int valueMax = Preferences.MAX_VALUE_LENGTH;
    // Get maximum length of byte array values
    int bytesMax = Preferences.MAX_VALUE_LENGTH * 3 / 4;
  }
}
```
