---
title: Obtain ScriptEngine
nav: Obtain ScriptEngine
description: Imported from the java2s.com archive: Obtain ScriptEngine
section: Imported - java2s Archive
order: 1981
source: https://web.archive.org/web/2020/http://www.java2s.com/Tutorial/Java/0120__Development/ObtainScriptEngine.htm
---
```java title=Example.java
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
public class ObtainScriptEngine {
  public static void main(String[] args) {
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine engine1 = manager.getEngineByExtension("js");
    System.out.println(engine1);
    ScriptEngine engine2 = manager
        .getEngineByMimeType("application/javascript");
    System.out.println(engine2);
    ScriptEngine engine3 = manager.getEngineByName("rhino");
    System.out.println(engine3);
  }
}
```

| 6.48.1. | Obtain ScriptEngine |
|---|---|
| 6.48.2. | Enumerate ScriptEngines |
| 6.48.3. | Function Evaluator |
| 6.48.4. | Bindings And Scopes |
| 6.48.5. | Pass value and get return value from script |
| 6.48.6. | Temperature Conversion with script |
| 6.48.7. | Test Compilation Speed |
| 6.48.8. | Threading Behavior |
