var wrapStyle = ["nowrap","normal"];
var wrapSelect1;
var wrapSelect2
window.onload= function() {
    wrapSelect1 = 0;
    wrapSelect2 = 0;
    $("#example1Collapse").click(function() {
        $(this).text(function(i, text) {
            return text === "Collapse" ? "Expand" : "Collapse";
        });
        $("#example1Body").fadeToggle("fast");
    });
    $("#example2Collapse").click(function() {
        $(this).text(function(i, text) {
            return text === "Collapse" ? "Expand" : "Collapse";
        });
        $("#example2Body").fadeToggle("fast");
    });
    $("#example1Wrap").click(function() {
        $(this).text(function(i, text) {
            return text === "Text Wrap: [ON]" ? "Text Wrap: [OFF]" : "Text Wrap: [ON]";
        });
        $("#example1Body").css("white-space",wrapStyle[wrapSelect1]);
        wrapSelect1 = (wrapSelect1+1)%2;
    });
    $("#example2Wrap").click(function() {
        $(this).text(function(i, text) {
            return text === "Text Wrap: [ON]" ? "Text Wrap: [OFF]" : "Text Wrap: [ON]";
        });
        $("#example2Body").css("white-space",wrapStyle[wrapSelect2]);
        wrapSelect2 = (wrapSelect2+1)%2;
    });
}