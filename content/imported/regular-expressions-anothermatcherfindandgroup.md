---
title: Another Matcher find and group
nav: Another Matcher find and g...
description: Another Matcher find and group : Java examples (example source code) » Regular Expressions » Matcher
section: Imported - java2s Archive
order: 1004
source: https://web.archive.org/web/20060510151924/http://www.java2s.com:80/Code/Java/Regular-Expressions/AnotherMatcherfindandgroup.htm
---
Another Matcher find and group : Java examples (example source code) » Regular Expressions » Matcher

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class PossesiveExample {
  public static void main(String args[]) {
    String regex = "(\\w++)(\\d\\d)(\\w+)";
    Pattern pattern = Pattern.compile(regex);
    String candidate = "X99SuperJava";
    Matcher matcher = pattern.matcher(candidate);
    if (matcher.find()) {
      System.out.println("GROUP 0:" + matcher.group(0));
      System.out.println("GROUP 1:" + matcher.group(1));
      System.out.println("GROUP 2:" + matcher.group(2));
      System.out.println("GROUP 3:" + matcher.group(3));
    } else {
      System.out.println("NO MATCHES");
    }
    System.out.println("Done");
  }
}
```

Related examples in the same category
---
1. Matcher: Find Demo
2. Matcher Reset
3. Matcher Pattern
4. Another Matcher reset
5. Matcher start
6. Matcher start with parameter
7. Matcher end
8. Matcher end with parameter
9. Matcher group
10. Matcher group with parameter
11. Matcher group count
12. Matcher match
13. Matcher find
14. Matcher find with parameter
15. Matcher LookingAt
16. Matcher appendReplacement
17. Matcher replaceAll
18. Matcher replaceFirst
19. Matcher group 2
20. Matcher group with parameter 2
21. Matcher ground count
22. Matcher replaceAll 2
23. Matcher find group
24. Pattern compile
25. Show line ending matching using Regular Expressions class
26. Matcher Groups
27. Matches Looking
