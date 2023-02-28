id = 0;
document.getElementById("submitImg").addEventListener("click",async function(){
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
    window.location.replace("/imageProcessing?id=" + id)
})


 
