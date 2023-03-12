let url_string = (window.location.href);
let url = new URL(url_string);
const id = String(url.searchParams.get("id"))
console.log(id)


function onpageLoad(){
    document.getElementById("image").src = "static/images/" + id + ".png"

document.getElementById("stegDecode").addEventListener("click", async function(){

    let data = {"id":id}
    message = await decode(data)
    console.log(message)
    document.getElementById("message").innerHTML = message
})

document.getElementById("homeButton").addEventListener("click", function(){
    window.location.replace("/")

})
}

async function decode(data){
    let response = await fetch("/Decode", {
        method:"POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response =>response.json())
    // window.location.reload()
    console.log(response)

    return response["message"]
}

window.onload = (event) => {
    onpageLoad()
  };