---
title: Reference Class Properties
nav: Reference Class Properties
description: Imported from the java2s.com archive: Reference Class Properties
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20070303101815/http://www.java2s.com:80/Code/Java/Velocity/ReferenceClassProperties.htm
---
```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import java.util.Date;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class VMDemo {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/VMDemo.vm");
    VelocityContext ctx = new VelocityContext();
    ctx.put("aDate",new Date());
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
//File: VMDemo.vm
Day: $aDate.Date
Month: $aDate.Month
Year: $aDate.Year
```

Download: velocity-Class-Properties.zip ( 875 K )
Related examples in the same category
