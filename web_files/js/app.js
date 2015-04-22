$(document).ready(function() {

  // Main nav toggle
  $('.toggle-main-nav').click(function() {
    $(this).next("ul").toggleClass("active");
  });

  // Hero slider
  $('#hero-slider').slick({
    arrows: false,
    autoplay: true,
    autoplaySpeed: 3000,
    dots: true,
    fade: true,
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    speed: 1000
  });

  // Stat slider
  $('#student-stat-slider').slick({
    infinite: true,
    responsive: [{
      breakpoint: 400,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
      }
    }],
    slidesToShow: 3,
    slidesToScroll: 3,
    speed: 500
  });

  // Scroll Depth
  $.scrollDepth({
    pixelDepth: false
  });

  // Screen Time
  $.screentime({
    googleAnalytics: true,
    fields: [{
      selector: '#hc_header',
      name: 'Header'
    }, {
      selector: '#hc_slider',
      name: 'Slider'
    }, {
      selector: '#hc_cta',
      name: 'CTA Top'
    }, {
      selector: '#hc_student_life',
      name: 'Student Life'
    }, {
      selector: '#hc_student_stories',
      name: 'Student Stories'
    }, {
      selector: '#hc_student_stats',
      name: 'Student Stats'
    }, {
      selector: '#hc_fac_stories',
      name: 'Faculty Stories'
    }, {
      selector: '#hc_news',
      name: 'News'
    }, {
      selector: '#hc_announcements',
      name: 'Announcements'
    }, {
      selector: '#hc_blogs',
      name: 'Blogs'
    }, {
      selector: '#hc_soc_media',
      name: 'Social Media'
    }, {
      selector: '#hc_cta_bottom',
      name: 'CTA Bottom'
    }, {
      selector: '#hc_footer',
      name: 'Footer'
    }],
    callback: function(data) {
      console.log(data);
    }
  });
});