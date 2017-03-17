Python-Knitr Guide
================
Marni Tausen
17/03/2017 - 14:45:16

-   [Installation](#installation)
-   [Introduction](#introduction)
-   [Functions](#functions)
-   [Example](#example)
-   [Linear regression](#linear-regression)
-   [Inject](#inject)

Installation
------------

To install the package, download the repository and run the setup.py command in the follow in style:

    python setup.py install

For it to work, it assumes you have R installed. The R package Knitr is also a requirement. The python script is version 2.7. For most compilations pandoc is also required. If Rstudio is installed on the computer then most of these will be included.

Introduction
------------

Python-Knitr is a wrapper that produces an R markdown document, by loading R scripts or python scripts, and sets up the document for you and compiles it.

The basic syntax of how to load the package is as follows, and then you initialize a document by creating a Knitr object.

``` python
from PythonKnitr import Knitr

document = Knitr()
```

Functions
---------

The Knitr object has a set of built-in functions which allows you to add text or scripts to the markdown document in different ways. The most simple function is the .text() function, which simply adds text into the document. An example usage shown below:

``` python
document.text('This is an example', title='Example')
```

This would produce the following result:

------------------------------------------------------------------------

Example
-------

This is an example

------------------------------------------------------------------------

.text() only has 2 parameters, body (which is required, and the text you are going to add) and title. Title is optional and always produces a new section. The parameter title is included with the other two core functions, .analysis() and .figure().

The second feature is including an analysis with .analysis()

``` python
document.analysis('''
x <- rnorm(50)
y <- rnorm(50, mean=x)
summary(lm(y ~ x))
''', title="Linear regression",
description="Linear regression produced by randomly generated data from rnorm",
language="R", display=True, echo=True)
```

This would produce the following result:

------------------------------------------------------------------------

Linear regression
-----------------

Linear regression produced by randomly generated data from rnorm

``` r
x <- rnorm(50)
y <- rnorm(50)
summary(lm(y ~ x))
```


    Call:
    lm(formula = y ~ x)

    Residuals:
         Min       1Q   Median       3Q      Max 
    -1.88478 -0.52608  0.06003  0.61189  1.85794 

    Coefficients:
                Estimate Std. Error t value Pr(>|t|)
    (Intercept)   0.1146     0.1330   0.862    0.393
    x            -0.2081     0.1260  -1.651    0.105

    Residual standard error: 0.9404 on 48 degrees of freedom
    Multiple R-squared:  0.05372,   Adjusted R-squared:  0.03401 
    F-statistic: 2.725 on 1 and 48 DF,  p-value: 0.1053

------------------------------------------------------------------------

.analysis() has many parameters, that can be specified. The first and only required parameter is script. This can either be straight code as shown above, or a file with the extension .R or .r. The function by default assumes that the code given is R code. However python code can also be included, by including a file with the extension .py, or by changing the parameter language, and changing it to 'python'. Second it also contains the title, parameter, which produces a new section with the given input. The third parameter is 'description', which allows you to write body text above the analysis outputs.

Next parameter is language, which was described earlier. By default it says 'R', but you can change it python for it to interpret python code instead. Next is display, which is a boolean parameter, which says whether the output from the script should be displayed or not. Finally the last parameter is echo, which tells the program whether or not code it self should be shown.

The third function is .figure(), which is specifically designed to include figures. .analysis() will also output figures, but does not contain parameters to control the aesthetics of the figures. Figure allows you to add an image file, or you can include an R script which produces a figure.

``` python
document.figure('''
reg <- coef(lm(y ~ x))
plot(x, y)
abline(reg[1], reg[2])
''', description = "Plot of the linear regression between variables x and y.",
width=9, height=5)
```

This would produce the following result:

------------------------------------------------------------------------

Plot of the linear regression between variables x and y. ![](README_files/figure-markdown_github/unnamed-chunk-8-1.png)

------------------------------------------------------------------------

.figure() has the same parameters as .analysis(), but also includes variables for modifying the size of the image, width and height, which are self explanatory.

Inject
------

There is another type of function, where you can 'inject' a python script from the environment you are working into the document. So you can write a python code, and whatever result you want to display you can inject. Example

``` python
a = 65
b = 15

document.inject("print a+b", globals(), echo=True)
```

This would produce the following result:

------------------------------------------------------------------------

``` python
print a+b
```

    80

------------------------------------------------------------------------
