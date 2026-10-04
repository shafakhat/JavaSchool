---
title: Compiling with a DiagnosticListener
nav: Compiling with a Diagnosti...
description: JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
section: Imported - java2s Archive
order: 1895
source: https://web.archive.org/web/20140829081512/http://www.java2s.com/Tutorial/Java/0120__Development/CompilingwithaDiagnosticListener.htm
---
```java title=Example.java
import java.io.IOException;
import java.util.Arrays;
import javax.tools.Diagnostic;
import javax.tools.DiagnosticCollector;
import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.StandardJavaFileManager;
import javax.tools.ToolProvider;
public class SecondCompile {
  public static void main(String args[]) throws IOException {
    JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
    DiagnosticCollector<JavaFileObject> diagnostics = new DiagnosticCollector<JavaFileObject>();
    StandardJavaFileManager fileManager = compiler.getStandardFileManager(diagnostics, null, null);
    Iterable<? extends JavaFileObject> compilationUnits = fileManager
        .getJavaFileObjectsFromStrings(Arrays.asList("YourFile.java"));
    Iterable<String> options = Arrays.asList("-d", "classes", "-sourcepath", "src");
    JavaCompiler.CompilationTask task = compiler.getTask(null, fileManager, diagnostics, options,
        null, compilationUnits);
    boolean success = task.call();
    for (Diagnostic diagnostic : diagnostics.getDiagnostics()) {
      System.out.println(diagnostic.getCode());
      System.out.println(diagnostic.getKind());
      System.out.println(diagnostic.getPosition());
      System.out.println(diagnostic.getStartPosition());
      System.out.println(diagnostic.getEndPosition());
      System.out.println(diagnostic.getSource());
      System.out.println(diagnostic.getMessage(null));
    }
    fileManager.close();
    System.out.println("Success: " + success);
  }
}
```

| 6.41.1. | Java Compiler tools: how you can compile a Java source from inside a Java program |
|---|---|
| 6.41.2. | Diagnostic Demo |
| 6.41.3. | Compile a Java code |
| 6.41.4. | Compile a Java file with JavaCompiler |
| 6.41.5. | Compiling with a DiagnosticListener |
| 6.41.6. | Compiling from Memory |
