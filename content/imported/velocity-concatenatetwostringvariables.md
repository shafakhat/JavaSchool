---
title: Concatenate two string variables
nav: Concatenate two string var...
description: Concatenate two string variables : Java examples (example source code) » Velocity » String
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20060513092140/http://www.java2s.com/Code/Java/Velocity/Concatenatetwostringvariables.htm
---
Concatenate two string variables : Java examples (example source code) » Velocity » String

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
#set($name = "joe")
#set($address = "@hotmail.com")
#set($email = "$name$address")
Mail me at: <a href="mailto:$email">$email</a>
```

Download: velocity-String-Variable-Add.zip (877 K)
---
Related examples in the same category
1. String concatenation
2. String Quotation Demo
