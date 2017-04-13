
var
	imageName = $('#main>div').css('background-image'),
	photog = imageName.split('-')[1];

console.log(photog);
$('div#photocredit>div').attr('data-content', photog)
