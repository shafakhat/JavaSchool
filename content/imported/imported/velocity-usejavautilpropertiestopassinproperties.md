---
title: Use java.util.Properties to pass in properties
nav: Use java.util.Properties t...
description: Template template = Velocity.getTemplate("./src/HelloWorld.vm");
section: Imported - java2s Archive
order: 1065
source: https://web.archive.org/web/20061026215433/http://www.java2s.com/Code/Java/Velocity/UsejavautilPropertiestopassinproperties.htm
---
Use java.util.Properties to pass in properties

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
//File: HelloWorld.vm
Hello World!
```

Download: velocity-WithProperties.zip ( 797 K )
Related examples in the same category
