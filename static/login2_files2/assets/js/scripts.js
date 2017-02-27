
jQuery(document).ready(function() {
    
    /*
        Fullscreen background
    */
   /* var FillWhatsapp  = function(f){
                                          $('.form-whatsapp').val($('.form-mobile-number').val()) ;
                                        
                                              
                                                }
*/ var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");

function validatePassword(){
  if(password.value != confirm_password.value) {
    $('.form-repeat-password').attr("background-color","red");
    confirm_password.setCustomValidity("Passwords Don't Match");
    return false;
  } else {
    confirm_password.setCustomValidity('');
    return true;
  }
}

password.onchange= validatePassword;
confirm_password.onkeyup= validatePassword;







   function phnvalidation()
    {
        var num = $('.form-mobile-number').val();
        console.log(num.length);
        if(num.length!=10)
           {
            document.getElementById("form-mobile").setCustomValidity("Invalid Phone no"); 
            console.log("here");
            return false;
        }
        else
        {
            
            return true;
        }
    }

    function emailvalidation()
    {
        var email = $('.form-email').val();
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if(re.test(email) == false)
        {
            abc = document.getElementById("form-email");
            abc.setCustomValidity("Invalid Email");
        }



        return re.test(email);
     }



     $("input[type=checkbox]").on("click", function()
     {
        $('.form-whatsapp').val($('.form-mobile-number').val()) ;
     });                                       
    $.backstretch("assets/img/backgrounds/1.jpg");
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
        $.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
        $.backstretch("resize");
    });
    
    /*
        Form
    */
    $('.registration-form fieldset:first-child').fadeIn('slow');
    
    $('.registration-form input[type="text"], .registration-form input[type="password"], .registration-form textarea').on('focus', function() {
        $(this).removeClass('input-error');
    });
    
    // next step
    $('.registration-form .btn-next').on('click', function() {
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;
        
        parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function() {
            if( $(this).val() == "" ) {
                $(this).addClass('input-error');
                next_step = false;
            }
            else 
            {
              
             next_step = (validatePassword() && emailvalidation())

        }});
        
        if( next_step ) {
            parent_fieldset.fadeOut(400, function() {
                $(this).next().fadeIn();
            });
        }
        
    });
    
    // previous step
    $('.registration-form .btn-previous').on('click', function() {
        $(this).parents('fieldset').fadeOut(400, function() {
            $(this).prev().fadeIn();
        });
    });
    
    // submit
    $('.registration-form').on('submit', function(e) {
        
        $(this).find('input[type="text"], input[type="password"], textarea').each(function() {
            if( $(this).val() == "" ) {
                e.preventDefault();
                $(this).addClass('input-error');
            }

            else {
                 if(!phnvalidation())
                 {
                   e.preventDefault();
                $(this).addClass('input-error');
                 }   
                 else
                 {
                $(this).removeClass('input-error');
            }
            }
        });
        
    });
    
    
});


