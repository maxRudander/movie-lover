// Author: Christopher

// Gör så att flash-meddelandena fadear efter några sekunder
$(document).ready(function(){
	setTimeout(function() {
		$(".fade-out-three-seconds").fadeOut(1000);
	}, 3000);
});
