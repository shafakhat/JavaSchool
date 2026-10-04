---
title: Diagnostic Demo
nav: Diagnostic Demo
description: JavaCompilerTool compiler = ToolProvider.getSystemJavaCompilerTool();
section: Imported - java2s Archive
order: 1894
source: https://web.archive.org/web/20140829082116/http://www.java2s.com/Tutorial/Java/0120__Development/DiagnosticDemo.htm
---
```java title=Example.java
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javax.tools.Diagnostic;
import javax.tools.DiagnosticCollector;
import javax.tools.JavaCompilerTool;
import javax.tools.JavaFileObject;
import javax.tools.StandardJavaFileManager;
import javax.tools.ToolProvider;
import javax.tools.JavaCompilerTool.CompilationTask;
public class DiagnosticDemo {
  public static void main(String[] args) {
    String sourceFile = "c:/HelloWorld.Java";
    JavaCompilerTool compiler = ToolProvider.getSystemJavaCompilerTool();
    DiagnosticCollector<JavaFileObject> diagnostics = new DiagnosticCollector<JavaFileObject>();
    StandardJavaFileManager fileManager =
    compiler.getStandardFileManager(diagnostics);
    List<File> sourceFileList = new ArrayList<File>();
    sourceFileList.add(new File(sourceFile));
    Iterable<? extends JavaFileObject> compilationUnits = fileManager
        .getJavaFileObjectsFromFiles(sourceFileList);
    CompilationTask task = compiler.getTask(null, fileManager, null, null, null, compilationUnits);
    task.run();
    try {
      fileManager.close();
    } catch (IOException e) {
    }
    List<Diagnostic<? extends JavaFileObject>> diagnosticList = diagnostics.getDiagnostics();
    for (Diagnostic<? extends JavaFileObject> diagnostic : diagnosticList) {
      System.out.println("Position:" + diagnostic.getStartPosition());
    }
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
