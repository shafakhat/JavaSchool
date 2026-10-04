---
title: Name validation
nav: Name validation
description: Imported from the java2s.com archive: Name validation
section: Imported - java2s Archive
order: 2259
source: https://web.archive.org/web/20140828212302/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/Namevalidation.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    String name = "First Name";
    String nameToken = "\\p{Upper}(\\p{Lower}+\\s?)";
    String namePattern = "(" + nameToken + "){2,3}";
    System.out.println(name.matches(namePattern));
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
