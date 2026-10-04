---
title: Ant task
nav: Ant task
description: <!-- NOTE: THE FOLLOWING LINES SHOULD BE EDITED FOR YOUR PROJECT: -->
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20071012154145/http://java2s.com:80/Code/Java/Ant/Anttaskmakedir.htm
---
Ant task: make dir

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

AntTaskMakeDir.zip( 1 k)
1.  Specify basedir
2.  File separator
3.  Path separator
4.  Build path unix
5.  Get current location
6.  Path convert
7.  Ant path
8.  Define path with file set
