let url_string = (window.location.href);
let url = new URL(url_string);
const id = String(url.searchParams.get("id"))
console.log(id)


document.getElementById("image").src = "static/images/" + id + ".png"

document.getElementById("grayscaleButton").addEventListener("click", async function(){
    let data = {"id":id,"process":"grayscale"}
    imageProcessing(data)
})

document.getElementById("meanblurButton").addEventListener("click", async function(){
    let data = {"id":id,"process":"meanblur"}
    imageProcessing(data)
})

document.getElementById("gaussianblurButton").addEventListener("click", async function(){
    let data = {"id":id,"process":"gaussianblur"}
    imageProcessing(data)
})

document.getElementById("sobelButton").addEventListener("click", async function(){
    let data = {"id":id,"process":"sobel"}
    imageProcessing(data)
})


document.getElementById("sharpenButton").addEventListener("click", async function(){
    let data = {"id":id,"process":"sharpen"}
    imageProcessing(data)
})



async function imageProcessing(data){//send appropriate data to get the server to do whatever you want
    let response = await fetch("/imageProcessing", {
        method:"POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(response =>response.json())
    console.log(response)
    window.location.reload()
    return response
}