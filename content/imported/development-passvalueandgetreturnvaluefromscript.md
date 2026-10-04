---
title: Pass value and get return value from script
nav: Pass value and get return ...
description: String calcMonthlyPaymentScript = "intrate = intrate/1200.0;"
section: Imported - java2s Archive
order: 1974
source: https://web.archive.org/web/20140829075335/http://www.java2s.com/Tutorial/Java/0120__Development/Passvalueandgetreturnvaluefromscript.htm
---
```java title=Example.java
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
public class MonthlyPayment {
  public static void main(String[] args) throws Exception {
    ScriptEngineManager manager = new ScriptEngineManager();
    ScriptEngine engine = manager.getEngineByExtension("js");
    String calcMonthlyPaymentScript = "intrate = intrate/1200.0;"
        + "payment = principal*intrate*(Math.pow (1+intrate, months)/"
        + "                            (Math.pow (1+intrate,months)-1));";
    engine.put("principal", 20000.0);
    System.out.println("Principal = " + engine.get("principal"));
    engine.put("intrate", 6.0);
    System.out.println("Interest Rate = " + engine.get("intrate") + "%");
    engine.put("months", 360);
    System.out.println("Months = " + engine.get("months"));
    engine.eval(calcMonthlyPaymentScript);
    System.out.printf("Monthly Payment = %.2f\n", engine.get("payment"));
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
