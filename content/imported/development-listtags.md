---
title: List Tags
nav: List Tags
description: Imported from the java2s.com archive: List Tags
section: Imported - java2s Archive
order: 1814
source: https://web.archive.org/web/20140829094311/http://www.java2s.com/Tutorial/Java/0120__Development/ListTags.htm
---
```java title=Example.java
import javax.swing.text.html.HTML;
public class MainClass {
  public static void main(String[] args) {
    HTML.Tag[] list = HTML.getAllTags();
    for (int i = 0; i < list.length; i++) {
      System.out.println((i + 1) + ": " + list[i]);
    }
  }
}
java title=Example.java
1: a
2: address
3: applet
4: area
5: b
6: base
7: basefont
8: big
9: blockquote
10: body
11: br
12: caption
13: center
14: cite
15: code
16: dd
17: dfn
18: dir
19: div
20: dl
21: dt
22: em
23: font
24: form
25: frame
26: frameset
27: h1
28: h2
29: h3
30: h4
31: h5
32: h6
33: head
34: hr
35: html
36: i
37: img
38: input
39: isindex
40: kbd
41: li
42: link
43: map
44: menu
45: meta
46: nobr
47: noframes
48: object
49: ol
50: option
51: p
52: param
53: pre
54: samp
55: script
56: select
57: small
58: span
59: strike
60: s
61: strong
62: style
63: sub
64: sup
65: table
66: td
67: textarea
68: th
69: title
70: tr
71: tt
72: u
73: ul
74: var
```

| 6.31.1. | List Tags |
|---|---|
| 6.31.2. | html parser DTD |
| 6.31.3. | Use javax.swing.text.html.HTMLEditorKit to parse HTML |
| 6.31.4. | extends HTMLEditorKit.ParserCallback |
| 6.31.5. | Parse HTML |
| 6.31.6. | Convert to HTML string |
| 6.31.7. | Escape HTML |
| 6.31.8. | Filter message string for characters that are sensitive in HTML |
| 6.31.9. | Filter the specified message string for characters that are sensitive in HTML |
| 6.31.10. | HTML color names |
| 6.31.11. | Text To HTML |
| 6.31.12. | Unescape HTML |
| 6.31.13. | Utility methods for dealing with HTML |
| 6.31.14. | insert HTML block dynamically |
| 6.31.15. | A collection of all character entites defined in the HTML4 standard. |
| 6.31.16. | Decode an HTML color string like '#F567BA;' into a Color |
