---
title: Validate the first name and last name
nav: Validate the first name an...
description: Imported from the java2s.com archive: Validate the first name and last name
section: Imported - java2s Archive
order: 1828
source: https://web.archive.org/web/20140829080212/http://www.java2s.com/Tutorial/Java/0120__Development/Validatethefirstnameandlastname.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String[] args )
   {
       System.out.println(validateFirstName("Tom"));
       System.out.println(validateLastName("Tom"));
   }
   // validate first name
   public static boolean validateFirstName( String firstName )
   {
      return firstName.matches( "[A-Z][a-zA-Z]*" );
   } // end method validateFirstName
   // validate last name
   public static boolean validateLastName( String lastName )
   {
      return lastName.matches( "[a-zA-z]+([ '-][a-zA-Z]+)*" );
   } // end method validateLastName
}
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
