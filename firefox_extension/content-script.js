console.log("Script injecté sur example.com !");
document.body.style.border = "5px solid red";

const rssUrl = 'http://localhost/get_password';



  

window.onload = async () => {
    const data = { host: window.location.href };
    const passwords = await browser.runtime.sendMessage({ action: "fetchData", data: data })
    if(passwords != null) {
        let password = document.querySelector("input[type=password]")
        if(password != null) {
            password.value = passwords["data"]["password"]
            password.style.backgroundColor = "rgb(252, 255, 163)"
        }
        let id = document.querySelector("input[type=text]")
        if(id != null) {
            id.value = passwords["data"]["username"]
            id.style.backgroundColor = "rgb(252, 255, 163)"
        }
        else {
            let id2 = document.querySelector("input[id*=email]")
            if(id2 != null) {
                id2.value = passwords["data"]["username"]
                id2.style.backgroundColor = "rgb(252, 255, 163)"
            }
        }
    }
}