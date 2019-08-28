# AJAX & Vue
Modern web development typically separates server-side (backend) and client-side (frontend) development. The server serves an API (application programming interface), packaging data into easy to consume endpoints for the frontend to request. The frontend focuses on UI development, presenting the data it got from the API. Modern frontend frameworks like **ReactJS** and **VueJS** focus solely on the frontend, so you can essentially "plug-and-play" a frontend application to any backend implementation.

Some benefits of decoupling client and server-side logic include:
- better user experience (user engages with UI and only loads data as needed from the server, i.e. better responsiveness)
- ability to develop different frontend implementations with same backend (for web/mobile/native apps)
- concurrent development (backend and frontend devs can work separately and simultaneously)

## Creating Your API
To keep your frontend and your backend separate, you'll want to create an API to allow your frontend to access and manipulate data stored in your backend.

You can build an API by hand, using `JsonResponse` to return a Python dictionary as JSON for your frontend client to consume, and specifying what logic to set off for different HTTP verbs.

#### Example: todo app
`GET` & `POST` on the same endpoint: `/todos`

| verb | logic | 
| ---- | ----- | 
| `GET` | sends `JsonResponse` of all todos | 
| `POST` | creates new todo with the request data and adds to db | 

`PUT`, `PATCH`, `DELETE` on the same endpoint: `/todos/1`

Note: The following are all modifying the todo with `id=1`

| verb | logic | 
| ---- | ----- | 
| `PUT` | updates all fields the todo with the request data and saves to the db | 
| `PATCH` | updates only fields from the request data and saves to the db | 
| `DELETE` | deletes the todo from the db | 

### Django Rest Framework
Alternatively, you can use [Django Rest Framework](https://www.django-rest-framework.org/) (DRF), which does all of the above automatically for you. DRF makes it easy to *serialize* your database tables into JSON and automatically sets up endpoints that handle HTTP verbs in expected ways.

## AJAX
If you tried sending a `POST/PUT/PATCH/DELETE` request to your Django endpoint, you likely had a `403 Forbidden` response. This is because Django requires a CSRF (Cross Site Request Forgery) token to be passed with the request data. The CSRF token protects against cross site request forgery. This basically means the token tells Django that this request is coming from the same site.

### CSRF token fix
You can get around this `403` issue by including the CSRF token in a cookie.

#### axios
You can configure `axios` to pass along the CSRF token as a default.

Include the following lines at the top of any JS files you are sending AJAX requests from.
```js
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
```
The names here are very important. These are the cookie and header names that Django is looking for. Django automatically passes the CSRF token cookies. We just have to let `axios` know which name to look out for.

Then, make your AJAX request as per usual.
```js
async function post(url, data, config) {
    try {
        const response = await axios.post(url, data, config)
        console.log(response)
    } catch (err) {
        console.log(err)
    }
```

#### fetch
Use the [js-cookie](https://github.com/js-cookie/js-cookie/) library to grab the CSRF token cookie.

Make sure to include the CDN script in the template page *above* your JS file where you are making AJAX calls.
```html
<!DOCTYPE html>
<head>...</head>
<body>
    ...
    <script src="https://cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js"></script>
    <script src='script-with-ajax.js'></script>    
</body>
</html>
```

Include the following lines at the top of any JS files you are sending AJAX requests from.
```js
const csrftoken = Cookies.get('csrftoken')
const headers = new Headers({
        "X-CSRFToken": csrftoken
});
```

Then, make sure to include the headers in your `fetch` request.

```js
async function apiCall(url, request_type, body) {
    const options = {
            method: request_type,
            credentials: 'same-origin',
            headers: headers,
            body: JSON.stringify(body)
    }
    try {
            const res = await fetch(url, options)
            const json = res.json()
            console.log(json)
    } catch (err) {
            console.log(err)
    }
}
```

## Connecting Vue Frontend to Django Backend
To connect a [VueJS](https://vuejs.org/v2/guide/) frontend with a Django backend, we have to *render* the HTML file containing Vue logic. We connect the **view** (controller) logic to *route* a URL to a template containing Vue. 

If we're using an API to interface with our data, we can use Django's generic `TemplateView` class to make things easy.

### Using TemplateView
In `app/urls.py`:
```py
from django.views.generic import TemplateView

urlpatterns = [
    ...
    path('', TemplateView.as_view(template_name='index.html')), 
    ...
]
```

So long as you're including a `<script>` to Vue.js, then `index.html` (or whatever your template name is here) should have access to Vue now.

But we have a problem here! Django's template syntax probably looks awfully familiar if you've worked with Vue before. Django and Vue use some of the *same template syntax*. This will cause some of your Vue code to not work.

Fear not, since the solution is very simple.

### Same templating syntax fix 
Add a `delimiters` property when initializing your Vue app. These replace Vue's handlebar `{{}}` syntax.

```js

const app = new Vue({
    el: '#app',
    delimiters: ['${', '}'], // set custom delimiters here instead of {{}}
    data: {...},
    methods: {...},
})
```

Vue interpolation should now work again.

## CORS
**CORS** stands for Cross Origin Resource Sharing.
This is an example of a common CORS error you can get: 
```
Error: Network Error
Access to XMLHttpRequest at 'http://xxx.xxx' from origin 'http://localhost:8000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.
```
The error appears because of a security policy called `same-origin policy`. This is the default CORS policy put into place to prevent a common cyber attack: `cross-site request forgery`.  Simply put, the browser checks if the origins of the request (your website) and the server (hosting the API you are requesting) match.

If you are using two different servers for your frontend and backend, such as Django (backend on port 8000) and live-server (frontend on port 8080), this CORS error can occur.

CORS allows browsers to bypass the `same-origin policy` which is enforced by default. CORS enables you to add headers that tell the browser if it's allowed to send/receive requests from domains other than the one serving the page.

### `django-cors-headers`
This Django app automatically adds CORS headers to your responses, allowing requests to your Django application from other origins.

#### Install 
```
pip install django-cors-headers
```
#### Use
All of the following is in `settings.py`

1. Add it to your installed apps:
```py
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
```

2. Add the middleware class
```py
MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```
Note: `CorsMiddleware` should be placed as high as possible, especially before any middleware that can generate responses.

3. Configure CORS settings
```py
CORS_ORIGIN_WHITELIST = (
    "http://localhost:8000",
    "http://localhost:8080",
)
```
Add any sites you want to allow cross origin resource sharing with.
Alternatively, you can allow all origins (Note: this can be dangerous!)

```py
CORS_ORIGIN_ALLOW_ALL = True # default is false
```