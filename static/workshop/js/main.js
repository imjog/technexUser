jQuery(document).ready(function($){
	//open the lateral panel
    var x=document.getElementsByClassName("cd-btn");
    var y=document.getElementsByClassName("cd-panel");
    




	$('.cd-btn').on('click', function(event){
		event.preventDefault();
		// console.log(indexOf(x));
		var z=$.inArray(event.currentTarget,x);

		$(y[z]).addClass('is-visible');
	});
	//clode the lateral panel
	$('.cd-panel').on('click', function(event){
		if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) { 
			$('.cd-panel').removeClass('is-visible');
			event.preventDefault();
		}
	});
});