---
title: Java Arithmetic Operator Body Mass Index Calculator(BMI)
nav: Java Arithmetic Operator B...
description: System.out.print("BMI calculator: 1 for imperial, 2 for metric: ");
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/ref/java/java-arithmetic-operator-body-mass-index-calculatorbmi.html
---
## Question

We would like to calculate Body Mass Index Calculator(BMI)

The formulas for calculating BMI are

```java title=Example.java
for imperial
         weightInPounds times  703
BMI = ------------------------------------
      heightInInches times heightInInches
for metric
               weight In Kilograms
BMI = ------------------------------------
      heightInMeters times heightInMeters
java title=Example.java
import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int weight;
    int height;
    int bmi;
    System.out.print("Enter your weight in kilograms: ");
    weight = input.nextInt();
    System.out.print("Enter your height in meters: ");
    height = input.nextInt();
    bmi = weight / (height * height);
    System.out.printf("Your BMI = %d%n", bmi);
    System.out.println("BMI VALUES");
    System.out.println("Underweight: less then 18.5");
    System.out.println("Normal:      between 18.5 and 24.9");
    System.out.println("Overweight:  between 25 and 29.9");
    System.out.println("Obese:       30 or greater");
    input.close();
  }
}
```

## Note

To support two systems:imperial and metric

```java title=Example.java
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        double weight, height, bmi;
        int choice;
        System.out.print("BMI calculator: 1 for imperial, 2 for metric: ");
        choice = input.nextInt(); System.out.printf("Input weight in %s: ",
                (choice == 1) ? "pounds" : "kilograms");
        weight = input.nextDouble();
        System.out.printf("Input height in %s: ",
                (choice == 1) ? "inches(ft * 12 * in)" : "metres");
        height = input.nextDouble();
        bmi = (choice == 1) ? calculateImperial(weight, height) : calculateMetric(weight, height);
        System.out.printf("Your BMI : %.1f\n", bmi);
        printBmiTable();
    }
    // calculate using imperial measures private static double calculateImperial(double weight, double height){
        return ((weight * 703) / (height * height));
    }
    // calculate using metric measures private static double calculateMetric(double weight, double height){
        return weight / (height * height);
    }
    // print BMI information from Department of Health and Human Services / // National Institutes of Health. private static void printBmiTable(){
        System.out.printf("BMI VALUES:");
        System.out.println("Underweight: less than 18.5");
        System.out.println("Normal:      between 18.5 and 24.9");
        System.out.println("Overweight:  between 25 and 29.9");
        System.out.println("Obese:       30 or greater");
    }
}
```

PreviousNext

## Related

- Java Operator Precedence
- Java Operator Precedence Question 1
- Java two's complement Integer in binary form
- Java Arithmetic Operator calculate area and perimeter of a circle
- Java Arithmetic Operator calculate area and perimeter of a rectangle
