---
title: Java OCA OCP Practice Question 1026
nav: Java OCA OCP Practice Ques...
description: if (flag) //1 if (flag) //2 System.out.println ("True False");
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-oca-ocp-practice-question-1026.html
---
## Question

Consider the following method...

```java title=Example.java
public void ifTest (boolean flag){
   if  (flag)   //1  if  (flag)   //2  System.out.println ("True False");
   else // 3  System.out.println ("True True");
   else // 4  System.out.println ("False False");
}
```

Which of the following statements are correct ?

Select 3 options

- A. If run with an argument of 'false', it will print 'False False'
- B. If run with an argument of 'false', it will print 'True True'
- C. If run with an argument of 'true', it will print 'True False'
- D. It will never print 'True True'
- E. It will not compile.

```java title=Example.java
Correct Options are  : A C D
```

## Note

Note that if and else do not cascade. They are like opening and closing braces.

```java title=Example.java
if  (flag)   //1  if  (flag)   //2  System.out.println ("True False");
       else // 3 This closes //2  System.out.println ("True True");
   else // 4 This closes //1  System.out.println ("False False");
```

So, else at //3 is associated with if at //2 and else at //4 is associated with if at // 1

PreviousNext

## Related

- Java OCA OCP Practice Question 1023
- Java OCA OCP Practice Question 1024
- Java OCA OCP Practice Question 1025
- Java OCA OCP Practice Question 1027
- Java OCA OCP Practice Question 1028
