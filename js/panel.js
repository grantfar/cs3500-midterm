var wrapStyle = ["nowrap","normal"];
var wrapSelect1;
var wrapSelect2
window.onload= function() {
    wrapSelect1 = 0;
    wrapSelect2 = 0;
    $("#example1Collapse").click(function() {
    $("#example1Body").fadeToggle("fast");});
    $("#example2Collapse").click(function() {
    $("#example2Body").fadeToggle("fast");});
    $("#example1Wrap").click(function() {
    $("#example1Body").css("white-space",wrapStyle[wrapSelect1]);
    wrapSelect1 = (wrapSelect1+1)%2});
    $("#example2Wrap").click(function() {
    $("#example2Body").css("white-space",wrapStyle[wrapSelect2]);
    wrapSelect2 = (wrapSelect2+1)%2});
}