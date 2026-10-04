---
title: String manipulation using English synonyms
nav: String manipulation using ...
description: System.out.println("REGEX PATTERN:\n" + splitPattern + "\n");
section: Imported - java2s Archive
order: 2263
source: https://web.archive.org/web/20140828211844/http://www.java2s.com/Tutorial/Java/0130__Regular-Expressions/StringmanipulationusingEnglishsynonyms.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    String statement = "A B AA";
    String tokens[] = null;
    String splitPattern = "A|B|C|E|(G H I J)|(AA BB CC)";
    tokens = statement.split(splitPattern);
    System.out.println("REGEX PATTERN:\n" + splitPattern + "\n");
    System.out.println("STATEMENT:\n" + statement + "\n");
    System.out.println("TOKENS:");
    for (int i = 0; i < tokens.length; i++) {
      System.out.println(tokens[i]);
    }
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
