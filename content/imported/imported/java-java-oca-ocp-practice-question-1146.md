---
title: Java OCA OCP Practice Question 1146
nav: Java OCA OCP Practice Ques...
description: Which of the following would be a valid class that can be inserted at // 1 ?
section: Imported - java2s Archive
order: 1114
source: https://web.archive.org/web/20210101014723/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1146.html
---
## Question

Given the following class definition:

```java title=Example.java
class MyClass {
  protectedint i;
  MyClass (int i)  {    this.i = i;     }

}
// 1  : Insert code here
```

Which of the following would be a valid class that can be inserted at // 1 ?

Select 2 options

- A. class MySubClass {}
- B. class MySubClass extends MyClass {}
- C. class MySubClass extends MyClass { MySubClass () { System.out.println ("i = " + i); } }
- D. class MySubClass { MySubClass () {} }

```java title=Example.java
Correct Options are  : A D
```

## Note

Since class MySubClass does not have any constructor, the compiler will try to insert the default constructor, which will look like this:

```java title=Example.java

MySubClass (){
    super();  //Notice that it is trying to call the no args constructor of the super class, MyClass .
}
```

Since MyClass doesn't have any no-args constructor, the above code will fail to compile.

Notice that class MyClass does not define a no-argument constructor.

Also note that the class MySubClass does not define a constructor.

Thus, class MySubClass relies on the default constructor MySubClass().

Class MySubClass's default constructor looks like this: public MySubClass() {}

However, Constructors implicitly (if an explicit call to the superclass's constructor is not present) call their superclass's constructor super().

So, class MySubClass's default constructor actually looks like this:

```java title=Example.java
public MySubClass (){
  super ();
}
```

Now, since class MyClass does not define a no-argument constructor the above code will not compile.

However, class MySubClass would be correct if changed to:

```java title=Example.java
class MySubClass extends MyClass {
  MySubClass (){
    super (1); // pass it any integer
   }
  // or
  MySubClass (int number){
    super (number);
   }
}
```

You could also add a no-argument constructor to class MyClass and leave class MySubClass as is.

PreviousNext

## Related

- Java OCA OCP Practice Question 1143
- Java OCA OCP Practice Question 1144
- Java OCA OCP Practice Question 1145
- Java OCA OCP Practice Question 1147
- Java OCA OCP Practice Question 1148
