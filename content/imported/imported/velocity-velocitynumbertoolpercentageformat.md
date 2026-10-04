---
title: Velocity Number Tool Percentage Format
nav: Velocity Number Tool Perce...
description: Download: velocity-NumberTool-Percentage-Formatting.zip ( 875 K )
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20060717063649/http://www.java2s.com:80/Code/Java/Velocity/VelocityNumberToolPercentageFormat.htm
---
Velocity Number Tool Percentage Format

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import java.util.Locale;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.NumberTool;
public class NumberToolExample {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/numberTool.vm");
    VelocityContext ctx = new VelocityContext();
    ctx.put("number", new NumberTool());
    ctx.put("aNumber", new Double(0.95));
    ctx.put("aLocale", Locale.UK);
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
Percentage Formatting:  $number.format("percent", $aNumber)
```

Download: velocity-NumberTool-Percentage-Formatting.zip ( 875 K )
---
Related examples in the same category
1. Velocity NumberTool Currency Formatting
2. Velocity Number Tool Currency Locale
3. Velocity Number Tool Integer Format
