let url_string = (window.location.href);
let url = new URL(url_string);
const id = String(url.searchParams.get("id"))
console.log(id)


function onpageLoad(){
    document.getElementById("image").src = "static/images/" + id + ".png"

    document.getElementById("stegEncode").addEventListener("click", async function(){
    message = document.getElementById("inputText").value
    console.log(message)
    let data = {"id":id,"message":message}
    encode(data)
})

document.getElementById("homeButton").addEventListener("click", function(){
    window.location.replace("/")

})

document.getElementById("download").addEventListener("click", ()=>{
    download("static/images/" + id + ".png")
})
}

async function encode(data){
    let response = await fetch("/Encode", {
        method:"POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response =>response.json())
    window.location.reload()
    console.log(response)

    return response
}

window.onload = (event) => {
    onpageLoad()
  };

function download(url) {
    const a = document.createElement('a')
    a.href = url
    a.download = url.split('/').pop()
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
}