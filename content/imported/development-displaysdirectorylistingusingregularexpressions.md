---
title: Displays directory listing using regular expressions
nav: Displays directory listing...
description: Imported from the java2s.com archive: Displays directory listing using regular expressions
section: Imported - java2s Archive
order: 1887
source: https://web.archive.org/web/20140829082322/http://www.java2s.com/Tutorial/Java/0120__Development/Displaysdirectorylistingusingregularexpressions.htm
---
```java title=Example.java
import java.io.File;
import java.io.FilenameFilter;
import java.util.Arrays;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String[] args) {
    File path = new File(".");
    String[] list;
    if (args.length == 0)
      list = path.list();
    else
      list = path.list(new DirFilter(args[0]));
    Arrays.sort(list);
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
    return pattern.matcher(new File(name).getName()).matches();
  }
}
```
