$(document).ready(function () {
	function equalcard(s) {
		var h = 0;
		var line_height = 0;
		$(s).css("display", "block").css("height", "auto");
		$(s).each(function () {
			var height = $(this).outerHeight(true);
			if (height > h) {
				h = height;
			}
		});
		$(s).height(h);
	}
	equalcard("#testimonials .container ul li p");

	// activating nav-menu elements
	$("header .nav-bar li a").click(function () {
		$("header .nav-bar li a.active").removeClass("active");
		$(this).addClass("active");
	});
	//  nav-elements-active
	$("header nav ul li").click(function () {
		$("header nav ul li.active").removeClass("active");
		$(this).addClass("active");
	});

	$(".slider-item").slick({
		autoplay: true,
		rows: 2,
		autoplaySpeed: 3000,
		arrows: false,
		draggable: true,
		infinite: true,
		pauseOnHover: false,
		slidesToShow: 2,
		slidesToScroll: 2,
		centerMode: false,
		dots: true,
		nav: false,
		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
					infinite: true,
					dots: true,
				},
				breakpoint: 980,
				settings: {
					dots: false,
				},
			},
		],
	});

	$(".testimonial-slider").slick({
		dots: false,
		arrows: true,
		infinite: true,
		pauseOnHover: true,
		speed: 1750,
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 2000,
		prevArrow:
			'<button class="slide-arrow prev-arrow"><i class="fa-solid fa-angle-left"></i></button>',
		nextArrow:
			'<button class="slide-arrow next-arrow"><i class="fa-solid fa-angle-right"></i></button>',
		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
					infinite: true,
					dots: false,
				},
			},
		],
	});

	$(".services-slider").slick({
		dots: false,
		arrows: true,
		infinite: true,
		pauseOnHover: true,
		speed: 1750,
		slidesToShow: 5,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 2000,
		prevArrow:
			'<button class="slide-arrow prev-arrow"><i class="fa-solid fa-angle-left"></i></button>',
		nextArrow:
			'<button class="slide-arrow next-arrow"><i class="fa-solid fa-angle-right"></i></button>',
		responsive: [
			{
				// breakpoint: 1024,
				// settings: {
				// 	slidesToShow: 1,
				// 	slidesToScroll: 1,
				// 	infinite: true,
				// 	dots: false,
				// },
				breakpoint: 980,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
					infinite: true,
					dots: false,
				},
			},
		],
	});

	// sticky-header
	window.onscroll = function () {
		headerFunction();
	};

	var body = document.body;
	var sticky = body.offsetTop;

	function headerFunction() {
		if (window.pageYOffset > 150) {
			body.classList.add("sticky");
		} else {
			body.classList.remove("sticky");
		}
	}

	// pagination-service-section
	var items = $(".pagination-item");
	var numItems = items.length;
	var perPage = 5;

	items.slice(perPage).hide();

	$("#pagination-container").pagination({
		items: numItems,
		itemsOnPage: 6,
		prevText: "&laquo;",
		nextText: "&raquo;",
		onPageClick: function (pageNumber) {
			var showFrom = perPage * (pageNumber - 1);
			var showTo = showFrom + perPage;
			items.hide().slice(showFrom, showTo).show();
		},
	});

	//   mobile-menu
	function MobileMenu() {
		let menuIcon = document.querySelector(".bar");
		let body = document.querySelector("body");
		let overlay = document.querySelector(".overlay");
		menuIcon.addEventListener("click", function () {
			body.classList.toggle("active");
		});
		overlay.addEventListener("click", function () {
			body.classList.remove("active");
		});
		$(".mobile-menu ul li").click(() => {
			body.classList.remove("active");
		});
		$(".mobile-menu .close").click(() => {
			body.classList.remove("active");
		});
	}
	MobileMenu();
});
var loader = document.getElementById("loader");
window.addEventListener("load", function () {
	loader.classList.add("active");
});
