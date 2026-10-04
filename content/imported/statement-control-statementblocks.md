---
title: Statement Blocks
nav: Statement Blocks
description: You can have a block of statements enclosed between braces. If the value of expression is true, all the statements enclosed in the block will be executed. Without the bra
section: Imported - java2s Archive
order: 1172
source: https://web.archive.org/web/20140829082055/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/StatementBlocks.htm
---
You can have a block of statements enclosed between braces. If the value of expression is true, all the statements enclosed in the block will be executed. Without the braces, the code no longer has a statement block.

```java title=Example.java
public class MainClass {
  public static void main(String[] arg) {
    int a = 0;
    if (a == 0) {
      System.out.println("in the block");
      System.out.println("in the block");
    }
  }
}
java title=Example.java
in the block
in the block
```
