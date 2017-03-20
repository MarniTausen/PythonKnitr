from PythonKnitr import Knitr

document = Knitr("Python-Knitr Guide", "Marni Tausen")

document.set_options(comment='', warning=False, message=False, background="#BBBBBB",
                     seed=True, seed_num=40)

document.text("To install the package, download the repository and run the setup.py command in the follow in style:", title="Installation")
document.makecodeblock("cat('python setup.py install')", "R")
document.text("""For it to work, it assumes you have R installed. There are some dependencies aswell that need to be installed. Here is a list of the dependencies:

* knitr (https://yihui.name/knitr/)
* rmarkdown (http://rmarkdown.rstudio.com)
* pandoc (http://pandoc.org)

If Rstudio is installed, then most of these dependencies are included.
Currently only supports python 2.7.

""")

document.text("Python-Knitr is a wrapper that produces an R markdown document, by loading R scripts or python scripts, and sets up the document for you and compiles it.", title="Introduction")

document.text("The basic syntax of how to load the package is as follows, and then you initialize a document by creating a Knitr object.")
document.makecodeblock("""from PythonKnitr import Knitr

document = Knitr()
""", "python", echo=True, eval=False)

document.text("The Knitr object has a set of built-in functions which allows you to add text or scripts to the markdown document in different ways. The most simple function is the .text() function, which simply adds text into the document. An example usage shown below:", title="Functions")
document.makecodeblock("document.text('This is an example', title='Example', level=3)", "python",
                       echo=True, eval=False)
document.text("This would produce the following result:\n\n___")
document.text('This is an example', title='Example', level=3)
document.text('\n___\n')
document.text(".text() only has 3 parameters, body (which is required, and the text you are going to add), title, and level. Title is optional and always produces a new section and level is what sets the size of the header, default is 2. The parameter title is included with the other two core functions, .analysis() and .figure().\n")

document.text("The second feature is including an analysis with .analysis()")
document.makecodeblock("""document.analysis('''
x <- rnorm(50)
y <- rnorm(50, mean=x)
summary(lm(y ~ x))
''', title="Linear regression",
description="Linear regression produced by randomly generated data from rnorm",
language="R", display=True, echo=True, level=3)
""", "python", echo=True, eval=False)

document.text("This would produce the following result:\n\n___")
document.analysis('''
x <- rnorm(50)
y <- rnorm(50)
summary(lm(y ~ x))
''', title="Linear regression", description="Linear regression produced by randomly generated data from rnorm", language="R", display=True, echo=True, level=3)
document.text('\n___\n')

document.text(""".analysis() has many parameters, that can be specified. The first and only required parameter is script. This can either be straight code as shown above, or a file with the extension .R or .r. The function by default assumes that the code given is R code. However python code can also be included, by including a file with the extension .py, or by changing the parameter language, and changing it to 'python'. Second it also contains the title, parameter, which produces a new section with the given input. The third parameter is 'description', which allows you to write body text above the analysis outputs.

Next parameter is language, which was described earlier. By default it says 'R', but you can change it python for it to interpret python code instead. Next is display, which is a boolean parameter, which says whether the output from the script should be displayed or not. Finally the last parameter is echo, which tells the program whether or not code it self should be shown.""")

document.text("""\nThe third function is .figure(), which is specifically designed to include figures. .analysis() will also output figures, but does not contain parameters to control the aesthetics of the figures. Figure allows you to add an image file, or you can include an R script which produces a figure.""")

document.makecodeblock("""document.figure('''
reg <- coef(lm(y ~ x))
plot(x, y)
abline(reg[1], reg[2])
''', description = "Plot of the linear regression between variables x and y.",
width=9, height=5)
""", "python", echo=True, eval=False)

document.text("This would produce the following result:\n\n___")
document.figure('''
reg <- coef(lm(y ~ x))
plot(x, y)
abline(reg[1], reg[2])
''', description = "Plot of the linear regression between variables x and y.")
document.text('\n___\n')

document.text(".figure() has the same parameters as .analysis(), but also includes variables for modifying the size of the image, width and height, which are self explanatory.")

document.text("There is another type of function, where you can 'inject' a python script from the main script you are working in, into the document. So you can write a python code, and whatever result you want to display you can inject. Example", title="Inject")

document.makecodeblock("""a = 65
b = 15

document.inject("print a+b", globals(), echo=True)
""", "python", echo=True, eval=False)

document.text("This would produce the following result:\n\n___")
a = 65
b = 15

document.inject("print a+b", globals(), echo=True)
document.text('\n___\n')

document.text("This allows for quick display of results from a python script into the Markdown document. Code given to the function, is executed as is, so anything given to it will run like it would in the script. So for anything to be displayed, the code explicitly needs to print stuff. There is also a mandatory parameter called globals(), which is necessary if you want to access any of namespace in python, from within the class. (If possible, in future I would like to remove this) Next there are the optional parameters, which are the same as for .figure(), .analysis(), where you can write a title, description, and choose the level of the header. Finally there is the echo boolean parameter, where you can specify where the code itself should be displayed or not.")

document.text("When the script is document is done, you want to produce the document. For that you use the .compile() function. This will result in the Markdown document, being saved, and compiled into the desired format. Example:", title="Compiling")
document.makecodeblock('document.compile("README.Rmd", output_type="github")', "python",
                       echo=True, eval=False)
document.text("""This would result in a github markdown document being made, with an addition of a preview html. There are multiple output_types which can be chosen from. Here is a list of all the types.

* html
* github
* word
* md
* pdf

""")

document.text("""There are a functions, which the other functions call specifically 'makecodeblock' and 'save_file'. save_file is very straight forward in that it saves the content generated into a markdown file. However it does not compile or run any of the code included.

Makecodeblock, is the core function that all of the other scripts use. Here you have direct access to how the code chunk from Rmarkdown documents is made. Here are all of the parameters the function has, and the default settings.
""", title="Extra functions")
document.makecodeblock("""makecodeblock(script, lang, echo=False, width=8, height=5, results="show",
              include=True, eval=True)""", 'python', echo=True, eval=False)
document.text("""Most of these are straight forward, but if you want to show code, without it being run, as with this document you can set eval=False.

The last function is 'set_options'. This sets the general options for the document and how the code blocks in the document should be displayed. Here are the parameters and their default settings.
""")

document.makecodeblock("""set_options(comment="##", warning=True, error=True,
            message=True, highlight=True, background="#FFFFFF", size="normalsize",
            seed=False, seed_num=100)""", 'python', echo=True, eval=False)

document.text("""Here is a list of the parameters, and an explanation of what the do. Note, that these parameter only apply for cases where R code is used.

* comment (What kind of symbol or text should be appended in front of each line in the output. Standard default. However for this document is option was set to comment='')
* warning (Whether to display warnings produced by functions. If set to False, then warnings are found on the compilation text instead on the document)
* error (Whether to display error messages on the document. If set to False, then error messages are shown on the compilation text instead)
* message (Whether to display messages from functions on the document. If set to False then messages are shown on the compilation text instead)
* highlight (Whether code should be syntax highlighted or not)
* background (The background color of the code areas. Default is white.)
* size (The text size of code areas. Uses the size names from latex, which are: tiny, scriptsize, footnotesize, small, normalsize, large, Large, huge, Huge. From smallest to largest)
* seed (A boolean whether a seed should be set in the document. This is for cases where randomness is included in the script, and to fix the results you can set a seed. Note this should usually only be done if you have illustrative examples.)
* seed_num (The specfic seed number which is set.)

Note: This document itself was generated using this tool. See README.py to see how this was written.""")


document.compile("README.Rmd", output_type="github")
