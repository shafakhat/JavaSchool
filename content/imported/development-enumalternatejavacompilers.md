---
title: Enum Alternate Java Compilers
nav: Enum Alternate Java Compil...
description: Imported from the java2s.com archive: Enum Alternate Java Compilers
section: Imported - java2s Archive
order: 1942
source: https://web.archive.org/web/20140829091742/http://www.java2s.com/Tutorial/Java/0120__Development/EnumAlternateJavaCompilers.htm
---
```java title=Example.java
import java.util.ServiceLoader;
import javax.tools.JavaCompiler;
public class EnumAlternateJavaCompilers {
  public static void main(String[] args) {
    ServiceLoader<JavaCompiler> compilers;
    compilers = ServiceLoader.load(JavaCompiler.class);
    System.out.println(compilers.toString());
    for (JavaCompiler compiler : compilers)
      System.out.println(compiler);
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
