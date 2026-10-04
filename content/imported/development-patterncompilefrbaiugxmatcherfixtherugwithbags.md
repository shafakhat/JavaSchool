---
title: Pattern.compile('[frb][aiu][gx]).matcher('fix the rug with bags')
nav: Pattern.compile('[frb][aiu...
description: Matcher m = Pattern.compile("[frb][aiu][gx]").matcher("fix the rug with bags");
section: Imported - java2s Archive
order: 1888
source: https://web.archive.org/web/20140829082436/http://www.java2s.com/Tutorial/Java/0120__Development/Patterncompilefrbaiugxmatcherfixtherugwithbags.htm
---
```java title=Example.java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class MainClass {
  public static void main(String[] args) throws Exception {
    Matcher m = Pattern.compile("[frb][aiu][gx]").matcher("fix the rug with bags");
    while (m.find())
      System.out.println(m.group());
    m.reset("fix the rig with rags");
    while (m.find())
      System.out.println(m.group());
  }
}
/*
*/
java title=Example.java
fix
rug
bag
fix
rig
rag
```
