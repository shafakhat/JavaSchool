---
title: Ant task delete tree
nav: Ant task delete tree
description: <copyfile src="${config}/remote.properties" dest="${runDir}\remote.properties" />
section: Imported - java2s Archive
order: 1022
source: https://web.archive.org/web/20100203133452/http://www.java2s.com:80/Code/Java/Ant/Anttaskdeletetree.htm
---
Ant task delete tree

```java title=Example.java
<project name="foo" default="deploy" basedir=".">
  <target name="init">
    <tstamp/>
    <property name="src" value="src" />
    <property name="build" value="build" />
    <property name="classes" value="classes" />
    <property name="deploy" value="deploy" />
    <property name="config" value="config" />
    <property name="runDir" value="." />
    <property name="local" value="local" />
    <property name="remote" value="remote" />
    <property name="lib" value="lib" />
  </target>
  <target name="clean" depends="init">
    <deltree dir="${classes}" />
    <deltree dir="${remote}" />
    <deltree dir="${deploy}" />
    <deltree dir="${lib}" />
  </target>
  <target name="prepare" depends="clean">
    <mkdir dir="${classes}" />
    <mkdir dir="${deploy}" />
    <mkdir dir="${lib}" />
  </target>
  <target name="compile" depends="prepare">
    <javac srcdir="${src}" destdir="${classes}" />
    <copyfile src="${lib}/app.jar" dest="${deploy}/app.jar" />
    <copyfile src="${config}/remote.properties" dest="${runDir}\remote.properties" />
    <jar jarfile="${lib}/app.jar" basedir="${classes}" />
  </target>
  <target name="prepareDeploy" depends="compile">
     <copyfile src="${lib}/app.jar" dest="${deploy}/app.jar" />
     <copyfile src="${build}/remotebuild.xml" dest="${deploy}/build.xml" />
     <mkdir dir="${remote}" />
  </target>
  <target name="deploy" depends="prepareDeploy">
     <ant antfile="${build}/deploy.xml" dir="." />
  </target>
</project>
```

1.  Ant copy file
---  ---
2.  Ant copy folder
3.  Ant task copy file
4.  Ant task make dir
5.  Create folder
6.  Delete folder
7.  Delete with file set
8.  File Checksum
9.  File file with fixcrlf
10.  File set includes
11.  copy todir, fileset, include, exclude
