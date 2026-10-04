---
title: Velocity input encoding
nav: Velocity input encoding
description: Template template = Velocity.getTemplate("./src/HelloWorld.vm");
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20061026204231/http://www.java2s.com/Code/Java/Velocity/Velocityinputencoding.htm
---
Velocity input encoding

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import java.util.Properties;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class HelloWorldProperties {
  public static void main(String[] args) throws Exception {
    Properties props = new Properties();
    props.put("input.encoding", "utf-8");
    Velocity.init(props);
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

Download: velocity-Inpout-Encoding.zip ( 795 K )
Related examples in the same category
