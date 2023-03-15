// document.getElementById("imageProcessing").addEventListener("click",async function(){
    
//     id = await uploadImage()
//     window.location.replace("/imageProcessing?id=" + id)
// })

document.getElementById("stegEncode").addEventListener("click",async function(){
    
    id = await uploadImage()
    window.location.replace("/Encode?id=" + id)
})

document.getElementById("stegDecode").addEventListener("click",async function(){
    
    id = await uploadImage()
    window.location.replace("/Decode?id=" + id)
})


async function uploadImage(){
    const formData = new FormData()
    console.log(document.getElementById("inputImg").files[0])
    let img = document.getElementById("inputImg").files[0]
    formData.append("file", img)
    const requestOptions = {
        headers: {
            "Content-Type": img.contentType,
        },
        method: "POST",
        mode: "no-cors",
        files: img,
        body: formData
    };

    let response = await fetch("/uploadImage", requestOptions).then(response=>response.json())
    console.log(response)
    id = response["id"]
    return id

}