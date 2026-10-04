---
title: Catch ScriptException
nav: Catch ScriptException
description: Bindings bindings = engine.getBindings(ScriptContext.ENGINE_SCOPE);
section: Imported - java2s Archive
order: 1901
source: https://web.archive.org/web/20140829082421/http://www.java2s.com/Tutorial/Java/0120__Development/CatchScriptException.htm
---
```java title=Example.java
import javax.script.Bindings;
import javax.script.ScriptContext;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
public class BindingDemo {
  public static void main(String[] args) {
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine engine = manager.getEngineByName("js");
    engine.put("a", 1);
    engine.put("b", 5);
    Bindings bindings = engine.getBindings(ScriptContext.ENGINE_SCOPE);
    Object a = bindings.get("a");
    Object b = bindings.get("b");
    System.out.println("a = " + a);
    System.out.println("b = " + b);
    Object result;
    try {
      result = engine.eval("c = aaaa + bbbb;");
      System.out.println("a + b = " + result);
    } catch (ScriptException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
  }
}
java title=Example.java
a = 1
b = 5
javax.script.ScriptException: sun.org.mozilla.javascript.internal.EcmaError: ReferenceError: "aaaa" is not defined. (#1) in  at line number 1
  at com.sun.script.javascript.RhinoScriptEngine.eval(RhinoScriptEngine.java:110)
  at com.sun.script.javascript.RhinoScriptEngine.eval(RhinoScriptEngine.java:124)
  at javax.script.AbstractScriptEngine.eval(AbstractScriptEngine.java:247)
  at BindingDemo.main(BindingDemo.java:22)
```

| 6.42.1. | Listing All Script Engines |
|---|---|
| 6.42.2. | List the script engines |
| 6.42.3. | Running Scripts with Java Script Engine |
| 6.42.4. | Execute Javascript script in a file |
| 6.42.5. | Variables bound through ScriptEngine |
| 6.42.6. | Catch ScriptException |
| 6.42.7. | Any script have to be compiled into intermediate code. |
| 6.42.8. | With Compilable interface you store the intermediate code of an entire script |
| 6.42.9. | Run JavaScript and get the result by using Java |
| 6.42.10. | Pass parameter to JavaScript through Java code |
| 6.42.11. | Get the value in JavaScript from Java Code by reference the variable name |
| 6.42.12. | Working with Compilable Scripts |
| 6.42.13. | Call a JavaScript function three times |
| 6.42.14. | Save the compiled JavaScript to CompiledScript object |
| 6.42.15. | Invoke an function |
| 6.42.16. | Using thread to run JavaScript by Java |
| 6.42.17. | Use jrunscript to execute JavaScript scripts |
| 6.42.18. | Get Script engine by extension name |
| 6.42.19. | Get a ScriptEngine by MIME type |
| 6.42.20. | Retrieving Script Engines by Name |
| 6.42.21. | Retrieving the Metadata of Script Engines |
| 6.42.22. | Retrieving the Supported File Extensions of a Scripting Engine |
| 6.42.23. | Retrieving the Supported Mime Types of a Scripting Engine |
| 6.42.24. | Retrieving the Registered Name of a Scripting Engine |
| 6.42.25. | Executing Scripts from Java Programs |
| 6.42.26. | Read and execute a script source file |
| 6.42.27. | Using Java Objects in JavaScript |
| 6.42.28. | Java Language Binding with JavaScript |
