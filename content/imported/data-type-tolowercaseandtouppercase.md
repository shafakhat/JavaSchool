---
title: toLowerCase and toUpperCase
nav: toLowerCase and toUpperCase
description: System.out.printf( "s1 = %s\ns2 = %s\ns3 = %s\n\n", s1, s2, s3 );
section: Imported - java2s Archive
order: 1352
source: https://web.archive.org/web/20140829090219/http://www.java2s.com/Tutorial/Java/0040__Data-Type/toLowerCaseandtoUpperCase.htm
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
      // test toLowerCase and toUpperCase
      System.out.printf( "s1.toUpperCase() = %s\n", s1.toUpperCase() );
      System.out.printf( "s2.toLowerCase() = %s\n\n", s2.toLowerCase() );
   }
}
```

```java title=Example.java
s1 = hello
s2 = GOODBYE
s3 =    spaces

s1.toUpperCase() = HELLO
s2.toLowerCase() = goodbye
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
