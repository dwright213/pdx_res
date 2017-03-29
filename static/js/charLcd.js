// $( document ).ready(function() {
// 	var
// 	dPixels = [4,9,11,12,14,15,18,19,20,24,25,29,31,32,33,34],
// 	aPixels = [11,12,13,19,21,22,23,24,25,29,31,32,33,34],
// 	nPixels = [10,12,13,15,16,19,20,24,25,29,30,34],
// 	clearPixels = [],
// 	usePixels = [],
// 	char1 = $('[class^=digit-pixel-1]'),
// 	char2 = $('[class^=digit-pixel-2]'),
// 	char3 = $('[class^=digit-pixel-3]'),
// 	from = document.referrer,
// 	host = window.location.host;

// 	// console.log(host);
// 	// console.log(from);
// 	// console.log(from.indexOf(host));

// 	function pushArray(pixels, character) {

// 		// and push the new pixels in
// 		for (var i = character.length - 1; i >= 0; i--) {
// 			if (pixels.indexOf(i) > -1) {
// 				usePixels.push($(character[i]))
// 			}
// 		}
// 	}

// 	function pixelFlip(pixels) {
// 		$(usePixels).toggleClass('pixel-on');
// 		usePixels = [];
// 	}

	// if (from.indexOf(host) > -1) {
	// 	pushArray(dPixels, char1);
	// 	pushArray(aPixels, char2);
	// 	pushArray(nPixels, char3);
	// 	pixelFlip(usePixels);

	// } else {
	// 	pushArray(dPixels, char1);
	// 	pushArray(aPixels, char2);
	// 	pushArray(nPixels, char3);
	// 	pixelFlip(usePixels);
	// }

	// $('a.clickme').on('click',function(){
	// 	pushArray(dPixels, char1);
	// 	pixelFlip(usePixels);
	// });

	// $('a.clickme2').on('click',function(){
	// 	pushArray(aPixels, char2);
	// 	pixelFlip(usePixels);
	// });

	// $('a.clickme3').on('click',function(){
	// 	pushArray(nPixels, char3);
	// 	pixelFlip(usePixels);
	// });

	// $('a.clickme4').on('click',function(){
	// 	pushArray(clearPixels, char1);
	// 	pushArray(clearPixels, char2);
	// 	pushArray(clearPixels, char3);
	// 	pixelFlip(usePixels);
	// });
// });
