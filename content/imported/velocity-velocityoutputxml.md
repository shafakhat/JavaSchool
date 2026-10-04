---
title: Velocity Output XML
nav: Velocity Output XML
description: Imported from the java2s.com archive: Velocity Output XML
section: Imported - java2s Archive
order: 1093
source: https://web.archive.org/web/20060503013139/http://www.java2s.com:80/Code/Java/Velocity/VelocityOutputXML.htm
---
Velocity Output XML

```java title=Example.java
import java.io.StringWriter;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.VelocityEngine;
public class EmailDemo
{
    public static void main( String[] args )
        throws Exception
    {
        /*
         *   first, get and initialize an engine
         */
        VelocityEngine ve = new VelocityEngine();
        ve.init();
        /*
         *   organize our data
         */
        ArrayList list = new ArrayList();
        Map map = new HashMap();
        map.put("name", "Cow");
        map.put("price", "$100.00");
        list.add( map );
        map = new HashMap();
        map.put("name", "Eagle");
        map.put("price", "$59.99");
        list.add( map );
        map = new HashMap();
        map.put("name", "Shark");
        map.put("price", "$3.99");
        list.add( map );
        /*
         *  add that list to a VelocityContext
         */
        VelocityContext context = new VelocityContext();
        context.put("petList", list);
        /*
         *   get the Template
         */
        Template t = ve.getTemplate( "./src/email_xml.vm" );
        /*
         *  now render the template into a Writer, here
         *  a StringWriter
         */
        StringWriter writer = new StringWriter();
        t.merge( context, writer );
        /*
         *  use the output in the body of your emails
         */
        System.out.println( writer.toString() );
    }
}
-------------------------------------------------------------------------------------
<?xml version="1.0"?>
<salelist>
#foreach( $pet in $petList )
  <pet>
    <name>$pet.name</name>
    <price>$pet.price</price>
  </pet>
#end
</salelist>
```

Download: velocity-OutputXML.zip (2190 K)
---
Related examples in the same category
1. Show basic XML handling in a template
