---
title: To check for equality between two strings ignoring the case
nav: To check for equality betw...
description: Imported from the java2s.com archive: To check for equality between two strings ignoring the case
section: Imported - java2s Archive
order: 1349
source: https://web.archive.org/web/2016/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Tocheckforequalitybetweentwostringsignoringthecase.htm
---
```java title=Example.java
public class MainClass {

  public static void main(String[] arg) {

    String a = "a";
    String b = "A";

    if(a.equalsIgnoreCase(b)){
      System.out.println("a==b");
    }else{
      System.out.println("a!=b");
    }
  }
}
```

```java title=Example.java
a==b
```

| 2.23.1. | Comparing Strings for Equality |
|---|---|
| 2.23.2. | To check for equality between two strings ignoring the case |
| 2.23.3. | Sequencing Strings |
| 2.23.4. | String length, charAt, equals |
| 2.23.5. | equals() and equalsIgnoreCase(). |
| 2.23.6. | equals() vs == |
| 2.23.7. | Region Matches |
| 2.23.8. | Compares all Strings in an array and returns the index at which the Strings begin to differ. |
| 2.23.9. | Compares all Strings in an array and returns the initial sequence of characters that is common to all of them. |
| 2.23.10. | Compares two Strings, and returns the index at which the Strings begin to differ. |
| 2.23.11. | Compares two Strings, and returns the portion where they differ. |
| 2.23.12. | Compress 2 adjacent (single or double) quotes into a single (s or d) quote when found in the middle of a String. |
