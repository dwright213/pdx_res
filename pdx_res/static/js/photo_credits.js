
var
	imageName = $('#main>div').css('background-image'),
	photog = imageName.split('-')[1].replace('_', ' ');

console.log(photog);
$('div#photocredit>div').attr('data-content', 'photo: ' + photog)
