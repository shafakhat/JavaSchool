---
title: equals() vs ==
nav: equals() vs ==
description: System.out.println(s1 + " equals " + s2 + " -> " + s1.equals(s2));
section: Imported - java2s Archive
order: 1148
source: https://web.archive.org/web/20140829085521/http://www.java2s.com/Tutorial/Java/0040__Data-Type/equalsvs.htm
---
```java title=Example.java
class EqualsNotEqualTo {
  public static void main(String args[]) {
    String s1 = "Hello";
    String s2 = new String(s1);
    System.out.println(s1 + " equals " + s2 + " -> " + s1.equals(s2));
    System.out.println(s1 + " == " + s2 + " -> " + (s1 == s2));
  }
}
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
