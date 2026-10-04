---
title: Range set
nav: Range set
description: Download: velocity-Rangein-conjunction-with-set.zip ( 1,876 K )
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20070428130853/http://www.java2s.com:80/Code/Java/Velocity/Rangeset.htm
---
Range set

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.IteratorTool;
public class VMDemo {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/demo.vm");
    VelocityContext ctx = new VelocityContext();
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
#set( $arr = [0..5] )
#foreach( $i in $arr )
   $i
#end
```

Download: velocity-Rangein-conjunction-with-set.zip ( 1,876 K )
Related examples in the same category
