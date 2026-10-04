---
title: Check Properties
nav: Check Properties
description: <project name="Template Buildfile" default="compile" basedir=".">
section: Imported - java2s Archive
order: 1046
source: https://web.archive.org/web/20061016080750/http://www.java2s.com/Code/Java/Ant/CheckProperties.htm
---
Check Properties

```java title=Example.java
<?xml version="1.0"?>
<project name="Template Buildfile" default="compile" basedir=".">
  <property name="dir.src" value="src"/>
  <property name="dir.build" value="build"/>
  <property environment="env"/>
  <target name="checkProperties">
    <fail unless="env.TOMCAT_HOME">TOMCAT_HOME must be set</fail>
    <fail unless="env.JUNIT_HOME">JUNIT_HOME must be set</fail>
    <fail unless="env.JBOSS_HOME">JBOSS_HOME must be set</fail>
  </target>
  <!-- Creates the output directories -->
  <target name="prepare" depends="checkProperties">
    <mkdir dir="${dir.build}"/>
  </target>
  <target name="clean"
          description="Remove all generated files.">
    <delete dir="${dir.build}"/>
  </target>
  <target name="compile" depends="prepare"
          description="Compile all source code.">
    <echo>Compile code...</echo>
  </target>
</project>
```

Related examples in the same category
