---
title: Displays directory listing using regular expressions
nav: Displays directory listing...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20061018194939/http://www.java2s.com/Code/Java/Regular-Expressions/Displaysdirectorylistingusingregularexpressions.htm
---
```java title=Example.java
// : c12:DirList.java
// {Args: "D.*\.java"}
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.io.File;
import java.io.FilenameFilter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.regex.Pattern;
public class DirList {
  public static void main(String[] args) {
    File path = new File(".");
    String[] list;
    if (args.length == 0)
      list = path.list();
    else
      list = path.list(new DirFilter(args[0]));
    Arrays.sort(list, new AlphabeticComparator());
    for (int i = 0; i < list.length; i++)
      System.out.println(list[i]);
  }
}
class DirFilter implements FilenameFilter {
  private Pattern pattern;
  public DirFilter(String regex) {
    pattern = Pattern.compile(regex);
  }
  public boolean accept(File dir, String name) {
    // Strip path information, search for regex:
    return pattern.matcher(new File(name).getName()).matches();
  }
} ///:~
class AlphabeticComparator implements Comparator {
  public int compare(Object o1, Object o2) {
    String s1 = (String) o1;
    String s2 = (String) o2;
    return s1.toLowerCase().compareTo(s2.toLowerCase());
  }
} ///:~
```

Related examples in the same category
---
1. Like Regular Expression Demo in a TextField
2. StringConvenience -- demonstrate java.lang.String convenience routine
3. Split a String into a Java Array of Strings divided by an Regular Expressions
4. Simple example of using Regular Expressions class.
5. Match the Q[^u] pattern against strings from command line
6. demonstrate Regular Expressions: Match -> group()
7. Show case control using Regular Expressions class.
8. Matcher and Pattern demo
9. Matcher and Pattern demo 2
10. Standalone Swing GUI application for demonstrating Regular expressions.
11. Regular Expressions in Action
