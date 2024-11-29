var header = document.querySelector("header")
var headerToggle = document.getElementById("toggle_header");
headerToggle.addEventListener("click", function() {
    if (header.className == "green") {
        header.className = "red";
    }
    else {
        header.className = "green";
    }
});

