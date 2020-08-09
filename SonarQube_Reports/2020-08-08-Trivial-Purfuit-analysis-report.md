# Code analysis
## Trivial-Purfuit 
#### Version not provided 

**By: Sam Pagano**

*Date: 2020-08-08*

## Introduction
This document contains results of the code analysis of Trivial-Purfuit



## Configuration

- Quality Profiles
    - Names: Sonar way [CSS]; Sonar way [JavaScript]; Sonar way [Python]; Sonar way [TypeScript]; Sonar way [HTML]; 
    - Files: AXPOxSLkoGHM501Hzcj6.json; AXPOxSTHoGHM501Hzcop.json; AXPOxSa3oGHM501Hzcwe.json; AXPOxS-ooGHM501HzdSl.json; AXPOxSr9oGHM501HzdHh.json; 
 - Quality Gate
    - Name: Sonar way
    - File: Sonar way.xml

## Synthesis
Quality Gate | Reliability | Security | Maintainability | Coverage | Duplications
:---:|:---:|:---:|:---:|:---:|:---:
OK | B | E | A | 0.0 % | 0.0 %

## Metrics

\ | Cyclomatic Complexity | Cognitive Complexity | Lines of code per file | Coverage | Comment density (%) | Duplication (%)
:---|:---:|:---:|:---:|:---:|:---:|:---:
Min | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0
Max | 121.0 | 115.0 | 545.0 | 0.0 | 100.0 | 0.0

## Volume

Language|Number
---|---
CSS|245
Python|746
HTML|121
Total|1112


## Issues count by severity and types

Type|Severity|Number
---|---|---
VULNERABILITY|BLOCKER|1
VULNERABILITY|CRITICAL|0
VULNERABILITY|MAJOR|0
VULNERABILITY|MINOR|0
VULNERABILITY|INFO|0
BUG|BLOCKER|0
BUG|CRITICAL|0
BUG|MAJOR|0
BUG|MINOR|3
BUG|INFO|0
CODE_SMELL|BLOCKER|0
CODE_SMELL|CRITICAL|9
CODE_SMELL|MAJOR|14
CODE_SMELL|MINOR|19
CODE_SMELL|INFO|0
SECURITY_HOTSPOT|BLOCKER|0
SECURITY_HOTSPOT|CRITICAL|0
SECURITY_HOTSPOT|MAJOR|0
SECURITY_HOTSPOT|MINOR|0
SECURITY_HOTSPOT|INFO|0


