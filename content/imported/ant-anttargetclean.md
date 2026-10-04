---
title: Ant target
nav: Ant target
description: Imported from the java2s.com archive: Ant target
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20070523084611/http://www.java2s.com:80/Code/Java/Ant/Anttargetclean.htm
---
Ant target: clean

```java title=Example.java
<?xml version="1.0"?>
<project name="sample" default="test" basedir=".">
   <target name="compile">
      <mkdir dir="build"/>
      <javac destdir="build"
             debug="on"
             optimize="on">
         <src path="src"/>
      </javac>
   </target>
   <target name="test" depends="compile">
      <java fork="no" failonerror="yes"
            classname="test.TestSample"
            classpath="build">
          <arg line=""/>
      </java>
   </target>
   <target name="clean">
      <delete dir="build"/>
   </target>
</project>
```

Download: AntCompileAndClean.zip ( 1 K )
Related examples in the same category
