---
title: Java Thread Tutorial - Java Thread Creation
nav: Java Thread Tutorial - Jav...
description: Java represents a thread as an object. An object of the java.lang.Thread class represents a thread.
section: Imported - java2s Archive
order: 50045
source: https://www.java2s.com/Tutorials/Java/Java_Thread/index.html
---
- Next »

Java represents a thread as an object. An object of the java.lang.Thread class represents a thread.

There are at least two steps involved in working with a thread:

- Creating an object of the Thread class
- Invoking the start() method of the Thread class to start the thread

We can use the default constructor of the Thread class to create a Thread object.

```java title=Example.java

Thread  simplestThread = new Thread();
```

We must call its start() method to start the thread represented by that object.

```java title=Example.java

simplestThread.start();
```

## Logic for Thread

There are three ways you can specify your code to be executed by a thread:

- By inheriting your class from the Thread class
- By implementing the Runnable interface in your class
- By using the method reference to a method that takes no parameters and returns void

## Inheriting Your Class from the Thread Class

When we inherit class from the Thread class, we should override the run() method and provide the code to be executed by the thread.

```java title=Example.java
class MyThreadClass extends Thread {
  @Override
  public void run() {
    System.out.println("Hello Java  thread!");
  }
}
```

The steps to create a thread object and start the thread.

```java title=Example.java

MyThreadClass  myThread = new MyThreadClass();
myThread.start();
```

The thread will execute the run() method of the MyThreadClass class.

## Implementing the Runnable Interface

We can create a class that implements the java.lang.Runnable interface. Runnable is a functional interface and it is declared as follows:

```java title=Example.java

@FunctionalInterface
publicinterface Runnable {
  void run();
}
```

From Java 8, we can use a lambda expression to create an instance of the Runnable interface.

```java title=Example.java

Runnable  aRunnableObject = () ->  System.out.println("Hello Java  thread!");
```

Create an object of the Thread class using the constructor that accepts a Runnable object.

```java title=Example.java

Thread  myThread = new Thread(aRunnableObject);
```

Start the thread by calling the start() method of the thread object.

```java title=Example.java

myThread.start();
```

The thread will execute the code contained in the body of the lambda expressions.

## Using a Method Reference

From Java 8, we can use the method reference of a method of any class that takes no parameters and returns void as the code to be executed by a thread.

The following code declares a ThreadTest class that contains an execute() method.

The method contains the code to be executed in a thread.

```java title=Example.java
publicclass ThreadTest {
  publicstatic void execute() {
    System.out.println("Hello Java  thread!");
  }
}
```

The following code uses the method reference of the execute() method of the ThreadTest class to create a Runnable object:

```java title=Example.java

Thread  myThread = new Thread(ThreadTest::execute);
myThread.start();
```

The thread will execute the code contained in the execute() method of the ThreadTest class.

The following code shows how to create a thread and print integers from 1 to 5 on the standard output.

```java title=Example.java
publicclass Main {
  publicstaticvoid main(String[] args) {
    // Create a Thread object
    Thread t = new Thread(Main::print);
//www.java2s.com// Start the thread
    t.start();
  }
  publicstaticvoid print() {
    for (int i = 1; i <= 5; i++) {
      System.out.print(i + "  ");
    }
  }
}
```

The code above generates the following result.

- Next »
