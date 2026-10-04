---
title: Any script have to be compiled into intermediate code.
nav: Any script have to be comp...
description: This compilation takes a relatively large amount of CPU cycles.
section: Imported - java2s Archive
order: 1905
source: https://web.archive.org/web/20140829081953/http://www.java2s.com/Tutorial/Java/0120__Development/Anyscripthavetobecompiledintointermediatecode.htm
---
This compilation takes a relatively large amount of CPU cycles.
With the Invocable interface you can save time by storing the compiled intermediate code for reuse.

```java title=Example.java
import javax.script.Invocable;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
public class InvocableDemo {
  public static void main(String[] args) throws Exception {
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine engine = manager.getEngineByName("js");
    engine.eval("function add (a, b) {c = a + b; return c; }");
    Invocable jsInvoke = (Invocable) engine;
    Object result1 = jsInvoke.invokeFunction("add", new Object[] { 10, 5 });
    System.out.println(result1);
    Adder adder = jsInvoke.getInterface(Adder.class);
    int result2 = adder.add(10, 5);
    System.out.println(result2);
  }
}
interface Adder {
  int add(int a, int b);
}
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
