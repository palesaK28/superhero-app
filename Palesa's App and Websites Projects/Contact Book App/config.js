

let rootPath = "https://mysite.itvarsity.org/api/ContactBook/";
let apiKey = checkApiKey();

function checkApiKey() {
    if (!localStorage.getItem("apiKey")) {
      ;// window.open("enter-api-key.html", "_self");
    }
    else
    return localStorage.getItem("apiKey");
}
