---
title: To replace one specific character with another throughout a string
nav: To replace one specific ch...
description: String newText = text.replace(' ', '/'); // Modify the string text
section: Imported - java2s Archive
order: 1129
source: https://web.archive.org/web/20070328233006/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Toreplaceonespecificcharacterwithanotherthroughoutastring.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    String text = "To be or not to be, that is the question.";
    String newText = text.replace(' ', '/');     // Modify the string text
    System.out.println(newText);
  }
}</code>
      <result>To/be/or/not/to/be,/that/is/the/question.</result>
   </topic>
   <topic title="To remove whitespace from the beginning and end of a string (but not the interior)">
      <code><![CDATA[
public class MainClass {
  public static void main(String[] arg) {
    String sample = "   This is a string   ";
    String result = sample.trim();
    System.out.println(">"+sample+"<");
    System.out.println(">"+result+"<");
  }
}
```

```java title=Example.java
>   This is a string   <
>This is a string<
```
