// COLLECT DATA:
var sidebar = document.getElementById("sidebar");
var blockSidebar = document.getElementById("block_sidebar");
var pageContent = document.getElementById("page_content");
var page = document.getElementById("page");


// SIDEBAR ACTION - SHOW HIDE WHOLE MENU WITH COOKIES:
blockSidebar.addEventListener("click", function(event) {

    if(sidebar.classList.contains("blocked_bigbar") === false) {
        sidebar.classList.add("blocked_bigbar");
        document.cookie = "sidebar=true;path=/";
    } else {
        sidebar.classList.remove("blocked_bigbar");
        document.cookie = "sidebar=false;path=/";
    }

});

sidebar.addEventListener("mouseenter", function(event) {
    sidebar.classList.add("bigbar");
});

sidebar.addEventListener("mouseleave", function(event) {
    sidebar.classList.remove("bigbar");
});




// MAIN COOKIES READER:
function cookies() {

    var cookies = document.cookie.split(";");

    for(let i=0; i<cookies.length; i++) {
        let cookie = cookies[i].split("=");

        // SHOW HIDE WHOLE MENU WITH COOKIES:
        if(cookie[0] === "sidebar" || cookie[0] === " sidebar") {
            if(cookie[1] == "true") {
                sidebar.classList.add("blocked_bigbar");
            };
        }

    };

    // Allow animations on page:
    setTimeout(function() {
        page.classList.add("animated");
    }, 100);

}

// FUNCTION EXECUTER:
cookies()

