---
title: apache-roller-src-4.0.1
nav: apache-roller-src-4.0.1
description: <project name="toplevel" default="build" basedir="." xmlns:artifact="urn:maven-artifact-ant">
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20100814052009/http://www.java2s.com:80/Code/Java/Ant/apacherollersrc401.htm
---
```java title=Example.java
<?xml version="1.0" encoding="UTF-8"?>
<project name="toplevel" default="build" basedir="." xmlns:artifact="urn:maven-artifact-ant">
    <!--
    Build/test script intended to be run by build/test server.
    For ordinary development use the separate build scripts.
    -->
    <target name="clean">
        <ant dir="components/core" target="clean" />
        <ant dir="apps/planet"     target="clean" />
        <ant dir="apps/weblogger"  target="clean" />
    </target>
    <target name="build-integrated"
        description="Build Core, Planet and Roller together (i.e. Rebuilds Core and Planet jars, uses them to build Roller)">
        <ant  dir="components/core" target="dist" />
        <copy file="components/core/dist/lib/roller-core.jar" todir="tools/roller-core" />
        <ant  dir="apps/planet" target="dist" />
        <copy file="apps/planet/dist/lib/roller-planet-business.jar" todir="tools/roller-planet" />
        <ant dir="apps/weblogger"  target="dist" />
        <ant dir="apps/weblogger"  target="apache-release" />
    </target>
    <target name="build"
        description="Build Core, Planet and Roller separately (i.e. uses Core and Planet jars from Subversion)" >
        <ant dir="components/core" target="dist" />
        <ant dir="apps/planet"     target="dist" />
        <ant dir="apps/weblogger"  target="dist" />
        <ant dir="apps/weblogger"  target="apache-release" />
    </target>
    <target name="test">
        <ant dir="apps/planet" target="test" />
        <ant dir="apps/weblogger" target="tests" />
    </target>
    <!-- get the ant maven tasks.  I wish I could understand ant logic so we could run this whenever the jar is missing -->
    <target name="mvn-get">
        <mkdir dir="tools/buildtime/maven"/>
        <get src="http://repo1.maven.org/maven2/org/apache/maven/maven-ant-tasks/2.0.7/maven-ant-tasks-2.0.7.jar" dest="tools/buildtime/maven/maven-ant-tasks-2.0.7.jar"/>
    </target>
    <target name="mvn-init">
        <echo>If this fails with a message like '  [typedef] Could not load definitions from resource org/apache/maven/artifact/ant/antlib.xml. It could not be found.' try running mvn-get first.</echo>
        <xmlproperty file="pom.xml" prefix="pom.xml"/>
        <path id="maven-ant-tasks.classpath" path="tools/buildtime/maven/maven-ant-tasks-2.0.7.jar"/>
        <typedef resource="org/apache/maven/artifact/ant/antlib.xml" uri="urn:maven-artifact-ant"
                 classpathref="maven-ant-tasks.classpath"/>
    </target>
    <!--This target will place the roller-weblogger.war file in a maven repository alongside with its
              corresponding pom.xml file. Before deploying be sure to check the version tag in the
              pom_ant_weblogger.xml file.
              For real usage change the repository url to http://www.ibiblio.org/maven2 or some other
              public repository of your choice. To test deployment localy use somting like file://localhost/xxx -->
    <target name="mvn-deploy" depends="build, mvn-init">
        <artifact:install-provider artifactId="wagon-ssh" version="1.0-alpha-5"/>
        <artifact:pom id="maven.project.weblogger.business.jar" file="apps/weblogger/pom_ant_weblogger_business.xml"/>
        <artifact:deploy file="apps/weblogger/dist/lib/roller-business.jar">
            <remoteRepository url="scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository"/>
            <pom refid="maven.project.weblogger.business.jar"/>
        </artifact:deploy>
        <artifact:pom id="maven.project.weblogger.web.jar" file="apps/weblogger/pom_ant_weblogger_web.xml"/>
        <artifact:deploy file="apps/weblogger/dist/lib/roller-web.jar">
            <remoteRepository url="scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository"/>
            <pom refid="maven.project.weblogger.web.jar"/>
        </artifact:deploy>
        <artifact:pom id="maven.project.weblogger.war" file="apps/weblogger/pom_ant_weblogger.xml"/>
        <artifact:deploy file="apps/weblogger/dist/webapp/roller-weblogger.war">
            <remoteRepository url="scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository"/>
            <pom refid="maven.project.weblogger.war"/>
        </artifact:deploy>
        <artifact:pom id="maven.project.planet.business.jar" file="apps/planet/pom_ant_planet_business.xml"/>
        <artifact:deploy file="apps/planet/dist/lib/roller-planet-business.jar">
            <remoteRepository url="scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository"/>
            <pom refid="maven.project.planet.business.jar"/>
        </artifact:deploy>
        <artifact:pom id="maven.project.planet.web.jar" file="apps/planet/pom_ant_planet_web.xml"/>
        <artifact:deploy file="apps/planet/dist/webapp/roller-planet-web.jar">
            <remoteRepository url="scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository"/>
            <pom refid="maven.project.planet.web.jar"/>
        </artifact:deploy>
        <artifact:pom id="maven.project.planet.war" file="apps/planet/pom_ant_planet.xml"/>
        <artifact:deploy file="apps/planet/dist/webapp/roller-planet.war">
            <remoteRepository url="scp://people.apache.org/www/people.apache.org/repo/m2-ibiblio-rsync-repository"/>
            <pom refid="maven.project.planet.war"/>
        </artifact:deploy>
    </target>
    <!-- Install roller-weblogger.war in the local maven repository -->
    <target name="mvn-install" depends="build, mvn-init">
        <artifact:pom id="maven.project.weblogger.business.jar" file="apps/weblogger/pom_ant_weblogger_business.xml"/>
        <artifact:install file="apps/weblogger/dist/lib/roller-business.jar">
            <pom refid="maven.project.weblogger.business.jar"/>
        </artifact:install>
        <artifact:pom id="maven.project.weblogger.web.jar" file="apps/weblogger/pom_ant_weblogger_web.xml"/>
        <artifact:install file="apps/weblogger/dist/lib/roller-web.jar">
            <pom refid="maven.project.weblogger.web.jar"/>
        </artifact:install>
        <artifact:pom id="maven.project.weblogger.war" file="apps/weblogger/pom_ant_weblogger.xml"/>
        <artifact:install file="apps/weblogger/dist/webapp/roller-weblogger.war">
            <pom refid="maven.project.weblogger.war"/>
        </artifact:install>
        <artifact:pom id="maven.project.planet.business.jar" file="apps/planet/pom_ant_planet_business.xml"/>
        <artifact:install file="apps/planet/dist/lib/roller-planet-business.jar">
            <pom refid="maven.project.planet.business.jar"/>
        </artifact:install>
        <artifact:pom id="maven.project.planet.web.jar" file="apps/planet/pom_ant_planet_web.xml"/>
        <artifact:install file="apps/planet/dist/lib/roller-planet-web.jar">
            <pom refid="maven.project.planet.web.jar"/>
        </artifact:install>
        <artifact:pom id="maven.project.planet.war" file="apps/planet/pom_ant_planet.xml"/>
        <artifact:install file="apps/planet/dist/webapp/roller-planet.war">
            <pom refid="maven.project.planet.war"/>
        </artifact:install>
    </target>
</project>
```

1.  Ant script for xmlgraphics-commons
---  ---
2.  nutch ant script
3.  rhino ant build script
4.  apache solr ant script
5.  Tomcat ant build script
6.  OFBiz ant build script
7.  Apache Lenya Build System
8.  Apache pivot ant build script
9.  XmlSchema ant script
10.  xml security
11.  velocity tools ant script
12.  weka build script
13.  xml bean ant script
14.  xml graphics common ant script
15.  uPortal ant script
16.  SmartGWT ant script
17.  Build file to fetch maven2 tasks; extracted from (Ant's) fetch.xml
18.  Build file to fetch optional libraries for Apache Ant
19.  Ant build script
20.  Build script for apache-cassandra-0.5.1-src
21.  apache-log4j-site\build.xml
22.  Build script from apache dbutils
23.  Fop build script
24.  Google guice ant script
25.  GWT ant script
26.  hadoop ant build script
27.  jakarta jmeter ant script
28.  jakarta oro ant script
29.  jakarta regexp ant script
30.  jedit build script
31.  jibx ant build script
32.  lucene ant build script
