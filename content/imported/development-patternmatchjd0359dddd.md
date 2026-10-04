---
title: Pattern match
nav: Pattern match
description: Imported from the java2s.com archive: Pattern match
section: Imported - java2s Archive
order: 1838
source: https://web.archive.org/web/20140829080206/http://www.java2s.com/Tutorial/Java/0120__Development/PatternmatchJd0359dddd.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass
{
   public static void main( String args[] )
   {
      // create regular expression
      Pattern expression =
         Pattern.compile( "J.*\\d[0-35-9]-\\d\\d-\\d\\d" );
      String string1 = "Jack's Birthday is 05-12-75\n" +
         "Joe's Birthday is 11-04-68\n" +
         "Tom's Birthday is 04-28-73\n" +
         "Lee" +
         "s Birthday is 12-17-77";
      // match regular expression to string and print matches
      Matcher matcher = expression.matcher( string1 );
      while ( matcher.find() )
         System.out.println( matcher.group() );
   }
}
java title=Example.java
Jack's Birthday is 05-12-75
Joe's Birthday is 11-04-68
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
