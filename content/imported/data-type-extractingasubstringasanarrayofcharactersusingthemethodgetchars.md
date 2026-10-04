---
title: Extracting a substring as an array of characters using the method getChars()
nav: Extracting a substring as ...
description: Imported from the java2s.com archive: Extracting a substring as an array of characters using the method getChars()
section: Imported - java2s Archive
order: 1154
source: https://web.archive.org/web/20140829081514/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ExtractingasubstringasanarrayofcharactersusingthemethodgetChars.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    String text = "To be or not to be";
    char[] textArray = new char[3];
    text.getChars(9, 12, textArray, 0);
    for(char ch: textArray){
      System.out.println(ch);
    }
  }
}
java title=Example.java
n
o
t
```

| 2.28.1. | Demonstrates the charAt and getChars |
|---|---|
| 2.28.2. | Converting Char array to String |
| 2.28.3. | Creating Character Arrays From String Objects |
| 2.28.4. | Copy characters from string into char Array |
| 2.28.5. | Creating String Objects From Character Arrays |
| 2.28.6. | new String(textArray, 9, 3): Creating String Objects From certain part of a character Array |
| 2.28.7. | Creating String Objects From Character Arrays using String.copyValueOf() |
| 2.28.8. | Creating a string from a subset of the array elements |
| 2.28.9. | Extracting a substring as an array of characters using the method getChars() |
| 2.28.10. | Using the Collection-Based for Loop with a String: Counting all vowels in a string |
| 2.28.11. | Construct one String from another. |
| 2.28.12. | demonstrates getChars( ): |
| 2.28.13. | implements CharSequence |
| 2.28.14. | Removes spaces (char <= 32) from end of this String with escape, handling null by returning null |
| 2.28.15. | Removes spaces (char <= 32) from end of this String, handling null by returning null |
| 2.28.16. | Swaps the case of a String changing upper and title case to lower case, and lower case to upper case. |
| 2.28.17. | Deletes all whitespaces from a String as defined by Character.isWhitespace(char). |
| 2.28.18. | Checks whether the String contains only digit characters. |
| 2.28.19. | Checks that the String does not contain certain characters. |
