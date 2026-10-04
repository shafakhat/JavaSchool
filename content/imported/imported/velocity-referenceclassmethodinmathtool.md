---
title: Reference Class method in Mathtool
nav: Reference Class method in ...
description: Imported from the java2s.com archive: Reference Class method in Mathtool
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20071104162726/http://www.java2s.com:80/Code/Java/Velocity/ReferenceClassmethodinMathtool.htm
---
```java title=Example.java
import java.io.StringWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collection;
import org.apache.velocity.Template;
import org.apache.velocity.VelocityContext;
import org.apache.velocity.app.Velocity;
import org.apache.velocity.tools.generic.MathTool;
public class ProductList {
    public static void main(String[] args) throws Exception {
        Velocity.init();
        Template t = Velocity.getTemplate("./src/calculation.vm");
        VelocityContext ctx = new VelocityContext();
        Collection products = new ArrayList();
        products.add(new Product("Product 1", 112.199));
        products.add(new Product("Product 2", 113.991));
        products.add(new Product("Product 3", 111.919));
        ctx.put("productList", products);
        ctx.put("math", new MathTool());
        Writer writer = new StringWriter();
        t.merge(ctx, writer);
        System.out.println(writer);
    }
}
public class Product {
    private String name;
    private double price;
    public Product(String aName, double aPrice) {
        name = aName;
        price = aPrice;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public double getPrice() {
        return price;
    }
    public void setPrice(double price) {
        this.price = price;
    }
}
-------------------------------------------------------------------------------------
#set($totalPrice = 0)
#foreach($product in $productList)
  $product.Name    $$product.Price
  #set($totalPrice = $math.add($totalPrice, $product.Price))
#end
Total Price: $$totalPrice
```

velocity-MathTool-OnClass.zip( 876 k)
1.  Velocity MathTool: Add
2.  Velocity MathTool Divide
3.  Velocity MathTool: Maximun
4.  Velocity MathTool Minimum
5.  Velocity MathTool: Multiply
6.  Velocity Math Tool: Power
7.  Velocity Math Tool Random
8.  Velocity MathTool Random Between
9.  Math tool: round to a given integer
10.  Velocity Math Tool Round To Integer
11.  Velocity Math Tool: Subtract
