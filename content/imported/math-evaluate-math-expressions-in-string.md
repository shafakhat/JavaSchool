---
title: Java Algorithms How to - Evaluate math expressions in String
nav: Java Algorithms How to - E...
description: We would like to know how to evaluate math expressions in String.
section: Imported - java2s Archive
order: 1013
source: https://web.archive.org/web/20160731162339/http://www.java2s.com:80/Tutorials/Java/Algorithms_How_to/Math/Evaluate_math_expressions_in_String.htm
---
## Question

We would like to know how to evaluate math expressions in String.

## Answer

```java title=Example.java
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
publicclass Main {
  publicstaticvoid main(String[] args) throws Exception {
    // create a script engine manager
    ScriptEngineManager factory = new ScriptEngineManager();
    // create a JavaScript engine
    ScriptEngine engine = factory.getEngineByName("JavaScript");
    // evaluate JavaScript code from String
    Object obj = engine.eval("1+2");
    System.out.println(obj);
  }
}
```

The code above generates the following result.
