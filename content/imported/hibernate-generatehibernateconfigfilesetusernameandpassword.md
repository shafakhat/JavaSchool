---
title: Generate Hibernate Config File
nav: Generate Hibernate Config ...
description: /////////////////////////////////////////////////////////////////////////
section: Imported - java2s Archive
order: 1059
source: https://web.archive.org/web/20061018180637/http://www.java2s.com/Code/Java/Hibernate/GenerateHibernateConfigFileSetUserNameAndPassword.htm
---
Generate Hibernate Config File: Set User Name And Password

```java title=Example.java
/////////////////////////////////////////////////////////////////////////
<project name="hibernate-tutorial" default="compile">
    <property name="sourcedir" value="${basedir}/src"/>
    <property name="targetdir" value="${basedir}/build"/>
    <property name="librarydir" value="${basedir}/lib"/>
    <path id="libraries">
        <fileset dir="${librarydir}">
            <include name="*.jar"/>
        </fileset>
    </path>
    <target name="clean">
        <delete dir="${targetdir}"/>
        <mkdir dir="${targetdir}"/>
    </target>
    <target name="compile" depends="clean, copy-resources">
      <javac srcdir="${sourcedir}"
             destdir="${targetdir}"
             classpathref="libraries"
             debug="on"/>
    </target>
    <target name="copy-resources">
        <copy todir="${targetdir}">
            <fileset dir="${sourcedir}">
                <exclude name="**/*.java"/>
            </fileset>
        </copy>
    </target>
    <target name="user">
        <property name="hibernate.connection.username" value="userName"/>
        <property name="hibernate.connection.password" value="passWord"/>
        <antcall target="hbm"/>
    </target>
    <target name="hbm" depends="compile">
        <taskdef
            name="hibernatedoclet"
            classname="xdoclet.modules.hibernate.HibernateDocletTask"
            classpathref="libraries"
            />
        <hibernatedoclet
            destdir="${targetdir}"
            verbose="true">
            <fileset dir="${sourcedir}">
                <include name="**/*.java"/>
            </fileset>
            <hibernate version="3.0"/>
            <hibernatecfg
                dialect="${hibernate.dialect}"
                jdbcUrl="${hibernate.connection.url}"
                driver="${hibernate.connection.driver_class}"
                userName="${hibernate.connection.username}"
                password="${hibernate.connection.password}"
                showSql="false"
                version="3.0"
                />
        </hibernatedoclet>
    </target>
</project>
```

Download: HibernateGenerateHibernateConfigFileSetUserNameAndPassword.zip ( 5,039 K )
Related examples in the same category
