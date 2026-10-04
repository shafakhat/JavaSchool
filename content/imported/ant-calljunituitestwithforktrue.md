---
title: Call junit ui test with fork=true
nav: Call junit ui test with fo...
description: <target name="junitgui" depends="build" description="run junitgui">
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/20100131220649/http://java2s.com/Code/Java/Ant/Calljunituitestwithforktrue.htm
---
```java title=Example.java
<?xml version="1.0"?>
<project name="yourName" default="junitgui" basedir=".">
  <property name="junitJar" value="\junit3.8.1\junit.jar" />
  <property name="src.dir" value="${basedir}\src" />
  <property name="build.dir" value="${basedir}\classes" />
  <path id="classpath">
    <pathelement location="${junitJar}" />
    <pathelement location="${build.dir}" />
  </path>
  <target name="init">
    <mkdir dir="${build.dir}" />
  </target>
  <target name="build" depends="init" description="build all">
    <javac
        srcdir="${src.dir}" destdir="${build.dir}"
        source="1.5"
        deprecation="on" debug="on" optimize="off" includes="**">
      <classpath refid="classpath" />
    </javac>
  </target>
  <target name="junitgui" depends="build" description="run junitgui">
    <java classname="junit.awtui.TestRunner" fork="yes">
      <arg value="sis.AllTests" />
      <classpath refid="classpath" />
    </java>
  </target>
   <target name="clean">
    <delete dir="${build.dir}" />
  </target>
   <target name="rebuildAll" depends="clean,build" description="rebuild all"/>
</project>
```

1.  Junit test
---  ---
2.  Junit report
3.  Prepare the test directories
4.  Use junit with call junit test cases
