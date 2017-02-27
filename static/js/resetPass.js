jQuery(document).ready(function() {


  $(".alert-confirm-password").hide();
  $('#close-confirm-password').on('click',function(){
       $(".alert-confirm-password").hide();
    });
function validatePassword(){
        var password = document.getElementById("reset-password");
         var confirm_password = document.getElementById("reset-confirm-password");

      if((password.value != confirm_password.value) || (password.value == "") || (confirm_password.value=="")) {
        console.log("kmdkmdkm,dkmdkmdkmd,ml");
        $('.alert-confirm-password').show();
        return false;
      } else {
        console.log("kmfkmfkmfkmfkmfkm kmvkmvkmvkmkmgvkmgv mkfkm5rfkmf5kmfkm")
        $('.alert-confirm-password').hide();
        return true;
      }
    }

$('#reset-confirm-password').keyup(function(e){
    var code = (e.keyCode ? e.keyCode : e.which);
        if(code !==13)
        {
          $('.alert-confirm-password').hide();
        }
       
    });


  $("#myModal2").modal('show');
  $('#back').hide();
  $.backstretch("/1.jpg");
	
$("#new-pass-btn-close").on('click',function(e){
  window.location = "/login";
});
$("#new-pass-cross-btn").on('click',function(e){
  window.location = "/login";
});


       $('.password-form').on('submit', function(e) {
        next = true;

 $(this).find('input[type="password"]').each(function() {
                if( $(this).val() == "") {
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
                                                if(next)
                                                {
                                                next = validatePassword(); 
                                                if(!next)
                                                {
                                                e.preventDefault();
                                              }
                                            }
                                            else
                                            {
                                              e.preventDefault();
                                            }



       });


});