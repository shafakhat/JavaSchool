---
title: Ant jar file setting the Main-Class
nav: Ant jar file setting the M...
description: <target name="all" depends="init,clean,compile,createJars,copyBuild" >
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/20100213130334/http://java2s.com/Code/Java/Ant/AntjarfilesettingtheMainClass.htm
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

1.  Ant task: jar
---  ---
2.  Jar with includes and excludes using filesets
3.  Jar with includes and excludes
4.  Generates java2s.jar
5.  Jar file with fileset and exclude
6.  Jar file: exclude files
7.  More than one filesets for jar
8.  Add attribute to jar file manifest
