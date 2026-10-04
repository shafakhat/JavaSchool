---
title: If and elseif
nav: If and elseif
description: Imported from the java2s.com archive: If and elseif
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20060513075034/http://www.java2s.com/Code/Java/Velocity/Ifandelseif.htm
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
    #if ($userType == "Type 1")
      <h2>You are Type 1!</h2>
    #elseif ($userType == "Type 2")
      <h2>You are an Type 2. </h2>
    #elseif ($userType == "Type 3")
      <h2>You are an Type 3!</h2>
    #else
      <h2>I don't know what you are!</h2>
    #end
  </body>
</html>
```

Download: velocity-If-elseif.zip (875 K)
---
Related examples in the same category
1. Use if in velocity
2. If Else and End
3. If statement inside a for loop
