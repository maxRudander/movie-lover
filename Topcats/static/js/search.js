window.onload = function() {
	searchField = document.getElementById("search-field");
	searchButton = document.getElementById("search-button");

	searchButton.addEventListener("click", search);

	function search(){
		window.location.href = "/search/" + searchField.value);
	};
};