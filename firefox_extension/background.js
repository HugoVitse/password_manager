// async function fetchRSS(url) {
//     try {
           
//         const response = await fetch(url, {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json" 
//             },
//             body: JSON.stringify(data) 
//         })
            
//         const text = await response.json();
        
//         console.log(text);
//         return text;
//     } 
//     catch (error) {
//         return "error"
//     }
// }
// function sendMessageToContentScript(tabId, argument) {
//     browser.tabs.sendMessage(tabId, { type: "setData", argument: argument });
// }
  

    
// window.onload = async()=>{
//     const rssUrl = 'http://localhost/get_unlocked_vault';

//     // Appel de la fonction au démarrage pour des fins de démonstration.
//     const passwords = await fetchRSS(rssUrl);
    
//     browser.webNavigation.onCompleted.addListener((details) => {
//         const site_pass = passwords.find((element) => element.data.host == details.url)
//         let password = site_pass.data.password
//         let username = site_pass.data.username
//         console.log(site_pass)
        
//     });
// }
  



browser.runtime.onMessage.addListener(async(message, sender, sendResponse) => {
    if (message.action === "fetchData") {
        const response = await fetch("http://localhost/get_password", {
            method: "POST",
            headers: {
            "Content-Type": "application/json"
            },
            body: JSON.stringify(message.data)
        })
        
        const text = await response.json();
    
      // Nécessaire pour utiliser sendResponse de manière asynchrone
        return text;
    }
  });