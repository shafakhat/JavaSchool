---
title: Combine StringWriter with template
nav: Combine StringWriter with ...
description: Combine StringWriter with template : Java examples (example source code) » Velocity » Output
section: Imported - java2s Archive
order: 1021
source: https://web.archive.org/web/20060513072913/http://www.java2s.com/Code/Java/Velocity/CombineStringWriterwithtemplate.htm
---
Combine StringWriter with template : Java examples (example source code) » Velocity » Output

Combine StringWriter with template

```java title=Example.java
-------------------------------------------------------------------------------------
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class HelloWorldWithVariable {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template template = Velocity.getTemplate("src/HelloWorldWithVariable.vm");
    VelocityContext context = new VelocityContext();
    context.put("name", "Joe Yin");
    Writer writer = new StringWriter();
    template.merge(context, writer);
    System.out.println(writer.toString());
  }
}
-------------------------------------------------------------------------------------
Hello $name!
```

Download: velocity-HelloWorldWithVariable.zip (795 K)
---
Related examples in the same category
1. Output a string from Velocity
