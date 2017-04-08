// define(scroller["vendor/jquery"],function($){
	// You can avoid the document.ready if you put the script at the bottom of the page
	$(document).ready(function() {
	  // Bind to the click of all links with a #hash in the href
	  $('a[href^="/#"], a[href^="#"], a').click(function(e) {
	  	var navbarHeight = $('nav.navbar').outerHeight();

	    // Prevent the jump and the #hash from appearing on the address bar
	    // Scroll the window, stop any previous animation, stop on user manual scroll
	    // Check https://github.com/flesler/jquery.scrollTo for more customizability
	    if (location.pathname == this.pathname && location.host == this.host) {
	    	e.preventDefault();
	    	$(window).stop(true).scrollTo(this.hash, {
	    		duration:700,
	    		interrupt:true,
	    		offset: -30
	    	});
	    }
	  });

	  $('.navbar-collapse a, a.navbar-brand').click(function(){
    	$(".navbar-collapse").collapse('hide');
		});

	});
// })