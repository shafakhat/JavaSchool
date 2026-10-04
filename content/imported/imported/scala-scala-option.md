---
title: Scala Tutorial - Scala Option
nav: Scala Tutorial - Scala Opt...
description: Option lets us express null value explicitly without the null "hack".
section: Imported - java2s Archive
order: 50086
source: https://www.java2s.com/Tutorials/Java/Scala/0170__Scala_Option.html
---
```java title=Example.java
« Previous
```

- Next »

Option lets us express null value explicitly without the null "hack".

Option is an abstract class and its two concrete subclasses are Some, for when we have a value, and None, when we don't.

## Example

You can see Option, Some, and None in action in the following example, where we create a map of state capitals in the United States:

```java title=Example.java

object Main {
  def main(args: Array[String]) {
     val stateCapitals = Map(
       "Alabama" -> "Montgomery",
       "Alaska"  -> "Juneau",
       "Wyoming" -> "Cheyenne")
     println( "Get the capitals wrapped in Options:" )
     println( "Alabama: " + stateCapitals.get("Alabama") )
     println( "Wyoming: " + stateCapitals.get("Wyoming") )
     println( "Unknown: " + stateCapitals.get("Unknown") )
     println( "Get the capitals themselves out of the Options:" )
     println( "Alabama: " + stateCapitals.get("Alabama").get )
     println( "Wyoming: " + stateCapitals.get("Wyoming").getOrElse("Oops!") )
     println( "Unknown: " + stateCapitals.get("Unknown").getOrElse("Oops2!") )
  }
}
```

## Note

The Map.get method returns an Option[T], where T is String in this case.

By returning an Option, we can't "forget" that we have to verify that something was returned.

If the Option is a Some, Some.get returns the value.

If the Option is actually None, then None.get throws a NoSuchElementException.

getOrElse in the last two println statements returns either the value in the Option, if it is a Some instance, or it returns the argument passed to getOrElse, if it is a None instance.

getOrElse argument behaves as the default return value.

- Next »
- « Previous
