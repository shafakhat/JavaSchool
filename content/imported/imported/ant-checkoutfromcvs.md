---
title: Check out from CVS
nav: Check out from CVS
description: <project name="Java XP Cookbook" default="build" basedir=".">
section: Imported - java2s Archive
order: 1044
source: https://web.archive.org/web/20061026221428/http://www.java2s.com/Code/Java/Ant/CheckoutfromCVS.htm
---
Check out from CVS

```java title=Example.java
<?xml version="1.0"?>
<project name="Java XP Cookbook" default="build" basedir=".">
  <target name="prepare">
    <!-- convert the CVS repository directory into
         a fully-qualitied Windows directory -->
    <pathconvert targetos="windows" property="cvsrepository.path">
       <path>
         <pathelement location="repository"/>
       </path>
    </pathconvert>
    <!-- store the CVS root in a property -->
    <property name="cvsroot" value=":local:${cvsrepository.path}"/>
    <!-- determine if the files have been checked out -->
    <available file="cookbook" type="dir" property="already.checked.out"/>
  </target>
  <target name="clean"
          description="Remove the entire cookbook directory.">
    <delete dir="cookbook"/>
  </target>
  <target name="cvscheckout" depends="prepare" unless="already.checked.out">
    <cvs cvsroot="${cvsroot}"
         package="cookbook"/>
  </target>
  <target name="cvsupdate" depends="prepare" if="already.checked.out">
    <cvs command="update -dP"
         cvsroot="${cvsroot}"
         dest="cookbook"/>
  </target>
  <target name="build" depends="cvscheckout,cvsupdate">
    <ant dir="cookbook" target="all" inheritAll="false"/>
  </target>
</project>
```

Download: AntCVSCheckout.zip ( 1 K )
Related examples in the same category
