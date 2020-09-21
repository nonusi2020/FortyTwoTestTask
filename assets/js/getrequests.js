var interval = 1000;
var pagetitle = "Requests";
var newRequests = 0;

window.addEventListener("focus", updatetitle);

function Requests() {
    window.setInterval(function() {
        getrequest();
    }, interval);
    updatetitle();
}

function getrequest() {
    url = "/request/?focus=" + document.hasFocus();
    $.get(url, updateRequests);
}

function updateRequests(response) {
    newRequests = response.new_requests;
    var requestList = response.request_list;
    var template = "";
    var finaltemplate = "";
    //update request page.
    requestList.forEach(function(request) {
        template = "<tr><td>" + request.path + "</td><td>" + request.time + "</td></tr>";
        finaltemplate += template;
    });
    $("tbody").html(finaltemplate);
    updatetitle();
}

function updatetitle() {
    if (document.hasFocus()) {
        $("title").text(pagetitle);
        newRequests = 0;
    } else {
        var n = newRequests > 0 ? "(" + newRequests + ")" : "";
        $("title").text(n + pagetitle);
    }

}