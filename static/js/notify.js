function context_update(){

console.log($('#badge_count span').text())
};


function notified(){
  $.ajax({
    url : "/notified/",
    type : "POST",
    dataType : "json",
    data : { msg_id : $('.checkbox').attr('id') },

    success : function(json){
      console.log(json);
    },
    error : function(xhr, errmsg, err){
      console.log(xhr.status + " : " + xhr.responseText);
    }
  });
};

$('.checkbox').on('change', function(event){
  notified();
  location.reload();


});
