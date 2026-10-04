---
title: Compile a Java file with JavaCompiler
nav: Compile a Java file with J...
description: JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
section: Imported - java2s Archive
order: 1893
source: https://web.archive.org/web/20140829082226/http://www.java2s.com/Tutorial/Java/0120__Development/CompileaJavafilewithJavaCompiler.htm
---
```java title=Example.java
import java.io.IOException;
import java.util.Arrays;
import javax.tools.DiagnosticCollector;
import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.StandardJavaFileManager;
import javax.tools.ToolProvider;
public class DiagnosticCollectorCompile {
  public static void main(String args[]) throws IOException {
    JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
    DiagnosticCollector<JavaFileObject> diagnostics = new DiagnosticCollector<JavaFileObject>();
    StandardJavaFileManager fileManager = compiler.getStandardFileManager(diagnostics, null, null);
    Iterable<? extends JavaFileObject> compilationUnits = fileManager
        .getJavaFileObjectsFromStrings(Arrays.asList("Foo.java"));
    JavaCompiler.CompilationTask task = compiler.getTask(null, fileManager, diagnostics, null,
        null, compilationUnits);
    boolean success = task.call();
    fileManager.close();
    System.out.println("Success: " + success);
  }
}
// File: MyClass.java
class MyClass {
  public static void main(String args[]) {
    System.out.println("Hello, World");
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
