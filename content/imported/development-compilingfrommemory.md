---
title: Compiling from Memory
nav: Compiling from Memory
description: JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
section: Imported - java2s Archive
order: 1896
source: https://web.archive.org/web/20140829081612/http://www.java2s.com/Tutorial/Java/0120__Development/CompilingfromMemory.htm
---
```java title=Example.java
import java.io.IOException;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.lang.reflect.InvocationTargetException;
import java.net.URI;
import java.util.Arrays;
import javax.tools.Diagnostic;
import javax.tools.DiagnosticCollector;
import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.SimpleJavaFileObject;
import javax.tools.ToolProvider;
import javax.tools.JavaCompiler.CompilationTask;
import javax.tools.JavaFileObject.Kind;
public class CompileSourceInMemory {
  public static void main(String args[]) throws IOException {
    JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
    DiagnosticCollector<JavaFileObject> diagnostics = new DiagnosticCollector<JavaFileObject>();
    StringWriter writer = new StringWriter();
    PrintWriter out = new PrintWriter(writer);
    out.println("public class HelloWorld {");
    out.println("  public static void main(String args[]) {");
    out.println("    System.out.println(\"This is in another java file\");");
    out.println("  }");
    out.println("}");
    out.close();
    JavaFileObject file = new JavaSourceFromString("HelloWorld", writer.toString());
    Iterable<? extends JavaFileObject> compilationUnits = Arrays.asList(file);
    CompilationTask task = compiler.getTask(null, null, diagnostics, null, null, compilationUnits);
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
    System.out.println("Success: " + success);
    if (success) {
      try {
        Class.forName("HelloWorld").getDeclaredMethod("main", new Class[] { String[].class })
            .invoke(null, new Object[] { null });
      } catch (ClassNotFoundException e) {
        System.err.println("Class not found: " + e);
      } catch (NoSuchMethodException e) {
        System.err.println("No such method: " + e);
      } catch (IllegalAccessException e) {
        System.err.println("Illegal access: " + e);
      } catch (InvocationTargetException e) {
        System.err.println("Invocation target: " + e);
      }
    }
  }
}
class JavaSourceFromString extends SimpleJavaFileObject {
  final String code;
  JavaSourceFromString(String name, String code) {
    super(URI.create("string:///" + name.replace('.','/') + Kind.SOURCE.extension),Kind.SOURCE);
    this.code = code;
  }
  @Override
  public CharSequence getCharContent(boolean ignoreEncodingErrors) {
    return code;
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
