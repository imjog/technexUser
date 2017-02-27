// $(document).ready(
//   $("#update-form").hide();
// );
$(document).ready(function() {
  //  $("#update-form").hide();
   $("#edit-profile-btn").on("click",function(){
     $("#details-table").hide();
     $("#edit-profile-btn").hide();
      $("#update-form").show();

   });
   $("#close-update").on("click",function(){
     $("#update-form").hide();
    //  $("")
    $("#details-table").show();
    $("#edit-profile-btn").show();

   })
});
