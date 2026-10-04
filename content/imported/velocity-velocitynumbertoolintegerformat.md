---
title: Velocity Number Tool Integer Format
nav: Velocity Number Tool Integ...
description: Download: velocity-NumberTool-Integer-Formating.zip ( 875 K )
section: Imported - java2s Archive
order: 1091
source: https://web.archive.org/web/20060717062942/http://www.java2s.com:80/Code/Java/Velocity/VelocityNumberToolIntegerFormat.htm
---
Velocity Number Tool Integer Format

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
Integer Formatting:     $number.format("integer", $aNumber)
```

Download: velocity-NumberTool-Integer-Formating.zip ( 875 K )
---
Related examples in the same category
1. Velocity NumberTool Currency Formatting
2. Velocity Number Tool Currency Locale
3. Velocity Number Tool Percentage Format
