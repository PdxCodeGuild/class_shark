# APIs and AJAX


**Table of Contents** 
- [API](#api)
- [HTTP Methods](#http-methods)
- [AJAX](#ajax)
  - [Fetch and ES6 Promises](#fetch-and-es6-promises)
  - [async/await](#asyncawait)
  - [axios](#axios)
  - [XMLHttpRequest](#xmlhttprequest)
  - [jQuery](#jquery)
- [Getting around CORS issues](#cors-issues)
- [JSON + XML](#json--xml)
- [Public APIs](#public-apis)


# API

API stands for "application programming interface", it's a standardized way to send and receive data from a web service via HTTP requests (GET, POST, PUT, DELETE). For example, try executing this url in your browser `http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en`. This is an api for random inspiration quotes. Note the query parameters, which specify a key, format, and language. When you enter it in your browser, you execute an HTTP GET request. You can do the same thing from JavaScript, then process the result and control how it's displayed to the user. Websites are for people, APIs are for programs.

There are many free and open APIs available on the internet that can provide many different forms of data. You can find some public APIs [here](https://apilist.fun) ,[here](https://github.com/toddmotto/public-apis), and [here](https://catalog.data.gov/dataset?q=-aapi+api+OR++res_format%3Aapi#topic=developers_navigation). When trying to access a url, remember the [parts of a url](https://doepud.co.uk/images/blogs/complex_url.png). APIs can receive parameters through query parameters and headers. You can see query parameters in the example url. Adding parameters to the request header is done through the `setRequestHeader` function on the `XMLHttpRequest` object.



------
# HTTP Methods

HTTP requests include a **method**, which indicates what the intention of the request is. These methods are conventional. You could use `GET` to delete an entry in the database, but you shouldn't. You can find more info [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods), [here](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods). The most common HTTP methods parallel the CRUD operations we discussed in Python.

| Method | Equivalent |
| ---    | ---        |
| POST   | Create     |
| GET    | Retrieve   |
| PUT    | Update     |
| DELETE | DELETE     |


### HTTP Status Codes

The response to an HTTP request will have a **status code** which indicates whether the request was successful or not, and what the error was. You can find a more thorough list of status codes [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

| Code | Description  |
| ---  | ---          |
| 1XX  | information  |
| 2XX  | success      |
| 3XX  | redirection  |
| 4XX  | client error |
| 5XX  | server error |


------
# AJAX

AJAX stands for "asynchronous javascript and XML", and allows you to execute HTTP requests from JavaScript. You can read more about AJAX [here](https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started), [here](https://developer.mozilla.org/en-US/docs/AJAX) and [here](https://www.w3schools.com/xml/ajax_intro.asp).


## Fetch and ES6 Promises
[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) provides a newer, easier-to-use method to send HTTP requests and process their responses compared to `XMLHttpRequest`.

Here's how to send a `GET` request and process it into JSON:
```js 
fetch('https://api.ipify.org/?format=json')
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    console.log(myJson);
  })
  .catch(error => console.error(error));  
```
This is a basic `GET` request sent to `https://api.ipify.org/?format=json`. `fetch()` uses JS **Promises** to handle processing the request asynchronously. Any `.then(callback)` calls make sure to only process the callback after the previous function has been completed. `.catch(callback)` handles any errors returned from the request. The simplest use of  `fetch()` takes one argument — the path to the resource you want to fetch — and returns a Promise containing the response (a Response object).

### Request options
The fetch() method can optionally accept a second parameter, an object that allows you to control a number of different settings. Some common parameters are below with their optional values. You can read more about others [**here**](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch).

- method: [\*GET, POST, PUT, DELETE, etc.]
- mode: [no-cors, cors, \*same-origin]
- cache: [\*default, no-cache, reload, force-cache, only-if-cached]
- credentials: "same-origin", [include, same-origin, \*omit]
- redirect: [manual, \*follow, error]
- referrer: "no-referrer", // no-referrer, *client
- body: The body you want to add to your request (not available for GET or HEAD requests)
\*Note: Starred options are the default setting.

This example is sending a `POST` request with some form data.
```js
let header = new Headers()
header.append('Authorization', 'Token token="<API key>"')
let form = new FormData(document.getElementById('todo-data'))

fetch('https://example.com/new/', {
    method: 'POST',
    headers: header,
    body: form
}).then((response) => console.log(response))
.catch((err) => console.log(err))
.then((response) => {
    console.log('Success!')   
})
```

## async/await

ECMAScript2017 (ES8) introduced an easier way to work with promises. 

### Examples 

#### Use `fetch` to make an AJAX request
Recall that `fetch()` is an *asynchronous function* that always returns a `Promise`.

Handle promise the ES6 way:
```js 
function getRandomQuote() {
    // fetch() returns promise
    fetch('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1') 
    // .then() resolves promise with response object and returns another promise
    .then(res => res.json()) 
    // console logs response JSON
    .then(jsonRes => console.log(jsonRes))  
    // catches any errors
    .catch(err => console.log(err));
}

getRandomQuote();
```

Using async/await:

1. Use the `async` keyword at a function declaration to specify that the function contains some asynchronous operation.

2. Add `await` keyword before any statement that returns a promise. Store the resolved values as variables.

3. Treat other operations as synchronous operations.

```js 
async function getRandomQuote() { // Step 1
    const res = await fetch('http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'); // Step 2
    const jsonRes = await res.json(); // Step 2

    console.log(jsonRes); // Step 3
}

getRandomQuote();
```

-----
## Axios

[Axios](https://github.com/axios/axios) is a JavaScript library which handles AJAX more succinctly. Ultimately it's built upon the Vanilla JavaScript form of AJAX, so it doesn't offer anything you can't otherwise do with Vanilla.

To use, you'll need to either install the library or use a **cdn**.

Using cdn:
```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

### Examples
```javascript
axios.get(url)
.then(function (response) {
  console.log(response.data)
})
```

```javascript
let config = {
  headers: {
    'x-api-key': api_key
  }
}
axios.get(url, config)
.then(function (response) {
  console.log(response.data)
})
```

```javascript
let data = {
  'key': 'value'
  'data': 'to send'
}
let config = {
  headers: {
    'header name': 'header value'
  }
}
axios.post(url, data, config)
.then(function(response) {
  console.log(response.data)
})
```

## XMLHttpRequest
Here's how to execute an AJAX request in native JavaScript. This was the older standard method of sending HTTP requests. You can read more about XMLHttpRequest [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest). Remember status 200 means 'success'.

```javascript
let xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        console.log(this.responseText);
    }
};
xhttp.open("GET", 'https://api.ipify.org/?format=json');
xhttp.send();
```

The possible values for `readyState` are shown below, you can find more info [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState)
- 0 UNSENT: the request has not yet been sent
- 1 OPENED: the connection has been opened
- 2 HEADERS_RECEIVED: the response headers have been received
- 3 LOADING: the response body is loading
- 4 DONE: the request has been completed

Here I've wrapped an AJAX request in a function to make it easier to use:

```javascript
function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();
}

http_get("https://api.ipify.org/?format=json", function(data) {
    console.log(data);
});
```

## jQuery

It's a little more succinct in jQuery:

```javascript
$.ajax({
    method: "GET", // specify the HTTP Verb
    url: 'https://api.ipify.org/?format=json' // specify the URL
}).done(function(data) {
    console.log(data); // log the data we get in response
}).fail(function() {
    alert("error"); // indicate that an error has occurred
});
```
If you receive the response "No 'Access-Control-Allow-Origin' header is present on the requested resource", it's because the remote server you're sending to the request from has security controls in place that prevent access from a client. You can read more about CORS [here](https://stackoverflow.com/questions/43871637/no-access-control-allow-origin-header-is-present-on-the-requested-resource-whe) and [here](https://security.stackexchange.com/questions/108835/how-does-cors-prevent-xss).


------
# CORS Issues

Taken from the [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS):

Cross-Origin Resource Sharing (**CORS**) is a mechanism that uses HTTP headers to tell a browser to allow a web app running at one origin (domain) permission to access resources from a server at a different origin. 

An example of a cross-origin request: The frontend JavaScript code for a web application served from http://dogs.com uses makes a `fetch` request for http://api.cats.com/pics/.

For security reasons, browsers restrict cross-origin HTTP requests initiated from within scripts. For example, `XMLHttpRequest` and `fetch` follow the same-origin policy. This means that a web application using those APIs can only request HTTP resources from the same origin the application was loaded from, unless the response from the other origin includes the right CORS headers.

**Note:** CORS is set on the server-side and *there is nothing you can do from the client-side to change that setting*. That is up to the server/API.

This is a common issue to get developing on the client-side and consuming APIs hosted on another origin.

## Workarounds
There are other workarounds, such as [JSONP](https://en.wikipedia.org/wiki/JSONP), and other less secure ways of bypassing this issue client-side, but we will focus on one of the simplest solutions: proxies.

### Proxy

Proxies are a way to circumvent the CORS issue. You can set up your own proxy server or use a third-party service that proxies your request and automatically enable CORS for your endpoint.


The simplest solution is to a web app such as: https://cors-anywhere.herokuapp.com/
You simply attach the url you are trying to request after it.

#### Example 
```js
fetch('https://cors-anywhere.herokuapp.com/https://api.cats.com/pics/')
.then(res => res.text())
.catch(err => console.log(err))
.then(text => console.log(text))
```

See other proxies [here](https://gist.github.com/jimmywarting/ac1be6ea0297c16c477e17f8fbe51347)


------
# JSON + XML

JSON and XML are two popular ways of formatting data. Most APIs either return information in JSON or XML.

[JSON](http://www.json.org/) is very similar to javascript object declarations, but the major difference is that the names are strings, and the values can only be numbers, strings, arrays, booleans, null, or objects.

```json
{"employees":[
    { "firstName":"John", "lastName":"Doe" },
    { "firstName":"Anna", "lastName":"Smith" },
    { "firstName":"Peter", "lastName":"Jones" }
]}
```

[XML](https://developer.mozilla.org/en-US/docs/XML_Introduction) resembles HTML, it has tags, and attributes, and inner text.

```xml
<employees>
    <employee>
        <firstName>John</firstName>
        <lastName>Doe</lastName>
    </employee>
    <employee>
        <firstName>Anna</firstName>
        <lastName>Smith</lastName>
    </employee>
    <employee>
        <firstName>Peter</firstName>
        <lastName>Jones</lastName>
    </employee>
</employees>
```

------
# Public APIs
- [categorized, user friendly list](https://apilist.fun)
- [a list on github](https://github.com/toddmotto/public-apis)
- [list on data.gov](https://catalog.data.gov/dataset?q=-aapi+api+OR++res_format%3Aapi#topic=developers_navigation)