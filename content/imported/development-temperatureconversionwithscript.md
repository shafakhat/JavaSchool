---
title: Temperature Conversion with script
nav: Temperature Conversion wit...
description: public static void main(String[] args) throws ScriptException {
section: Imported - java2s Archive
order: 1970
source: https://web.archive.org/web/20140829075555/http://www.java2s.com/Tutorial/Java/0120__Development/TemperatureConversionwithscript.htm
---
```java title=Example.java
import javax.script.Invocable;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
public class TemperatureConversion {
  public static void main(String[] args) throws ScriptException {
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine engine = manager.getEngineByName("rhino");
    String script = "function c2f(degrees){return degrees*9.0/5.0+32;}";
        + "function f2c(degrees){return (degrees-32)*5.0/9.0;}" + " "
        + "function convertTemperature (degrees, toCelsius){"
        + "   if (toCelsius)" + "return f2c (degrees);elsereturn c2f (degrees);}";
    engine.eval(script);
    Invocable invocable = (Invocable) engine;
    TempConversion tc = invocable.getInterface(TempConversion.class);
    if (tc == null)
      System.err.println("Unable to obtain TempConversion interface");
    else {
      System.out.println("212 degrees Fahrenheit = "
          + tc.convertTemperature(212.0, true) + " degrees Celsius");
    }
  }
}
interface TempConversion {
  double convertTemperature(double degrees, boolean toCelsius);
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
