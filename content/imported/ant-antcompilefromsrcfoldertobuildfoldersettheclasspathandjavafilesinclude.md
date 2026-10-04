---
title: Ant compile from src folder to build folder, set the class path and java files include
nav: Ant compile from src folde...
description: Ant compile from src folder to build folder, set the class path and java files include
section: Imported - java2s Archive
order: 1006
source: https://web.archive.org/web/20100810021948/http://www.java2s.com:80/Code/Java/Ant/Antcompilefromsrcfoldertobuildfoldersettheclasspathandjavafilesinclude.htm
---
Ant compile from src folder to build folder, set the class path and java files include

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

1.  Compile the web application
---  ---
2.  Ant target:compile
3.  Compile the stand-alone application
4.  Use a precompiler with Java
5.  Indicate the init and max memory when compiling
6.  Ant Javac setting
7.  Ant javac includes
8.  Javac include and exclude
9.  Javac with classpath
10.  Javac with encoding
11.  Javac with optimize
12.  Set debug and optimize for javac
13.  Set failonerror for javac
14.  Set debuglevel for javac
15.  Set link for Javac
16.  Set source version in javac
17.  Set target for javac
