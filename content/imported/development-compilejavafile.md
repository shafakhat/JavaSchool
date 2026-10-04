---
title: Compile Java file
nav: Compile Java file
description: JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
section: Imported - java2s Archive
order: 1944
source: https://web.archive.org/web/20140829091841/http://www.java2s.com/Tutorial/Java/0120__Development/CompileJavafile.htm
---
```java title=Example.java
import javax.tools.Diagnostic;
import javax.tools.DiagnosticCollector;
import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.StandardJavaFileManager;
import javax.tools.ToolProvider;
public class CompileFiles2 {
  public static void main(String[] args) {
    JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
    DiagnosticCollector<JavaFileObject> dc;
    dc = new DiagnosticCollector<JavaFileObject>();
    StandardJavaFileManager sjfm;
    sjfm = compiler.getStandardFileManager(dc, null, null);
    Iterable<? extends JavaFileObject> fileObjects;
    fileObjects = sjfm.getJavaFileObjects(args);
    compiler.getTask(null, sjfm, dc, null, null, fileObjects).call();
    for (Diagnostic d : dc.getDiagnostics()) {
      System.out.println(d.getMessage(null));
      System.out.printf("Line number = %d\n", d.getLineNumber());
      System.out.printf("File = %s\n", d.getSource());
    }
  }
}
```

| 6.46.1. | JavaCompiler.run to compile |
|---|---|
| 6.46.2. | Enum Alternate Java Compilers |
| 6.46.3. | Compile String |
| 6.46.4. | Compile Java file |
| 6.46.5. | Compiler Info |
| 6.46.6. | Get classpath using System class |
| 6.46.7. | Programmatically compile Java class |
