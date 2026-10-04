---
title: Show basic XML handling in a template
nav: Show basic XML handling in...
description: Show basic XML handling in a template : Java examples (example source code) » Velocity » XML
section: Imported - java2s Archive
order: 1057
source: https://web.archive.org/web/20060424151504/http://www.java2s.com:80/Code/Java/Velocity/ShowbasicXMLhandlinginatemplate.htm
---
Show basic XML handling in a template : Java examples (example source code) » Velocity » XML

```java title=Example.java
/*
 * Copyright 2000,2004 The Apache Software Foundation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.Writer;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.Template;
import org.apache.velocity.app.Velocity;
import org.jdom.Document;
import org.jdom.input.SAXBuilder;
/**
 * Example to show basic XML handling in a template.
 *
 * @author <a href="mailto:geirm@optonline.net">Geir Magnusson Jr.</a>
 * @version $Id: XMLTest.java,v 1.2.12.1 2004/03/04 00:18:30 geirm Exp $
 */
public class XMLTest
{
    public XMLTest( String templateFile)
    {
        Writer writer = null;
        try
        {
            /*
             *  and now call init
             */
            Velocity.init();
            /*
             * build a Document from our xml
             */
            SAXBuilder builder;
            Document root = null;
            try
            {
                builder = new SAXBuilder(  "org.apache.xerces.parsers.SAXParser" );
                root = builder.build("./src/test.xml");
            }
            catch( Exception ee)
            {
                System.out.println("Exception building Document : " + ee);
                return;
            }
            /*
             * now, make a Context object and populate it.
             */
            VelocityContext context = new VelocityContext();
            context.put("root", root);
            /*
             *  make a writer, and merge the template 'against' the context
             */
            Template template = Velocity.getTemplate(templateFile);
            writer = new BufferedWriter(new OutputStreamWriter(System.out));
            template.merge( context , writer);
        }
        catch( Exception e )
        {
           System.out.println("Exception : " + e);
        }
        finally
        {
            if ( writer != null)
            {
                try
                {
                    writer.flush();
                    writer.close();
                }
                catch( Exception ee )
                {
                    System.out.println("Exception : " + ee );
                }
            }
        }
    }
    public static void main(String[] args)
    {
        XMLTest t;
        t = new XMLTest("./src/xml.vm");
    }
}
-------------------------------------------------------------------------------------
//File: test.xml
<?xml version="1.0" encoding="UTF-8"?>
<document>
  <properties>
    <author>
  <email>velocity-user@jakarta.apache.org</email>
  <name>
     <last>
    <full>Team</full>
    <firstinitial>T</firstinitial>
     </last>
     <first>
    Velocity
     </first>
  </name>
    </author>
    <title>
        The Jakarta Project
    </title>
  </properties>
  <body>
  I am the body
  </body>
</document>
-------------------------------------------------------------------------------------
//File: xml.vm
#macro ( recursive $e $indent )
    #if( $e.getChildren().size() > 0 )
        $indent <$e.getName()>
        #foreach ($child in $e.getChildren() )
            #recursive( $child "$indent  " )
        #end
        $indent </$e.getName()>
    #else
        $indent <$e.getName()>
        $indent    $e.getTextTrim()
        $indent </$e.getName()>
    #end
#end
#set($i = " ")
First, we print out the document tree with a
recursive Velocimacro :
#recursive( $root.getRootElement() $i )
Next, we access pieces of data directly :
email : $root.getRootElement().getChild("properties").getChild("author").getChild("email").getText()
last name :  $root.getRootElement().getChild("properties").getChild("author").getChild("name").getChild("last").getChild("full").getText()
```

Download: velocity-XML-handling-in-a-template.zip (2195 K)
---
Related examples in the same category
1. Velocity Output XML
