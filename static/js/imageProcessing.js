let url_string = (window.location.href);
let url = new URL(url_string);
const id = String(url.searchParams.get("id"))
console.log(id)


document.getElementById("image").src = "static/images/" + id + ".png"

