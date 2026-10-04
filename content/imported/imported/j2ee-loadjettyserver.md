---
title: Load Jetty Server
nav: Load Jetty Server
description: /* ------------------------------------------------------------------------
section: Imported - java2s Archive
order: 1034
source: https://web.archive.org/web/20100212020820/http://java2s.com/Code/Java/J2EE/LoadJettyServer.htm
---
```java title=Example.java
/* ------------------------------------------------------------------------
 * $Id: JettyServer.java,v 1.1 2005/12/26 12:59:25 tpv Exp $
 * Copyright 2005 Tim Vernum
 * ------------------------------------------------------------------------
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
 * ------------------------------------------------------------------------
 */
//Revised from adjective wild
import java.io.File;
import org.apache.log4j.ConsoleAppender;
import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.log4j.PatternLayout;
import org.mortbay.http.SocketListener;
import org.mortbay.jetty.Server;
/**
 * @version $Revision: 1.1 $
 */
public class JettyServer
{
    private static final int PORT_NUMBER = 8080;
    public static void main(String[] args)
    {
        new JettyServer().run();
    }
    public void run()
    {
        try
        {
            configureLog4J();
            Server jetty = new Server();
            String appDir = getWebAppDirectory("source/webapp/demo").getAbsolutePath();
            jetty.addWebApplication("/demo", appDir);
            SocketListener httpPort = new SocketListener();
            httpPort.setPort(PORT_NUMBER);
            jetty.addListener(httpPort);
            jetty.start();
        }
        catch (Exception e)
        {
            throw new RuntimeException(e);
        }
    }
    private void configureLog4J()
    {
        ConsoleAppender console = new ConsoleAppender(new PatternLayout(PatternLayout.TTCC_CONVERSION_PATTERN));
        Logger root = Logger.getRootLogger();
        root.setLevel(Level.INFO);
        root.addAppender(console);
    }
    private File getWebAppDirectory(String relativeDir)
    {
        File directory = getDirectory(relativeDir);
        File webxml = new File(directory, "WEB-INF/web.xml");
        if (!webxml.exists())
        {
            throw new RuntimeException("Cannot find web.xml at " + webxml);
        }
        return directory;
    }
    private File getDirectory(String relativeDir)
    {
        File directory = getFile(relativeDir);
        if (!directory.isDirectory())
        {
            throw new RuntimeException("Not a directory: " + directory);
        }
        return directory;
    }
    private File getFile(String relativeName)
    {
        File file = new File(relativeName);
        if (!file.exists())
        {
            throw new RuntimeException("File not found: " + file);
        }
        return file;
    }
}
```

1.  Launch Jetty embedded.
