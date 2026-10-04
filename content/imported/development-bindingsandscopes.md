---
title: Bindings And Scopes
nav: Bindings And Scopes
description: dumpBindings(engine.getBindings(ScriptContext.GLOBAL_SCOPE));
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20111105121428/http://java2s.com/Tutorial/Java/0120__Development/BindingsAndScopes.htm
---
```java title=Example.java
import javax.script.Bindings;
import javax.script.ScriptContext;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
public class GetToKnowBindingsAndScopes {
  public static void main(String[] args) {
    ScriptEngineManager manager = new ScriptEngineManager();
    manager.put("global", "global bindings");
    dumpBindings(manager.getBindings());
    ScriptEngine engine = manager.getEngineByExtension("js");
    engine.put("engine", "engine bindings");
    dumpBindings(engine.getBindings(ScriptContext.GLOBAL_SCOPE));
    dumpBindings(engine.getBindings(ScriptContext.ENGINE_SCOPE));
    try {
      Bindings bindings = engine.createBindings();
      bindings.put("engine", "overridden engine bindings");
      bindings.put("app", new GetToKnowBindingsAndScopes());
      bindings.put("bindings", bindings);
      engine.eval("app.dumpBindings (bindings);", bindings);
    } catch (ScriptException se) {
      System.err.println(se.getMessage());
    }
    ScriptEngine engine2 = manager.getEngineByExtension("js");
    engine2.put("engine2", "engine2 bindings");
    dumpBindings(engine2.getBindings(ScriptContext.GLOBAL_SCOPE));
    dumpBindings(engine2.getBindings(ScriptContext.ENGINE_SCOPE));
    dumpBindings(engine.getBindings(ScriptContext.ENGINE_SCOPE));
  }
  public static void dumpBindings(Bindings bindings) {
    if (bindings == null)
      System.out.println("  No bindings");
    else
      for (String key : bindings.keySet())
        System.out.println("  " + key + ": " + bindings.get(key));
    System.out.println();
  }
}
```
