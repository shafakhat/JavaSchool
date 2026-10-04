---
title: Compile String
nav: Compile String
description: JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
section: Imported - java2s Archive
order: 1943
source: https://web.archive.org/web/20140216231854/http://www.java2s.com/Tutorial/Java/0120__Development/CompileString.htm
---
```java title=Example.java
import java.lang.reflect.Method;
import java.net.URI;
import java.util.Iterator;
import java.util.NoSuchElementException;
import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.SimpleJavaFileObject;
import javax.tools.ToolProvider;
public class CompileString {
  public static void main(String[] args) throws Exception {
    JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
    String program = "class Test{" + "   public static void main (String [] args){"
        + "      System.out.println (\"Hello, World\");"
        + "      System.out.println (args.length);" + "   }" + "}";
    Iterable<? extends JavaFileObject> fileObjects;
    fileObjects = getJavaSourceFromString(program);
    compiler.getTask(null, null, null, null, null, fileObjects).call();
    Class<?> clazz = Class.forName("Test");
    Method m = clazz.getMethod("main", new Class[] { String[].class });
    Object[] _args = new Object[] { new String[0] };
    m.invoke(null, _args);
  }
  static Iterable<JavaSourceFromString> getJavaSourceFromString(String code) {
    final JavaSourceFromString jsfs;
    jsfs = new JavaSourceFromString("code", code);
    return new Iterable<JavaSourceFromString>() {
      public Iterator<JavaSourceFromString> iterator() {
        return new Iterator<JavaSourceFromString>() {
          boolean isNext = true;
          public boolean hasNext() {
            return isNext;
          }
          public JavaSourceFromString next() {
            if (!isNext)
              throw new NoSuchElementException();
            isNext = false;
            return jsfs;
          }
          public void remove() {
            throw new UnsupportedOperationException();
          }
        };
      }
    };
  }
}
class JavaSourceFromString extends SimpleJavaFileObject {
  final String code;
  JavaSourceFromString(String name, String code) {
    super(URI.create("string:///" + name.replace('.', '/') + Kind.SOURCE.extension), Kind.SOURCE);
    this.code = code;
  }
  public CharSequence getCharContent(boolean ignoreEncodingErrors) {
    return code;
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
