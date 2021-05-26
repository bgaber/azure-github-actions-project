$(document).ready(function() {
    $.ajax({
        url: "https://httpgetsetcosmoscounter.azurewebsites.net/api/httptriggergetsetcounter",
        data: {id: "1234567", account_number: "resume"},
        type: "GET",
        // The type of data expected back
        dataType: "json",
        success: function (jsonlist) {
            console.log(jsonlist);
            alert("Counter: " + jsonlist.counter);
            //$("#view_count").html(jsonlist.counter);
            
        },
        error: function (xhr, status, errorThrown) {
            alert("There was an AJAX problem with /api/httpgetsetcosmoscounter");
            console.log("Error: " + errorThrown);
            console.log("Status: " + status);
            console.dir(xhr);
        }
    });
});