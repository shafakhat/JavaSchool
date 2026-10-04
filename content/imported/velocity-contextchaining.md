---
title: Context Chaining
nav: Context Chaining
description: Template template = Velocity.getTemplate("./src/ContextChaining.vm");
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20060926092723/http://www.java2s.com:80/Code/Java/Velocity/ContextChaining.htm
---
```java title=Example.java
-------------------------------------------------------------------------------------
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class ContextChaining {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template template = Velocity.getTemplate("./src/ContextChaining.vm");
    VelocityContext context1 = new VelocityContext();
    VelocityContext context2 = new VelocityContext(context1);
    context1.put("firstName", "Joe");
    context2.put("lastName", "Yin");
    Writer writer = new StringWriter();
    template.merge(context2, writer);
    System.out.println(writer.toString());
  }
}
-------------------------------------------------------------------------------------
This is my first name $firstName
This is my last name $lastName
Full Name is $firstName $lastName
```

Download: velocity-ContextChaining.zip ( 795 K )
Related examples in the same category
