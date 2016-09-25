
function theAjax(uri,data){
 return $.ajax({
    type:"POST",
    dataType:"json",
    url: uri,
    data : data
 });
}

window.fbAsyncInit = function () {
    FB.init({
        appId: '461359507257085',
        cookie: false,  // enable cookies to allow the server to access
        // the session
        xfbml: true,  // parse social plugins on this page
        version: 'v2.0' // use version 2.0
    });
};

// Load the SDK asynchronously
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


function fb_login() {
    FB.login(function (response) {

        if (response.authResponse) {
            //console.log('Welcome!  Fetching your information.... ');
            //console.log(response); // dump complete info
            access_token = response.authResponse.accessToken; //get access token
            user_id = response.authResponse.userID; //get FB UID
            console.log(access_token);
            data = {}
            data['accessToken'] = response.authResponse.accessToken;
    data['uid'] = response.authResponse.userID;
    theAjax('/fbConnect/',data).done(function(response){
      console.log(response);
      location.reload();
    });

        } else {
            //user hit cancel button
            console.log('User cancelled login or did not fully authorize.');

        }
    }, {
        scope: 'email,publish_actions,public_profile'
    });
}

$(document).ready(function(){
  var bitch = $("#id_directorDetail").html();
  console.log(bitch);
  if(bitch != "") $("#1 button").html("Update");
  bitch = $("#id_studentBodyDetail").html();
  if(bitch != "") $("#2 button").html("Update");
});

$("form button").click(function(event){
  event.preventDefault();
  id = "#id_"+$(this).val();
  url = $(this).prop("id");
  detail = $(id).val();
  data = {}
  data[$(this).val()] = detail
  console.log(detail);
  theAjax(url,data).done(function(){

    location.reload();
  })
});


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
