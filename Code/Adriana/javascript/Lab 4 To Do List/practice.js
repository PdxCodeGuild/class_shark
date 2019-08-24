let header = new Headers()
header.append('Authorization', 'Token token="<API key>"')
let form = new FormData(document.getElementById('todo-data'))

fetch('https://webhook.site/19e52b98-84bf-4e20-8193-e8b6c71ad154', {
    method: 'POST',
    headers: header,
    body: form
}).then((response) => console.log(response))
.catch((err) => console.log(err))
.then((response) => {
    console.log('Success!')   
})