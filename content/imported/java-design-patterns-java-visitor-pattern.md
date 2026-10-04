---
title: Java Design Patterns Tutorial - Java Design Pattern - Visitor Pattern
nav: Java Design Patterns Tutor...
description: In visitor pattern, element object accepts the visitor object and visitor object handles the operation on the element object.
section: Imported - java2s Archive
order: 50134
source: https://www.java2s.com/Tutorials/Java/Java_Design_Patterns/0280__Java_Visitor_Pattern.html
---
```java title=Example.java
```

In visitor pattern, element object accepts the visitor object and visitor object handles the operation on the element object.

This pattern is a behavior pattern.

By this way, execution algorithm of element can be changed from different visitors.

## Example

```java title=Example.java
class TreeNode {private String name;
  public TreeNode(String name) {
    this.name = name;
  }
  public String getName() {
    return name;
  }
  publicvoid accept(NodeVisitor v) {
    v.visit(this);
  }
}
interface NodeVisitor {
  publicvoid visit(TreeNode n);
}
class ConsoleVisitor implements NodeVisitor {
  @Override
  publicvoid visit(TreeNode n) {
    System.out.println("console:" + n.getName());
  }
}
class EmailVisitor implements NodeVisitor {
  @Override
  publicvoid visit(TreeNode n) {
    System.out.println("email:" + n.getName());
  }
}
publicclass Main {
  publicstaticvoid main(String[] args) {
    TreeNode computer = new TreeNode("JavaSchool");
    computer.accept(new ConsoleVisitor());
    computer.accept(new EmailVisitor());
  }
}
```

The code above generates the following result.

- « Previous
