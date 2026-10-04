---
title: Ant copy file
nav: Ant copy file
description: <target name="all" depends="init,clean,compile,createJars,copyBuild" >
section: Imported - java2s Archive
order: 1007
source: https://web.archive.org/web/20100203135506/http://www.java2s.com:80/Code/Java/Ant/Antcopyfile.htm
---
```java title=Example.java
<project name="YourName" default="all">
  <target name="all" depends="init,clean,compile,createJars,copyBuild" >
  </target>
  <target name="init" description="Project">
    <property environment="env" />
    <property name="j2sdkApi" value="${env.JAVA_HOME}/jre/lib/rt.jar" />
      <property name="src" value="./src" />
    <property name="build" value= "./build" />
  </target>
  <target name="clean" description="build" depends="init">
    <delete dir="${build}" />
    <mkdir dir="${build}" />
  </target>
  <target name="compile" description="compile" depends="init">
    <javac srcdir="${src}" destdir="${build}" >
      <classpath path="${j2sdkApi}" />
            <include name="**/application/**"/>
      <include name="**/types/**"/>
    </javac>
  </target>
  <target name="copyBuild" description="desccription here">
    <copy file="${src}/LOGOUNB_CAPA.JPG" todir="${build}/" />
    <copydir src="${src}/config" dest="${build}/config" />
  </target>
  <target name="createJars" description="jars" depends="compile">
    <mkdir dir="${build}/xml/jar"/>
    <jar jarfile="${build}/br/xml/jar/xpfg.jar"
       basedir="${build}/unb/cic/xml" />
      <manifest file="manifest.mf">
        <attribute name="Main-Class" value="${build}/br/unb/cic/xml/XMLMain" />
      </manifest>
  </target>
</project>
```

1.  Ant copy folder
---  ---
2.  Ant task copy file
3.  Ant task delete tree
4.  Ant task make dir
5.  Create folder
6.  Delete folder
7.  Delete with file set
8.  File Checksum
9.  File file with fixcrlf
10.  File set includes
11.  copy todir, fileset, include, exclude
