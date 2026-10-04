---
title: Apache Lenya Build System
nav: Apache Lenya Build System
description: Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1027
source: https://web.archive.org/web/20101207185055/http://www.java2s.com:80/Code/Java/Ant/ApacheLenyaBuildSystem.htm
---
Apache Lenya Build System

```java title=Example.java
<?xml version="1.0"?>
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
<!-- $Id: build.xml 473861 2006-11-12 03:51:14Z gregor $ -->
<!DOCTYPE project [
<!-- ---------------------------------------------------------------------------
                       * --------------------------- *
Apache Lenya Build System
                       * --------------------------- *
       CVS $Id: build.xml 473861 2006-11-12 03:51:14Z gregor $:
---------------------------------------------------------------------------- -->
]>
<project default="webapp" basedir="." name="lenya">
  <!-- ----------------==  Apache Lenya targets  ------------------------ -->
  <!-- ------------------------------------------------------------------- -->
  <!-- Global properties  -->
  <import file="src/targets/properties-build.xml" />
  <!-- Initialization targets  -->
  <import file="src/targets/init-build.xml" />
  <!-- IDE targets             -->
  <import file="src/targets/ide-build.xml" />
  <!-- Compile targets         -->
  <import file="src/targets/compile-build.xml" />
  <!-- Documentation targets   -->
  <import file="src/targets/docs-build.xml" />
  <!-- Web application targets -->
  <import file="src/targets/webapp-build.xml" />
  <!-- Testcases targets       -->
  <import file="src/targets/test-build.xml" />
  <!-- Distribution targets    -->
  <import file="src/targets/dist-build.xml" />
  <!-- Kupu targets            -->
  <import file="src/targets/kupu-build.xml" />
  <!-- Export targets          -->
  <import file="src/targets/export-build.xml" />
  <!-- module targets          -->
  <import file="src/targets/modules-build.xml" />
  <!-- migration targets          -->
  <import file="src/targets/migration-build.xml" />
  <!-- Publication tests       -->
  <import file="src/targets/publication-test-build.xml" />
  <!-- Successfully Built Message       -->
  <import file="src/targets/message-build.xml" />
  <!-- ------------------------------------------------------------------- -->
</project>
File: build.properties
## Licensed to the Apache Software Foundation (ASF) under one or more
## contributor license agreements.  See the NOTICE file distributed with
## this work for additional information regarding copyright ownership.
## The ASF licenses this file to You under the Apache License, Version 2.0
## (the "License"); you may not use this file except in compliance with
## the License.  You may obtain a copy of the License at
#
##     http://www.apache.org/licenses/LICENSE-2.0
#
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
#------------------------------------------------------------------------------------
## Properties controlling the build process
## NOTE:
## Don't modify this file directly but create a file named
## 'local.build.properties' and implement ONLY
## the properties you need.
## You do NOT have to copy the whole 'build.properties' file.
## The build system will first read all properties defined
## in the 'local.build.properties' file and then will read out the
## ones in 'build.properties'. Ant will use the first found.
## You can as well execute ./configure.sh (Linux) or configure (Windows)
## to generate the 'local.build.properties'.
#------------------------------------------------------------------------------------
## Build properties version to make sure that local.build.properties is kept in sync
## NOTE: Do NOT modify this number unless you are a Dev and want to modify this file
## NOTE for Devs: Update this number if this file is being updated.
##                Also update the version number within src/targets/properties-build.xml
build.properties.version=594644
#------------------------------------------------------------------------------------
## The root of the Cocoon source tree
cocoon.src.dir=externals/cocoon_2_1_x
#cocoon.src.dir=../../cocoon/branches/BRANCH_2_1_X
#------------------------------------------------------------------------------------
## The cocoon webapp directory
## You do not have to change this since Lenya will build Cocoon for you
cocoon.webapp.dir=${cocoon.src.dir}/build/webapp
#------------------------------------------------------------------------------------
## Root directories where publications are located
pubs.root.dirs=src/pubs
#pubs.root.dirs=src/pubs:../anotherproject/pubs:/home/user/my-pub
#------------------------------------------------------------------------------------
## Root directories where modules are located
modules.root.dirs=src/modules:src/modules-core:src/pubs/default/modules
#modules.root.dirs=src/modules:src/pubs/default/modules:src/modules-optional
## copy modules to the web application?
modules.copy=true
#------------------------------------------------------------------------------------
## Web Application Server
## NOTE: There are slight differences re deployment on the various servlet containers, e.g. endorsed libraries ...
web.app.server=Jetty
## NOTE: This only works for lenya.sh (Linux). TODO: Make it also work for lenya.bat (Windows)
web.app.server.jetty.port=8888
web.app.server.jetty.admin.port=8889
#web.app.server=Tomcat
#web.app.server=WLS
#------------------------------------------------------------------------------------
## Where the 'install' build target should put the webapp context
## WARNING: This has to be an absolute path! (FIXME: cocoon.xconf needs absolute path (scr/targets/init-build.xml))
## NOTE: Do not use white spaces within the path
tomcat.home.dir=/usr/local/tomcat
#tomcat.home.dir=C:/build/tomcat
#------------------------------------------------------------------------------------
## Where the 'install' build target should put the webapp context
## NOTE: This path is not necessarily relative to tomcat.home.dir
tomcat.webapps.dir=${tomcat.home.dir}/webapps/lenya
#------------------------------------------------------------------------------------
## The server cache directory to be cleaned by the 'reset' target
## NOTE: This path is not necessarily relative to tomcat.home.dir
## Tomcat 5.x
tomcat.cache.dir=${tomcat.home.dir}/work/Catalina/localhost/lenya
## Tomcat 4.x
#tomcat.cache.dir=${tomcat.home.dir}/work/Standalone/localhost/lenya
#------------------------------------------------------------------------------------
## Where the 'install' build target should copy the endorsed libraries
## NOTE: This path is not necessarily relative to tomcat.home.dir
tomcat.endorsed.dir=${tomcat.home.dir}/common/endorsed
#------------------------------------------------------------------------------------
## Files and directories which should be excluded during 'install', 'clean' and 'reset'
## Comma- or space-separated list of patterns
## All files are included when commented
## This is useful for preserving content while you are developing a publication
#target.install.excludes=**/pubs/default/content/**,**/pubs/default/resources/authoring/**,**/pubs/default/resources/live/**,**/pubs/default/config/ac/passwd/*.iml
#target.reset.excludes=${target.install.excludes}
#------------------------------------------------------------------------------------
## TODO: This seems to have moved to src/confpatch/enable-uploads.xweb whereas it
##       does NOT seem to work properly!
## Enable file uploads in Lenya
## If you leave this set to false, asset and image upload will not work.
## It is disabled by default for security reasons
## NOTE: One can change this after the build within build/lenya/webapp/WEB-INF/web.xml
##       where also the max upload size can be configured (upload-max-size parameter)
enable.uploads=false
#------------------------------------------------------------------------------------
## Anteater home directory
#anteater.home=/usr/local/anteater
#------------------------------------------------------------------------------------
## Canoo Webtest configuration
## Webtest home directory
#webtest.home=/usr/local/canoo-webtest-2.1
## Webtest configuration parameters
webtest.config.host=localhost
webtest.config.port=8888
webtest.config.basepath=default/authoring
#------------------------------------------------------------------------------------
## Eclipse Properties for use with the eclipse-project target
ide.eclipse.outputdir=build/eclipse/classes
ide.eclipse.export.libs=false
#------------------------------------------------------------------------------------
## The Java version.
src.java.version=1.4
#------------------------------------------------------------------------------------
## Xopus context name
xopus.context=Xopus2.1.64
xopus.path=../../ROOT
#------------------------------------------------------------------------------------
## JCR repository factory
repository.factory=org.apache.lenya.cms.jcr.jackrabbit.JackrabbitRepositoryFactory
## NOTE: JeceiraRepositoryFactory has not been implemented yet
#repository.factory=org.apache.lenya.cms.jcr.jeceira.JeceiraRepositoryFactory
#------------------------------------------------------------------------------------
## NOTE: The node factory needs to be configured within "build/lenya/webapp/WEB-INF/classes/org/apache/lenya/lenya.roles" after having build Lenya
#node.factory=org.apache.lenya.cms.repository.SourceNodeFactory
#node.factory=org.apache.lenya.cms.repo.adapter.RepoNodeFactory
#node.factory=org.apache.lenya.cms.jcr.JCRNodeFactory
#------------------------------------------------------------------------------------
## SVN Revision number
lenya.revision=xxx
```

1.  Ant script for xmlgraphics-commons
---  ---
2.  nutch ant script
3.  rhino ant build script
4.  apache solr ant script
5.  Tomcat ant build script
6.  OFBiz ant build script
7.  Apache pivot ant build script
8.  XmlSchema ant script
9.  xml security
10.  velocity tools ant script
11.  weka build script
12.  xml bean ant script
13.  xml graphics common ant script
14.  uPortal ant script
15.  SmartGWT ant script
16.  Build file to fetch maven2 tasks; extracted from (Ant's) fetch.xml
17.  Build file to fetch optional libraries for Apache Ant
18.  Ant build script
19.  Build script for apache-cassandra-0.5.1-src
20.  apache-log4j-site\build.xml
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
