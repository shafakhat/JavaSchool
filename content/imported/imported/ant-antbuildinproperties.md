---
title: Ant buildin properties
nav: Ant buildin properties
description: <project name="Apache Ant Properties Project" default="properties.built-in" basedir=".">
section: Imported - java2s Archive
order: 1003
source: https://web.archive.org/web/20061026220107/http://www.java2s.com/Code/Java/Ant/Antbuildinproperties.htm
---
```java title=Example.java
<?xml version="1.0"?>
<project name="Apache Ant Properties Project" default="properties.built-in" basedir=".">
  <target name="properties.built-in">
    <echo message="The base directory: ${basedir}"/>
    <echo message="This file: ${ant.file}"/>
    <echo message="Ant version: ${ant.version}"/>
    <echo message="Project name: ${ant.project.name}"/>
    <echo message="Java version: ${ant.java.version}"/>
  </target>
</project>
```

Download: AntBasicTags.zip ( 2 K )
Related examples in the same category
