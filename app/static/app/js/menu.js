let menu = document.getElementById("menu")
let header = document.getElementById("header")
let nav = document.getElementById("nav")

menu.addEventListener("click", function() {
    if(header.style.height == "80px" || header.offsetHeight == 80) {
        header.style.height = 80 + nav.offsetHeight + "px"
    } else {
        header.style.height = "80px"
    }
})

window.addEventListener("resize", function() {
    let width = document.documentElement.clientWidth
    if(width > 480) {
        header.style = "none"
    }
}) 