---
title: Resource Loader Demo
nav: Resource Loader Demo
description: Resource Loader Demo : Java examples (example source code) » Velocity » Resource Loader
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/20060513085544/http://www.java2s.com/Code/Java/Velocity/ResourceLoaderDemo.htm
---
Resource Loader Demo : Java examples (example source code) » Velocity » Resource Loader

Resource Loader Demo

```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
public class ResourceLoaders {
  private static final String FILE_RESOURCE_LOADER_TEMPLATE = "./src/ResourceLoader1.vm";
  private static final String JAR_RESOURCE_LOADER_TEMPLATE = "./src/ResourceLoader2.vm";
  private static final String CLASSPATH_RESOURCE_LOADER_TEMPLATE = "./src/ResourceLoader3.vm";
  public static void main(String[] args) throws Exception {
    processTemplate(FILE_RESOURCE_LOADER_TEMPLATE);
    processTemplate(FILE_RESOURCE_LOADER_TEMPLATE);
    processTemplate(JAR_RESOURCE_LOADER_TEMPLATE);
    processTemplate(JAR_RESOURCE_LOADER_TEMPLATE);
    processTemplate(CLASSPATH_RESOURCE_LOADER_TEMPLATE);
    processTemplate(CLASSPATH_RESOURCE_LOADER_TEMPLATE);
  }
  private static void processTemplate(String templateName) throws Exception {
    Velocity.init();
    Template template = Velocity.getTemplate(templateName);
    VelocityContext context = new VelocityContext();
    Writer writer = new StringWriter();
    template.merge(context, writer);
    System.out.println(writer.toString());
  }
}
-------------------------------------------------------------------------------------
//File: ResourceLoader1.vm
ResourceLoader1 Template!
//File: ResourceLoader2.vm
ResourceLoader2 Template Modified!
//File: ResourceLoader3.vm
ResourceLoader3 Template 3
```

Download: velocity-ResourceLoaders.zip (797 K)
---
Related examples in the same category
1. Caching Class path Resource Loader
