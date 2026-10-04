---
title: Composition with public objects
nav: Composition with public ob...
description: Imported from the java2s.com archive: Composition with public objects
section: Imported - java2s Archive
order: 1125
source: https://web.archive.org/web/20140829080554/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Compositionwithpublicobjects.htm
---
```java title=Example.java
class Engine {
  public void start() {}
  public void rev() {}
  public void stop() {}
}
class Wheel {
  public void inflate(int psi) {}
}
class Window {
  public void rollup() {}
  public void rolldown() {}
}
class Door {
  public Window window = new Window();
  public void open() {}
  public void close() {}
}
class Car {
  public Engine engine = new Engine();
  public Wheel[] wheel = new Wheel[4];
  public Door
    left = new Door(),
    right = new Door(); // 2-door
  public Car() {
    for(int i = 0; i < 4; i++)
      wheel[i] = new Wheel();
  }
}
public class MainClass{
  public static void main(String[] args) {
    Car car = new Car();
    car.left.window.rollup();
    car.wheel[0].inflate(72);
  }
}
```

| 5.25.1. | Access Control: four access control modifiers |
|---|---|
| 5.25.2. | Class Access Control Modifiers |
| 5.25.3. | Using Access Attributes |
| 5.25.4. | Class Member Access Matrix |
| 5.25.5. | Specifying Access Attributes |
| 5.25.6. | The public Book class |
| 5.25.7. | Default access level |
| 5.25.8. | Class Member Access Control Modifiers |
| 5.25.9. | Composition with public objects |
| 5.25.10. | The protected keyword |
| 5.25.11. | Private Override |
| 5.25.12. | Understand the effects of public and private access |
| 5.25.13. | In a class hierarchy, private members remain private to their class. |
| 5.25.14. | A Superclass Variable Can Reference a Subclass Object |
| 5.25.15. | Create a Singleton Object |
