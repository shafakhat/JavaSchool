---
title: Create Timestamp
nav: Create Timestamp
description: <zip destfile="${dist}\actionServlet-${DSTAMP}${TSTAMP}.zip">
section: Imported - java2s Archive
order: 1054
source: https://web.archive.org/web/20100211103101/http://java2s.com/Code/Java/Ant/CreateTimestamp.htm
---
Create Timestamp

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

1.  Ant tstamp
