---
title: Comparing Two Strings
nav: Comparing Two Strings
description: In the following code, if s1 is null, the if statement will return false without evaluating the second expression.
section: Imported - java2s Archive
order: 1381
source: https://web.archive.org/web/20140829090016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ComparingTwoStrings.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] args) {
    String s1 = "Java";
    String s2 = "Java";
    if (s1.equals(s2)) {
      System.out.println("==");
    }
  }
}
```

Sometimes you see this style.

```java title=Example.java
if ("Java".equals (s1))
```

In the following code, if s1 is null, the if statement will return false without evaluating the second expression.

```java title=Example.java
if (s1 != null && s1.equals("Java"))
```

| 2.19.1. | Using String class |
|---|---|
| 2.19.2. | String Literals |
| 2.19.3. | String class constructors |
| 2.19.4. | Create String with char array |
| 2.19.5. | Length of a string |
| 2.19.6. | Assign String variable to null |
| 2.19.7. | Attempts to use string variable before it has been initialized |
| 2.19.8. | toLowerCase and toUpperCase |
| 2.19.9. | Comparing Two Strings |
| 2.19.10. | Demo for escape |
| 2.19.11. | Arrays of Strings: using 'new' operator |
| 2.19.12. | Arrays of Strings: Declare an array of String objects where the initial values determine the size of the array |
| 2.19.13. | String class substring methods |
| 2.19.14. | String Concatenation |
| 2.19.15. | String HashCode |
| 2.19.16. | Using trim() to process commands. |
| 2.19.17. | Remove leading and trailing white space from string |
| 2.19.18. | To remove a character |
| 2.19.19. | Remove a character at a specified position using String.substring |
| 2.19.20. | Get InputStream from a String |
| 2.19.21. | Demonstrate toUpperCase() and toLowerCase(). |
| 2.19.22. | A string can be compared with a StringBuffer |
