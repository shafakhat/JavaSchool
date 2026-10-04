---
title: Primitive address validation
nav: Primitive address validation
description: String namePattern = "([A-Za-z])+ (([A-Za-z])+\\.? )?([A-Za-z])+\\s*";
section: Imported - java2s Archive
order: 2256
source: https://web.archive.org/web/20140827195532/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Primitiveaddressvalidation.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    String addr = "my Address 12345";
    String namePattern = "([A-Za-z])+ (([A-Za-z])+\\.? )?([A-Za-z])+\\s*";
    String zipCodePattern = "\\d{5}(-\\d{4})?";
    String addressPattern = "^" + namePattern + "\\w+ .*, \\w+ " + zipCodePattern + "$";
    System.out.println(addr.matches(addressPattern));
  }
}
```

| 8.10.1. | Primitive address validation |
|---|---|
| 8.10.2. | Date format consists of one or two digits followed by a hyphen, followed by one or two digits, followed by a hypen, followed by four digits |
| 8.10.3. | Finding duplication of words |
| 8.10.4. | Name validation |
| 8.10.5. | Phone number validation |
| 8.10.6. | Zip code validation |
| 8.10.7. | String manipulation using English synonyms |
| 8.10.8. | Match a digit |
