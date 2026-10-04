---
title: Compile a Java code
nav: Compile a Java code
description: JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
section: Imported - java2s Archive
order: 1892
source: https://web.archive.org/web/20140829081641/http://www.java2s.com/Tutorial/Java/0120__Development/CompileaJavacode.htm
---
```java title=Example.java
import java.io.IOException;
import javax.tools.JavaCompiler;
import javax.tools.ToolProvider;
public class FirstCompile {
  public static void main(String args[]) throws IOException {
    JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
    int results = compiler.run(null, null, null, "Foo.java");
    System.out.println("Success: " + (results == 0));
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
