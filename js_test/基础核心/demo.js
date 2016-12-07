/**
 * Created by Administrator on 2016/11/7.
 */
/*
$(function(){
    $("#box").css('color','red');
});

jQuery(function(){
    jQuery("#box").css('color','red');
});
    */



//
//$(function(){
//    alert($);  //jQuery对象的内部函数
//    alert($());  //返回jQuery对象
//    alert($('#box'));  //返回的也是jQuery对象
//    alert($('#box').css('color','red').css('font-size','200px').css('font-weight','bold'));  //返回的仍然是jQuery对象
//});
//window.onload = function(){
//    $('#box').css('color','red');
//};
//
//$(document).ready(function(){
//    $('#box').css('color','red');
//});
//window.onload = function(){
//    alert(1);
//};
//window.onload = function(){
//    alert(2);
//};

//$(document).ready(function(){
//    alert(1);
//});
//$(document).ready(function(){
//    alert(2);
//});
//$(document).ready(function(){
//    alert(3);
//});
var $$ = jQuery;   //解决多个库冲突的问题
jQuery.noConflict();  //自行了断，把自己的$所有权剔除掉
$(function(){
    //alert(document.getElementById('box'))
    //alert($("#box").get(0))
    alert($$(document.getElementById('box')));
});
