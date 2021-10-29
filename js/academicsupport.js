function onClick() {
    alert("Test1234.")
}

window.onload = function enableButton() {  
    var button = document.getElementById('submit_button');
    var form = document.getElementById("academicsupportfundform");
    var checkboxes1 = form.elements["role"];
    if(checkboxes1 != ("Other" || "Educator" || "Assistant Principal" || "Principal's Assistant or Main Office Mgr" || "Principal")) 
    {       
        button.disabled = true;
    } else {
    	button.disabled = false;
    	enableButton();
    }        
}    