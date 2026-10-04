---
title: Ant call another ant script
nav: Ant call another ant script
description: <copyfile src="${config}/remote.properties" dest="${runDir}\remote.properties" />
section: Imported - java2s Archive
order: 1005
source: https://web.archive.org/web/20100212032454/http://java2s.com/Code/Java/Ant/Antcallanotherantscript.htm
---
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

1.  Use main ant build file call sub build file
---  ---
2.  Ant script calls another ant script
3.  One ant script calls another antscript and dir setting
