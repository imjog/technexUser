$(document).ready(function() {

    $('.tasks a').click(function() {
        var id = $(this).attr('href');
        $('.dial').css('display', 'none');
        $(id).css('display', 'block');
    });

    if( $('#glyddpro')[0].style.width == '100%'){
        $('#glydd').css('display', 'inline-block');
    }
    if( $('#glysbdpro')[0].style.width == '100%'){
        $('#glysbd').css('display', 'inline-block');
    }
    if( $('#glyfbcpro')[0].style.width == '100%'){
        $('#glyfbc').css('display', 'inline-block');
    }
    if( $('#glyfblpro')[0].style.width == '100%'){
        $('#glyfbl').css('display', 'inline-block');
    }

});
