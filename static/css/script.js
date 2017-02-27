$(document).ready(function() {

    $('.tasks a').click(function() {
        var id = $(this).attr('href');
        $('.dial').css('display', 'none');
        $(id).css('display', 'block');
    });

});