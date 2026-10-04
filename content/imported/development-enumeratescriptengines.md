---
title: Enumerate ScriptEngines
nav: Enumerate ScriptEngines
description: List<ScriptEngineFactory> factories = manager.getEngineFactories();
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20111105115605/http://java2s.com/Tutorial/Java/0120__Development/EnumerateScriptEngines.htm
---
```java title=Example.java
import java.util.List;
import javax.script.ScriptEngineFactory;
import javax.script.ScriptEngineManager;
public class EnumerateScriptEngines {
  public static void main(String[] args) {
    ScriptEngineManager manager = new ScriptEngineManager();
    List<ScriptEngineFactory> factories = manager.getEngineFactories();
    for (ScriptEngineFactory factory : factories) {
      System.out.println("Engine name (full): " + factory.getEngineName());
      System.out.println("Engine version: " + factory.getEngineVersion());
      System.out.println("Supported extensions:");
      List<String> extensions = factory.getExtensions();
      for (String extension : extensions)
        System.out.println("  " + extension);
      System.out.println("Language name: " + factory.getLanguageName());
      System.out.println("Language version: " + factory.getLanguageVersion());
      System.out.println("Supported MIME types:");
      List<String> mimetypes = factory.getMimeTypes();
      for (String mimetype : mimetypes)
        System.out.println("  " + mimetype);
      System.out.println("Supported short names:");
      List<String> shortnames = factory.getNames();
      for (String shortname : shortnames)
        System.out.println("  " + shortname);
      System.out.println();
    }
  }
}
```
