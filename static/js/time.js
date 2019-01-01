function getCalendar() {
	var lunarInfo = new Array(0x04bd8, 0x04ae0, 0x0a570, 0x054d5, 0x0d260,
			0x0d950, 0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0, 0x0a5b6,
			0x0a4d0, 0x0d250, 0x1d255, 0x0b540, 0x0d6a0, 0x0ada2, 0x095b0,
			0x14977, 0x04970, 0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54,
			0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566, 0x0d4a0, 0x0ea50,
			0x06e95, 0x05ad0, 0x02b60, 0x186e3, 0x092e0, 0x1c8d7, 0x0c950,
			0x0d4a0, 0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0, 0x092d0,
			0x0d2b2, 0x0a950, 0x0b557, 0x06ca0, 0x0b550, 0x15355, 0x04da0,
			0x0a5d0, 0x14573, 0x052d0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6,
			0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260, 0x0f263, 0x0d950,
			0x05b57, 0x056a0, 0x096d0, 0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4,
			0x0d250, 0x0d558, 0x0b540, 0x0b5a0, 0x195a6, 0x095b0, 0x049b0,
			0x0a974, 0x0a4b0, 0x0b27a, 0x06a50, 0x06d40, 0x0af46, 0x0ab60,
			0x09570, 0x04af5, 0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58,
			0x055c0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960, 0x0d954, 0x0d4a0,
			0x0da50, 0x07552, 0x056a0, 0x0abb7, 0x025d0, 0x092d0, 0x0cab5,
			0x0a950, 0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0, 0x0a5b0,
			0x15176, 0x052b0, 0x0a930, 0x07954, 0x06aa0, 0x0ad50, 0x05b52,
			0x04b60, 0x0a6e6, 0x0a4e0, 0x0d260, 0x0ea65, 0x0d530, 0x05aa0,
			0x076a3, 0x096d0, 0x04bd7, 0x04ad0, 0x0a4d0, 0x1d0b6, 0x0d250,
			0x0d520, 0x0dd45, 0x0b5a0, 0x056d0, 0x055b2, 0x049b0, 0x0a577,
			0x0a4b0, 0x0aa50, 0x1b255, 0x06d20, 0x0ada0);
	var str = "日一二三四五六七八九十";
	var now = new Date(), SY = now.getFullYear(), SM = now.getMonth(), SD = now
			.getDate();
	var SW = now.getDay();
	var lDObj = new Lunar(now);
	var LM = lDObj.month;
	var LD = lDObj.day;
	function cyclical(num) {
		var Gan = "甲乙丙丁戊己庚辛壬癸";
		var Zhi = "子丑寅卯辰巳午未申酉戌亥";
		return (Gan.charAt(num % 10) + Zhi.charAt(num % 12));
	}
	function lYearDays(y) {
		var i, sum = 348;
		for (i = 0x8000; i > 0x8; i >>= 1)
			sum += (lunarInfo[y - 1900] & i) ? 1 : 0;
		return sum + leapDays(y);
	}
	function leapDays(y) {
		if (leapMonth(y))
			return (lunarInfo[y - 1900] & 0x10000) ? 30 : 29;
		else
			return (0);
	}
	function leapMonth(y) {
		return lunarInfo[y - 1900] & 0xf;
	}
	function monthDays(y, m) {
		return (lunarInfo[y - 1900] & (0x10000 >> m)) ? 30 : 29;
	}
	function Lunar(objDate) {
		var i, leap = 0, temp = 0;
		var baseDate = new Date(1900, 0, 31);
		var offset = (objDate - baseDate) / 86400000;
		this.dayCyl = offset + 40;
		this.monCyl = 14;
		for (i = 1900; i < 2050 && offset > 0; i++) {
			temp = lYearDays(i);
			offset -= temp;
			this.monCyl += 12;
		}
		if (offset < 0) {
			offset += temp;
			i--;
			this.monCyl -= 12;
		}
		this.year = i;
		this.yearCyl = i - 1864;
		leap = leapMonth(i);
		this.isLeap = false
		for (i = 1; i < 13 && offset > 0; i++) {
			if (leap > 0 && i == (leap + 1) && this.isLeap == false) {
				--i;
				this.isLeap = true;
				temp = leapDays(this.year);
			} else {
				temp = monthDays(this.year, i);
			}
			if (this.isLeap == true && i == (leap + 1))
				this.isLeap = false;
			offset -= temp;
			if (this.isLeap == false)
				this.monCyl++;
		}
		if (offset == 0 && leap > 0 && i == leap + 1)
			if (this.isLeap) {
				this.isLeap = false;
			} else {
				--i;
				this.isLeap = true;
				--this.monCyl;
			}
		if (offset < 0) {
			offset += temp;
			--i;
			--this.monCyl;
		}
		this.month = i;
		this.day = offset + 1;
	}
	function YYMMDD() {
		var cl = '<font color="#333">';
		if (SW == 0)
			cl = '<font color="#333">';
		if (SW == 6)
			cl = '<font color="#333">';
		return (cl + SY + '年' + (SM + 1) + '月' + SD + '日</font>');
	}
	function weekday() {
		var cl = '<font color="#ff0000">';
		if (SW == 0 || SW == 6)
			cl = '<font color="#ff0000">';
		return cl + "星期" + str.charAt(SW) + '</font>';
	}
	function cDay(m, d) {
		var nStr = "初十廿卅　", s;
		if (m > 10)
			s = '十' + str.charAt(m - 10);
		else
			s = str.charAt(m);
		s += '月';
		switch (d) {
		case 10:
			s += '初十';
			break;
		case 20:
			s += '二十';
			break;
		case 30:
			s += '三十';
			break;
		default:
			s += nStr.charAt(Math.floor(d / 10));
			s += str.charAt(d % 10);
		}
		if (lDObj.isLeap)
			s = "闰" + s;
		return (s);
	}
	function lunarTime() {
		//return ('<font color="#006600">' + cyclical(SY - 4) + '年 ' + cDay(LM, LD) + '</font>');
		return ('<font color="#333">' + cDay(LM, LD) + '</font>');
	}
	function specialDate() {
		var sTermInfo = new Array(0, 21208, 42467, 63836, 85337, 107014,
				128867, 150921, 173149, 195551, 218072, 240693, 263343, 285989,
				308563, 331033, 353350, 375494, 397447, 419210, 440795, 462224,
				483532, 504758);
		var solarTerm = new Array("小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明",
				"谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
				"秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至");
		var lFtv = "0101春节0115元宵节0505端午节0707七夕情人节0715中元节0815中秋节0909重阳节1208腊八节1224小年0100除夕";
		var sFtv = "0101元旦0214情人节0308妇女节0312植树节0315消费者权益日0401愚人节0501劳动节0504青年节0512护士节0601儿童节0701建党节香港回归纪念0801建军节0808父亲节0909毛主席逝世纪念0910教师节0928孔子诞辰1001国庆节1006老人节1024联合国日1112孙中山诞辰1220澳门回归纪念1225圣诞节1226毛主席诞辰";
		var tmp1, tmp2, festival = '';
		tmp1 = new Date(
				(31556925974.7 * (SY - 1900) + sTermInfo[SM * 2 + 1] * 60000)
						+ Date.UTC(1900, 0, 6, 2, 5));
		tmp2 = tmp1.getUTCDate();
		if (tmp2 == SD)
			festival += ' <p class="js_time_jieqi">节气：' + solarTerm[SM * 2 + 1]+ '</p>';
		tmp1 = new Date(
				(31556925974.7 * (SY - 1900) + sTermInfo[SM * 2] * 60000)
						+ Date.UTC(1900, 0, 6, 2, 5));
		tmp2 = tmp1.getUTCDate();
		if (tmp2 == SD)
			festival += ' <p class="js_time_jieqi">节气：' + solarTerm[SM * 2] + '</p>';
		var reg = new RegExp((LM < 10 && "0" || "") + LM
				+ (LD < 10 && "0" || "") + LD + '([^\\d]+)', '');
		if (lFtv.match(reg) != null)
			festival += ' <p class="js_time_jieqi">' + RegExp.$1 + '</p>';
		reg = new RegExp((SM < 9 && "0" || "") + (SM + 1)
				+ (SD < 10 && "0" || "") + SD + '([^\\d]+)', '');
		if (sFtv.match(reg) != null)
			festival += ' <p class="js_time_jieqi">' + RegExp.$1 + '</p>';
		return (festival);
	}
	return YYMMDD() + ' ' + weekday() + ' ' + lunarTime() + specialDate();
}