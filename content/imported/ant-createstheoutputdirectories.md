---
title: Creates the output directories
nav: Creates the output directo...
description: <project name="Template Buildfile" default="compile" basedir=".">
section: Imported - java2s Archive
order: 1053
source: https://web.archive.org/web/20061016080740/http://www.java2s.com/Code/Java/Ant/Createstheoutputdirectories.htm
---
Creates the output directories

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
---
Related examples in the same category
2. Check Properties
