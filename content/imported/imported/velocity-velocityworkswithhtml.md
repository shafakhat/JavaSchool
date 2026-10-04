---
title: Velocity works With HTML
nav: Velocity works With HTML
description: Velocity works With HTML : Java examples (example source code) » Velocity » HTML
section: Imported - java2s Archive
order: 1101
source: https://web.archive.org/web/20060513101055/http://www.java2s.com/Code/Java/Velocity/VelocityworksWithHTML.htm
---
Velocity works With HTML : Java examples (example source code) » Velocity » HTML

Velocity works With HTML

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.RenderTool;
public class VMDemo {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/VMDemo.vm");
    VelocityContext ctx = new VelocityContext();
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
#set ($companyName = "Name")
<html>
  <head>
    <title>$companyName Homepage</title>
  </head>
  <body>
    <h1>Welcome!!</h1>
    #if ($userType == "VIP")
      <h2>You are a VIP!</h2>
    #else
      <h2>You are not a VIP!</h2>
    #end
  </body>
</html>
```

Download: velocity-WithHTML.zip (877 K)
---
Related examples in the same category
1. Use Velocity to generate HTML based email
2. Use Velocity to generate HTML document
3. Velocity Generate Document: anakia task
