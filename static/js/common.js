$(document).ready(function () {
	
    //检测ie 6789
    if (!(/msie [6|7|8|9]/i.test(navigator.userAgent))) {
        window.scrollReveal = new scrollReveal({reset: true});
    }
    // 日期
    $(getCalendar()).appendTo(".js_time");
    
    // 标签云
    var array = [
            {text: "python", weight: 13,},
    		{text: "Django", weight: 10.5},
    		{text: "Java", weight: 9.4}
      ];
    $("#tag").jQCloud(array, {
        removeOverflowing: true,
        shape: "elliptic",
        height: 300
    });  
      
});