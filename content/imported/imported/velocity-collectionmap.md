---
title: Collection
nav: Collection
description: Imported from the java2s.com archive: Collection
section: Imported - java2s Archive
order: 1020
source: https://web.archive.org/web/20070328224159/http://www.java2s.com:80/Code/Java/Velocity/CollectionMap.htm
---
Collection: Map

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class MapDemo {
  public static void main(String[] args) throws Exception {
    Velocity.init();
    Template t = Velocity.getTemplate("./src/mapProperty.vm");
    VelocityContext ctx = new VelocityContext();
    Map map = new HashMap();
    map.put("firstName", "Joe");
    map.put("lastName", "Yin");
    ctx.put("map", map);
    Writer writer = new StringWriter();
    t.merge(ctx, writer);
    System.out.println(writer);
  }
}
-------------------------------------------------------------------------------------
My first name is $map.firstName
My last name is $map.lastName
```

Download: velocity-Map.zip ( 875 K )
Related examples in the same category
