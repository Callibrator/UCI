index_functions = {}

index_functions.check_all = function(){
	$("#check-all").click(function(){
		$(".subject-checkbox").prop('checked', true);
		
	})
}

index_functions.uncheck_all = function(){
	$("#uncheck-all").click(function(){
		$(".subject-checkbox").prop('checked', false);
		
	})
}

index_functions.subject_clicked = function(){
	$(".subject_tr").click(function(target){
		
		if(target.target.type != "checkbox"){
			cbox = $(this).find(".subject-checkbox")
			x = !$(cbox).prop('checked')
			$(cbox).prop('checked', x);
		}
	})
	
}

$(document).ready(function() {
	index_functions.check_all()
	index_functions.uncheck_all()
	index_functions.subject_clicked()
  
  
});
