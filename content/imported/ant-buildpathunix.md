---
title: Build path unix
nav: Build path unix
description: <project name="Apache Ant Properties Project" default="build.path.unix" basedir=".">
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20071012045432/http://java2s.com:80/Code/Java/Ant/Buildpathunix.htm
---
```java title=Example.java
<?xml version="1.0"?>
<project name="Apache Ant Properties Project" default="build.path.unix" basedir=".">
  <target name="build.path.unix">
    <echo message="File: ${basedir}/build.xml"/>
    <echo message="Path: ${basedir}/build.xml;${basedir}/build.properties"/>
  </target>
</project>
```

AntBasicTags.zip( 2 k)
1.  Specify basedir
2.  File separator
3.  Path separator
4.  Get current location
5.  Path convert
6.  Ant path
7.  Define path with file set
8.  Ant task: make dir
