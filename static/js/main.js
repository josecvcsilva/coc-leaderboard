(function($) {

	"use strict";

	$('[data-toggle="tooltip"]').tooltip()

	$("#slct").change(function(){
		var val = $(this).val();
		var args = "";
		if (val !== ""){
			args = "?date=" + val
		}
		window.location.href = window.location.href.split('?')[0]+args;
	 });
})(jQuery);
