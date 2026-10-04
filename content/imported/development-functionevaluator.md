---
title: Function Evaluator
nav: Function Evaluator
description: .println("usage: java FuncEvaluator scriptfile " + "script-exp");
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20111105115342/http://java2s.com/Tutorial/Java/0120__Development/FunctionEvaluator.htm
---
```java title=Example.java
import java.io.FileReader;
import java.io.IOException;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
public class FuncEvaluator {
  public static void main(String[] args) {
    if (args.length != 2) {
      System.err
          .println("usage: java FuncEvaluator scriptfile " + "script-exp");
      return;
    }
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine engine = manager.getEngineByName("rhino");
    try {
      System.out.println(engine.eval(new FileReader(args[0])));
      System.out.println(engine.eval(args[1]));
    } catch (ScriptException se) {
      System.err.println(se.getMessage());
    } catch (IOException ioe) {
      System.err.println(ioe.getMessage());
    }
  }
}
//////////////
function combinations (n, r)
{
   return fact (n)/(fact (r)*fact (n-r))
}
function fact (n)
{
   if (n == 0)
       return 1;
   else
       return n*fact (n-1);
}
```
