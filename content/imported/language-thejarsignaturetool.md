---
title: The jarsignature Tool
nav: The jarsignature Tool
description: The jarsigner tool enables you to sign Java ARchive (JAR) files and verify the signatures of signed JAR files.
section: Imported - java2s Archive
order: 1075
source: https://web.archive.org/web/20140829082107/http://www.java2s.com/Tutorial/Java/0020__Language/ThejarsignatureTool.htm
---
The jarsigner tool enables you to sign Java ARchive (JAR) files and verify the signatures of signed JAR files.
---
The jarsigner tool uses key and certificate information from a keystore to generate digital signatures for JAR files.
A keystore is a database of private keys.
The jarsignature also uses an entity's private key to generate a signature.
The syntax to use the jarsignature tool is:

```java title=Example.java
jarsigner [ options ] jar-file alias
jarsigner -verify [ options ] jar-file
```
