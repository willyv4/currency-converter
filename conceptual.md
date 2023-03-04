# Conceptual Exercise

Answer the following questions below:

## What are important differences between Python and JavaScript?

- Python is generally used on the server side while JavaScript is generally used on the client side, however, that is not always the case. Python is generally more readable and consistent on the ohter hand JavaScript can be a little harder to read but the language is more flexible and allows for more precise code.

- For the most part JavaScript is faster than Python because it's a compiled language and python is an interperted language. this is true in most but not all cases as it depends on the implementations.

- Python has a more structured community and debugging tools which enhances the ease of learning the language. While JavaScript has a large community but not as much of a structure.

## Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you can try to get a missing key (like "c") _without_ your programming crashing.

- 1: In example one we use the get method to grab the value from the dictionary
  we then use an if else statement to check if the return value is None. if None we print NO KEY otherwise we print value.

2: In example two we attempt to grab the value of "c" using bracket notation if it is not succesful a KeyError exception is raised and we print NO KEY if it is succesful we print the value2

EXAMPLE 1
dictionary = {"a": 1, "b": 2}

value = dictionary.get("c")
print("NO KEY") if value is None else print("value", value)

EXAMPLE 2
try:
value2 = dictionary["c"]
print("value", value)
except KeyError:
print("NO KEY")

## What is a unit test?

- unit tests are focused on testing small specific pieces of code, such as functions or methods to ensure they work as intended

## What is an integration test?

- integration tests are meant to test the interactions between functions, methods, compenants and modules. unlike unit tests, they test the applications more broadly, for an example they test how the api and database might interact together or how the backend api works with the api calls on the frontend.

## What is the role of web application framework, like Flask?

- frameworks in general provide rules and templates to build applications quicker and more effectively. they might provide libraries of tools or compenants that simplify processes. for example the flask framework provides tools like, a built in server, supports RESTFUL API, and jinja templates. which enhances the development process.

## You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like'foods?type=pretzel'). How might you choose which one is a better fit for an application?

- Using a parameter in route such as '/foods/pretzel' would be better if the page you are going to is specifc about just the url pretzels. that url might tell you all about different kinds of pretzels and anything about pretzels.

- while using a URL query param such as 'foods?type=pretzel' would be better if the info passed is optional or for filtering specific data. example if i had a list of food options i wanted to add to my food order using a URL query param would be better

## How do you collect data from a URL placeholder parameter using Flask?

- using route parameter such as '/books/<int:book_id>'
  has a place holder '<int:book_id>' this excepts a number
  a route can then access the the place holder val using request.view_args["book_id"]

## How do you collect data from the query string using Flask?

- using request.args example.com/search?query=flask
  we could define a route that handles a GET request to /search endpoint
  doing something like query = request.args.get('query')

## How do you collect data from the body of the request using Flask?

- collecting data from the body request is done using request.form
  say you have a route with a url '/submit' and methods "POST"
  whatever data is sent through the html form can be retrieved using request.form. Example email = request.form.get("email) we get the email from the form

## What is a cookie and what kinds of things are they commonly used for?

- Cookies are small pieces of data stored on the user's device and are commonly used for various purposes such as authentication, login sessions, user preferences, shopping cart contents, and tracking user behavior on a website. Websites use cookies to personalize the user experience by remembering user preferences and previous actions.

## What is the session object in Flask?

- The session object in Flask allows you to store data that persists throughout the user's interaction with your web application. Session data is stored on the server-side. When a user interacts with your web application, Flask generates a unique session ID that is stored as a cookie on the user's browser. This session ID is used to retrieve the corresponding session data from the server on requests.

## What does Flask's `jsonify()` do?

- jsonify turns a python object into a JSON string
