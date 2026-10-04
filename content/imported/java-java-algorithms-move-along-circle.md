---
title: Java Algorithms Move along circle
nav: Java Algorithms Move along...
description: @Override//fromwww.java2s.compublicvoid start(Stage primaryStage) {
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/20210102113326/http://www.java2s.com/ref/java/java-algorithms-move-along-circle.html
---
## Description

```java title=Example.java
import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.text.Text;
import javafx.scene.paint.Color;
import javafx.scene.input.MouseButton;
publicclass Main extends Application {
  @Overridepublicvoid start(Stage primaryStage) {
    finaldouble WIDTH = 500.0;
    finaldouble HEIGHT = 500.0;
    finaldouble RADIUS = 200.0;
    Circle[] points = new Circle[3];
    Line[] lines = newLine[3];
    Text[] labels = newText[3];
    Pane pane = new Pane();
    Circle circle = new Circle(WIDTH / 2, HEIGHT / 2, RADIUS);
    circle.setFill(Color.WHITE);
    circle.setStroke(Color.BLACK);
    pane.getChildren().add(circle);
    // create three points around the circle represented by Circle objectsfor (int i = 0; i < 3; i++) {
      Circle point = new Circle(RADIUS / 20);
      double randomAngle = Math.random() * 2 * Math.PI;
      double x = circle.getCenterX() + RADIUS * Math.cos(randomAngle);
      double y = circle.getCenterY() + RADIUS * Math.sin(randomAngle);
      point.setCenterX(x);
      point.setCenterY(y);
      point.setOnMouseDragged(e -> {
        if (e.getButton().equals(MouseButton.PRIMARY)) {
          double angle = Math.atan2(e.getY() - circle.getCenterY(), e.getX() - circle.getCenterX());
          Circle c = (Circle)e.getSource();
          c.setCenterX(circle.getCenterX() + RADIUS * Math.cos(angle));
          c.setCenterY(circle.getCenterY() + RADIUS * Math.sin(angle));
          angle = getAngle(lines[1], lines[2], lines[0]);
          labels[0].setText(String.format("%.5f", angle));
          angle = getAngle(lines[2], lines[1], lines[0]);
          labels[1].setText(String.format("%.5f", angle));
          angle = getAngle(lines[0], lines[2], lines[1]);
          labels[2].setText(String.format("%.5f", angle));
        }
      });
      points[i] = point;
    }
    // create three lines connecting the pointsfor (int i = 0; i < 3; i++) {
      int next = i == 2 ? 0 : i + 1;
      Line line = newLine();
      line.startXProperty().bind(points[i].centerXProperty());
      line.startYProperty().bind(points[i].centerYProperty());
      line.endXProperty().bind(points[next].centerXProperty());
      line.endYProperty().bind(points[next].centerYProperty());
      lines[i] = line;
    }
    // create three Text objects to display the anglesfor (int i = 0; i < 3; i++) {
      Text text = newText();
      text.xProperty().bind(points[i].centerXProperty());
      text.yProperty().bind(points[i].centerYProperty().subtract(RADIUS / 20));
      labels[i] = text;
    }
    pane.getChildren().addAll(points[0], points[1], points[2],
      lines[0], lines[1], lines[2], labels[0], labels[1], labels[2]);
    Scene scene = new Scene(pane, WIDTH, HEIGHT);
    primaryStage.setTitle("JavaSchool");
    primaryStage.setScene(scene);
    primaryStage.show();
  }
  publicstaticdouble getAngle(Line x, Line y, Line z) {
    double a = distance(x);
    double b = distance(y);
    double c = distance(z);
    returnMath.toDegrees(Math.acos((a * a - b * b - c * c) / (-2 * b * c)));
  }
  publicstaticdouble distance(Line line) {
    double x1 = line.getStartX();
    double y1 = line.getStartY();
    double x2 = line.getEndX();
    double y2 = line.getEndY();
    returnMath.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
  }
  publicstaticvoid main(String[] args) {
    launch(args);
  }
}
```

PreviousNext

## Related
