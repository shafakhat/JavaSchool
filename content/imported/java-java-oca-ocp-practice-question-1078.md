---
title: Java OCA OCP Practice Question 1078
nav: Java OCA OCP Practice Ques...
description: What will be the result of attempting to run the following program?
section: Imported - java2s Archive
order: 1058
source: https://web.archive.org/web/20210101014712/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1078.html
---
## Question

What will be the result of attempting to run the following program?

```java title=Example.java
publicclass Main{
   publicstaticvoid main (String args []){
      String [][][] arr  ={{
            { "a", "b" , "c"},
            { "d", "e", null  }
        }, {
            {"AAA"}, null  },
            {{"BBB"}},
            {  { "z","p"},  {}
        }};
      System.out.println (arr [0][1][2]);
    }
}
```

Select 1 option

```java title=Example.java
A. It will throw NullPointerBoundsException.
B. It will throwArrayIndexOutOfBoundsException.
C. It will print null.
D. It will run without any error but will print nothing.
E. None of the above.
java title=Example.java
Correct Option is  : C
```

## Note

A. is wrong. There is no such exception.

```java title=Example.java
arr [0][1][2] => [0] =  {
      { "a", "b" , "c"},
      { "d", "e", null  }
}, [1] =  { "d", "e", null  }
```

and [2] = null.

So it will print null.

PreviousNext

## Related

- Java OCA OCP Practice Question 1075
- Java OCA OCP Practice Question 1076
- Java OCA OCP Practice Question 1077
- Java OCA OCP Practice Question 1079
- Java OCA OCP Practice Question 1080
