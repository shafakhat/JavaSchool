---
title: Replace all words with another string
nav: Replace all words with ano...
description: System.out.printf( "Every word replaced by \"word\": %s\n\n",
section: Imported - java2s Archive
order: 1835
source: https://web.archive.org/web/20140829075744/http://www.java2s.com/Tutorial/Java/0120__Development/Replaceallwordswithanotherstring.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String firstString = "This sentence ends in 5 stars *****";
      String secondString = "1, 2, 3, 4, 5, 6, 7, 8";
      System.out.printf( "Original String 1: %s\n", firstString );
      // replace words with 'word'
      System.out.printf( "Every word replaced by \"word\": %s\n\n",
         firstString.replaceAll( "\\w+", "word" ) );
      System.out.printf( "Original String 2: %s\n", secondString );
   }
}
java title=Example.java
Original String 1: This sentence ends in 5 stars *****
Every word replaced by "word": word word word word word word *****
Original String 2: 1, 2, 3, 4, 5, 6, 7, 8
```

| 6.32.1. | Validate the first name and last name |
|---|---|
| 6.32.2. | Validate Address |
| 6.32.3. | Validate city and state |
| 6.32.4. | Validate Zip |
| 6.32.5. | Validate Phone |
| 6.32.6. | Replace '*' with '^' |
| 6.32.7. | Replace one string with another string |
| 6.32.8. | Replace all words with another string |
| 6.32.9. | Replace first three digits with 'digit' |
| 6.32.10. | Split string with comma |
| 6.32.11. | Pattern match: J.*\\d[0-35-9]-\\d\\d-\\d\\d |
