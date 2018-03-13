// Write your Javascript code.
$(document).ready(function(){
    $.get("https://jsonplaceholder.typicode.com/posts/1", function(res)
    {
        console.log(res);
        $('.info').html("<h2>" + res.title + "</h2>");
    },'json');
    $(".query").click(function(){
        $.get("https://jsonplaceholder.typicode.com/posts/2", function(response)
        {
            $('.empty').html("<h2>" + response.title + "</h2>");
        }, 'json');
    });


    $(".newtest").click(function(){
        var x = $(".infobox").val();
        console.log(x);
        $.get("https://jsonplaceholder.typicode.com/posts/"+ x, function(response)
        {
            $('.empty').append("<h2>" + response.title + "</h2>");
        }, 'json');
    });

})