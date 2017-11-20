jQuery(function($){

	window.patterns = YAML.load("pattern.yaml");

	var n = 794;

	var list = ("" + n).split("");
	_.each(list, function(i){
		i = +(i);
		console.log( patterns[i] );
		// console.log( _.sample(patterns[i]) );
	});

});