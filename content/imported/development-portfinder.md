---
title: Port Finder
nav: Port Finder
description: Imported from the java2s.com archive: Port Finder
section: Imported - java2s Archive
order: 1982
source: https://web.archive.org/web/20140217003509/http://www.java2s.com/Tutorial/Java/0120__Development/PortFinder.htm
---
```java title=Example.java
import java.io.*;
import javax.comm.*;
import java.util.*;
public class Main
{
    public static void main(String[] args)
    {
        Enumeration ports = CommPortIdentifier.getPortIdentifiers();
        while(ports.hasMoreElements())
        {
            CommPortIdentifier cpi =
                           (CommPortIdentifier)ports.nextElement();
            System.out.println("Port " + cpi.getName());
        }
    }
}
```

| 6.53.1. | Port Finder |
|---|---|
| 6.53.2. | Port Reader |
| 6.53.3. | Port Sniffer |
| 6.53.4. | Port Writer |
