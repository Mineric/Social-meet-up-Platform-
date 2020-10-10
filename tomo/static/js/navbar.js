$(document).ready(function () {
    var searchInput = $("#search-input");
    searchInput.keyup((event) => {
        var str = $(event.target).val();
        if(str != "") {
            var url = "/search" + "?q=" + str;
            console.log(`Search bar: ${url}`);
            $(".search-results").load(url, function (data) {
                console.log(data);
            });
        }
    });
    searchInput.blur((event) => {
        $(".search-results").empty();
    });
})