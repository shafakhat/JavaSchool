---
title: Use jrunscript to execute JavaScript scripts
nav: Use jrunscript to execute ...
description: Imported from the java2s.com archive: Use jrunscript to execute JavaScript scripts
section: Imported - java2s Archive
order: 1913
source: https://web.archive.org/web/20140829082045/http://www.java2s.com/Tutorial/Java/0120__Development/UsejrunscripttoexecuteJavaScriptscripts.htm
---
| You can use jrunscript in interactive or batch mode to execute scripts. |
|---|
| In interactive mode, you can type and execute scripts from the jrunscript prompt. |
| In batch mode, you can load and execute script files using jrunscript. |
| By default, jrunscript executes scripts developed using the JavaScript scripting language. |
| To specify a different language, you can use the –l option while executing jrunscript. |
| jrunscript [options] |
| Option Description -classpath path Specifies the path to the Java class files. -l language Specifies the scripting language. -e script Evaluates the given script. -encoding encoding Specifies the character encoding used while reading script files. -f script-file Evaluates a script file. -f Reads and evaluates a script from the console. This is called interactive mode. -q Lists all available script engines. |

```java title=Example.java
jrunscript -e "print('hello world')"
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
