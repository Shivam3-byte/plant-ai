const API = "https://your-render-url/predict";

async function predict() {

    const file = document.getElementById('file').files[0];

    let formData = new FormData();
    formData.append("file", file);

    let res = await fetch(API, {
        method: "POST",
        body: formData
    });

    let data = await res.json();

    document.getElementById("result").innerHTML =
        JSON.stringify(data);
}
