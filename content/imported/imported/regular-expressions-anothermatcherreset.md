---
title: Another Matcher reset
nav: Another Matcher reset
description: Another Matcher reset : Java examples (example source code) » Regular Expressions » Matcher
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20060510151734/http://www.java2s.com:80/Code/Java/Regular-Expressions/AnotherMatcherreset.htm
---
Another Matcher reset : Java examples (example source code) » Regular Expressions » Matcher

Another Matcher reset

```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MatcherResetCharSequenceExample {
  public static void main(String args[]) {
    test();
  }
  public static void test() {
    String output = "";
    Pattern p = Pattern.compile("\\d");
    Matcher m1 = p.matcher("01234");
    while (m1.find()) {
      System.out.println("\t\t" + m1.group());
    }
    //now reset the matcher with new data
    m1.reset("56789");
    System.out.println("After resetting the Matcher");
    //iterate through the matcher
    while (m1.find()) {
      System.out.println("\t\t" + m1.group());
    }
  }
}
```

Related examples in the same category
---
1. Matcher: Find Demo
2. Matcher Reset
3. Matcher Pattern
4. Matcher start
5. Matcher start with parameter
6. Matcher end
7. Matcher end with parameter
8. Matcher group
9. Matcher group with parameter
10. Matcher group count
11. Matcher match
12. Matcher find
13. Matcher find with parameter
14. Matcher LookingAt
15. Matcher appendReplacement
16. Matcher replaceAll
17. Matcher replaceFirst
18. Matcher group 2
19. Matcher group with parameter 2
20. Matcher ground count
21. Matcher replaceAll 2
22. Matcher find group
23. Another Matcher find and group
24. Pattern compile
25. Show line ending matching using Regular Expressions class
26. Matcher Groups
27. Matches Looking
