---
title: Custom log for Velocity
nav: Custom log for Velocity
description: Custom log for Velocity : Java examples (example source code) » Velocity » Velocity Log
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/20060513091841/http://www.java2s.com/Code/Java/Velocity/CustomlogforVelocity.htm
---
Custom log for Velocity : Java examples (example source code) » Velocity » Velocity Log

```java title=Example.java
/*
 * Copyright 2000-2001,2004 The Apache Software Foundation.
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
import org.apache.velocity.app.Velocity;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.Template;
import org.apache.velocity.exception.ParseErrorException;
import org.apache.velocity.exception.ResourceNotFoundException;
import java.io.*;
import java.util.ArrayList;
/**
 * This class is a simple demonstration of how the Velocity Template Engine
 * can be used in a standalone application.
 *
 * @author <a href="mailto:jvanzyl@apache.org">Jason van Zyl</a>
 * @author <a href="mailto:geirm@optonline.net">Geir Magnusson Jr.</a>
 * @version $Id: Example.java,v 1.4.8.1 2004/03/04 00:18:29 geirm Exp $
 */
public class Example
{
    public Example(String templateFile)
    {
        try
        {
            /*
             * setup
             */
            Velocity.init("./src/velocity.properties");
            /*
             *  Make a context object and populate with the data.  This
             *  is where the Velocity engine gets the data to resolve the
             *  references (ex. $list) in the template
             */
            VelocityContext context = new VelocityContext();
            context.put("list", getNames());
            /*
             *  get the Template object.  This is the parsed version of your
             *  template input file.  Note that getTemplate() can throw
             *   ResourceNotFoundException : if it doesn't find the template
             *   ParseErrorException : if there is something wrong with the VTL
             *   Exception : if something else goes wrong (this is generally
             *        indicative of as serious problem...)
             */
            Template template =  null;
            try
            {
                template = Velocity.getTemplate(templateFile);
            }
            catch( ResourceNotFoundException rnfe )
            {
                System.out.println("Example : error : cannot find template " + templateFile );
            }
            catch( ParseErrorException pee )
            {
                System.out.println("Example : Syntax error in template " + templateFile + ":" + pee );
            }
            /*
             *  Now have the template engine process your template using the
             *  data placed into the context.  Think of it as a  'merge'
             *  of the template and the data to produce the output stream.
             */
            BufferedWriter writer = writer = new BufferedWriter(
                new OutputStreamWriter(System.out));
            if ( template != null)
                template.merge(context, writer);
            /*
             *  flush and cleanup
             */
            writer.flush();
            writer.close();
        }
        catch( Exception e )
        {
            System.out.println(e);
        }
    }
    public ArrayList getNames()
    {
        ArrayList list = new ArrayList();
        list.add("ArrayList element 1");
        list.add("ArrayList element 2");
        list.add("ArrayList element 3");
        list.add("ArrayList element 4");
        return list;
    }
    public static void main(String[] args)
    {
        Example t = new Example("./src/example.vm");
    }
}
-------------------------------------------------------------------------------------
## This is an example velocity template
#set( $this = "Velocity")
$this is great!
#foreach( $name in $list )
    $name is great!
#end
#set( $condition = true)
#if ($condition)
    The condition is true!
#else
    The condition is false!
#end
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
```

Download: velocity-Log.zip (1875 K)
---
Related examples in the same category
1. This is a toy demonstration of how Velocity can use an externally configured logger
2. Console Log System
3. How to use an existing Log4j Categeory as the Velocity logging target
