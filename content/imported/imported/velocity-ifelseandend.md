---
title: If Else and End
nav: If Else and End
description: Imported from the java2s.com archive: If Else and End
section: Imported - java2s Archive
order: 1041
source: https://web.archive.org/web/20060513075042/http://www.java2s.com/Code/Java/Velocity/IfElseandEnd.htm
---
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

Download: velocity-If-else-end.zip (875 K)
---
Related examples in the same category
1. Use if in velocity
2. If and elseif
3. If statement inside a for loop
