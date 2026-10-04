---
title: Ant task
nav: Ant task
description: <!-- NOTE: THE FOLLOWING LINES SHOULD BE EDITED FOR YOUR PROJECT: -->
section: Imported - java2s Archive
order: 1023
source: https://web.archive.org/web/20061018180504/http://www.java2s.com/Code/Java/Ant/Anttaskjar.htm
---
Ant task: jar

```java title=Example.java
<?xml version="1.0"?>
<project name="sample" default="test" basedir=".">
    <!--  NOTE: THE FOLLOWING LINES SHOULD BE EDITED FOR YOUR PROJECT:  -->
    <property name="root.project.name" value="demo2"/>
    <property name="test.class" value="test.TestSample"/>
   <!-- NOTE: THE REST OF THIS FILE CAN PROBABLY REMAIN UNCHANGED FOR YOUR NEW PROJECTS -->
   <property name="jar.module" value="${root.project.name}.jar"/>
    <path id="test.classpath">
        <pathelement location="dist/${jar.module}"/>
        <pathelement location="dist/test.jar"/>
    </path>
   <target name="compile">
      <mkdir dir="build"/>
      <javac destdir="build"
             debug="on"
             optimize="on">
         <src path="src"/>
      </javac>
   </target>
   <target name="makejar" depends="compile">
      <mkdir dir="dist"/>
      <jar jarfile="dist/${jar.module}">
         <fileset dir="build">
             <include name="**/*.class"/>
       <exclude name="test/*.class"/>
         </fileset>
       </jar>
      <jar jarfile="dist/test.jar">
         <fileset dir="build">
             <include name="test/*.class"/>
         </fileset>
       </jar>
      <delete dir="build"/>
   </target>
   <target name="test" depends="makejar">
      <java fork="no" failonerror="yes"
            classname="${test.class}">
          <classpath refid="test.classpath"/>
          <arg line=""/>
      </java>
   </target>
   <target name="clean">
      <delete dir="build"/>
      <delete dir="dist"/>
   </target>
</project>
```

Download: AntTaskMakeDir.zip ( 1 K )
---
Related examples in the same category
1. Jar with includes and excludes using filesets
2. Jar with includes and excludes
