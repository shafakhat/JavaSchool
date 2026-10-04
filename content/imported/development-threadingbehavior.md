---
title: Threading Behavior
nav: Threading Behavior
description: List<ScriptEngineFactory> factories = manager.getEngineFactories();
section: Imported - java2s Archive
order: 1972
source: https://web.archive.org/web/20140829075352/http://www.java2s.com/Tutorial/Java/0120__Development/ThreadingBehavior.htm
---
```java title=Example.java
import java.util.List;
import javax.script.ScriptEngineFactory;
import javax.script.ScriptEngineManager;
public class ThreadingBehavior {
  public static void main(String[] args) {
    ScriptEngineManager manager = new ScriptEngineManager();
    List<ScriptEngineFactory> factories = manager.getEngineFactories();
    for (ScriptEngineFactory factory : factories)
      System.out.println("Threading behavior: "
          + factory.getParameter("THREADING"));
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
