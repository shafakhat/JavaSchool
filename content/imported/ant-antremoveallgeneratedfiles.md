---
title: Ant
nav: Ant
description: <project name="Template Buildfile" default="compile" basedir=".">
section: Imported - java2s Archive
order: 1014
source: https://web.archive.org/web/20070523093810/http://www.java2s.com:80/Code/Java/Ant/AntRemoveallgeneratedfiles.htm
---
Ant: Remove all generated files

```java title=Example.java
<?xml version="1.0"?>
<project name="Template Buildfile" default="compile" basedir=".">
  <property name="dir.src" value="src"/>
  <property name="dir.build" value="build"/>
  <property name="dir.dist" value="dist"/>
  <!-- Creates the output directories -->
  <target name="prepare">
    <mkdir dir="${dir.build}"/>
    <mkdir dir="${dir.dist}"/>
  </target>
  <target name="clean"
          description="Remove all generated files.">
    <delete dir="${dir.build}"/>
    <delete dir="${dir.dist}"/>
  </target>
  <target name="compile" depends="prepare"
          description="Compile all source code.">
    <javac srcdir="${dir.src}" destdir="${dir.build}"/>
  </target>
  <target name="jar" depends="compile"
          description="Generates java2s.jar in the 'dist' directory.">
    <jar jarfile="${dir.dist}/java2s.jar"
         basedir="${dir.build}"/>
  </target>
</project>
```

Download: AntBasic.zip ( 3 K )
Related examples in the same category
