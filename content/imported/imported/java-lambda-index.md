---
title: Java Lambda Introduction
nav: Java Lambda Introduction
description: A lambda expression is an unnamed function with parameters and a body.
section: Imported - java2s Archive
order: 50051
source: https://www.java2s.com/Tutorials/Java/Java_Lambda/index.html
---
A lambda expression is an unnamed function with parameters and a body.

The lambda expression body can be a block statement or an expression.

-> separates the parameters and the body.

(int x) -> x + 1 takes an int parameter and returns the parameter value incremented by 1.

(int x, int y) -> x + y takes two int parameters and returns the sum.

(String msg)->{System.out.println(msg);} takes a String parameter and prints it on the standard output.

msg->System.out.println(msg) takes a parameter and prints it on the standard output. It is identical to the code above.

() -> "hi" takes no parameters and returns a string.

(String str) -> str.length() takes a String parameter and returns its length.

The following lambda takes two int parameters and returns the maximum of the two.

```java title=Example.java

(int x, int y)  ->  {
    int max = x  > y  ?  x  : y;
    return max;
}
```

## Why Lambda Expressions

The lambda expressions allows us to pass logic in a compact way.

The following code uses an anonymous inner class to add event handler for a button click action.

```java title=Example.java

button.addActionListener(new ActionListener() {
    publicvoid actionPerformed(ActionEvent e) {
       System.out.println("hi");
    }
});
```

The action handler prints out a message when that the button is clicked.

By using a lambda expression we can add the action handler to a button click event in a single line of code.

```java title=Example.java
button.addActionListener(e -> System.out.println("hi"));
```

## Note

Instead of passing in an inner class that implements an interface, we're passing in a block of code.

e is the name of a parameter,

-> separates the parameter from the body of
the lambda expression.

In the lambda expression the parameter e is not declared with a type. javac is inferring the type of e from its context, the signature of addActionListener.

We don't need to explicitly write out the type when it's obvious. The lambda method parameters are still statically typed.
