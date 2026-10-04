---
title: Java java.awt.Color
nav: Java java.awt.Color
description: The Color class is used to encapsulate colors in the default sRGB color space or colors in arbitrary color spaces identified by a ColorSpace.
section: Imported - java2s Archive
order: 1002
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorials/Java/java.awt/Color/Java_java_awt_Color.htm
---
In this chapter you will learn:

- Get to know java.awt.Color
- JDK Version for java.awt.Color
- Fields from java.awt.Color
- Constructors from java.awt.Color
- Methods from java.awt.Color

### Description

The Color class is used to encapsulate colors in the default sRGB color space or colors in arbitrary color spaces identified by a ColorSpace.

### Since

### Field

Modifier and Type  Field and Description
---  ---
static Color  black The color black.
static Color  BLACK The color black.
static Color  blue The color blue.
static Color  BLUE The color blue.
static Color  cyan The color cyan.
static Color  CYAN The color cyan.
static Color  DARK_GRAY The color dark gray.
static Color  darkGray The color dark gray.
static Color  gray The color gray.
static Color  GRAY The color gray.
static Color  green The color green.
static Color  GREEN The color green.
static Color  LIGHT_GRAY The color light gray.
static Color  lightGray The color light gray.
static Color  magenta The color magenta.
static Color  MAGENTA The color magenta.
static Color  orange The color orange.
static Color  ORANGE The color orange.
static Color  pink The color pink.
static Color  PINK The color pink.
static Color  red The color red.
static Color  RED The color red.
static Color  white The color white.
static Color  WHITE The color white.
static Color  yellow The color yellow.
static Color  YELLOW The color yellow.

### Constructor

Constructor and Description
---
Color(ColorSpace cspace, float[] components, float alpha) Creates a color in the specified ColorSpace with the color components specified in the float array and the specified alpha.
Color(float r, float g, float b) Creates an opaque sRGB color with the specified red, green, and blue values in the range (0.0 - 1.0).
Color(float r, float g, float b, float a) Creates an sRGB color with the specified red, green, blue, and alpha values in the range (0.0 - 1.0).
Color(int rgb) Creates an opaque sRGB color with the specified combined RGB value consisting of the red component in bits 16-23, the green component in bits 8-15, and the blue component in bits 0-7.
Color(int rgba, boolean hasalpha) Creates an sRGB color with the specified combined RGBA value consisting of the alpha component in bits 24-31, the red component in bits 16-23, the green component in bits 8-15, and the blue component in bits 0-7.
Color(int r, int g, int b) Creates an opaque sRGB color with the specified red, green, and blue values in the range (0 - 255).
Color(int r, int g, int b, int a) Creates an sRGB color with the specified red, green, blue, and alpha values in the range (0 - 255).

### Method

Modifier and Type  Method and Description
---  ---
Color  brighter() Creates a new Color that is a brighter version of this Color .
PaintContext  createContext(ColorModel cm, Rectangle r, Rectangle2D r2d, AffineTransform xform, RenderingHints hints) Creates and returns a PaintContext used to generate a solid color field pattern.
Color  darker() Creates a new Color that is a darker version of this Color .
static Color  decode(String nm) Converts a String to an integer and returns the specified opaque Color .
boolean  equals(Object obj) Determines whether another object is equal to this Color .
int  getAlpha() Returns the alpha component in the range 0-255.
int  getBlue() Returns the blue component in the range 0-255 in the default sRGB space.
static Color  getColor(String nm) Finds a color in the system properties.
static Color  getColor(String nm, Color v) Finds a color in the system properties.
static Color  getColor(String nm, int v) Finds a color in the system properties.
float[]  getColorComponents(ColorSpace cspace, float[] compArray) Returns a float array containing only the color components of the Color in the ColorSpace specified by the cspace parameter.
float[]  getColorComponents(float[] compArray) Returns a float array containing only the color components of the Color , in the ColorSpace of the Color .
ColorSpace  getColorSpace() Returns the ColorSpace of this Color .
float[]  getComponents(ColorSpace cspace, float[] compArray) Returns a float array containing the color and alpha components of the Color , in the ColorSpace specified by the cspace parameter.
float[]  getComponents(float[] compArray) Returns a float array containing the color and alpha components of the Color , in the ColorSpace of the Color .
int  getGreen() Returns the green component in the range 0-255 in the default sRGB space.
static Color  getHSBColor(float h, float s, float b) Creates a Color object based on the specified values for the HSB color model.
int  getRed() Returns the red component in the range 0-255 in the default sRGB space.
int  getRGB() Returns the RGB value representing the color in the default sRGB ColorModel .
float[]  getRGBColorComponents(float[] compArray) Returns a float array containing only the color components of the Color , in the default sRGB color space.
float[]  getRGBComponents(float[] compArray) Returns a float array containing the color and alpha components of the Color , as represented in the default sRGB color space.
int  getTransparency() Returns the transparency mode for this Color .
int  hashCode() Computes the hash code for this Color .
static int  HSBtoRGB(float hue, float saturation, float brightness) Converts the components of a color, as specified by the HSB model, to an equivalent set of values for the default RGB model.
static float[]  RGBtoHSB(int r, int g, int b, float[] hsbvals) Converts the components of a color, as specified by the default RGB model, to an equivalent set of values for hue, saturation, and brightness that are the three components of the HSB model.
String  toString() Returns a string representation of this Color .

#### Next chapter...

What you will learn in the next chapter:

- Get to know Color.black
- Syntax for Color.black
- Example - Color.black
