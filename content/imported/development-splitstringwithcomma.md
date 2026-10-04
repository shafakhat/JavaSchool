---
title: Split string with comma
nav: Split string with comma
description: String[] results = secondString.split( ",\\s*" ); // split on commas
section: Imported - java2s Archive
order: 1839
source: https://web.archive.org/web/20140829075723/http://www.java2s.com/Tutorial/Java/0120__Development/Splitstringwithcomma.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String args[] )
   {
      String secondString = "1, 2, 3, 4, 5, 6, 7, 8";
      String output = "String split at commas: [";
      String[] results = secondString.split( ",\\s*" ); // split on commas
      for ( String string : results )
         output += "\"" + string + "\", ";
      output = output.substring( 0, output.length() - 2 ) + "]";
      System.out.println( output );
   }
}
java title=Example.java
String split at commas: ["1", "2", "3", "4", "5", "6", "7", "8"]
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
