const header = document.querySelector("header")
const headerToggle = document.getElementById("toggle_header");
headerToggle.addEventListener("click", function() {
    if (header.className == "green") {
        header.className = "red";
    }
    else {
        header.className = "green";
    }
});
