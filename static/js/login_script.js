jQuery(document).ready(function() {

  // $("#abcd").modal('show');
   $(".alert-email").hide();
   $('#close-email').on('click',function(){
      $('.alert-email').hide();
    });
  $.backstretch("/1.jpg");
    // $('.form-password').addClass('input-error');
 $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
        $(this).removeClass('input-error');
    });
    

$(".sign-up-btn").click(function(e){
         e.preventDefault();
         window.location = "/register";    
});
 $('.reset-password-form input[type="text"], .password-form input[type="password"]').on('focus', function() {
        $(this).removeClass('input-error');
    });
    

function emailvalidation()
    {

        var email = $('#reset-email').val();
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        console.log(email);
       
        if(re.test(email) == false)
        {
             console.log(email);
             $('.alert-email').show();
             //document.getElementById("laluram").setCustomValidity("Invalid");
             //$("#email-error").html("Invalid Email Address");
             // $(".alert").show();
             return false;
        }
         else
        { 
              //   document.getElementById("laluram").setCustomValidity("");
              //$("#email-error").html("");
              $(".alert-email").hide();
              return true;
        }
}

     $('#reset-email').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
          $('.alert-email').hide();
        //document.getElementById("laluram").setCustomValidity("");
        //$("#email-error").html(""); 

    });   

$('.login-form').on('submit', function(e) {
   var next = true;
            console.log("ancd");
            $(this).find('input[type="text"], input[type="password"], textarea').each(function() {
                if( $(this).val() == "" ) {
                    e.preventDefault();
                    $(this).addClass('input-error');
                    next =false;
                }
                 else
                {
                    $(this).removeClass('input-error');
                };

                console.log("add");
            });


});
 $('.reset-password-form').on('submit', function(e) {
        next = true;

       $(this).find('input[type="text"], input[type="password"], textarea').each(function() {
                if( $(this).val() == "") {
                    e.preventDefault();
                    // if($(this).text() == "--SELECT YOUR YEAR--")
                    // {
                    //   console.log("select box wpvalidation")
                    // }
                    $(this).addClass('input-error');
                    next =false;
                }
                 else
                {
                    $(this).removeClass('input-error');
                    console.log("add");
                };

                
            });
       if(next)
       {
         next= emailvalidation();
        
         if(!next)
         {
        e.preventDefault();
    }
}
       
});


});
