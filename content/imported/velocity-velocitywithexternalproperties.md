---
title: Velocity with External Properties
nav: Velocity with External Pro...
description: Template template = Velocity.getTemplate("./src/HelloWorld.vm");
section: Imported - java2s Archive
order: 1100
source: https://web.archive.org/web/20061026215440/http://www.java2s.com/Code/Java/Velocity/VelocitywithExternalProperties.htm
---
```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class HelloWorldExternalProperties {
  public static void main(String[] args) throws Exception {
    Velocity.init("./src/velocity.properties");
    Template template = Velocity.getTemplate("./src/HelloWorld.vm");
    VelocityContext context = new VelocityContext();
    Writer writer = new StringWriter();
    template.merge(context, writer);
    System.out.println(writer.toString());
  }
}
-------------------------------------------------------------------------------------
#
## This is a simple example of a velocity properties file.
#
## Any property that is not listed here will have it's default
## value used.  The default values are located in :
##  *  src/java/org/apache/velocity/runtime/default/velocity.defaults
##  *  http://jakarta.apache.org/velocity/developer-guide.html
#
## as an example, we are changing the name of the velocity log
#
runtime.log = velocity_example.log
-------------------------------------------------------------------------------------
Hello World!
```

Download: velocity-HelloWorldExternalProperties.zip ( 795 K )
Related examples in the same category
