---
title: Demonstrates various initializers
nav: Demonstrates various initi...
description: * This software is granted under the terms of the Common Public License,
section: Imported - java2s Archive
order: 1260
source: https://web.archive.org/web/20140829084335/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Demonstratesvariousinitializers.htm
---
```java title=Example.java
/*
 *     file: InitializerDemo.java
 *  package: oreilly.hcj.review
 *
 * This software is granted under the terms of the Common Public License,
 * CPL, which may be found at the following URL:
 * http://www-124.ibm.com/developerworks/oss/CPLv1.0.htm
 *
 * Copyright(c) 2003-2005 by the authors indicated in the @author tags.
 * All Rights are Reserved by the various authors.
 *
########## DO NOT EDIT ABOVE THIS LINE ########## */
import java.util.StringTokenizer;
/**
 *
 * @author <a href=mailto:kraythe@arcor.de>Robert Simmons jr. (kraythe)</a>
 * @version $Revision: 1.4 $
 */
public class InitializerDemo {
  /** Simple static initialization. */
  public static final String NAME = "Initializer Demo";
  /** Initialized static on one line. */
  public static final String ARCH = System.getProperty("os.arch");
  /** Static method based initialization. */
  public static final String USER_HOME;
  static {
    USER_HOME = System.getProperty("user.home");
  }
  /** Simple instance member initialization. */
  public String description = "An initialized member";
  /** Method call instance member initialization. */
  public long timestamp = System.currentTimeMillis();
  /** Complex instance member initialization. */
  private String xmlClasspath;
  {
    final StringBuffer buf = new StringBuffer(500);
    final String classPath = System.getProperty("java.class.path");
    StringTokenizer tok =
      new StringTokenizer(classPath, System.getProperty("path.separator"));
    buf.append("<classpath>\n");
    while (tok.hasMoreTokens()) {
      buf.append("  <pathelement location=\"");
      buf.append(tok.nextToken());
      buf.append("\"/>\n");
    }
    buf.append("</classpath>");
    xmlClasspath = buf.toString();
  }
  /**
   * Creates a new instance of Initalizers
   */
  public InitializerDemo() {
  }
  /**
   * Main method of the demonstration.
   *
   * @param args Command line arguments (ignored).
   */
  public static final void main(final String[] args) {
    InitializerDemo demo = new InitializerDemo();
    System.out.println("------Dumping Contents-----------");
    System.out.println("---------------------------------");
    System.out.println(InitializerDemo.NAME);
    System.out.println(InitializerDemo.ARCH);
    System.out.println(InitializerDemo.USER_HOME);
    System.out.println(demo.description);
    System.out.println(demo.xmlClasspath);
    System.out.println("---------------------------------");
  }
}
/* ########## End of File ########## */
```
