---
title: apache-log4j-site\build.xml
nav: apache-log4j-site\build.xml
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/20100814054245/http://www.java2s.com:80/Code/Java/Ant/apachelog4jsitebuildxml.htm
---
```java title=Example.java
<!--
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->
<project name="logging-site" default="usage" basedir="." >
  <property name="svnrepo.url" value="https://svn.apache.org/repos/asf"/>
  <property name="svnsite.url" value="${svnrepo.url}/logging/site/trunk/docs"/>
  <available property="svn-available" file="target/site-deploy/.svn"/>
  <target name="usage">
    <echo>
    This file provides services to the Maven build and is not
    intended for independent use.
    </echo>
  </target>
  <target name="checkout-site" unless="svn-available">
    <exec executable="svn">
      <arg value="co"/>
      <arg value="${svnsite.url}"/>
      <arg value="target/site-deploy"/>
    </exec>
  </target>
  <target name="update-site" if="svn-available">
    <exec executable="svn" dir="target/site-deploy" failonerror="true">
      <arg value="update"/>
    </exec>
  </target>
  <target name="post-site" depends="checkout-site, update-site"/>
        <target name="mime=html">
            <exec executable="svn">
    <arg value="propset"/>
                <arg value="svn:mime-type"/>
                <arg value="text/html"/>
                <arg value="${src.html}"/>
            </exec>
        </target>
        <target name="mime=css">
            <exec executable="svn">
    <arg value="propset"/>
                <arg value="svn:mime-type"/>
                <arg value="text/css"/>
                <arg value="${src.css}"/>
            </exec>
        </target>
        <target name="mime=jnlp">
            <exec executable="svn">
    <arg value="propset"/>
                <arg value="svn:mime-type"/>
                <arg value="application/x-java-jnlp-file"/>
                <arg value="${src.jnlp}"/>
            </exec>
        </target>
  <target name="site-deploy">
    <!-- Add any new files (and generate innocuous warnings for the existing content)  -->
                <delete file="target/site-deploy/svn-commit.tmp~"/>
    <exec executable="bash" dir="target/site-deploy" failonerror="true">
      <arg line='-c "svn add --force *"'/>
    </exec>
                <taskdef name="foreach" classname="net.sf.antcontrib.logic.ForEach" />
                <foreach target="mime=html" param="src.html">
                        <path>
                                <fileset dir="target/site-deploy" includes="**/*.html">
                  <exclude name="log4j/1.2/**/*.html"/>
                  <exclude name="log4cxx/**/*.html"/>
                  <exclude name="log4net/**/*.html"/>
                  <exclude name="chainsaw/**/*.html"/>
                  <exclude name="log4j/companions/component/**/*.html"/>
                  <exclude name="log4j/companions/extras/**/*.html"/>
                  <exclude name="log4j/companions/receivers/**/*.html"/>
                  <exclude name="log4j/companions/zeroconf/**/*.html"/>
                </fileset>
                        </path>
                </foreach>
                <foreach target="mime=css" param="src.css">
                        <path>
                                <fileset dir="target/site-deploy" includes="**/*.css"/>
                        </path>
                </foreach>
                <foreach target="mime=jnlp" param="src.jnlp">
                        <path>
                                <fileset dir="target/site-deploy" includes="**/*.jnlp"/>
                        </path>
                </foreach>
    <!--  requires that SVN_EDITOR, VISUAL or EDITOR being set to edit commit description -->
    <exec executable="svn" dir="target/site-deploy" failonerror="true">
        <arg value="commit"/>
    </exec>
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
21.  apache-roller-src-4.0.1
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
