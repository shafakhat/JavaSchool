---
title: copy todir, fileset, include, exclude
nav: copy todir, fileset, inclu...
description: //COMMON DEVELOPMENT AND DISTRIBUTION LICENSE (CDDL) Version 1.0
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/20100202001924/http://www.java2s.com:80/Code/Java/Ant/copytodirfilesetincludeexclude.htm
---
```java title=Example.java
//COMMON DEVELOPMENT AND DISTRIBUTION LICENSE (CDDL) Version 1.0
<project name="ajax4jsf" default="distribute">
  <property name="commonLibs.dir" value="${basedir}/commonLibs"></property>
  <property name="distrib.dir" value="${basedir}/distribution"/>
  <property name="work.dir" value="${basedir}/build"/>
  <property name="src.root.dir" value="${basedir}/src"></property>
  <property name="test.src.dir" value="${src.root.dir}/testCase"></property>
  <property name="framework.src.dir" value="${src.root.dir}/framework"></property>
  <property name="framework.java.src.dir" value="${framework.src.dir}/java"></property>
  <property name="framework.js.src.dir" value="${framework.src.dir}/JavaScript"></property>
  <property name="framework.generate.src.dir" value="${framework.src.dir}/generate"></property>
  <property name="framework.build.dir" value="${work.dir}/framework"></property>
  <property name="cdk.src.dir" value="${src.root.dir}/cdk"></property>
  <property name="cdk.build.dir" value="${work.dir}/cdk"></property>
    <property name="test.src.dir" value="${src.root.dir}/test"></property>
    <property name="test.build.dir" value="${work.dir}/test"></property>
  <property name="doc.root.dir" value="${distrib.dir}/docs"></property>
  <property name="tlddoc.dir" value="${doc.root.dir}/tldDoc"></property>
  <property name="javadoc.dir" value="${doc.root.dir}/javaAPI"></property>
  <property name="tlddoc.jar" value="${commonLibs.dir}/tlddoc.jar"></property>
  <property name="framework-distribution-name" value="ajax4jsf"></property>
  <property name="cdk-distribution-name" value="ajax4jsf-cdk" />
    <property name="test-distribution-name" value="ajax4jsf-test" />
  <property name="generated-source.dir" value="${work.dir}/gen-src"></property>
  <fileset id="commonLibs" dir="${commonLibs.dir}">
    <include name="*.jar"/>
  </fileset>
  <path id="class-path">
    <fileset refid="commonLibs"></fileset>
  </path>
  <target name="prepare">
    <mkdir dir="${distrib.dir}"/>
    <mkdir dir="${work.dir}"/>
  </target>
  <target name="generate-framework" depends="compile-framework,compile-cdk">
    <ant antfile="${framework.generate.src.dir}/build.xml" inheritall="true" dir="${basedir}" target="xml-merge">
    </ant>
  </target>
  <target name="prepare-framework">
    <mkdir dir="${framework.build.dir}" />
  </target>
  <target name="prepare-cdk">
    <mkdir dir="${cdk.build.dir}" />
  </target>
    <target name="prepare-test">
        <mkdir dir="${test.build.dir}" />
    </target>
  <target name="compile-framework" depends="prepare-framework">
    <javac
      destdir="${framework.build.dir}"
      compiler="javac1.4"
      source="1.4"
      target="1.4"
      debug="true"
            failonerror="false"
      debuglevel="lines,vars,source">
      <classpath refid="class-path"></classpath>
      <src path="${framework.src.dir}"></src>
    </javac>
    <copy todir="${framework.build.dir}">
      <fileset dir="${framework.java.src.dir}">
        <include name="**/*.*"/>
        <exclude name="**/*.java"/>
        <exclude name="META-INF/*faces-config.xml"/>
      </fileset>
    </copy>
  </target>
  <target name="compile-cdk" depends="prepare-cdk">
    <javac
      destdir="${cdk.build.dir}"
      compiler="javac1.5"
      source="1.5"
      target="1.5"
      debug="true"
      debuglevel="lines,vars,source">
        <classpath refid="class-path"></classpath>
      <src path="${cdk.src.dir}"></src>
    </javac>
    <copy todir="${cdk.build.dir}/META-INF">
      <fileset dir="${cdk.src.dir}/META-INF">
        <include name="**/*.*"/>
      </fileset>
    </copy>
  </target>
    <target name="compile-test" depends="prepare-test">
        <javac
            destdir="${test.build.dir}"
            compiler="javac1.4"
            source="1.4"
            target="1.4"
            debug="true"
            debuglevel="lines,vars,source"
            includes="org/ajax4jsf/tests/*.*" >
                <classpath refid="class-path"></classpath>
            <classpath path="${framework.build.dir}"></classpath>
            <src path="${test.src.dir}">
            </src>
        </javac>
        <copy todir="${test.build.dir}/META-INF">
            <fileset dir="${test.src.dir}/META-INF">
                <include name="**/*.*"/>
            </fileset>
        </copy>
        <copy todir="${test.build.dir}/WEB-INF">
            <fileset dir="${test.src.dir}/WEB-INF">
                <include name="**/*.*"/>
            </fileset>
        </copy>
    </target>
    <target name="compile-framework-phase2" depends="generate-framework">
    <javac
      destdir="${framework.build.dir}"
      compiler="javac1.4"
      source="1.4"
      target="1.4"
      debug="true"
      debuglevel="lines,vars,source">
      <classpath>
        <path>
        <path refid="class-path"></path>
        <pathelement path="${framework.build.dir}"/>
        </path>
      </classpath>
      <src path="${generated-source.dir}"></src>
    </javac>
    <copy todir="${framework.build.dir}">
      <fileset dir="${generated-source.dir}">
        <include name="**/*.*"/>
        <exclude name="**/*.java"/>
        <exclude name="META-INF/*-faces-config.xml"/>
      </fileset>
    </copy>
  </target>
  <target name="assemble-javascripts" depends="prepare-framework">
    <ant antfile="${framework.js.src.dir}/build.xml" dir="${framework.js.src.dir}">
      <property name="target-dir" value="${framework.build.dir}"></property>
    </ant>
  </target>
  <target name="build-framework" depends="compile-framework,assemble-javascripts,compile-framework-phase2">
  </target>
  <target name="build-cdk" depends="compile-cdk">
  </target>
    <target name="build-test" depends="compile-test">
    </target>
        <target name="prepare-distribution-dir">
    <mkdir dir="${distrib.dir}/lib"/>
  </target>
  <target name="package-framework" depends="build-framework, prepare-distribution-dir">
    <jar destfile="${distrib.dir}/lib/${framework-distribution-name}.jar">
      <fileset dir="${framework.build.dir}">
        <include name="**/*.*"/>
      </fileset>
    </jar>
  </target>
  <target name="package-cdk" depends="prepare-distribution-dir,build-cdk">
    <jar destfile="${distrib.dir}/lib/${cdk-distribution-name}.jar">
      <fileset dir="${cdk.build.dir}">
        <include name="**/*.*"/>
      </fileset>
    </jar>
  </target>
    <target name="package-test" depends="prepare-distribution-dir,build-test">
        <jar destfile="${distrib.dir}/lib/${test-distribution-name}.jar">
            <fileset dir="${test.build.dir}">
                <include name="**/*.*"/>
            </fileset>
        </jar>
    </target>
  <target name="prepare-docs">
    <mkdir dir="${doc.root.dir}"/>
  </target>
  <target name="docs" depends="prepare-docs, javadoc, tlddoc, copy-doc">
  </target>
  <target name="copy-doc" depends="prepare-docs">
    <copy todir="${doc.root.dir}" failonerror="false">
      <fileset dir="${basedir}/doc">
        <include name="**/*"/>
      </fileset>
    </copy>
  </target>
  <target name="javadoc">
    <mkdir dir="${javadoc.dir}"/>
    <javadoc packagenames="org.*" destdir="${javadoc.dir}">
      <sourcepath>
        <pathelement path="${framework.java.src.dir}"/>
      </sourcepath>
      <classpath refid="class-path"></classpath>
    </javadoc>
  </target>
  <target name="tlddoc">
    <mkdir dir="${tlddoc.dir}"/>
    <echo message="${tlddoc.jar}"></echo>
    <apply executable="java" parallel="true" verbose="true">
      <!-- dir="${tlddoc.dir}">-->
      <arg line="-jar ${tlddoc.jar}"/>
      <arg line="-doctitle 'AJAX4JSF'"/>
      <!--arg line="-xslt ${tlddocxsl.dir}"/-->
      <arg line="-d ${tlddoc.dir}"/>
      <fileset dir="${framework.build.dir}/META-INF" includes="**.tld"/>
    </apply>
  </target>
  <target name="copy-dependencies" depends="prepare-distribution-dir">
    <copy todir="${distrib.dir}/lib">
      <fileset dir="${commonLibs.dir}">
        <include name="oscache*.jar"/>
      </fileset>
    </copy>
  </target>
  <target name="copy-src">
    <mkdir dir="${distrib.dir}/src"/>
    <copy todir="${distrib.dir}/src">
      <fileset dir="${framework.src.dir}">
        <include name="**/*"/>
      </fileset>
    </copy>
  </target>
  <target name="copy-demo">
    <mkdir dir="${distrib.dir}/demo"/>
    <copy todir="${distrib.dir}/demo" failonerror="false">
      <fileset dir="${basedir}/demo">
        <include name="**/*"/>
      </fileset>
    </copy>
  </target>
  <target name="copy-txt">
    <copy todir="${distrib.dir}">
      <fileset dir="${basedir}">
        <include name="*.txt"/>
        <include name="*.TXT"/>
      </fileset>
    </copy>
  </target>
  <target name="build-test-framework">
    <javac
      destdir="${framework.build.dir}"
      compiler="javac1.4"
      source="1.4"
      target="1.4"
      debug="true"
      debuglevel="lines,vars,source">
      <classpath refid="class-path"></classpath>
      <src path="${test.src.dir}"></src>
    </javac>
    <copy todir="${framework.build.dir}">
      <fileset dir="${test.src.dir}">
        <include name="**/*.*"/>
        <exclude name="**/*.java"/>
        <exclude name="META-INF/*"/>
        <exclude name="WEB-INF/*"/>
      </fileset>
    </copy>
  </target>
  <target name="distribute" depends="clean,build-framework,package-framework, copy-dependencies, docs, copy-src, copy-txt, copy-demo, package-cdk, package-test">
    <!--delete dir="${work.dir}"></delete-->
    <delete file="${basedir}/velocity.log" failonerror="false" verbose="true"></delete>
  </target>
  <target name="clean">
    <delete dir="${work.dir}"></delete>
    <delete includeemptydirs="true" failonerror="false">
      <fileset dir="${distrib.dir}">
        <include name="**/*"/>
      </fileset>
    </delete>
  </target>
</project>
```

1.  Ant copy file
---  ---
2.  Ant copy folder
3.  Ant task copy file
4.  Ant task delete tree
5.  Ant task make dir
6.  Create folder
7.  Delete folder
8.  Delete with file set
9.  File Checksum
10.  File file with fixcrlf
11.  File set includes