## Issues
Name|Description|Type|Severity|Number
---|---|---|---|---
"<strong>" and "<em>" tags should be used|The &lt;strong&gt;/&lt;b&gt; and &lt;em&gt;/&lt;i&gt; tags have exactly the same effect in most <br /> web browsers, but there is a fundamental difference between them: &lt;strong&gt; and &lt;em&gt; have a semantic meaning <br /> whereas &lt;b&gt; and &lt;i&gt; only convey styling information like CSS.  <br /> While &lt;b&gt; can have simply no effect on a some devices with limited display or when a screen reader software is used by a blind <br /> person, &lt;strong&gt; will: <br />  <br />    Display the text bold in normal browsers  <br />    Speak with lower tone when using a screen reader such as Jaws  <br />  <br /> Consequently: <br />  <br />    in order to convey semantics, the &lt;b&gt; and &lt;i&gt; tags shall never be used,  <br />    in order to convey styling information, the &lt;b&gt; and &lt;i&gt; should be avoided and CSS should be used instead. <br />    <br />  <br /> Noncompliant Code Example <br />  <br /> &lt;i&gt;car&lt;/i&gt;             &lt;!-- Noncompliant --&gt; <br /> &lt;b&gt;train&lt;/b&gt;         &lt;!-- Noncompliant --&gt; <br />  <br /> Compliant Solution <br />  <br /> &lt;em&gt;car&lt;/em&gt; <br /> &lt;strong&gt;train&lt;/strong&gt; <br />  <br /> Exceptions <br /> This rule is relaxed in case of icon <br /> fonts usage. <br />  <br /> &lt;i class="..." aria-hidden="true" /&gt;    &lt;!-- Compliant icon fonts usage --&gt; <br /> |BUG|MINOR|3
Functions and methods should not be empty|There are several reasons for a function or a method not to have a body: <br />  <br />    It is an unintentional omission, and should be fixed to prevent an unexpected behavior in production.  <br />    It is not yet, or never will be, supported. In this case an exception should be thrown.  <br />    The method is an intentionally-blank override. In this case a nested comment should explain the reason for the blank override.  <br />  <br /> Noncompliant Code Example <br />  <br /> def myfunc1(foo="Noncompliant"): <br />     pass <br />  <br /> class MyClass: <br />     def mymethod1(self, foo="Noncompliant"): <br />         pass <br />  <br />  <br /> Compliant Solution <br />  <br /> def myfunc1(): <br />     pass  # comment explaining why this function is empty <br />  <br /> def myfunc2(): <br />     raise NotImplementedError() <br />  <br /> def myfunc3(): <br />     """ <br />     Docstring explaining why this function is empty. <br />     """ <br />  <br /> class MyClass: <br />     def mymethod1(self): <br />         pass  # comment explaining why this function is empty <br />  <br />     def mymethod2(self): <br />         raise NotImplementedError() <br />  <br />     def mymethod3(self): <br />         """ <br />         Docstring explaining why this method is empty. Note that this is not recommended for classes <br />         which are meant to be subclassed. <br />         """ <br />  <br /> Exceptions <br /> No issue will be raised when the empty method is abstract and meant to be overriden in a subclass, i.e. it is decorated with <br /> abc.abstractmethod, abc.abstractstaticmethod, abc.abstractclassmethod or abc.abstractproperty. <br /> Note however that these methods should normally have a docstring explaining how subclasses should implement these methods. <br />  <br /> import abc <br />  <br /> class MyAbstractClass(abc.ABC): <br />     @abc.abstractproperty <br />     def myproperty(self): <br />         pass <br />  <br />     @abc.abstractclassmethod <br />     def myclassmethod(cls): <br />         pass <br />  <br />     @abc.abstractmethod <br />     def mymethod(self): <br />         pass <br />  <br />     @abc.abstractstaticmethod <br />     def mystaticmethod(): <br />         pass <br /> |CODE_SMELL|CRITICAL|4
String literals should not be duplicated|Duplicated string literals make the process of refactoring error-prone, since you must be sure to update all occurrences. <br /> On the other hand, constants can be referenced from many places, but only need to be updated in a single place. <br /> Noncompliant Code Example <br /> With the default threshold of 3: <br />  <br /> def run(): <br />     prepare("this is a duplicate")  # Noncompliant - "this is a duplicate" is duplicated 3 times <br />     execute("this is a duplicate") <br />     release("this is a duplicate") <br />  <br /> Compliant Solution <br />  <br /> ACTION_1 = "action1" <br />  <br /> def run(): <br />     prepare(ACTION_1) <br />     execute(ACTION_1) <br />     release(ACTION_1) <br />  <br /> Exceptions <br /> No issue will be raised on: <br />  <br />    duplicated string in decorators  <br />    strings with less than 5 characters  <br />    strings with only letters, numbers and underscores  <br />  <br />  <br /> @app.route("/api/users/", methods=['GET', 'POST', 'PUT']) <br /> def users(): <br />     pass <br />  <br /> @app.route("/api/projects/", methods=['GET', 'POST', 'PUT'])  # Compliant <br /> def projects(): <br />     pass <br /> |CODE_SMELL|CRITICAL|3
Cognitive Complexity of functions should not be too high|Cognitive Complexity is a measure of how hard the control flow of a function is to understand. Functions with high Cognitive Complexity will be <br /> difficult to maintain. <br /> See <br />  <br />    Cognitive Complexity  <br /> |CODE_SMELL|CRITICAL|2
"aria-label" or "aria-labelledby" attributes should be used to differentiate similar elements|If a page contains multiple &lt;nav&gt;&nbsp;or &lt;aside&gt; elements, each one should have an aria-label <br /> or aria-labelledby attribute so that they can be differentiated. The same rule applies when multiple elements have <br /> a&nbsp;role attribute with the same "landmark" value. <br /> Landmark roles are: banner, complementary, contentinfo, form, main, <br /> navigation, search, application.&nbsp; <br /> The use of ARIA markup helps users of&nbsp;screen readers navigate across blocks of content. For example it makes groups of links easier to locate <br /> or skip. <br /> Noncompliant Code Example <br /> Multiple &lt;nav&gt; element <br />  <br /> &lt;nav&gt; &lt;!-- Noncompliant --&gt; <br />     &lt;ul&gt; <br />         &lt;li&gt;A list of navigation links&lt;/li&gt; <br />     &lt;/ul&gt; <br /> &lt;/nav&gt; <br />  <br /> &lt;article&gt; <br />     &lt;nav&gt; &lt;!-- Noncompliant --&gt; <br />         Another list of navigation links <br />     &lt;/nav&gt; <br /> &lt;/article&gt; <br />  <br /> Repeated "landmark" role "navigation" <br />  <br /> &lt;div id="mainnav" role="navigation"&gt; &lt;!-- Noncompliant --&gt; <br />     &lt;h2 id="mainnavheading"&gt;Site Navigation&lt;/h2&gt; <br />     &lt;ul&gt; <br />        &lt;li&gt;List of links&lt;/li&gt; <br />     &lt;/ul&gt; <br /> &lt;/div&gt; <br /> &lt;div id="secondarynav" role="navigation"&gt; &lt;!-- Noncompliant --&gt; <br />     &lt;h2 id="secondarynavheading"&gt;Related links&lt;/h2&gt; <br />     &lt;ul&gt; <br />        &lt;li&gt;List of links&lt;/li&gt; <br />     &lt;/ul&gt; <br /> &lt;/div&gt; <br />  <br /> Compliant Solution <br />  <br /> &lt;nav aria-label="Site menu"&gt; <br />     &lt;ul&gt; <br />         &lt;li&gt;A list of navigation links&lt;/li&gt; <br />     &lt;/ul&gt; <br /> &lt;/nav&gt; <br />  <br /> &lt;article&gt; <br />     &lt;nav aria-label="Related links"&gt; <br />         Another list of navigation links <br />     &lt;/nav&gt; <br /> &lt;/article&gt; <br />  <br />  <br /> &lt;div id="mainnav" role="navigation" aria-labelledby="mainnavheading"&gt; <br />     &lt;h2 id="mainnavheading"&gt;Site Navigation&lt;/h2&gt; <br />     &lt;ul&gt; <br />        &lt;li&gt;List of links&lt;/li&gt; <br />     &lt;/ul&gt; <br /> &lt;/div&gt; <br /> &lt;div id="secondarynav" role="navigation" aria-labelledby="secondarynavheading"&gt; <br />     &lt;h2 id="secondarynavheading"&gt;Related links&lt;/h2&gt; <br />     &lt;ul&gt; <br />        &lt;li&gt;List of links&lt;/li&gt; <br />     &lt;/ul&gt; <br /> &lt;/div&gt; <br />  <br /> See <br />  <br />    WCAG2, ARIA11 - Using ARIA landmarks to identify regions of a page  <br />    WCAG2, H97 - Grouping related links using the nav element  <br />    WCAG2 <br />   1.3.1 Info and Relationships  <br /> |CODE_SMELL|MAJOR|6
Collapsible "if" statements should be merged|Merging collapsible if statements increases the code's readability. <br /> Noncompliant Code Example <br />  <br /> if condition1: <br />     if condition2: <br />         # ... <br />  <br /> Compliant Solution <br />  <br /> if condition1 and condition2: <br />     # ... <br /> |CODE_SMELL|MAJOR|1
"Exception" and "BaseException" should not be raised|Raising instances of Exception and BaseException will have a negative impact on any code trying <br /> to catch these exceptions. <br /> First, the only way to handle differently multiple Exceptions is to check their message, which is error-prone and difficult to maintain. <br /> What's more, it becomes difficult to catch only your exception. The best practice is to catch only exceptions which require a specific handling. <br /> When you raise Exception or BaseException in a function the caller will have to add an except Exception or <br /> except BaseException and re-raise all exceptions which were unintentionally caught. This can create tricky bugs when the caller forgets <br /> to re-raise exceptions such as SystemExit and the software cannot be stopped. <br /> It is recommended to either: <br />  <br />    raise a more specific Built-in exception when one matches. For example <br />   TypeError should be raised when the type of a parameter is not the one expected.  <br />    create a custom exception class deriving from Exception or one of its subclasses. A common practice for libraries is to have one <br />   custom root exception class from which every other custom exception class inherits. It enables other projects using this library to catch all errors <br />   coming from the library with a single "except" statement  <br />  <br /> This rule raises an issue when Exception or BaseException are raised. <br /> Noncompliant Code Example <br />  <br /> def process1(): <br />     raise BaseException("Wrong user input for field X")  # Noncompliant <br />  <br /> def process2(): <br />     raise BaseException("Wrong configuration")  # Noncompliant <br />  <br /> def process3(param): <br />     if not isinstance(param, int): <br />         raise Exception("param should be an integer")  # Noncompliant <br />  <br /> def caller(): <br />     try: <br />          process1() <br />          process2() <br />          process3() <br />     except BaseException as e: <br />         if e.args[0] == "Wrong user input for field X": <br />             # process error <br />             pass <br />         elif e.args[0] == "Wrong configuration": <br />             # process error <br />             pass <br />         else: <br />             # re-raise other exceptions <br />             raise <br />  <br /> Compliant Solution <br />  <br /> class MyProjectError(Exception): <br />     """Exception class from which every exception in this library will derive. <br />          It enables other projects using this library to catch all errors coming <br />          from the library with a single "except" statement <br />     """ <br />     pass <br />  <br /> class BadUserInputError(MyProjectError): <br />     """A specific error""" <br />     pass <br />  <br /> class ConfigurationError(MyProjectError): <br />     """A specific error""" <br />     pass <br />  <br /> def process1(): <br />     raise BadUserInputError("Wrong user input for field X") <br />  <br /> def process2(): <br />     raise ConfigurationError("Wrong configuration") <br />  <br /> def process3(param): <br />     if not isinstance(param, int): <br />         raise TypeError("param should be an integer") <br />  <br /> def caller(): <br />     try: <br />          process1() <br />          process2() <br />          process3() <br />     except BadUserInputError as e: <br />         # process error <br />         pass <br />     except ConfigurationError as e: <br />         # process error <br />         pass <br />  <br /> See <br />  <br />    PEP 352  Required Superclass for Exceptions <br />    <br />    Python Documentation - Built-in exceptions  <br />    MITRE, CWE-397 - Declaration of Throws for Generic Exception  <br />    CERT, ERR07-J. - Do not throw RuntimeException, Exception, or Throwable <br />    <br />  <br /> See <br />  <br />    MITRE, CWE-397 - Declaration of Throws for Generic Exception  <br />    CERT, ERR07-J. - Do not throw RuntimeException, Exception, or Throwable <br />    <br /> |CODE_SMELL|MAJOR|5
Sections of code should not be commented out|Programmers should not comment out code as it bloats programs and reduces readability. <br /> Unused code should be deleted and can be retrieved from source control history if required.|CODE_SMELL|MAJOR|1
A field should not duplicate the name of its containing class|It's confusing to have a class member with the same name (case differences aside) as its enclosing class. This is particularly so when you consider <br /> the common practice of naming a class instance for the class itself. <br /> Best practice dictates that any field or member with the same name as the enclosing class be renamed to be more descriptive of the particular <br /> aspect of the class it represents or holds. <br /> Noncompliant Code Example <br />  <br /> class Foo: <br />   foo = '' <br />  <br />   def getFoo(self): <br />     ... <br />  <br /> foo = Foo() <br /> foo.getFoo() # what does this return? <br />  <br /> Compliant Solution <br />  <br /> class Foo: <br />   name = '' <br />  <br />   def getName(self): <br />     ... <br />  <br /> foo = Foo() <br /> foo.getName() <br /> |CODE_SMELL|MAJOR|1
Class names should comply with a naming convention|Shared coding conventions allow teams to collaborate effectively. This rule allows to check that all class names match a provided regular <br /> expression. <br /> Noncompliant Code Example <br /> With default provided regular expression ^[A-Z][a-zA-Z0-9]*$: <br />  <br /> class myClass: <br />    ... <br />  <br /> Compliant Solution <br />  <br /> class MyClass: <br />    ... <br /> |CODE_SMELL|MINOR|2
Local variable and function parameter names should comply with a naming convention|Shared naming conventions allow teams to collaborate effectively. This rule raises an issue when a local variable or function parameter name does <br /> not match the provided regular expression. <br /> Exceptions <br /> Loop counters are ignored by this rule. <br />  <br /> for i in range(limit):  # Compliant <br />     print(i) <br /> |CODE_SMELL|MINOR|8
Unused local variables should be removed|If a local variable is declared but not used, it is dead code and should be removed. Doing so will improve maintainability because developers will <br /> not wonder what the variable is used for. <br /> Noncompliant Code Example <br />  <br /> def hello(name): <br />     message = "Hello " + name # Noncompliant <br />     print(name) <br /> for i in range(10): <br />     foo() <br />  <br /> Compliant Solution <br />  <br /> def hello(name): <br />     message = "Hello " + name <br />     print(message) <br /> for _ in range(10): <br />     foo() <br />  <br /> Exceptions <br /> _ as well as tuples will not raise an issue for this rule. The following examples are compliant: <br />  <br /> for _ in range(10): <br />     do_something() <br /> username, login, password = auth <br /> do_something_else(username, login) <br /> |CODE_SMELL|MINOR|4
Jump statements should not be redundant|Jump statements, such as return, break and continue let you change the default flow of program execution, <br /> but jump statements that direct the control flow to the original direction are just a waste of keystrokes. <br /> Noncompliant Code Example <br />  <br /> def redundant_jump(x): <br />     if x == 1: <br />         print(True) <br />         return  # NonCompliant <br />  <br /> Compliant Solution <br />  <br /> def redundant_jump(x): <br />     if x == 1: <br />         print(True) <br />  <br /> Exceptions <br />  <br />    No issue is raised if the jump statement is the only statement of a statement suite:  <br />  <br />  <br /> def my_function(x): <br />     if x &gt; 5: <br />         do_something() <br />     elif x == 0: <br />         return # ok even it could be changed to "pass" <br />     else: <br />         do_something_else() <br />  <br />  <br />    No issue is raised for return None because this was certainly done on purpose to be explicit that a function is really returning <br />   None.  <br /> |CODE_SMELL|MINOR|5
Links with "target=_blank" should prevent phishing attacks|When a link opens a URL in a new tab with target="_blank", it is very simple for the opened page to change the location <br /> of the original page because the JavaScript variable window.opener is not null and thus "window.opener.location <br /> can be set by the opened page. This exposes the user to very simple phishing attacks. <br /> Imagine a link posted on a comment of a popular web site (say: http://petssocialnetwork.io/) that opens <br /> a new tab that changes the URL of the original page to http://petssocialnetwork-pishing.io/. On <br /> "http://petssocialnetwork-pishing.io/" you land at a fake login page similar to the one at "http://petssocialnetwork.io/" but controlled by the hacker <br /> and asking the user to log in again, pretending that the session just timed-out. <br /> To prevent pages from abusing window.opener, use rel=noopener on &lt;a href=&gt; to force its value to be <br /> null on the opened pages. With this in place, window.opener is null in Chrome 49+, Opera 36+, Firefox 52+, <br /> Desktop Safari 10.1+, and iOS Safari 10.3+. For older browsers, use "noreferrer". Cumulatively, rel="noopener noreferrer" is the safest <br /> way to mitigate this vulnerability. <br /> Noncompliant Code Example <br />  <br /> &lt;a href="http://dangerouswebsite.com" target="_blank"&gt; &lt;!-- Noncompliant; "window.opener" will be not null on the new tab/window and can be changed by http://dangerouswebsite.com --&gt; <br />  <br /> &lt;a href="http://dangerouswebsite.com" target="_blank" rel="noopener"&gt; &lt;!-- Noncompliant; will not prevent the attack on old browsers --&gt; <br />  <br /> &lt;a href="{{variable}}" target="_blank" rel="noopener"&gt; &lt;!-- Noncompliant  --&gt; <br />  <br /> Compliant Solution <br />  <br /> &lt;a href="http://dangerouswebsite.com" target="_blank" rel="noopener noreferrer"&gt; &lt;!-- Compliant --&gt; <br />  <br /> Exceptions <br /> No Issue will be raised when href contains a hardcoded relative url as there it has less chances of being vulnerable. An url is <br /> considered hardcoded and relative if it doesn't start with http:// or https://, and if it does not contain any of the <br /> characters {}$()[] <br />  <br /> &lt;a href="internal.html" target="_blank" &gt; &lt;!-- Compliant --&gt; <br />  <br /> See <br />  * https://mathiasbynens.github.io/rel-noopener/|VULNERABILITY|BLOCKER|1