---
title: Ant javac includes
nav: Ant javac includes
description: <zip destfile="${dist}\actionServlet-${DSTAMP}${TSTAMP}.zip">
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20100709054147/http://www.java2s.com:80/Code/Java/Ant/Antjavacincludes.htm
---
Ant javac includes

```java title=Example.java
<?xml version="1.0"?>
<project name="yourname" basedir=".." default="all">
  <property name="dist" location="dist/"/>
  <property name="lib" location="lib/"/>
  <property name="src" location="src/"/>
  <path id="class.path">
    <pathelement path="${src}"/>
    <fileset dir="${lib}">
      <include name="**/*.jar"/>
      <include name="**/*.zip"/>
    </fileset>
    <fileset dir="/dev">
      <include name="**/*.jar"/>
      <include name="**/*.zip"/>
    </fileset>
  </path>
  <target name="clean">
    <delete>
      <fileset dir="${src}" includes="**/*.class"/>
    </delete>
    <delete dir="${dist}"/>
  </target>
  <target name="zip" depends="clean">
    <tstamp/>
    <mkdir dir="${dist}"/>
    <zip destfile="${dist}\actionServlet-${DSTAMP}${TSTAMP}.zip">
      <zipfileset dir=".">
        <exclude name="${dist}"/>
      </zipfileset>
    </zip>
  </target>
  <target name="compile">
    <javac>
      <src path="${src}" />
      <classpath refid="class.path"/>
      <include name = "*/**" />
    </javac>
   </target>
  <target name="jar" depends="compile">
    <mkdir dir="${dist}"/>
    <tstamp/>
    <jar
      basedir="src"
      jarfile="${dist}/actionServlet.jar"
      excludes="**/*.java, *.mdb"
    />
  </target>
  <target name="all" depends="jar"/>
</project>
```

1.  Compile the web application
---  ---
2.  Ant target:compile
3.  Compile the stand-alone application
4.  Use a precompiler with Java
5.  Indicate the init and max memory when compiling
6.  Ant Javac setting
7.  Javac include and exclude
8.  Javac with classpath
9.  Javac with encoding
10.  Javac with optimize
11.  Set debug and optimize for javac
12.  Set failonerror for javac
13.  Set debuglevel for javac
14.  Set link for Javac
15.  Set source version in javac
16.  Set target for javac
17.  Ant compile from src folder to build folder, set the class path and java files include
