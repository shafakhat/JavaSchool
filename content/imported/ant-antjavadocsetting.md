---
title: Ant Javadoc setting
nav: Ant Javadoc setting
description: <!-- You may freely edit this file. See commented blocks below for -->
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20100210140153/http://java2s.com/Code/Java/Ant/AntJavadocsetting.htm
---
```java title=Example.java
<?xml version="1.0" encoding="UTF-8"?>
<!-- You may freely edit this file. See commented blocks below for -->
<!-- some examples of how to customize the build. -->
<!-- (If you delete it and reopen the project it will be recreated.) -->
<project name="actions" default="default" basedir=".">
    <description>Builds, tests, and runs the project Actions.</description>
    <import file="nbproject/build-impl.xml"/>
    <import file="nbproject/profiler-build-impl.xml"/>
    <target name="-post-compile-test">
        <copy file="test/actions/ActionsXML1.xml" todir="build/classes/test"/>
        <copy file="test/actions/Bundle1.properties" todir="build/classes/test"/>
    </target>
    <target name="-post-compile-test-single" depends="-post-compile-test"/>
    <target name="cleanjavadoc" description="Delete javadoc files from the web site area">
        <!-- Delete all the javadoc files, so no stale files for deleted
         classes can possibly be around (though nobody should really be
         deleting any classes) -->
        <delete failonerror="false">
            <fileset dir="www/javadoc" includes="**/*.html"/>
        </delete>
    </target>
    <target name="javadoc">
        <mkdir dir="dist/javadoc"/>
        <property file="${basedir}/nbproject/project.properties"/>
        <property file="${basedir}/nbproject/private/private.properties"/>
        <javadoc overview="${basedir}/doc/api/overview.html"
                 destdir="dist/javadoc"
                 source="1.5"
                 notree="${javadoc.notree}"
                 use="${javadoc.use}"
                 nonavbar="${javadoc.nonavbar}"
                 noindex="${javadoc.noindex}"
                 splitindex="${javadoc.splitindex}"
                 author="${javadoc.author}"
                 version="${javadoc.version}"
                 windowtitle="${javadoc.windowtitle}"
                 private="${javadoc.private}"
                 failonerror="true" stylesheetfile="doc/api/stylesheet.css"
                 >
            <classpath>
                <path path="${javac.classpath}"/>
            </classpath>
            <packageset dir="src" defaultexcludes="yes">
              <include name="actions/**" />
              <exclude name="actions/ui/**" />
              <exclude name="actions/borrowed/**"/>
            </packageset>
        </javadoc>
        <copy file="doc/api/actions.dtd" tofile="dist/javadoc/actions.dtd"/>
        <copy file="doc/api/actionsDoc.html" tofile="dist/javadoc/actionsDoc.html"/>
    </target>
    <target name="-post-jar">
        <echo message="Copying jar to JNN dev dir"/>
        <delete failonerror="false" file="../jnn_new/jnn/lib/Actions.jar"/>
        <delete failonerror="false" file="../jnn_new/jnn/jnn.app/Contents/Resources/Java/lib/Actions.jar"/>
        <copy failonerror="true" file="dist/Actions.jar" todir="../jnn_new/jnn/lib/"/>
        <copy failonerror="true" file="dist/Actions.jar" todir="../jnn_new/jnn/jnn.app/Contents/Resources/Java/lib/"/>
    </target>
    <target name="release" depends="jar,cleanjavadoc,javadoc" description="Prepare a new release">
        <copy file="dist/Actions.jar" todir="www"/>
        <zip destfile="www/ActionsAPI.zip" basedir="dist/javadoc" update="false" whenempty="fail" compress="true"/>
        <mkdir dir="www/javadoc"/>
        <copy todir="www/javadoc">
            <fileset dir="dist/javadoc" includes="**"/>
        </copy>
    </target>
</project>
```

1.  Checking that the documentation is up to date
---  ---
2.  Generate Javadocs for the application
3.  Generate Javadocs for the application, using offline package-list files
4.  Assemble the documentation
5.  Zip the documentation
6.  Generate Javadoc from Ant
