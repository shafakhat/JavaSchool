---
title: Output a string from Velocity
nav: Output a string from Veloc...
description: Output a string from Velocity : Java examples (example source code) » Velocity » Output
section: Imported - java2s Archive
order: 1045
source: https://web.archive.org/web/20060513072910/http://www.java2s.com/Code/Java/Velocity/OutputastringfromVelocity.htm
---
Output a string from Velocity : Java examples (example source code) » Velocity » Output

```java title=Example.java
-------------------------------------------------------------------------------------
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class HelloWorld {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template template = Velocity.getTemplate("./src/HelloWorld.vm");
    VelocityContext context = new VelocityContext();
    Writer writer = new StringWriter();
    template.merge(context, writer);
    System.out.println(writer.toString());
  }
}
-------------------------------------------------------------------------------------
Hello World!
```

Download: velocity-HelloWorld.zip (795 K)
---
Related examples in the same category
1. Combine StringWriter with template
