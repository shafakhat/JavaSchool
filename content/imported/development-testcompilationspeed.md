---
title: Test Compilation Speed
nav: Test Compilation Speed
description: String fact = "function fact (n){if (n == 0)return 1; else return n*fact (n-1);};";
section: Imported - java2s Archive
order: 1971
source: https://web.archive.org/web/20140829075421/http://www.java2s.com/Tutorial/Java/0120__Development/TestCompilationSpeed.htm
---
```java title=Example.java
import javax.script.Compilable;
import javax.script.CompiledScript;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
public class TestCompilationSpeed {
  final static int MAX_ITERATIONS = 10000;
  public static void main(String[] args) throws Exception {
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine engine = manager.getEngineByName("JavaScript");
    String fact = "function fact (n){if (n == 0)return 1; else return n*fact (n-1);};";
    long time = System.currentTimeMillis();
    for (int i = 0; i < MAX_ITERATIONS; i++)
      engine.eval(fact);
    System.out.println(System.currentTimeMillis() - time);
    Compilable compilable = null;
    if (engine instanceof Compilable) {
      compilable = (Compilable) engine;
      CompiledScript script = compilable.compile(fact);
      time = System.currentTimeMillis();
      for (int i = 0; i < MAX_ITERATIONS; i++)
        script.eval();
      System.out.println(System.currentTimeMillis() - time);
    }
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
