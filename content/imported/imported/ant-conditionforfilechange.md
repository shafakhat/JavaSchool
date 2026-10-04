---
title: Condition for file change
nav: Condition for file change
description: <project name="Apache Ant Properties Project" default="compile" basedir=".">
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20061027015614/http://www.java2s.com/Code/Java/Ant/Conditionforfilechange.htm
---
```java title=Example.java
<?xml version="1.0"?>
<project name="Apache Ant Properties Project" default="compile" basedir=".">
  <fileset dir="." id="uptodate.id">
    <include name="src/jstl/One.java"/>
  </fileset>
  <property name="jstl.src" value="jstl"/>
  <property name="jstl.jar" value="jstl.jar"/>
  <condition property="jstl.src.exists">
    <available file="${jstl.src}" filepath="./src"/>
  </condition>
  <condition property="jstl.jar.exists">
    <available file="${jstl.jar}" filepath="./lib"/>
  </condition>
  <condition property="uptodate">
    <uptodate>
      <srcfiles refid="uptodate.id"/>
      <mapper type="merge" to="./One.java"/>
    </uptodate>
  </condition>
  <target name="checkout-jstl" unless="jstl.src.exists">
    <echo message="Checking out ${jstl.jar}"/>
  </target>
  <target name="build-jstl" depends="checkout-jstl" unless="jstl.jar.exists">
    <echo message="Building ${jstl.jar}"/>
  </target>
  <target name="compile" if="uptodate">
    <echo message="File changed: ${uptodate}"/>
  </target>
  <condition property="is.fileset">
    <isreference refid="uptodate.id" type="fileset"/>
  </condition>
  <target name="fileset-prepare">
    <echo message="Value of is.fileset = ${is.fileset}"/>
  </target>
</project>
```

Download: AntBasicTags.zip ( 2 K )
Related examples in the same category
