---
title: Maven Tutorial - Maven Introduction
nav: Maven Tutorial - Maven Int...
description: When creating software project we normally use a build tool to automate processes.
section: Imported - java2s Archive
order: 50044
source: https://www.java2s.com/Tutorials/Java/Maven_Tutorial/index.html
---
When creating software project we normally use a build tool to automate processes.

Building a software project typically includes the following activities:

- Compile source code
- Run test cases
- Create documentation from the source code
- Package compiled code into JAR files or ZIP files
- Install the library JAR file to classpath
- Deploy the packaged code to a server

A build tool can minimize the risk of humans errors while building the software manually.

Building software has several life cycles, such as compile, test, package. Different build tools handle the life cycles differently.

## What is Maven

Maven is a project management tool which can manage the complete building life cycle.

Maven simplifies and standardizes the project build process. by handling compilation, testing, library dependency, distribution, documentation and team collaboration.

The Maven developers claim that Maven is more than just a build tool. We can think of Maven as a build tool with more features.

Maven provides developers ways to manage following:

- Builds
- Test
- Documentation
- Reporting
- Dependencies
- Releases
- Distribution
- Mailing List

You will have your own answer once you understand it and start using it.

## Maven History

Maven was originally built to simplify building processes for Jakarta Turbine project.

Jakarta Turbine project has many sub projects and each project was built by using ANT. The generated JARs were checked into version control system.

Apache group then developed Maven to build multiple projects together.

Maven can publish projects information, deploy projects, share JARs across projects. The JAR files and building blocks are generated and managed by Maven.

Maven uses a standard directory layout and a default build lifecycle.

Maven is developed in Java, and is thus used more for Java projects.

## Convention over Configuration

Maven defines a comprehensive and declarative model for projects to make source code more reusable, maintainable, and easier to comprehend.

Maven uses plugins to interact with this declarative model. Most of the features are actually provided by plugins.

Maven uses pom.xml file to describe a project. pom.xml is referred as Project Object Model (POM), which is the fundamental unit of the Maven system.

Maven uses Convention over Configuration in managing projects and provides default behavior for projects. Developers need not to specify the source code folder, where to put the jar files, etc.

When creating a project, Maven creates default project structure. Developer can just save files accordingly.

The following table shows the default values for project source code files, test case folders, resource files and other configurations.

${basedir} denotes the project root folder:

Item  Default
---  ---
pom.xml  ${basedir}/pom.xml
source code  ${basedir}/src/main/java
resources  ${basedir}/src/main/resources
test cases source files  ${basedir}/src/test/java
test cases resource files  ${basedir}/src/test/resources
Complied source code  ${basedir}/target
Generated JAR files  ${basedir}/target/classes

## Maven vs. Ant

Ant is a popular build tool also from Apache.

Ant uses an imperative approach to declare the build files. By using Ant we have to specify in the build file what actions Ant should take and what folders/files to use.

In Ant we can specify low level actions like copying files, compiling code, zip the jar files etc.

Ant has no default directory layout.

Maven uses a more declarative approach. By using Maven we only specify in the POM file what to build, not how to build it.

In Maven, how to build your project is predefined in the Maven Build Life Cycles, Phases and Goals.
