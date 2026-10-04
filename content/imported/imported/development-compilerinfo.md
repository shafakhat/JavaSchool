---
title: Compiler Info
nav: Compiler Info
description: JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20100909074411/http://www.java2s.com:80/Tutorial/Java/0120__Development/CompilerInfo.htm
---
```java title=Example.java
import java.util.Set;
import javax.lang.model.SourceVersion;
import javax.tools.JavaCompiler;
import javax.tools.ToolProvider;
public class CompilerInfo {
  public static void main(String[] args) {
    JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
    System.out.println("Supported source versions:");
    Set<SourceVersion> srcVer = compiler.getSourceVersions();
    for (SourceVersion sv : srcVer)
      System.out.println("  " + sv.name());
    int nargs = compiler.isSupportedOption(args[0]);
    if (nargs == -1)
      System.out.println("Option " + args[0] + " is not supported");
    else
      System.out.println("Option " + args[0] + " takes " + nargs + " arguments");
  }
}
```
