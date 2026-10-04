---
title: Call class methods
nav: Call class methods
description: Imported from the java2s.com archive: Call class methods
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20071104100032/http://www.java2s.com:80/Code/Java/Velocity/Callclassmethods.htm
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
Day: $aDate.getDate()
Month: $aDate.getMonth()
Year: $aDate.getYear()
```

velocity-Class-Methods.zip( 875 k)
1.  Reference Class Properties
