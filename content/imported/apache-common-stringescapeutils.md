---
title: String Escape Utils
nav: String Escape Utils
description: Imported from the java2s.com archive: String Escape Utils
section: Imported - java2s Archive
order: 1067
source: https://web.archive.org/web/20071025002319/http://www.java2s.com:80/Code/Java/Apache-Common/StringEscapeUtils.htm
---
```java title=Example.java
/*
Are you for real?
What\'s in a name?
Mc''Williams
&lt;data&gt;
&lt;data&gt;
*/
import org.apache.commons.lang.StringEscapeUtils;
public class StringUtilsEscapeExampleV1 {
  public static void main(String args[]) {
    String unescapedJava = "Are you for real?";
    System.err.println(
      StringEscapeUtils.escapeJava(unescapedJava));
    String unescapedJavaScript = "What's in a name?";
    System.err.println(
      StringEscapeUtils.escapeJavaScript(unescapedJavaScript));
    String unescapedSql = "Mc'Williams";
    System.err.println(
      StringEscapeUtils.escapeSql(unescapedSql));
    String unescapedXML = "<data>";
    System.err.println(
      StringEscapeUtils.escapeXml(unescapedXML));
    String unescapedHTML = "<data>";
    System.err.println(
      StringEscapeUtils.escapeHtml(unescapedHTML));
  }
}
```

BeanUtilsStringUtilsEscapeExampleV1.zip( 1,005 k)
1.  String abbreviate
2.  String capitalize
3.  String center
4.  String chop by
5.  String chop
6.  String contains
7.  String contains none
8.  String contains only
9.  String count matches
10.  String delete white space
11.  String difference
12.  Get difference between two strings

w_w__w__._ja___v__a2__s___._c___o__m__
