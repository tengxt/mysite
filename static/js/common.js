$(document).ready(function () {
    //images views
    document.addEventListener('DOMContentLoaded', function () {
        const zooming = new Zooming({
            customSize: '30%'
        });
        zooming.listen('img');
    });
	
    //scrollReveal animate
    window.scrollReveal = new scrollReveal({reset: true});

    //回到顶部
    // browser window scroll (in pixels) after which the "back to top" link is shown
    var offset = 400,
        //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        offset_opacity = 1200,
        //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,
        //grab the "back to top" link
        $back_to_top = $('.cd-top');
    $(window).scroll(function () {
        ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }
    });
    $back_to_top.on('click', function (event) {
        event.preventDefault();
        $('body,html').animate({
                scrollTop: 0,
            }, scroll_top_duration
        );
    });
    // 日期
    $(getCalendar()).appendTo(".js_time");
    // 网站运行时间
    $("#day").text(datedifference() + " (天)");
});


//运行天数
function datedifference() {
    var urodz= new Date("12/25/2018");
    var now = new Date();
    var ile = now.getTime() - urodz.getTime();
    var day = Math.floor(ile / (1000 * 60 * 60 * 24));
    return day;
}