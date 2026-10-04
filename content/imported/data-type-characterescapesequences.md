---
title: Character Escape Sequences
nav: Character Escape Sequences
description: An escape sequence for a Unicode character: adding '\u' in front of the code
section: Imported - java2s Archive
order: 1181
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CharacterEscapeSequences.htm
---
A backslash indicates the start of an escape sequence.

An escape sequence for a Unicode character: adding '\u' in front of the code

Website for unicode http://www.unicode.org/

```java title=Example.java
public class MainClass{
  public static void main(String[] arg){
     char myCharacter = '\u0058';
     System.out.println(myCharacter);
  }
}
java title=Example.java
X
```
