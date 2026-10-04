---
title: Validate Phone
nav: Validate Phone
description: Imported from the java2s.com archive: Validate Phone
section: Imported - java2s Archive
order: 1832
source: https://web.archive.org/web/20140829075841/http://www.java2s.com/Tutorial/Java/0120__Development/ValidatePhone.htm
---
```java title=Example.java
public class MainClass
{
   public static void main( String[] args )
   {
       System.out.println(validatePhone("123-456-1111"));
   }
   public static boolean validatePhone( String phone )
   {
      return phone.matches( "[1-9]\\d{2}-[1-9]\\d{2}-\\d{4}" );
   } // end method validatePhone
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
