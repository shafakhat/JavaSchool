---
title: String Quotation Demo
nav: String Quotation Demo
description: Imported from the java2s.com archive: String Quotation Demo
section: Imported - java2s Archive
order: 1059
source: https://web.archive.org/web/20060513092144/http://www.java2s.com/Code/Java/Velocity/StringQuotationDemo.htm
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
#set($name = "joe")
#set($address = "@hotmail.com")
#set($email = "$name$address")
#set($quote = '"')
#set($link = "<a href=${quote}mailto:$email${quote}>$email</a>")
Mail me at: $link
```

Download: velocity-String-quotation.zip (877 K)
---
Related examples in the same category
1. String concatenation
2. Concatenate two string variables
