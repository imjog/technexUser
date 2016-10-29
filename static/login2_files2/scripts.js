function theAjax(uri,data){
 return $.ajax({
    type:"POST",
    dataType:"json",
    url: uri,
    data : data
 });
};


jQuery(document).ready(function() {
    
    $(".alert-email").hide();
    $(".alert-confirm-password").hide();
    $(".alert-mobile").hide();
    $('#close-confirm-password').on('click',function(){
      $('.alert-confirm-password').hide();
    });
     $('#close-email').on('click',function(){
      $('.alert-email').hide();
    });
      $('#close-email-repeat').on('click',function(){
      $('.alert-email').hide();
    });
     $('#close-mobile').on('click',function(){
      $('.alert-mobile').hide();
    }); 
      $('#close-no-referral').on('click',function(){
      $('.alert-email').hide();
    });
       $('#close-invalid-referral').on('click',function(){
      $('.alert-email').hide();
    });

function phnvalidation()
    {
        var num = $('.form-mobile-number').val();

        console.log(num.length);
        if((num.length!==10) || (isNaN(parseInt(num))) || (parseInt(num).toString().length  != num.length))
           { 
            $('.alert-mobile').show();
            return false;
        }
        else
        {
           $('.alert-mobile').hide();
            return true;
        }
    }
    $.backstretch("/static/login2_files/1.jpg");
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
        $.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
        $.backstretch("resize");
    });

    function emailvalidation()
    {

        var email = $('#laluram').val();
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
       
        if(re.test(email) == false)
        {
             $('#email-error').show();
             return false;
        }
        else
        { 
              $("#email-error").hide();
              return true;
        }
        
    }
     function referralemailvalidation()
    {

        var email = $('#referral-email').val();
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
       
        if(re.test(email) == false)
        {
             $('#invalid-referral').show();
             return false;
        }
        else
        { 
              $("#invalid-referral").hide();
              return true;
        }
        
    }

function validatePassword(){
        var password = document.getElementById("password");
        confirm_password = document.getElementById("confirm_password");

      if((password.value != confirm_password.value) || (password.value == "") || (confirm_password.value=="")) {
        $('.alert-confirm-password').show();
        return false;
      } else {
        $('.alert-confirm-password').hide();
        return true;
      }
    }                                    
    $('.registration-form fieldset:first-child').fadeIn('slow');
    
    $('.registration-form input[type="text"], .registration-form input[type="password"], .registration-form textarea, .registration-form select').on('focus', function() {
        $(this).removeClass('input-error');
    });
    $('#btn-next').on('click', function() {
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;
        
        parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function() {
            if( $(this).val() == "" ) {
                $(this).addClass('input-error');
                next_step = false;
            }});
              if(next_step){
            next_step = emailvalidation() && validatePassword();
            next_step = validatePassword() && emailvalidation();
        }
        if(next_step)
        {
          function emailUnique(){
  var email = $("#laluram").val();
  theAjax('/checkEmail/',{"email":email}).done(function(response){
    if(response == '1') return true;
    else return false;
  })
};
          //next_step=emailUnique();
          //if(!next_step)
          var email = $("#laluram").val();
          theAjax('/checkEmail/',{"email":email}).done(function(response){
          if(response == '0') {$('#email-repeat').show();next_step = false;}
   
  if( next_step ) {

            parent_fieldset.fadeOut(400, function() {
                $(this).next().fadeIn();
                $($(this).next()).find('input[type="text"], input[type="password"], textarea, select').each(function()
                {
                $(this).removeClass('input-error');   
               });

            });
        }
  });
          //$('#email-repeat').show();

        }
        
        
        
    });


    $("input[type=checkbox]").on("click", function()
    {

         if($('#someSwitchOptionInfo').is(":checked"))
        {
          $("#referral-email").attr("disabled",false);
        }
        else
        {
          $("#referral-email").attr("disabled",true);
        }
    });       

        $('#btn-next-page-email').on('click', function() {
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;        
        if( next_step ) {
            parent_fieldset.fadeOut(400, function() {
                $(this).next().fadeIn();
                $($(this).next()).find('input[type="text"], input[type="password"], textarea').each(function()
                {
                $(this).removeClass('input-error');   
               });

            });
        }
        
    });

    
    $('.registration-form .btn-previous').on('click', function() {
        $(this).parents('fieldset').fadeOut(400, function() {
            $(this).prev().fadeIn();
        });
    });

    $('#form-mobile').keyup(function(e){
        var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
        $('.alert-mobile').hide();
    });

$('#laluram').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
          $('#email-error').hide();
        $('#email-repeat').hide();
    });
$('#confirm_password').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
        {
          $('.alert-confirm-password').hide();
        } 
 });
$('#referral-email').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
          $('#invalid-referral').hide();
        $('#no-referral').hide();
    });
$('#btn-next-page').on('click', function(e) {

        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;
        if($('#id_year option:selected').text() == "--SELECT YOUR YEAR--")
            {
              $("#id_year").addClass('input-error');
              next_step =false;
            }
            else
                {
                    $("#id_year").removeClass('input-error');
                }   
        
       parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function() {
            if( $(this).val() == "" && $(this).prop('disabled') != true) {
              
              e.preventDefault();
                $(this).addClass('input-error');
                next_step = false;
            }});
             if(next_step)
             {
                var mb=phnvalidation();
                next_step = mb;
               }
               if(next_step && $("#referral-email").prop('disabled')==false)
               {
                next_step = referralemailvalidation();
               } 
               if(next_step && $("#referral-email").prop('disabled')==false)
                {
                  if($("#referral-email").val()=="ishandeepgandhi@gmail.com")
                  {
                    next_step=false;
                    //$("#no-referral").show();
                  }
                }
               if(next_step)
               {
                data = {
                  "name":$("#form-first-name").val(),
                  "email":$("#laluram").val(),
                  "password":$("#password").val(),
                  "college":$("#form-college").val(),
                  "year":$("#id_year").val(),
                  "city":$("#form-city").val(),
                  "mobileNumber":$("#form-mobile").val(),
                  "uid":$("#uid").val(),
                  "city":$("#form-city").val(),
                  "csrfmiddlewaretoken":$("input[name=csrfmiddlewaretoken]").val()
                };
                if(!$("#referral-email").prop("disabled")) data['referral'] = $("#referral-email").val();
                console.log(data);
                $("#btn-next-page").attr("disabled",true);

                $("#btn-next-page").html("Submitting Info Please Wait !!");

                theAjax('/register/',data).done(function(response){
                  if( response == '1') {
          //$(".fb-send-to-messenger").attr(
            //"data-ref",$("#laluram").val());
          $("#personal").html('THANK YOU '+ $("#form-first-name").val() +' FOR REGISTERING<br>Checkout the <a href="/events"><u>Events</u></a> we have in store for you :) <br> (Confirmation Mail sent to your Email)');
           parent_fieldset.fadeOut(400, function() {
                $(this).next().fadeIn();
            });

        }
        else{
          console.log(response); //yahan error dikhana hai
        }
                })
                .fail(function(){
                  $("#btn-next-page").attr("disabled",false);
                  $("#btn-next-page").html("Next");
                  alert("Error Registeration. Report error at bikram.bharti99@gmail.com");
                });
                
               };
         
    });
});

