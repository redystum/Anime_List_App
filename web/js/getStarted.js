function welcomeTransition(){
    setTimeout(() => { document.getElementById("welcomeRow").classList.add("welcomeRowTop"); }, 2000);
}

async function verifyToken(){
    let token = document.getElementById("clientIdInp").value; 
    if(token.length == 0){
        showToast("Error", "Empty Client ID", "red", "soft-black");
        return;
    }
    let response = await eel.checkToken(token)();
    if(response.status != "success"){
        showToast("Error", "Invalid Client ID", "red", "soft-black");
        return;
    }
    showToast("Success", "Valid Client ID! Please restart the app", "soft-green", "soft-black");
    document.getElementById("clientIdInp").disabled = true;
    document.getElementById("checkButton").disabled = true;
    alert("Please restart the app");
    setTimeout(() => { window.close(); }, 3000);
}

function showToast(title, msg, colorH, colorT) {
    // set toast colors and text
    document.getElementById("toastHeader").style.backgroundColor = `var(--${colorH})`;
    document.getElementById("toastBodyText").style.backgroundColor = `var(--${colorT})`;
    let color;
    if (colorH == "soft-green") {
        color = "black";
    } else {
        color = "white";
    }
    document.getElementById("toastHeader").style.color = color;
    document.getElementById("toastBodyText").innerHTML = msg;
    document.getElementById("toastTitle").innerHTML = title;
    // show toast
    toast = document.getElementById('toast');
    var bsToast = new bootstrap.Toast(toast)
    bsToast.show()
}