---
title: How to use an existing Log4j Categeory as the Velocity logging target
nav: How to use an existing Log...
description: How to use an existing Log4j Categeory as the Velocity logging target : Java examples (example source code) » Velocity » Velocity Log
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20060513091832/http://www.java2s.com/Code/Java/Velocity/HowtouseanexistingLog4jCategeoryastheVelocityloggingtarget.htm
---
How to use an existing Log4j Categeory as the Velocity logging target : Java examples (example source code) » Velocity » Velocity Log

How to use an existing Log4j Categeory as the Velocity logging target

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
import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.Category;
import org.apache.velocity.app.VelocityEngine;
import org.apache.velocity.runtime.RuntimeConstants;
/**
 *  Simple example class to show how to use an existing Log4j Categeory
 *  as the Velocity logging target.
 *
 * @author <a href="mailto:geirm@apache.org">Geir Magnusson Jr.</a>
 * @version $Id: Log4jCategoryExample.java,v 1.1.8.1 2004/03/04 00:18:29 geirm Exp $
 */
public class Log4jCategoryExample
{
    public static String CATEGORY_NAME = "velexample";
    public static void main( String args[] )
        throws Exception
    {
        /*
         *  configure log4j to log to console
         */
        BasicConfigurator.configure();
        Category log = Category.getInstance( CATEGORY_NAME );
        log.info("Hello from Log4jCategoryExample - ready to start velocity");
        /*
         *  now create a new VelocityEngine instance, and
         *  configure it to use the category
         */
        VelocityEngine ve = new VelocityEngine();
        ve.setProperty( RuntimeConstants.RUNTIME_LOG_LOGSYSTEM_CLASS,
            "org.apache.velocity.runtime.log.SimpleLog4JLogSystem" );
        ve.setProperty("runtime.log.logsystem.log4j.category", CATEGORY_NAME);
        ve.init();
        log.info("this should follow the initialization output from velocity");
    }
}
```

Download: velocity-Log4J.zip (2193 K)
---
Related examples in the same category
1. This is a toy demonstration of how Velocity can use an externally configured logger
2. Console Log System
3. Custom log for Velocity
