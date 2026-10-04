---
title: Java Packages
nav: Packages
description: Organize classes into packages, import rules, static imports and package naming conventions.
section: Object Oriented
order: 70
---

## Why packages?

A **package** is a namespace - a folder for related classes. Packages give you:

- **No name clashes** (`com.acme.util.Date` vs `java.util.Date`)
- **Access control** - package-private members stay inside the package
- **Organization** - large codebases stay navigable
- **Safer recompiles** - unrelated code can't accidentally depend on your internals

## Declaring and using a package

The package declaration must be the **first line** of the file, and the folder structure must match it:

```text title=Project layout
src/
└── com/
    └── shop/
        ├── App.java          -> package com.shop;
        └── model/
            └── Product.java  -> package com.shop.model;
```

```java title=App.java
package com.shop;

import com.shop.model.Product;      // import a specific class
// import com.shop.model.*;        // or the whole package
import java.util.List;              // java.* packages live in the JDK
// import static java.lang.Math.PI; // static import: use PI directly

public class App {
    public static void main(String[] args) {
        Product p = new Product("Keyboard", 2499);
        System.out.println(p);
        System.out.println("pi = " + PI);
    }
}
```

```java title=Product.java
package com.shop.model;

public class Product {
    private String name;
    private double price;

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public String toString() {
        return name + " @ " + price;
    }
}
```

Compile and run from the source root with the folder structure intact:

```bash title=Terminal
javac com/shop/App.java com/shop/model/Product.java
java com.shop.App
```

## Import rules (the ones everyone forgets)

| Rule | Detail |
|---|---|
| `java.lang` is auto-imported | `String`, `System`, `Math` need no import |
| No import needed for the *same* package | classes in `com.shop` see each other directly |
| `import` doesn't load code | it only resolves *names* |
| Name clash? | use the fully qualified name inline |

```java title=NameClash.java
import java.util.Date;        // wins by explicit import
// import java.sql.Date;      // can't import both - use fully qualified names instead

public class NameClash {
    public static void main(String[] args) {
        Date d = new Date();                    // java.util.Date
        java.sql.Date sqlD = new java.sql.Date(0L);  // fully qualified
        System.out.println(d.getClass().getSimpleName());
        System.out.println(sqlD.getClass().getSimpleName());
    }
}
```

> **Note:** `import` is purely compile-time name sugar. It has zero runtime cost - the JVM identifies classes by their *fully qualified name* (`com.shop.model.Product`) anyway.

## Static imports

```java title=StaticImport.java
import static java.lang.Math.max;
import static java.lang.Math.PI;

public class StaticImport {
    public static void main(String[] args) {
        System.out.println(max(3, 9));     // no "Math." prefix
        System.out.println(2 * PI);
    }
}
```

Use sparingly - they're great for constants (`PI`), less great for hiding where `max` came from.

## Package naming conventions

- All lowercase: `com.shop.order`, not `Com.Shop`
- Reverse your domain: `com.google.common`, `org.apache.commons`
- Company/team prefix avoids collisions in the global namespace
- Keep packages cohesive: one job per package (`service`, `model`, `repo`)

## Access - what package-private really means

```text title=Visibility by package
  class A  in package p      class B in package q
  +-------------------+      +-------------------+
  | public method     |      | can call A.public |
  | protected method  |      | (only if B extends|
  | package-private   |  X   |  A - protected)   |
  | private method    |      | package-private:  |
  |                   |      |   NO ACCESS       |
  +-------------------+      +-------------------+
```

Package-private (no modifier) is a deliberate tool: it keeps a class or method **invisible to the outside world** while staying usable by sibling classes - often the perfect level for implementation helpers.

```java title=p2/Helper.java (package p2)
package p2;

class Hidden { }              // package-private class - invisible outside p2
public class Helper {
    void internal() { }       // package-private method
    public void api() { }     // visible everywhere
}
```

## JAR packages

In practice you ship packages inside a **JAR** (a zip of `.class` files):

```bash title=Terminal
jar -cf shop.jar com/
java -cp shop.jar com.shop.App
```

`-cp` (classpath) tells Java where to search for compiled packages - folders or JARs, separated by `:` (Linux/macOS) or `;` (Windows).

Next: [The static keyword](static-keyword.html).
