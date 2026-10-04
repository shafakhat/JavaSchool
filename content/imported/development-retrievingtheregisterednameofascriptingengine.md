---
title: Retrieving the Registered Name of a Scripting Engine
nav: Retrieving the Registered ...
description: List<ScriptEngineFactory> factories = manager.getEngineFactories();
section: Imported - java2s Archive
order: 1919
source: https://web.archive.org/web/20140829081746/http://www.java2s.com/Tutorial/Java/0120__Development/RetrievingtheRegisteredNameofaScriptingEngine.htm
---
```java title=Example.java
import java.util.List;
import javax.script.ScriptEngineFactory;
import javax.script.ScriptEngineManager;
public class RegisteredNameDemo {
  public static void main(String[] args) {
    ScriptEngineManager manager = new ScriptEngineManager();
    List<ScriptEngineFactory> factories = manager.getEngineFactories();
    for (ScriptEngineFactory factory : factories) {
      List<String> regNames = factory.getNames();
      for (int i = 0; i < regNames.size(); i++) {
        System.out.printf("Registered name " + i + " " + (String) regNames.get(i) + "\n");
      }
    }
  }
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
