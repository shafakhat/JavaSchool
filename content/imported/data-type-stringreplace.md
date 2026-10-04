---
title: String.Replace
nav: String.Replace
description: System.out.printf( "s1 = %s\ns2 = %s\ns3 = %s\n\n", s1, s2, s3 );
section: Imported - java2s Archive
order: 1326
source: https://web.archive.org/web/20140829080256/http://www.java2s.com/Tutorial/Java/0040__Data-Type/StringReplace.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String s1 = new String( "hello" );
      String s2 = new String( "GOODBYE" );
      String s3 = new String( "   spaces   " );
      System.out.printf( "s1 = %s\ns2 = %s\ns3 = %s\n\n", s1, s2, s3 );
      // test method replace
      System.out.printf("Replace 'l' with 'L' in s1: %s\n\n", s1.replace( 'l', 'L' ) );
   } // end main
}
java title=Example.java
s1 = hello
s2 = GOODBYE
s3 =    spaces
Replace 'l' with 'L' in s1: heLLo
```

| 2.21.1. | To replace one specific character with another throughout a string |
|---|---|
| 2.21.2. | To remove whitespace from the beginning and end of a string (but not the interior) |
| 2.21.3. | Replacing Characters in a String: replace() method creates a new string with the replaced characters. |
| 2.21.4. | Replacing Substrings in a String |
| 2.21.5. | String.Replace |
| 2.21.6. | Replaces all occourances of given character with new one and returns new String object. |
| 2.21.7. | Replaces only first occourances of given String with new one and returns new String object. |
| 2.21.8. | Replaces all occourances of given String with new one and returns new String object. |
| 2.21.9. | Replace/remove character in a String: replace all occurences of a given character |
| 2.21.10. | To replace a character at a specified position |
| 2.21.11. | Replace \r\n with the tag |
| 2.21.12. | Replace multiple whitespaces between words with single blank |
| 2.21.13. | Unaccent letters |
| 2.21.14. | Only replace first occurence |
| 2.21.15. | Get all digits from a string |
| 2.21.16. | Returns a new string with all the whitespace removed |
| 2.21.17. | Removes specified chars from a string |
| 2.21.18. | Remove/collapse multiple spaces. |
