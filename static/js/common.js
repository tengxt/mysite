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

    //图片查看
    document.addEventListener('DOMContentLoaded', function () {
            const zooming = new Zooming({
                customSize: '30%'
            });
            zooming.listen('img');
    });

    //底部栏置底
    //窗体改变大小事件
    $(window).resize(function(){
        //正文高度
        var body_height = $(document.body).outerHeight(true);
        //底部元素高度
        var bottom_height = $(".footer").outerHeight(true);
        //浏览器页面高度
        var window_height = $(window).height();
        // 宽度
        var window_width = $(window).width();
        if(window_width >= 500){
            $("#masthead").css("height","426px");
        }else {
            $("#masthead").css("height","320px");
        }
        //判断并调整底部元素的样式
        if($(".footer").hasClass('page-bottom')){
            if(body_height + bottom_height >= window_height){
                $(".footer").removeClass('page-bottom');
            }
        }else{
            if(body_height < window_height){
                $(".footer").addClass('page-bottom');
            }
        }
    });
    //页面加载时，模拟触发一下resize事件
    $(window).trigger('resize');
	
	
	
	// tags 
	var ele = $(".cloud");
	var zdheight = 320;
	var eleChlid = $(".cloud .panel-body");
	eleIsHidden(ele, zdheight, eleChlid);
});

// 设置标签的显示
function eleIsHidden(ele,zdheight,eleChlid){
	// 获取高
	var tagsHeight=ele.outerHeight(true);
	// 标签的高与指定的高比较
	if(tagsHeight > zdheight){
		// 超出隐藏
		ele.css({"overflow":"hidden", "height":zdheight+"px", "marginBottom":"20px"});
		// 声明span元素并追加
		var zkEle = $("<span class=\"tagsZkClick\">展开</span>");
		zkEle.prependTo(eleChlid);
		
		eleChlid.css({"position":"relative"});
		// 设置样式
		$(".tagsZkClick").css({
			"position":"absolute",
			"width":"100%",
			"height":"30px",
			"lineHeight":"30px",
			"top":(zdheight-75)+"px",
			"textAlign":"center",
			"backgroundColor":"#FFF",
			"cursor":"pointer",
			"color":"#c88326"
		});
		// 展开
		$(".tagsZkClick").click(function(){
			$(this).css({"display":"none"});
			ele.css({"overflow":"visible", "height":"auto","marginBottom":"40px"});
			var sqEle = $("<span class=\"tagsSqClick\">收起</span>");
			sqEle.appendTo(eleChlid);
			$(".tagsSqClick").css({
				"position":"absolute",
				"bottom":"-20px",
				"width":"100%",
				"height":"30px",
				"lineHeight":"30px",
				"textAlign":"center",
				"backgroundColor":"#FFF",
				"cursor":"pointer",
				"color":"#c88326"
			});
			// 收起
			$(".tagsSqClick").click(function(){
				$(this).remove();
				// 超出隐藏并设置展开的样式为可见
				ele.css({"overflow":"hidden", "height":zdheight+"px", "marginBottom":"20px"});
				$(".tagsZkClick").css({"display":"block"});
			});
		});
	}
}

//运行天数
function datedifference() {
    var urodz= new Date("12/25/2018");
    var now = new Date();
    var ile = now.getTime() - urodz.getTime();
    var day = Math.floor(ile / (1000 * 60 * 60 * 24));
    return day;
}

//自定义实时获取未读消息
function my_special_notification_callback(data){
    unread_count = data['unread_count'];
    if (unread_count == 0) {
        unread_count = '';
    }
    $('.live_notify_badge').text(unread_count);
}