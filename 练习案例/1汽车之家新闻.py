import requests
from bs4 import BeautifulSoup
# pip3 install requests
# pip3 install BeautifulSoup4
# 练习题一：获取一个
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# soup = BeautifulSoup(response.text,'html.parser')
# tag = soup.find(id='auto-channel-lazyload-article')
# h3 = tag.find(name='h3')
# print(h3)
# 找到所有新闻
# 标题，简介，url，图片
# response = requests.get('http://www.autohome.com.cn/news/')
# response.encoding = 'gbk'
# print(response.text)
# soup = BeautifulSoup(response.text,'html.parser')

html = """

<!doctype html>
<html>
<head>
	<meta charset="gb2312" />
	<title>【图】最新汽车新闻_资讯_汽车之家</title>
<meta name="keywords" content="最新汽车新闻,汽车新闻">
<meta name="description" content="汽车之家新闻频道提供国产新车,进口新车,汽车热点追踪,汽车行业动态,车闻轶事,人物访谈等最新信息."><meta http-equiv="mobile-agent" content="format=html5; url=https://m.autohome.com.cn/news/" /><meta http-equiv="mobile-agent" content="format=xhtml; url=https://m.autohome.com.cn/news/" /><link rel="canonical" href="https://www.autohome.com.cn/news/" /><link rel="alternate" media="only screen and (max-width: 640px)"  href="https://m.autohome.com.cn/news/"/>
    <meta name="robots" content="all" />
	<link href="//x.autoimg.cn/com/bo.ashx?path=|as|css-2.0.2|global|autoshow.css,|as|css-2.0.2|infor|focusimg.css,|as|css-2.0.2|infor|nav-typebar.css,|as|css-2.0.2|infor|page.css,|as|css-2.0.2|infor|search.css,|as|css-2.0.2|public|btn.css,|as|css-2.0.2|public|icon.css,|as|static|monkey.css" rel="stylesheet">
    <!-- start Dplus -->
<!--<script type="text/javascript">!function(a,b){if(!b.__SV){var c,d,e,f;window.dplus=b,b._i=[],b.init=function(a,c,d){function g(a,b){var c=b.split(".");2==c.length&&(a=a[c[0]],b=c[1]),a[b]=function(){a.push([b].concat(Array.prototype.slice.call(arguments,0)))}}var h=b;for("undefined"!=typeof d?h=b[d]=[]:d="dplus",h.people=h.people||[],h.toString=function(a){var b="dplus";return"dplus"!==d&&(b+="."+d),a||(b+=" (stub)"),b},h.people.toString=function(){return h.toString(1)+".people (stub)"},e="disable track track_links track_forms register unregister get_property identify clear set_config get_config get_distinct_id track_pageview register_once track_with_tag time_event people.set people.unset people.delete_user".split(" "),f=0;f<e.length;f++)g(h,e[f]);b._i.push([a,c,d])},b.__SV=1.1,c=a.createElement("script"),c.type="text/javascript",c.charset="utf-8",c.async=!0,c.src="//w.cnzz.com/dplus.php?id=1262640694",d=a.getElementsByTagName("script")[0],d.parentNode.insertBefore(c,d)}}(document,window.dplus||[]),dplus.init("1262640694");</script>-->
<!-- end Dplus -->

<!--<script type="text/javascript">
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?9924a05a5a75caf05dbbfb51af638b07";
        var s = document.getElementsByTagName("script")[0]; 
        s.parentNode.insertBefore(hm, s);
    })();
</script>-->
    <link href="" rel="stylesheet">
    <style type="text/css">
        @charset "UTF-8";a.more{display:inline-block;position:absolute;right:10px;top:0;z-index:200;font-size:12px;font-weight:100;font-family:"\5B8B\4F53"}a.more:link,a.more:visited{color:#666;text-decoration:none}a.more:hover{color:#d60000;text-decoration:underline}.navFixed{position:fixed;_position:absolute;top:0;z-index:990}.hot-title,.relative{position:relative}.nav-typebar{width:990px}.subnav{margin-top:10px;margin-bottom:20px}.subnav-title-name{padding-bottom:5px;font:700 22px/1.5 'Microsoft YaHei',arial,tahoma,sans-serif;color:#3a5998}.subnav-title-ad{padding:3px 0 0 15px}.subnav-title-ad img{vertical-align:top;width:65px;height:30px;*margin-top:-4px}.subnav-title-ad span{font:16px 'Microsoft YaHei',arial,tahoma,sans-serif;line-height:30px}.advbox{line-height:0}.icon-tuiguang{display:inline-block;height:12px;padding:1px 1px 1px 2px;background-color:#d60000;overflow:hidden;vertical-align:middle;text-align:center;font-family:"\5B8B\4F53",arial,tahoma,sans-serif;font-weight:400;font-style:normal;font-size:12px;line-height:12px;color:#fff;-webkit-border-radius:2px;-moz-border-radius:2px;border-radius:2px}.advlist{margin:10px 0;font-size:14px;font-weight:700;line-height:20px}.advlist i{float:left;margin:1px 0 0}.advlist li,.advlist ul{float:left}.advlist li{width:194px;padding-left:6px}.advlist a{color:#666}.advlist a:hover{color:#d60000;text-decoration:underline}.news,.news-focus p{height:36px;color:#666}.grid-left{padding-right:20px;border-right:1px solid #f0f0f0}.content .row .grid-right{width:309px;margin-left:20px;_margin-left:10px}.num-big{font-size:32px}.num-small{font-size:18px}.news{width:545px;line-height:18px}.news-focus h2{font:28px/1.5 'Microsoft YaHei',arial,tahoma,sans-serif}.news-focus p{line-height:18px;margin-bottom:15px}.article-wrapper ul,.article-wrapper ul li a:link,.article-wrapper ul li a:visited{color:#999}.news-focus .focusimg02 .focusimg-pic,.news-focus .focusimg02 .focusimg-pic ul{height:413px}.news-focus .focusimg02 .focusimg-bt-left,.news-focus .focusimg02 .focusimg-bt-right{height:323px;top:90px}.news-focus .focusimg02 .focusimg-bt a{margin-top:130px}.news-focus .focusimg02 .focusimg-bt-left{left:0;padding-left:10px}.news-focus .focusimg02 .focusimg-bt-right{right:0;padding-right:10px}.article-wrapper{width:630px;margin-top:10px}.article-wrapper ul li{height:100px;padding-top:10px}.article-wrapper ul li a{display:block;*display:inline-block;width:620px;height:100px;padding:0 5px;overflow:hidden;cursor:pointer}.loading,.loading-cont,.loadmore{display:inline-block}.article-wrapper ul li a:hover{text-decoration:none;background-color:#f9f9f9}.article-wrapper ul li img{float:left;margin-right:15px;padding-top:5px}.article-wrapper ul li h3{line-height:30px;font-family:\5FAE\8F6F\96C5\9ED1;font-size:18px;color:#3b5998}.article-wrapper ul li h3 i{margin-left:10px}.article-wrapper ul li .article-bar{height:21px;line-height:21px;overflow:hidden;padding-bottom:5px}.article-wrapper ul li .article-bar em{display:inline-block;line-height:16px;padding-left:20px;font-size:12px}.article-wrapper ul li .article-bar i{float:left;margin:2px 3px 0 0}.article-wrapper ul li p{line-height:22px}.loading,.loadmore{width:630px;height:40px;border-radius:5px;background:#efefef;text-align:center;font:700 18px/40px "\5B8B\4F53",arial,tahoma,sans-serif;color:#666}.loadmore:hover{background:#333;text-decoration:none;color:#fff}.loading{margin-top:20px}.loading img{margin-top:10px;margin-left:5px;vertical-align:top}.loading:hover{text-decoration:none;color:#666}.page{margin-top:20px}.editorblog,.hot{margin-top:15px;margin-bottom:15px}.hot-title{_margin-top:2px}.editorblog-title,.hot-title{border-bottom:2px solid #3b5998;padding-bottom:12px;font:700 14px/14px "\5B8B\4F53",arial,tahoma,sans-serif}.hot-more{float:right;font-weight:400;font-style:normal;font-size:12px}.comment-ul li{width:309px;margin-bottom:20px;vertical-align:top}.comment-tittle{height:23px;font-size:12px;color:#999;white-space:nowrap}.comment-tittle div{line-height:20px}.comment-tittle a{font-size:14px}.comment-tittle .comment-pic{width:30px;height:30px;float:left;margin-right:10px}.comment-content{margin-bottom:9px;*margin-bottom:6px}.comment-content a{display:block;*display:inline-block;width:307px;position:relative;border:1px solid #ccd3e4;background-color:#f9f9f9;-moz-border-radius:3px;border-radius:3px}.comment-content p{line-height:22px;padding:10px 10px 12px;color:#666;word-break:break-all}.comment-content-author{color:#999}.comment-content-arrow{background:url(//x.autoimg.cn/www/channnel/2014/images/artjt-bg.png);width:10px;height:11px;overflow:hidden;position:absolute;bottom:-11px;left:14px}.comment-popup,.pop-content{position:relative;cursor:pointer}.comment-content a:hover{text-decoration:none;background-color:#efefef}.comment-content a:hover .comment-content-author,.comment-content a:hover p{color:#3b5998}.comment-content a:hover .comment-content-arrow{background-position:-20px 0}.editorblog{margin-top:20px}.editor-change{float:right;margin-top:2px;height:12px;line-height:12px}.editor-change:hover i{background-position:-100px -80px}.editor-change:hover a{text-decoration:underline;color:red}.editor-change i{vertical-align:middle;margin-top:-2px;*margin-right:5px}.hot-article-wrap li{width:297px;border-bottom:1px dotted #d0d0d0;color:#999;padding-top:18px;padding-bottom:10px;overflow:hidden;_display:inline-block}.hot-intro{line-height:22px}.editor-wrap img,.hot-article-wrap img,.hot-comment-wrap .avatar{margin-right:10px;float:left}.hot-comment-wrap .avatar{margin-top:5px}.hot-article-wrap h2{margin-bottom:10px;font:700 16px/24px "Microsoft YaHei",arial,tahoma,sans-serif}.editor-wrap li,.hot-comment-wrap li{margin-top:15px;color:#999}.hot-article-rec{padding-top:10px}.hot-article-rec img{vertical-align:top}.hot-article-rec li{float:left;width:140px;margin:6px 10px 0 0;text-align:center}.hot-article-rec li p{margin:5px 0}.coo-media .media-abstract{font-size:14px;line-height:26px;padding-top:5px}.coo-media .media-abstract p{background:url(//x.autoimg.cn/www/channnel/2014/images/icon-square.png) 0 12px no-repeat;padding-left:13px}.editor-wrap li{height:55px;width:154px;float:left}.comment-link{margin-left:8px}.comment-wrapper i,.view-wrapper i{vertical-align:sub;*vertical-align:middle}.comment-popup{display:block;margin-top:10px;margin-bottom:9px;border:1px solid #ccd3e4;background:#f9f9f9;padding:10px;-moz-border-radius:3px;border-radius:3px}.div-fouc-tx ul li,.div-fouc-tx ul li a,.pop-content,.tuiguang i,.tuiguang li,.tuiguang ul,.tuiguang-arrow{display:inline-block}.user-right{height:23px;padding-left:32px;font-size:14px}.comment-from{line-height:14px;padding-bottom:2px;color:#999;white-space:nowrap}.comment-num,.view-num{*margin-left:5px}.pop-content{color:#666;z-index:10}.btns,.btns i{position:absolute}.editorname{margin-top:1px}.editorname a{font:700 14px/14px "\5B8B\4F53",arial,tahoma,sans-serif}.grid-right .advbox{width:290px}.btns{width:74px;height:37px;right:0;top:45px}.btns i{top:50%;left:50%;margin-top:-8px;margin-left:-8px}.app-ad{margin:15px auto 20px}.tuiguang{margin-top:15px;font-size:14px;line-height:16px}.tuiguang i{position:relative;float:left;margin-right:10px;height:14px;line-height:14px;background:#D60000;color:#FFF;font-style:normal;font-size:12px;vertical-align:top;padding:1px}.tuiguang-arrow{width:0;height:0;float:left;line-height:0;margin-left:-10px;border-left:8px solid #D60000;border-top:7px solid #FFF;border-bottom:8px solid #FFF}.tuiguang ul{width:600px}.tuiguang li{width:200px;float:left}.tuiguang a{color:#666;font-weight:700}.news-item h1{font:28px/1.5 'Microsoft YaHei',arial,tahoma,sans-serif}.btn-small.btn-blue.icon16-search1{_background:url(//x.autoimg.cn/as/images/ie6-search-icon.png) no-repeat}.gotop02{position:fixed;_position:absolute;left:50%;margin-left:505px}.article img,.hot-article-wrap img{width:120px;height:90px}.editor-wrap img{width:40px;height:52px}.m-nav-title{height:28px;line-height:28px;border:1px solid #ccd3e4;position:relative;padding:0 0 0 10px;clear:both;font-weight:700;color:#333;font-size:14px;margin:25px 0 -5px}.m-nav-title-border{height:27px;line-height:27px;border:1px solid #ccd3e4;border-top:solid 2px #3b5998}.m-nav-title h3{padding:0 15px 0 0;float:left;color:#333}.m-nav-title h3 a:link,.m-nav-title h3 a:visited{color:#333}.m-nav-title h3 a:hover{text-decoration:none;color:#d60000}.m-nav-title h3.h3cur a:link,.m-nav-title h3.h3cur a:visited{color:#3b5998;font-weight:700}.m-nav-title .div-fouc{float:left;width:582px}.m-nav-title .div-fouc-bt{width:16px}.m-nav-title .div-fouc-bt-left{float:left;margin:3px 15px 0 0;*margin:5px 15px 0 0}.m-nav-title .div-fouc-bt-right{float:right;margin:3px 0 0 10px;*margin:5px 0 0 10px}.m-nav-title .div-fouc-tx{width:525px;float:left;overflow:hidden;height:27px;line-height:27px;position:relative}.div-fouc-tx ul{width:525px;height:27px;position:absolute;opacity:0;filter:0}.div-fouc-tx ul.fouc-current{z-index:10;opacity:10}.div-fouc-tx ul li{float:left;height:27px;padding:0}.div-fouc-tx ul li a{padding:0 9px;width:auto;float:left;font-weight:400}.div-fouc-tx ul li a:link,.div-fouc-tx ul li a:visited{color:#333}.div-fouc-tx ul li a:hover{color:#d60000;text-decoration:none}.div-fouc-tx ul li.current{background-color:#fff;text-decoration:none}.div-fouc-tx ul li.current a:link,.div-fouc-tx ul li.current a:visited{color:#3b5998;font-weight:700}.flos{margin:50px auto;text-align:center}.aname{font-size:0;line-height:0}.wide-body .content,.wide-body .content .subnav .nav-typebar{width:1000px}.wide-body .content .row .grid-left{padding-left:19px}.wide-body .content .row .grid-right{width:300px}.wide-body .content .row .grid-right .hot-article-rec ul{width:302px}.wide-body .content .row .grid-right .hot-article-rec li{width:136px;margin:6px 15px 0 0}.wide-body .content .row .grid-right .hot-article-rec img{width:136px;height:78px}.wide-body .content .row .grid-right .hot-article-wrap li{width:300px}.wide-body .content .row .grid-right .editor-wrap li{width:150px}.wide-body .content .row .grid-right .advbox{width:300px}.wide-body .mini-main{width:1000px}.wide-body .header-main{width:1000px}.wide-body .topbar-header-main{width:1000px}.wide-body .footer_auto{width:1000px}
    </style>
    <meta name="apple-itunes-app" content="app-id=415842508">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="renderer" content="webkit" />
<script src="//x.autoimg.cn/bi/mda/ahas_head.min.js?v=20180205"></script>
<style type="text/css">.mini-left,.mini-left li,.mini-logo,.topbar-tip{float:left}.find-club a,.mini-logo img{vertical-align:top}.citypop-ct ul li a,.citypop-scity dl,.citypop-scity dl dd,.topbar-clearfix{zoom:1}.citypop-ct ul,.pop_forum ol,.pop_login ul{list-style:none}.topbar{position:relative;z-index:10000;_zoom:1}.topbar-helper{z-index:999}.citypop-close i,.citypop-ct .ntextdicon,.citypop-ct .zdicon,.citypop-search,.navcar .icon-newcar,.topbar-icon{background:url(//x.autoimg.cn/www/common/images/topbar-bg_20150728.png) no-repeat}.moreli-title-app,.moreli-title-notice{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAAMCAMAAACUVSdlAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjQ5NzQ3MUEwMDMxOTExRTRCNjU2OTE4QzQ2NEQ5NEQ5IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjQ5NzQ3MUExMDMxOTExRTRCNjU2OTE4QzQ2NEQ5NEQ5Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NDk3NDcxOUUwMzE5MTFFNEI2NTY5MThDNDY0RDk0RDkiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6NDk3NDcxOUYwMzE5MTFFNEI2NTY5MThDNDY0RDk0RDkiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5hF5cPAAAABlBMVEXS0tIAAACF+VnAAAAADklEQVR42mJgwA4AAgwAABgAAWQOeGIAAAAASUVORK5CYII=) no-repeat;_background:url(//x.autoimg.cn/www/common/images/split_bg.png) no-repeat}.citypop,.topbar-dropdown,.topbar-tip{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAAbSURBVHjaYjQ2NpZiIAIwMRAJRhVSRyFAgAEALsEAx5m+/ZYAAAAASUVORK5CYII=);_background:url(//x.autoimg.cn/as/images/shadow_bg.png?v=20140322)}.topbar-clearfix:after{visibility:hidden;display:block;font-size:0;content:" ";clear:both;height:0}.topbar-icon,.topbar-tip .topbar-tip-arrow{display:inline-block;overflow:hidden}.topbar-icon16{width:16px;height:16px}.topbar-icon12{width:12px;height:12px}.topbar-icon10{width:10px;height:10px}.topbar-icon10-sjb{background-position:0 -205px}.topbar-icon12-array1{background-position:-40px -165px}.topbar-icon16-club{background-position:-20px -165px}.topbar-icon16-building{background-position:-60px -405px}.topbar-icon-fm{width:18px;height:16px;background-position:0 -434px}.topbar-icon-close{width:12px;height:12px;background-position:-22px -367px}.topbar-tip{min-width:50px;max-width:250px;position:absolute;z-index:100;padding:2px;font-size:12px}.topbar-tip .topbar-tip-content{position:relative;z-index:1;border:1px solid #ccd3e4;background-color:#FFF;padding:5px;line-height:18px;font-size:12px}.topbar-tip .topbar-tip-arrow{position:absolute;z-index:2;background:url(//x.autoimg.cn/as/images/layer_arrow24.png?v=20141215) no-repeat;_background:url(//x.autoimg.cn/as/images/layer_arrow8.png?v=20141215) no-repeat}.citi-active,.moreli-active,.moreli-fm{z-index:800}.topbar-tip .topbar-tip-bottom{width:15px;height:11px;top:-8px;left:43%;background-position:0 -26px}.topbar-tip .topbar-tip-left{width:11px;height:15px;top:30%;right:-8px;background-position:-30px -29px}.topbar-dropdown{width:80px;position:absolute;display:none;padding:2px;font-size:12px}.topbar-dropdown dl{border:1px solid #ccd3e3;background-color:#fff}.topbar-dropdown dd a{display:block;text-align:left;height:27px;line-height:27px;color:#666;text-decoration:none;padding:0 6px}.topbar-dropdown dd a:hover{background-color:#f1f5f8;color:#3b589a}.minitop{background-color:#333;color:#999}.mini-main{margin:0 auto;width:1000px;height:30px;line-height:30px}.mini-main a:hover{text-decoration:underline}.mini-main a.orangelink:hover,.mini-main a.orangelink:link,.mini-main a.orangelink:visited{color:#f60}.mini-main a.greylink:link,.mini-main a.greylink:visited{color:#999}.mini-main a.greylink:hover{color:#f60}.mini-main a.whitelink:link,.mini-main a.whitelink:visited{color:#fff}.mini-main a.whitelink:hover{color:#f60}.mini-main li.vlli{padding:0 5px}.mini-left ul{padding-left:184px}.mini-left li{position:relative}.mini-left .topbar-icon16-building{float:left;margin:7px 5px 0 0}.mini-right{float:right}.mini-right li{float:left;position:relative;z-index:800}.mini-right li.frs-login{padding-right:14px}.mini-right .frs-login a{padding:0 2px}.mini-right .frs-login a:link,.mini-right .frs-login a:visited{color:#fff}.mini-right .frs-login a.minitop-uname:hover,.mini-right .frs-login a.minitop-uname:link,.mini-right .frs-login a.minitop-uname:visited,.mini-right .frs-login a:hover{color:#f60}.mini-right .frs-login a.minitop-logoff:link,.mini-right .frs-login a.minitop-logoff:visited{color:#999}.mini-right .frs-login a.minitop-jifen-link:hover,.mini-right .frs-login a.minitop-jifen-link:link,.mini-right .frs-login a.minitop-jifen-link:visited,.mini-right .frs-login a.minitop-logoff:hover{color:#f60}.mini-right li.frs-zhaopin{padding:0 14px}.moreli-title{float:left;height:30px;*vertical-align:middle}.moreli-title a{display:block;_display:inline-block;height:30px;padding:0 14px;cursor:pointer}.moreli-title a:hover,.moreli-title a:link,.moreli-title a:visited{color:#999}.moreli-title a:hover{text-decoration:none}.moreli-title i,.moreli-title span{float:left;cursor:pointer}.moreli-title .topbar-icon10-sjb{position:relative;margin-left:5px;top:10px}.moreli-title .topbar-icon16{margin:8px 5px 0 0}.moreli-title .topbar-icon12{margin:10px 7px 0 0}.moreli-title .topbar-icon-fm{margin:7px 5px 0 0}.moreli-title-notice{background-position:left center}.moreli-title-notice span.info{display:inline-block;height:12px;padding:2px 3px;text-align:center;line-height:12px;background-color:#f60;border-radius:2px;color:#fff;margin:7px 1px 0 5px;font-weight:700}.moreli-title-club a{background-color:#f60}.moreli-title-club span{color:#fff}.moreli-title-club .topbar-icon10-sjb{background-position:-20px -205px}.moreli-title-app{background-position:left center}.moreli-active .active-bg{background-color:#f9f9f9}.moreli-active .moreli-title span{color:#666}.moreli-active .moreli-title-notice span.info{color:#fff}.moreli-active .moreli-title .topbar-icon12-array1{background-position:-60px -165px}.moreli-active .moreli-title .topbar-icon16-club{background-position:0 -165px}.moreli-active .moreli-title .topbar-icon10-sjb{background-position:-60px -205px}.moreli-title-fm a:hover .topbar-icon-fm{background-position:-22px -434px}.moreli-fm{position:relative}.moreli-fm .topbar-tip{width:178px;top:30px;left:0}.moreli-fm .topbar-tip .topbar-tip-content{padding:8px}.moreli-fm .topbar-tip .topbar-tip-bottom{left:25px}.citi-title a{padding:0 0 0 6px}.citi-title .topbar-icon10-sjb{margin-left:2px}.citi-title a:hover .topbar-icon10-sjb{background-position:-60px -205px}.find-club{padding:0 14px}.find-club a{display:inline-block;height:20px;line-height:20px;padding:0 20px;background-color:#f60;color:#fff;border-radius:2px;margin-top:5px;_margin-top:5px}.find-club a:hover,.find-club a:link{color:#fff;text-decoration:none}.topchadiv{position:absolute;right:-2px;top:31px;z-index:10;*background-image:url(about:blank);display:none}.topchadiv-dw02,.topchadiv-dw03{_right:-3px}.topchadiv-box{padding:0 2px 2px 0;clear:both;position:relative;top:-1px}.topchadiv-dw01 .topchadiv-box{width:110px}.topchadiv-dw02 .topchadiv-box{min-width:130px;overflow:visible;_width:130px}.topchadiv-dw03 .topchadiv-box{width:210px}.topchadiv-con{border:1px solid #ccd3e4;background-color:#fff;line-height:20px;text-align:left;padding:5px 0}.topchadiv-con a{display:block;height:27px;line-height:27px;white-space:nowrap;padding:0 15px;overflow:hidden}.topchadiv-con a:hover,.topchadiv-con a:link,.topchadiv-con a:visited{color:#666;text-decoration:none}.topchadiv-con a span{display:inline-block}.topchadiv-con a span.cn{color:#666;float:left}.topchadiv-con a span.ck{cursor:pointer;float:right}.topchadiv-con a:hover{color:#3b5998;background-color:#f9f9f9}.topchadiv-con .linedc{border-top:dotted 1px #cecece;height:1px;clear:both;font-size:0;margin:5px;line-height:0}.topchadiv-dw02 .topchadiv-con a{min-width:120px;overflow:visible}.topchadiv-dw03 .topchadiv-con a{padding:0 10px}.topchadiv-dw03 .topchadiv-con a:hover,.topchadiv-dw03 .topchadiv-con a:link,.topchadiv-dw03 .topchadiv-con a:visited{color:#3b5998}.topbar-header{position:relative;height:85px;margin-bottom:10px;background-color:#efefef}.topbar-header-blue{width:100%;height:35px;background-color:#3b5998;position:absolute;top:0;left:0;overflow:hidden}.topbar-header-main{width:1000px;height:85px;margin:0 auto;position:relative;z-index:100}.topbar-header .logo{width:170px;height:90px;float:left;background-color:#fff;position:relative;top:-5px;margin-bottom:-5px}.topbar-header .logo-shadow1{width:0;height:0;overflow:hidden;border:6px solid #333;border-left-color:#999;border-right:0;position:absolute;top:-5px;left:170px}.topbar-header .logo-shadow2{display:inline-block;width:6px;height:7px;overflow:hidden;background-color:#3b5998;position:absolute;top:0;left:170px}.topbar-header .nav{width:820px;height:87px;float:right;position:relative;top:-2px;margin-bottom:-2px;z-index:10}.topbar-header .navlink{width:820px}.topbar-header .navlink ul{height:37px;}.topbar-header .navlink li{float:left;position:relative}.topbar-header .navlink a.navlink-item{display:inline-block;height:37px;line-height:40px;float:left;overflow:hidden;text-align:center;font-size:14px;font-weight:700}.topbar-header .navlink a.navlink-item:link,.topbar-header .navlink li a.navlink-item:visited{color:#fff;text-decoration:none}.topbar-header .navlink a.navlink-item:hover,.topbar-header .navlink li a.navlink-item-current{color:#fff;text-decoration:none;background-color:#57b}.topbar-header .navlink a.navlink-item .topbar-icon10-sjb{float:right;position:relative;top:15px;right:1px;width:7px;background-position:-21px -205px}.topbar-header .navlink a.navlink-item sup{font-size:12px;line-height:0;position:relative;vertical-align:baseline;top:-.5em;font-weight:400}.topbar-header .navlink a.nw-2{width:43px}.topbar-header .navlink a.nw-25{width:51px}.topbar-header .navlink a.nw-2arrow{width:49px;padding-right:6px}.topbar-header .navlink a.nw-3{width:62px}.topbar-header .navlink a.nw-4{width:78px}.topbar-header .navlink .topbar-dropdown{width:80px;left:-2px;top:35px;background-image:none;font-family:"\5B8B\4F53",simsun,arial,tahoma,sans-serif}.topbar-header .navcar ul{width:814px;height:50px;padding-left:6px}.topbar-header .navcar li{width:72px;height:50px;line-height:14px;text-align:center;float:left}.topbar-header .navcar li a{display:block;height:25px;line-height:22px;padding-top:25px}.topbar-header .navcar li.navcar07{position:relative}.topbar-header .navcar li.navcar07 .topbar-icon10-sjb{float:right;position:relative;top:6px;right:21px}.topbar-header .navcar li a:hover .topbar-icon10-sjb{background-position:-60px -205px}.topbar-header .navcar li.navcar07 div.topbar-dropdown{width:78px;left:-2px;top:48px}.topbar-header .navcar li.navcar07 div.topbar-dropdown a{background:0 0;height:27px;line-height:27px;padding:0 6px}.topbar-header .navcar li.navcar07 div.topbar-dropdown a:hover{background-color:#f1f5f8;color:#3b589a}.topbar-header .navcar li.navcar01,.topbar-header .navcar li.navcar02,.topbar-header .navcar li.navcar11{width:58px}.topbar-header .navcar li a:link,.topbar-header .navcar li a:visited{color:#666}.topbar-header .navcar li a:hover{color:#d60000;text-decoration:none;background-color:#fff}.topbar-header .navcar li .icon-newcar{position:absolute;right:0;top:-3px;width:21px;height:11px;background-position:-170px -358px}.topbar-header .navcar li.navcar06{width:80px}.topbar-header .navcar li.navcar12{width:56px;position:relative}.topbar-header .navcar li a{background:url(//x.autoimg.cn/www/common/images/topbar_car.png) no-repeat;background-image:-webkit-image-set(url(//x.autoimg.cn/www/common/images/topbar_car.png) 1x,url(//x.autoimg.cn/www/common/images/topbar_car@2x.png) 2x)}.topbar-header .navcar li.navcar01 a{background-position:-11px 0}.topbar-header .navcar li.navcar02 a{background-position:-91px 0}.topbar-header .navcar li.navcar03 a{background-position:-164px 0}.topbar-header .navcar li.navcar04 a{background-position:-244px 0}.topbar-header .navcar li.navcar05 a{background-position:-4px -60px}.topbar-header .navcar li.navcar06 a{background-position:-80px -60px}.topbar-header .navcar li.navcar07 a{background-position:-164px -58px}.topbar-header .navcar li.navcar08 a{background-position:-244px -58px}.topbar-header .navcar li.navcar09 a{background-position:-4px -120px}.topbar-header .navcar li.navcar10 a{background-position:-84px -118px}.topbar-header .navcar li.navcar11 a{background-position:-171px -120px}.topbar-header .navcar li.navcar12 a{background-position:-251px -120px}.citypop{position:absolute;top:28px;left:-12px;padding:2px;z-index:1000;font-size:12px;line-height:26px;display:none}.citypop a:link,.citypop a:visited{text-decoration:none}.citypop a:hover{color:#d60000}.citypop .citypop-content{width:485px;position:relative;z-index:1;border:1px solid #ccd3e4;background-color:#FFF}.citypop .citypop-content .citypop-close{display:inline-block;width:29px;height:29px;overflow:hidden;position:absolute;right:0;_right:-1px;top:0;background-color:#fafbfc;border-left:solid 1px #cfd5e5}.citypop .citypop-content .citypop-content-top{height:29px;line-height:29px;padding-left:8px;position:relative;background-color:#fcfcfc;border-bottom:solid 1px #ccd3e4}.citypop .citypop-content .citypop-close i{display:inline-block;width:16px;height:16px;background-position:-19px -365px;margin:6px;cursor:pointer;line-height:16px}.citypop .citypop-content a.citypop-close:hover{background-color:#3b5998}.citypop .citypop-content a.citypop-close:hover i{background-position:1px -365px}.citypop .citypop-arrow{overflow:hidden;position:absolute;z-index:2;font-family:"\5b8b\4f53"}.citypop-nb a,.citypop-scity dl dt .nu{font-family:Arial,Helvetica,sans-serif}.citypop .citypop-arrow .citypop-arrow-shadow{filter:alpha(opacity=10);-moz-opacity:.1;opacity:.1}.citypop .citypop-arrow .citypop-arrow-background,.citypop .citypop-arrow .citypop-arrow-border,.citypop .citypop-arrow .citypop-arrow-shadow{overflow:hidden;position:absolute;font-size:12pt}.citypop-bottom .citypop-arrow{width:16px;height:14px;top:-11px;left:23px}.citypop-bottom .citypop-arrow .citypop-arrow-background,.citypop-bottom .citypop-arrow .citypop-arrow-border,.citypop-bottom .citypop-arrow .citypop-arrow-shadow{height:11px}.citypop-bottom .citypop-arrow .citypop-arrow-border{top:3px;color:#d0d0e8}.citypop-bottom .citypop-arrow .citypop-arrow-background{top:4px;color:#f8fcff}.citypop-search{width:140px;height:22px;float:left;margin-top:3px;background-position:-36px -182px;border:1px solid #ccd3e4;background-color:#fff;position:relative}.citypop-search input{outline:0;height:22px;line-height:22px;width:118px;position:absolute;left:22px;top:0;border:none;background-color:#fff;color:#b8bbc1;padding:0}.citypop-search input.focus{width:132px;padding:0 4px;left:0;color:#000}.citypop-hotcity{float:left;padding-left:5px}.citypop-hotcity a{margin-left:10px;display:inline-block;float:left}.citypop-nb{height:28px;padding:8px 6px;border-bottom:dotted 1px #cecfd3}.citypop-nb a{display:inline-block;width:19px;height:19px;line-height:19px;border-radius:2px;margin:4px;font-size:14px;text-align:center;border:1px solid #cbddeb;background-color:#f0f9fe;float:left}.citypop-nb a.current:hover,.citypop-nb a.current:link,.citypop-nb a.current:visited,.citypop-nb a:hover{background-color:#3b5997;border:1px solid #17469e;color:#fff}.citypop-scity{height:255px;overflow-y:scroll;overflow-x:hidden}.citypop-scity dl{border-top:dotted 1px #cecfd3;margin:0;overflow:hidden;padding:8px 0}.citypop-scity .dlbg{background-color:#f9f9f9}.citypop-scity dl.dlbg-top{border-top:none}.citypop-scity dl dd,.citypop-scity dl dt{float:left;margin:0}.citypop-scity dl dt{width:78px;color:#333;text-align:right;font-weight:700;padding-top:2px}.citypop-scity dl dt .nu,.citypop-scity dl dt .tx{height:20px;line-height:20px;display:inline-block;float:right;padding:0}.citypop-scity dl dt .nu{float:left;font-size:18px;color:#d0d0d0;font-weight:100;padding-left:10px}.citypop-scity dl dd{width:390px}.citypop-scity dl dd a:active,.citypop-scity dl dd a:link,.citypop-scity dl dd a:visited{height:20px;line-height:20px;display:block;float:left;padding:0 5px;margin:2px;white-space:nowrap}.citypop-scity dl dd a:hover{height:20px;line-height:20px;color:#fff;background-color:#ff9410;_color:#D60000;_background-color:none}.citypop-scity a.current:hover,.citypop-scity a.current:link,.citypop-scity a.current:visited{background-color:#ff600f;color:#fff}.citypop-ct ul li a:after,.citypop-scity dl dd:after,.citypop-scity dl:after{visibility:hidden;display:block;font-size:0;content:" ";clear:both;height:0;line-height:0}.citypop-ct{width:195px;position:absolute;left:-1px;top:24px;border:1px solid #ccd3e4;background-color:#fff}.citypop-ct .ntextdicon,.citypop-ct .zdicon{height:14px;line-height:14px;padding:2px 0 2px 15px;color:#b8bbc1;margin-left:5px}.citypop-ct ul li,.citypop-ct ul li a{height:26px;line-height:26px;overflow:hidden}.citypop-ct .zdicon{background-position:-279px -161px}.citypop-ct .ntextdicon{background-position:-280px -182px}.citypop-ct ul{padding:0;margin:0}.citypop-ct ul li{float:none;clear:both;border-top:dotted 1px #ccd3e4}.citypop-ct ul li a{display:block;padding:0 12px}.citypop-ct ul li a:hover,.citypop-ct ul li.selected{background-color:#f9f9f9}.citypop-ct ul li span{float:left;display:inline-block}.citypop-ct ul li b{display:inline-block;font-weight:100;color:#b8bbc1;float:right}.pop_forum .ico_close,.pop_forum .ico_del,.pop_forum .pf_search,.pop_forum .pf_search .glass,.pop_forum .pf_search_fous{background:url(//x.autoimg.cn/club/v1Content/images_1/pub_pop_bg.png?11) no-repeat}.pop_forum blockquote,.pop_forum dd,.pop_forum div,.pop_forum dl,.pop_forum dt,.pop_forum fieldset,.pop_forum form,.pop_forum h1,.pop_forum h2,.pop_forum h3,.pop_forum h4,.pop_forum h5,.pop_forum h6,.pop_forum input,.pop_forum li,.pop_forum ol,.pop_forum pre,.pop_forum textarea,.pop_forum ul{margin:0;padding:0}.pop_forum li{list-style-type:none}.pop_forum img{vertical-align:top;border:0}.pop_forum h1,.pop_forum h2,.pop_forum h3,.pop_forum h4,.pop_forum h5,.pop_forum h6,.pop_forum table,.pop_forum td,.pop_forum th,.pop_forum tr{font-size:12px}.pop_forum table{margin:0 auto}.pop_forum{width:744px;height:420px;background:#fff;border-top:solid #005ab0 1px;font-family:\5B8B\4F53,Arial Narrow,arial,serif;font-size:12px;line-height:normal}.pop_forum a:link,.pop_forum a:visited{color:#3b5998;text-decoration:none}.pop_forum a:hover{text-decoration:underline}.pop_forum .pf_inner{border:6px solid #3b5998}.pop_forum .pf_tt{position:relative;height:37px;background:#f2f5f8;border-bottom:solid #ccd3e4 1px}.pop_forum .pf_tt .ico_close{position:absolute;top:6px;right:4px;width:30px;height:28px;text-indent:-999px;overflow:hidden;background-position:0 -31px}.pop_forum .pf_tab{position:absolute;top:12px;left:17px;font-size:12px}.pop_forum .pf_tab a:link,.pop_forum .pf_tab a:visited{display:block;float:left;width:83px;height:18px;padding:6px 0 0;margin:0 8px 0 0;background:#fff;border:solid #ccd3e4;border-width:1px 1px 0;font-weight:400;color:#3e3e3e;text-align:center}.pop_forum .pf_tab a:hover{text-decoration:none}.pop_forum .pf_tab a.cur:link,.pop_forum .pf_tab a.cur:visited{height:19px;padding:5px 0 0;font-weight:700;color:#3b5998;border:solid;border-color:#fc7400 #adc9df;border-width:2px 1px 0}.pop_forum .pf_bradet_tt h3{padding-left:18px;font-size:12px;color:#3b5998;line-height:37px}.pop_forum .pf_cont{height:370px;overflow:auto;position:relative}.pop_forum .pf_search,.pop_forum .pf_search_fous{position:relative;width:394px;height:28px;margin:21px auto 36px;border:1px solid #afc5e0;background-position:0 -87px}.pop_forum .pf_search_fous{border:1px solid #7692cd;width:394px}.pop_forum .pf_search .glass{width:16px;height:16px;display:inline-block;background-position:-83px 0;position:absolute;margin:7px 0 0 11px}.pop_forum .pf_search_fous .glasss{display:none}.pop_forum .pf_search .s_tx,.pop_forum .pf_search_fous .s_tx{width:275px;height:20px;padding:0 7px 0 33px;margin:5px 0 0;background:#fff;border:0;outline:0;box-shadow:none;font-size:12px;color:#999;line-height:20px}.pop_forum .pf_search_fous .s_tx{width:301px;padding:0 7px;color:#000}.pop_forum .pf_search .s_btn,.pop_forum .pf_search_fous .s_btn{background-color:#3b5998;position:absolute;right:-1px;top:-1px;width:80px;height:30px;line-height:30px;padding:0;text-shadow:none;overflow:hidden;font-weight:700;text-align:center;z-index:1}.pop_forum .pf_search .s_btn:link,.pop_forum .pf_search .s_btn:visited,.pop_forum .pf_search_fous .s_btn:link,.pop_forum .pf_search_fous .s_btn:visited{color:#fff;text-decoration:none}.pop_forum .pf_search .s_btn:hover,.pop_forum .pf_search_fous .s_btn:hover{padding:0}.pop_forum .pf_search .keywordsbox,.pop_forum .pf_search_fous .keywordsbox{z-index:1000;position:absolute;top:28px;left:-1px;background-color:#fff;font-size:12px;line-height:22px}.pop_forum .pf_search .keywordsbox ul,.pop_forum .pf_search_fous .keywordsbox ul{width:315px;padding:0;border:1px solid #7692cd;line-height:22px;overflow:hidden}.pop_forum .pf_search .keywordsbox ul li,.pop_forum .pf_search_fous .keywordsbox ul li{width:100%;height:22px;padding:0;line-height:22px;overflow:hidden}.pop_forum .pf_search .keywordsbox ul li a:link,.pop_forum .pf_search .keywordsbox ul li a:visited,.pop_forum .pf_search_fous .keywordsbox ul li a:link,.pop_forum .pf_search_fous .keywordsbox ul li a:visited{display:block;float:none;padding:0 8px;height:22px;line-height:22px;color:#000;text-decoration:none;text-shadow:none;overflow:hidden}.pop_forum .pf_search .keywordsbox ul li a:hover,.pop_forum .pf_search_fous .keywordsbox ul li a:hover{background-color:#f0f9fe;border:none;color:#000}.pop_forum .pf_list{padding:0 0 0 20px}.pop_forum .pf_list h3{margin:28px 0 0;font-weight:700;color:#3e3a39}.pop_forum .pf_default h3{margin:20px 0 0;text-align:left;font-size:12px;font-weight:700}.pop_forum .pf_default h3 span{display:inline-block;height:20px;line-height:20px;padding:0 5px;color:#fff;font-weight:700;background:#fc7400}.pop_forum .pf_list ul{width:690px;padding:12px 0 8px 2px;overflow:hidden}.pop_forum .pf_list li{float:left;width:132px;padding:0 6px 12px 0}.pop_forum .pf_list li a:link,.pop_forum .pf_list li a:visited{float:left;display:block;height:14px;overflow:hidden}.pop_forum .pf_collect .ico_del{display:block;float:left;width:11px;height:11px;margin:0 0 0 1px;overflow:hidden;cursor:pointer;background-position:-30px -31px}.pop_forum .pf_brand{padding:0 0 0 20px}.pop_forum .pf_brand h3{height:25px;margin:19px 0 0;overflow:hidden;font-size:12px}.pop_forum .pf_brand h3 a:link,.pop_forum .pf_brand h3 a:visited{display:block;float:left;width:86px;height:23px;margin-right:7px;background:#e4e9f1;border:1px solid #ccd3e4;font-family:Arial;font-weight:700;line-height:24px;text-align:center;overflow:hidden;letter-spacing:2px;_letter-spacing:-2px}.pop_forum .pf_brand h3 a:hover{text-decoration:none}.pop_forum .pf_brand h3 a.cur:link,.pop_forum .pf_brand h3 a.cur:visited{width:88px;height:25px;background:#526ca4;border:none;color:#fff}.pop_forum .pf_brand h3 i{font-style:normal;_font-weight:400}.pop_forum .pf_brand h4{margin:12px 0 0 4px;font-family:Arial;font-weight:700;color:#e75e15}.pop_forum .pf_brand ul{width:690px;padding:8px 0 0 2px;overflow:hidden}.pop_forum .pf_brand li{float:left;width:138px;padding:0 0 8px;overflow:hidden}.pop_forum .pf_brand li a:link,.pop_forum .pf_brand li a:visited{float:left;display:block;height:14px;overflow:hidden}.pop_forum .pf_hr,.pop_forum .pf_hr02{display:block;width:692px;height:0;border-top:dotted #ccc 1px;overflow:hidden}.pop_forum .pf_hr02{border-top:solid 1px #ccd3e4}.icon-new-01{display:inline-block;vertical-align:top;width:26px;height:12px;margin:6px 0 0 3px;background:url(//s.autoimg.cn/www/common/images/icon-new.png?v=2.1) no-repeat -20px -35px}.icon-new-02{display:inline-block;vertical-align:top;width:26px;height:14px;position:absolute;right:-3px;top:0;background:url(//s.autoimg.cn/www/common/images/icon-new.png?v=2.1) no-repeat -50px -35px}.topbar-header .navlink{ width:828px; }.topbar-header .navlink ul{ height:37px;}.topbar-header .navlink li{z-index:2}.topbar-header .navcar li.navcar12{position:relative;z-index:1}.topbar-header .navcar li.navcar12 .icon-new-02{top:-5px;right:0}.topbar-header .navlink a.nw-3arrow {width: 60px;padding-right:6px;}</style>  
    <base target="_blank" href="//www.autohome.com.cn/" />
</head>
<body class="wide-body">
     <script language="javascript" type="text/javascript">
         var pvTrack = function(){};
         pvTrack.site = 1;
         pvTrack.category = 401;
         pvTrack.subcategory = 2151;
         pvTrack.object = 0;
         pvTrack.series = 0;
         pvTrack.type = 0;
         pvTrack.typeid = 0;
         pvTrack.spec = 0;
         pvTrack.level = 0;
         pvTrack.dealer = 0;
     </script>
    <script type="text/javascript">
  (function(doc){
  var _as = doc.createElement('script');
  _as.type = 'text/javascript';
  _as.async = true;
  _as.src = '//x.autoimg.cn/bi/mda/ahas_body.min.js?d=' + Math.floor((new Date()).getTime()/(1000*60*60*24));
  var s = doc.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(_as, s);
  })(document);
</script>
<SCRIPT language=javascript type=text/javascript>
var url_stats="//al.autohome.com.cn/pv_count.php?SiteId=";
(function (){
    if (typeof(pvTrack)!="undefined"){				
		setTimeout("func_stats()",3000);		
		var doc = document,t=pvTrack;
		var pv_site,pv_category ,pv_subcategory,pv_object,pv_series,pv_type,pv_typeid,pv_spec,pv_level,pv_dealer,pv_ref,pv_cur;
		pv_ref=escape(doc.referrer);pv_cur=escape(doc.URL);
		pv_site=t.site;pv_category=t.category ;pv_subcategory= t.subcategory;pv_object=t.object;pv_series=t.series;pv_type=t.type;pv_typeid=t.typeid;pv_spec=t.spec;pv_level=t.level;pv_dealer=t.dealer;
		url_stats+= pv_site+(pv_category != null ? "&CategoryId=" + pv_category : "")+ (pv_subcategory != null ? "&SubCategoryId=" + pv_subcategory : "")+ (pv_object != null ? "&objectid=" + pv_object : "")+ (pv_series != null ? "&seriesid=" + pv_series : "")+ (pv_type != null ? "&type=" + pv_type : "")+ (pv_typeid != null ? "&typeid=" + pv_typeid : "")+ (pv_spec != null ? "&specid=" + pv_spec : "")+ (pv_level != null ? "&jbid=" + pv_level : "")+ (pv_dealer != null ? "&dealerid=" + pv_dealer : "")+ "&ref=" + pv_ref + "&cur=" + pv_cur+"&rnd="+Math.random();
		var len_url_stats =url_stats.length;
		}
})();
//document.write('<iframe id="PageView_stats" src="" style="display:none;"></iframe>');
function func_stats(){
	var image=new Image();
	image.src=url_stats;
//document.getElementById('PageView_stats').src =url_stats;
}
</SCRIPT>
<script type='text/javascript'>
  var _ahs = _ahs || {};
  window._ahs = _ahs;
  (function() {
  if (typeof(pvTrack) !== "undefined") {
  _ahs['site'] = pvTrack['site'];
  _ahs['category'] = pvTrack['category'];
  _ahs['subcategory'] = pvTrack['subcategory'];
  }
  var ahs = document.createElement('script');
  ahs.type='text/javascript';
  ahs.async = true;
  ahs.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'x.autoimg.cn/bi/risk/ah_fp.min.js';
  var s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(ahs, s);
  })();
</script>
<script type='text/javascript'>
    var _ahs = _ahs || {};
    window._ahs = _ahs;
    (function () {
        if (typeof (pvTrack) !== "undefined") {
            _ahs['site'] = pvTrack['site'];
            _ahs['category'] = pvTrack['category'];
            _ahs['subcategory'] = pvTrack['subcategory'];
        }
        var ahs = document.createElement('script');
        ahs.type = 'text/javascript';
        ahs.async = true;
        ahs.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'x.autoimg.cn/bi/risk/ah_fp.min.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ahs, s);
    })();
</script>

    

    <script type="text/javascript">
        //导航头登录标识
        window.__AccountConfig = {
            fPosition: 10001,
            sPosition: 1000101,
            platform: 1
        };
    </script>
    <div id="auto-header" class="topbar">
    <!-- minitop begin -->
    <div class="minitop">
        <div class="mini-main">
            <div class="mini-left">
                <ul>
                    <li id="auto-header-fenzhan"><a target="_blank" href="//www.autohome.com.cn/beijing/cheshi/" class="orangelink"><i class="topbar-icon topbar-icon16 topbar-icon16-building"></i>进入北京车市</a></li>
                    <li class="vlli">|</li>
                    <li><a target="_blank" href="//www.autohome.com.cn/AreaList.html" class="greylink">查看其它地方车市</a></li>
                </ul>
            </div>
            <div class="mini-right">
                <ul>
                    <li id="auto-header-login" class="frs-login" style="display:none">
                        <div id="auto-header-login-text">
                        </div>

                    </li>
                    <li id="auto-header-info" style="display:none">
                        <div class="moreli-title moreli-title-notice">
                            <a href="javascript:void(0);" class="active-bg" target="_self">
                                <span>消息</span><span id="auto-header-info-allcount" class="info" style="display: none"></span><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>
                            </a>
                        </div>
                        <div id="auto-header-info-list" class="topchadiv topchadiv-dw03" style="display: none;">
                            <div class="topchadiv-box">
                                <div id="auto-header-info-listdata" class="topchadiv-con">
                                </div>
                            </div>
                        </div>
                    </li>
                    <li>
                        <div class="find-club">
                            <a id="auto-header-find-club" target="_self" href="javascript:void(0);">找论坛</a>
                        </div>
                    </li>
                    <li id="auto-header-app">
                        <div class="moreli-title">
                            <a target="_self" class="active-bg" href="javascript:void(0);">
                                <span>更多应用</span>
                                <i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>
                            </a>
                        </div>
                        <div id="auto-header-app-list" class="topchadiv topchadiv-dw01" style="display:none">
                            <div class="topchadiv-box">
                                <div class="topchadiv-con">
                                    <a target="_blank" href="//app.autohome.com.cn/appn/">移动App</a>
                                    <a target="_blank" href="//app.autohome.com.cn/appn/m/">触屏版</a>
                                    <a target="_blank" href="//j.autohome.com.cn/quankuan_calculation.html">购车计算器</a>
                                    <a target="_blank" href="//www.autohome.com.cn/Violation/">违章查询</a>
                                    <a target="_blank" href="//car.autohome.com.cn/zhaoche/jiage/">按价格找车</a>
                                    <a target="_blank" href="//car.autohome.com.cn/zhaoche/pinpai/">按品牌找车</a>
                                    <a target="_blank" href="//www.autohome.com.cn/chezhan/#pvareaid=103405">车展</a>
                                    <div class="linedc"></div>
                                    <a target="_blank" href="//ics.autohome.com.cn/#pvareaid=104317">i车商</a>
                                    <a target="_blank" href="//www.che168.com/">二手车之家</a>
                                    <a target="_blank" href="//mall.autohome.com.cn/subject/2017/6/recruitment/#pvareaid=2023627">车商城入驻</a>
                                    <!--<a target="_blank" href="//www.pcpop.com">泡泡网</a>
                                    <a target="_blank" href="//www.it168.com">IT168</a>-->
                                </div>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <!-- minitop end -->
    <!-- 双十一车商城推广位 begin -->
    <div class="ad-top-1111" style="display:none;" id="ad-top-1111">
        <div class="monkey">
            <div>
                <!-- 广告图图片路径写在 style 里 -->
                <a href="//mall.autohome.com.cn/carevent/?page=prea#pvareaid=2023272" id="header-ad-top-1111" target="_blank"></a>
            </div>
        </div>
    </div>
    <style type="text/css">
          .ad-top-1111{width:100%;margin:0 auto;}
          .ad-top-1111 a{display:block;width:100%;height:60px;margin:0 auto;}
          .topbar-header .logo-shadow1{border-top-color: transparent;}
    </style>
    <!-- 双十一车商城推广位 end -->
    <!-- club pop begin -->
    <div id="auto-header-clubmask" style="width: 100%; height: 100%; position: fixed; left: 0px; top: 0px; z-index: 1100; display: none; background-color: #000; opacity: 0.5; filter: alpha(opacity=50); -moz-opacity: 0.5; -khtml-opacity: 0.5;"></div>
    <div id="auto-header-clublayer" style="display:none; z-index: 1101; position: fixed; top:50%; left:50%; margin-top:-210px; margin-left:-377px;">
        <div class="pop_forum">
            <div class="pf_inner">
                <div class="pf_tt">
                    <h2 class="pf_tab">
                        <a id="auto-header-club-tab0" href="javascript:void(0);" target="_self" tabindex="0" class="cur">找论坛</a>
                        <a id="auto-header-club-tab1" href="javascript:void(0);" target="_self" tabindex="1">全部车系</a>
                        <a id="auto-header-club-tab2" href="javascript:void(0);" target="_self" tabindex="2">全部地区</a>
                        <a id="auto-header-club-tab3" href="javascript:void(0);" target="_self" tabindex="3">全部主题</a>
                        <a id="auto-header-club-tab4" href="javascript:void(0);" target="_self" tabindex="4">摩托车论坛</a>
                    </h2>
                    <a id="auto-header-clubclose" class="ico_close" href="javascript:void(0);" target="_self">关闭</a>
                </div>
                <div id="auto-header-clubhtml" class="pf_cont"></div>
            </div>
        </div>
    </div>
    <!-- club pop end -->
    <!-- header begin -->
    <div class="topbar-header">
        <div class="topbar-header-main">
            <div class="topbar-clearfix">
                <div class="logo"><a href="//www.autohome.com.cn/"><img width="170" height="90" alt="汽车之家" src="//x.autoimg.cn/www/common/images/logo_slogan_beta_01.png" srcset="//x.autoimg.cn/www/common/images/logo_slogan_beta_01.png 170w,//x.autoimg.cn/www/common/images/logo_slogan_beta_2x_01.png 340w" sizes="170px"></a></div>
                <div class="nav">
                    <div class="navlink">
                        <ul>
                            <li id="auto-header-news">
                                <a id="auto-header-channel2" class="navlink-item nw-2arrow" href="//www.autohome.com.cn/all/" target="_blank"><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>文章</a>
                                <div id="auto-header-news-list" class="topbar-dropdown" style="display: none;">
                                    <dl>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/all/">查看全部</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/newbrand/">上市新车</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/xianfengduihua/#pvareaid=3311118" data-tjposition="3|1|3">先锋对话</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/ah-100/">AH-100评价</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/23660/0/1/conjunction.html">长期测试</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/youji/">编辑游记</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/topics/#pvareaid=2023455">互动话题</a></dd>
                                    </dl>
                                </div>
                            </li>
                            <li><a id="auto-header-channel3" class="navlink-item nw-2" href="//www.autohome.com.cn/bestauto/">评测</a></li>
                            <li><a id="auto-header-channel19" class="navlink-item nw-3" href="//chejiahao.autohome.com.cn/#pvareaid=2023585">车家号</a></li>
                            <li id="auto-header-v">
                                <a id="auto-header-channel4" class="navlink-item nw-2arrow" href="//v.autohome.com.cn/#pvareaid=2029173"><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>视频</a>
                                <div id="auto-header-v-list" class="topbar-dropdown" style="display: none;">
                                    <dl>
                                        <dd><a target="_blank" href="//v.autohome.com.cn/#pvareaid=103409 ">查看全部</a></dd>
                                        <dd><a target="_blank" href="//v.autohome.com.cn/u/19987472#pvareaid=106552">原创试车</a></dd>
                                        <dd><a target="_blank" href="//v.autohome.com.cn/u/20380947#pvareaid=106554">用车小百科</a></dd>
                                        <dd><a target="_blank" href="//v.autohome.com.cn/u/27493450#pvareaid=106548">微试车</a></dd>
                                    </dl>
                                </div>
                            </li>
                            <li><a id="auto-header-channel17" class="navlink-item nw-2" href="//www.autohome.com.cn/hangye/#pvareaid=6825588">行业</a></li>
                            <li><a id="auto-header-channel6" class="navlink-item nw-4" href="//car.autohome.com.cn/duibi/chexing/">车型对比</a></li>
                            <li><a id="auto-header-channel7" class="navlink-item nw-2" href="//car.autohome.com.cn/pic/index.html">图片</a></li>
                            <li><a id="auto-header-channel8" class="navlink-item nw-2" href="//car.autohome.com.cn/">报价</a></li>
                            <li><a id="auto-header-channel9" class="navlink-item nw-3" href="//mall.autohome.com.cn/#pvareaid=3278573">车商城</a></li>
                            <li><a id="auto-header-channel10" class="navlink-item nw-2" href="//buy.autohome.com.cn/">降价</a></li>
                            <li id="auto-header-dealer">
                                <a class="navlink-item nw-3arrow" target="_blank" href="//dealer.autohome.com.cn/"><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>经销商</a>
                                <div id="auto-header-dealer-list" class="topbar-dropdown" style="display: none;">
                                    <dl>
                                        <dd><a target="_blank" href="//vr4s.autohome.com.cn/#pvareaid=3311250">智能展厅</a></dd>
                                    </dl>
                                </div>
                            </li>
                            <li><a id="auto-header-channel12" class="navlink-item nw-3" href="//www.che168.com/#pvareaid=2023133">二手车</a></li>
                            <li><a class="navlink-item nw-2" target="_blank" href="//j.autohome.com.cn/pcplatform/index.html?pt=_t&pvareaid=2020996" data-tjposition="">金融</a></li>
                            <li><a id="auto-header-channel14" class="navlink-item nw-2" href="//club.autohome.com.cn/">论坛</a></li>
                            <li><a id="auto-header-channel18" class="navlink-item nw-2" href="//club.autohome.com.cn/jingxuan/">精选</a></li>
                            <li><a id="auto-header-channel15" class="navlink-item nw-2" href="//k.autohome.com.cn/">口碑</a></li>
                        </ul>
                    </div>

                    <div class="navcar">
                        <ul>
                            <li class="navcar12"><a target="_blank" href="//ev.autohome.com.cn#pvareaid=103686">新能源<i class="icon-new-02"></i></a></li>
                            <li class="navcar01"><a target="_blank" href="//www.autohome.com.cn/a00/">微型车</a></li>
                            <li class="navcar02"><a target="_blank" href="//www.autohome.com.cn/a0/">小型车</a></li>
                            <li class="navcar03"><a target="_blank" href="//www.autohome.com.cn/a/">紧凑型车</a></li>
                            <li class="navcar04"><a target="_blank" href="//www.autohome.com.cn/b/">中型车</a></li>
                            <li class="navcar05"><a target="_blank" href="//www.autohome.com.cn/c/">中大型车</a></li>
                            <li class="navcar06"><a target="_blank" href="//www.autohome.com.cn/d/">大型车</a></li>
                            <li class="navcar07" id="auto-header-suv">
                                <a target="_blank" href="//www.autohome.com.cn/suv/"><i class="topbar-icon topbar-icon10 topbar-icon10-sjb"></i>SUV</a>
                                <div id="auto-header-suv-list" style="display: none;" class="topbar-dropdown">
                                    <dl>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suv/">全部SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suva0/">小型SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suva/">紧凑型SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suvb/">中型SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suvc/">中大型SUV</a></dd>
                                        <dd><a target="_blank" href="//www.autohome.com.cn/suvd/">大型SUV</a></dd>
                                    </dl>
                                </div>
                            </li>
                            <li class="navcar08"><a target="_blank" href="//www.autohome.com.cn/mpv/">MPV</a></li>
                            <li class="navcar09"><a target="_blank" href="//www.autohome.com.cn/s/">跑车</a></li>
                            <li class="navcar10"><a target="_blank" href="//www.autohome.com.cn/p/">皮卡</a></li>
                            <li class="navcar11"><a target="_blank" href="//www.autohome.com.cn/mb/">微面</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <i class="logo-shadow1"></i><i class="logo-shadow2"></i>
        </div>
        <div class="topbar-header-blue"></div>
    </div>
    <!-- header end -->
</div>

<script type="text/javascript">
    //sync-login.js
    !function(e){function n(e,n){var o,t,i=e+"=",u=m.cookie.split(";");for(o=0;o<u.length;o+=1){for(t=u[o];" "===t.charAt(0);)t=t.substring(1,t.length);if(0===t.indexOf(i))return decodeURIComponent(t.substring(i.length,t.length))}return"undefined"==typeof n?null:n}function o(e,n,o){var t=m.getElementsByTagName("body")[0],i=m.createElement("iframe");i.style.display="none",i.src=n,i.id=e,i.domain=o,t.appendChild(i)}function t(){var e,t=n("sessionuserid");null!=t&&0!==t.length||(e=n("autouserid"),null!=e&&e.length>0&&(m.domain.indexOf("autohome")>=0?o("tempIframe","//sso.autohome.com.cn/Home/CookieIFrame","autohome.com.cn"):o("tempIframe","//sso.che168.com/Home/CookieIFrame","che168.com")))}function i(){u&&clearTimeout(u),u=null,u=setTimeout(function(){t(),i()},432e5)}var m=e.document,u=null;t(),i()}(this);
    //auto-header.js
    !function (e) { function t(e) { var t = []; for (var n in e) e.hasOwnProperty(n) && null != e[n] && t.push(n + "=" + encodeURIComponent(e[n])); return t.join("&") } function n(e, t) { var n, a, o = e + "=", i = document.cookie.split(";"); for (n = 0; n < i.length; n += 1) { for (a = i[n]; " " === a.charAt(0) ;) a = a.substring(1, a.length); if (0 === a.indexOf(o)) return decodeURIComponent(a.substring(o.length, a.length)) } return "undefined" == typeof t ? null : t } function a(e) { var t = document.createElement("script"); t.setAttribute("type", "text/javascript"), t.setAttribute("src", e.url), t.onload = t.onreadystatechange = function () { if (!this.readyState || "loaded" === this.readyState || "complete" === this.readyState) { "function" == typeof e.callBack && e.callBack(e.args), t.onload = t.onreadystatechange = null; try { t.parentNode && t.parentNode.removeChild(t) } catch (n) { } } }, document.getElementsByTagName("head")[0].appendChild(t) } function o(e) { this.isPageFocus = !0, this.Aleng = 0, this.init(e) } var i = window.__AccountConfig || {}, r = encodeURIComponent(document.location.href), s = t({ backurl: r, fPosition: i.fPosition, sPosition: i.sPosition, platform: i.platform, popWindow: i.popWindow }); o.prototype = { $dom: function () { for (var e = [], t = 0; t < arguments.length; t++) { var n = arguments[t]; if ("string" == typeof n && (n = document.getElementById(n)), 1 === arguments.length) return n; e.push(n) } return e }, cookies: { read: function (e, t) { for (var n = e + "=", a = document.cookie.split(";"), o = 0; o < a.length; o++) { for (var i = a[o]; " " === i.charAt(0) ;) i = i.substring(1, i.length); if (0 === i.indexOf(n)) return decodeURIComponent(i.substring(n.length, i.length)) } return "undefined" == typeof t ? null : t }, set: function (e, t, n) { var a = e + "=" + encodeURIComponent(t); if (n) { if (n.expireHours) { var o = new Date; o.setTime(o.getTime() + 3600 * n.expireHours * 1e3), a += "; expires=" + o.toGMTString() } a += n.path ? "; path=" + n.path : "; path=/", n.domain && (a += "; domain=" + n.domain), n.secure && (a += "; true") } document.cookie = a }, del: function (e) { var t = new Date; t.setTime(t.getTime() - 1); var n = this.read(e); null != n && (document.cookie = e + "=" + n + ";expires=" + t.toGMTString()) } }, eventHandle: { add: function (e, t, n) { window.addEventListener ? e.addEventListener(t, n, !1) : e.attachEvent("on" + t, n) }, remove: function (e, t, n) { window.removeEventListener ? e.removeEventListener(t, n, !1) : e.detachEvent("on" + t, n) } }, jsLoad: function () { var e, t, n = [], a = arguments.length; if (1 == a) { var o = arguments[0] || {}; "object" == typeof o ? (e = o.url, t = o.fn, n = o.args) : e = o } else { e = arguments[0], t = arguments[1]; for (var i = 0; i < a - 2; i++) n[i] = arguments[i + 2] } var r = document.createElement("script"); r.setAttribute("type", "text/javascript"), r.setAttribute("src", e), r.onload = r.onreadystatechange = function () { if (!r.readyState || "loaded" === r.readyState || "complete" === r.readyState) { "function" == typeof t && t.apply(this, n), r.onload = r.onreadystatechange = null; try { r.parentNode && r.parentNode.removeChild(r) } catch (e) { } } }, document.getElementsByTagName("head")[0].appendChild(r) }, domReady: function () { var e, t = document, n = [], a = "complete" === t.readyState, o = function () { var e = n.shift(); for (a = !0; e;) e(), e = n.shift() }; return a ? function (e) { e() } : (t.addEventListener ? t.addEventListener("DOMContentLoaded", e = function () { t.removeEventListener("DOMContentLoaded", e, !1), o() }, !1) : (t.attachEvent("onreadystatechange", e = function () { "complete" === t.readyState && (t.detachEvent("onreadystatechange", e), o()) }), t.documentElement.doScroll && self == top && !function i() { if (!a) { try { t.documentElement.doScroll("left") } catch (e) { return setTimeout(i, 50) } o() } }()), function (e) { a ? e() : n.push(e) }) }(), logoffFunctionArray: [], host: { www: "//www.autohome.com.cn/", club: "//club.autohome.com.cn/", clubService: "//club.service.autohome.com.cn/", user: "//i.autohome.com.cn", login: "//account.autohome.com.cn/?" + s, register: "//account.autohome.com.cn/register?" + s }, user: { isLogin: !1, uid: null, un: null, up: null }, userArea: { cookieArea: null, cookieCityId: null, areaId: null, oldCityId: null, cityName: null, cityPinyin: null, provinceId: null, provinceName: null, provincePinyin: null, provinceSimple: null }, init: function (e) { this.initChannel(e), this.popControl("auto-header-info", "moreli-active", !0), this.popControl("auto-header-app", "moreli-active", !0), this.popControl("auto-header-suv", "", !0), this.popControl("auto-header-news", "", !0), this.popControl("auto-header-v", "", !0), this.popControl("auto-header-dealer", "", !0), this.getUserArea(), this.getUser(), this.showUserStatus(), this.showUserMsg(), this.trackRead() }, initChannel: function (e) { var t; e && (t = document.getElementById("auto-header-channel" + e), t && (t.className += " navlink-item-current")) }, popControl: function (e, t, n) { var a = this, o = function (e) { return this.li = document.getElementById(e), this.list = document.getElementById(e + "-list"), this.shown = !1, this.init() }; return o.prototype = { init: function () { var e, t = this; a.eventHandle.add(this.li, "mouseover", function () { clearTimeout(e), t.show() }), a.eventHandle.add(this.li, "mouseout", function () { e = setTimeout(function () { t.hide() }, 50) }) }, show: function () { this.shown = !0, this.list && (this.list.style.display = "block"), t && (this.li.className = t); var e = navigator.userAgent.indexOf("MSIE 6.0") > 0; if (n && e && 0 == this.li.getElementsByTagName("iframe").length) { var a = this.list.offsetWidth, o = this.list.offsetHeight, i = document.createElement("iframe"); i.setAttribute("scrolling", "no"), i.setAttribute("frameborder", 0), i.style.cssText = "zoom:1;position:absolute;top:0;left:0;filter:alpha(opacity=0);z-index:-1; width:" + a + "px;height:" + o + "px", this.list.appendChild(i) } }, hide: function () { this.shown = !1, this.list && (this.list.style.display = "none"), t && (this.li.className = "") } }, document.getElementById(e) ? new o(e) : null }, getUserArea: function (e) { var t; if (e) t = this.host.www + "Ashx/AjaxHeadArea.ashx?OperType=GetAreaInfo&VarName=areaData&CityId=" + (0 == e ? "110100" : e); else { var n = { cookieCityId: this.cookies.read("cookieCityId"), area: this.cookies.read("area") }; this.userArea.cookieCityId = n.cookieCityId ? parseInt(n.cookieCityId, 10) : 0, this.userArea.cookieArea = n.area ? parseInt(n.area) : 0, this.userArea.areaId = 0 == this.userArea.cookieCityId ? 100 * parseInt(this.userArea.cookieArea / 100) : this.userArea.cookieCityId, 0 == this.userArea.areaId && (this.userArea.areaId = 110100), t = this.host.www + "Ashx/AjaxHeadArea.ashx?OperType=GetAreaInfo&VarName=areaData&CityId=" + this.userArea.areaId } var a = this; return this.jsLoad(t, function () { "undefined" != typeof areaData && areaData.Status && (a.userArea.oldCityId = areaData.AreaInfo[0].DealerCityId, a.userArea.cityName = areaData.AreaInfo[0].CityName, a.userArea.cityPinyin = areaData.AreaInfo[0].Pinyin, a.userArea.provinceId = areaData.ProvinceInfo[0].ProvinceId, a.userArea.provinceName = areaData.ProvinceInfo[0].ProvinceName, a.userArea.provincePinyin = areaData.ProvinceInfo[0].Pinyin, a.userArea.provinceSimple = areaData.ProvinceInfo[0].ProvinceSample, a.getUserAreaCallback()) }), !1 }, getUserAreaCallback: function () { var e = document.getElementById("auto-header-fenzhan"), t = document.getElementById("auto-header-channel12"), n = '<a target="_blank" class="orangelink" href="' + this.host.www + this.userArea.cityPinyin + '/cheshi/"><i class="topbar-icon topbar-icon16 topbar-icon16-building"></i>\u8fdb\u5165' + this.userArea.cityName + "\u8f66\u5e02</a>"; e && (e.innerHTML = n), t && t.setAttribute("href", "//www.che168.com/" + this.userArea.cityPinyin + "/list/#pvareaid=100533") }, getUser: function () { var e, t = this.cookies.read("clubUserShow"); return null == t ? this.user.isLogin = !1 : (e = t.split("|"), this.user.isLogin = !0, this.user.un = e[3], this.user.uid = e[0], this.user.up = e[2]), !1 }, showUserStatus: function () { var e, t, n = this, a = this.$dom("auto-header-login"), o = this.$dom("auto-header-login-text"); t = this.user.isLogin ? '\u60a8\u597d\uff01 <a class="minitop-uname" href="' + this.host.user + '" target="_blank">' + this.user.un + '</a> <a id="auto-header-logoff" class="minitop-logoff" href="javascript:void(0);" target="_self">\u9000\u51fa</a>' : '\u60a8\u597d\uff01\u8bf7 <a href="' + this.host.login + '" target="_self">\u767b\u5f55</a> \u6216 <a href="' + this.host.register + '" target="_self">\u6ce8\u518c</a>', a.style.display = "", o.innerHTML = t, e = document.getElementById("auto-header-logoff"), e && n.eventHandle.add(e, "click", function () { n.logoff() }) }, showUserMsg: function () { var e = this, t = this.$dom("auto-header-info"); this.user.isLogin ? (t.style.display = "", setTimeout(function () { e.jsonpGetUserMsg() }, 100), setInterval(function () { e.jsonpGetUserMsg() }, 2e4), this.eventHandle.add(window, "focus", function () { e.isPageFocus = !0 }), this.eventHandle.add(window, "blur", function () { e.isPageFocus = !1 })) : t.style.display = "none" }, jsonpGetUserMsg: function () { if (!this.isPageFocus) return !1; if (!this.user.isLogin) return !1; var e = "AuScrJsonpId", t = "//msg.autohome.com.cn/clubalert?uid=" + this.user.uid + "&callback=AjaxCallBackMessage&ALeng=" + this.Aleng, n = document.getElementById(e); n && n.parentNode.removeChild(n); var a = document.createElement("script"); a.setAttribute("id", e), a.setAttribute("src", t), document.getElementsByTagName("head")[0].appendChild(a), window.AjaxCallBackMessage = function (e) { var t, n = "", a = ""; e.NewReply > 0 ? n += '<a href="//i.autohome.com.cn/receivereply/#pvareaid=101298"><span class="cn">' + (e.NewReply > 99 ? "99+" : e.NewReply) + '\u6761\u65b0\u8bba\u575b\u56de\u590d</span><span class="ck">\u67e5\u770b\u8bba\u575b\u56de\u590d</span></a>' : a += '<a  href="//i.autohome.com.cn/receivereply/#pvareaid=101606">\u67e5\u770b\u8bba\u575b\u56de\u590d</a>', e.commentreply > 0 ? n += '<a href="//i.autohome.com.cn/inbox/#pvareaid=101482"><span class="cn">' + (e.commentreply > 99 ? "99+" : e.commentreply) + '\u6761\u65b0\u8bc4\u8bba\u56de\u590d</span><span class="ck">\u67e5\u770b\u8bc4\u8bba\u56de\u590d</span></a>' : a += '<a href="//i.autohome.com.cn/inbox/#pvareaid=101607">\u67e5\u770b\u8bc4\u8bba\u56de\u590d</a>', e.NewLetter > 0 ? n += '<a href="//i.autohome.com.cn/club/message/#pvareaid=101300"><span class="cn">' + (e.NewLetter > 99 ? "99+" : e.NewLetter) + '\u6761\u65b0\u79c1\u4fe1</span><span class="ck">\u67e5\u770b\u79c1\u4fe1</span></a>' : a += '<a href="//i.autohome.com.cn/club/message/#pvareaid=101609">\u67e5\u770b\u79c1\u4fe1</a>', e.NewNotice > 0 ? n += '<a href="//i.autohome.com.cn/club/notice/#pvareaid=101301"><span class="cn">' + (e.NewNotice > 99 ? "99+" : e.NewNotice) + '\u6761\u65b0\u901a\u77e5</span><span class="ck">\u67e5\u770b\u901a\u77e5</span></a>' : a += '<a href="//i.autohome.com.cn/club/notice/#pvareaid=101610">\u67e5\u770b\u901a\u77e5</a>', e.NewFollowers > 0 ? n += '<a href="//i.autohome.com.cn/club/follower/#pvareaid=101297"><span class="cn">' + (e.NewFollowers > 99 ? "99+" : e.NewFollowers) + '\u4e2a\u65b0\u7c89\u4e1d</span><span class="ck">\u67e5\u770b\u7c89\u4e1d</span></a>' : a += '<a href="//i.autohome.com.cn/club/follower/#pvareaid=101611">\u67e5\u770b\u7c89\u4e1d</a>', e.order && e.order > 0 ? n += '<a href="//i.autohome.com.cn/orderlist/#pvareaid=101548"><span class="cn">' + (e.order > 99 ? "99+" : e.order) + '\u6761\u65b0\u8ba2\u5355</span><span class="ck">\u67e5\u770b\u8ba2\u5355</span></a>' : a += '<a href="//i.autohome.com.cn/orderlist/#pvareaid=101612">\u67e5\u770b\u8ba2\u5355</a>', t = "" != n && "" != a ? n + '<div class="linedc"></div>' + a : "" == a ? n : a; var o = document.getElementById("auto-header-info-listdata"); o && (o.innerHTML = t); var i = e.NewReply + e.commentreply + e.NewLetter + e.NewNotice + e.NewFollowers + (e.order && null != e.order ? e.order : 0), r = document.getElementById("auto-header-info-allcount"); i > 99 ? (r.innerHTML = "99+", r.style.display = "") : i > 0 ? (r.innerHTML = i, r.style.display = "") : (r.innerHTML = "", r.style.display = "none") } }, trackRead: function () { var e = this; e.domReady(function () { var t = !1, n = !1, a = !1; window.onscroll = function () { var o = document.body.scrollHeight, i = document.documentElement.scrollTop || document.body.scrollTop, r = document.documentElement.clientHeight; i = parseInt(i, 10) + parseInt(r, 10), e.Aleng = parseInt(i / o * 100, 10), t || i - .3 * o > 0 && (e.Aleng = 30, e.jsonpGetUserMsg(), t = !0), n || i - .5 * o > 0 && (e.Aleng = 50, e.jsonpGetUserMsg(), n = !0), a || i - .8 * o > 0 && (e.Aleng = 80, e.jsonpGetUserMsg(), a = !0) } }) }, logoff: function () { var e = this; this.jsLoad("//account.autohome.com.cn/login/logoutjson?backvar=autologinout&timestamp=" + Math.random(), function () { for (var t = 0, n = e.logoffFunctionArray.length; t < n; t++) if ("function" == typeof e.logoffFunctionArray[t]) try { e.logoffFunctionArray[t]() } catch (a) { } e.init(), e.jsLoad("//account.che168.com/login/logoutjson?backvar=cheloginout&timestamp=" + Math.random()) }) } }, e.readCookie = n, e.AutohomeJsLoad = a, e.AutoHeader = o }(this);
    //auto-header-club.js
    !function(e){function t(e,t){return new RegExp(" "+t+" ").test(" "+e.className+" ")}function n(e,n){t(e,n)||(e.className+=" "+n)}function a(e,n){var a=" "+e.className.replace(/[\t\r\n]/g," ")+" ";if(t(e,n)){for(;a.indexOf(" "+n+" ")>=0;)a=a.replace(" "+n+" "," ");e.className=a.replace(/^\s+|\s+$/g,"")}}function l(e,t){var n,a,l,o=t||document,u=[];if(o.querySelectorAll)return o.querySelectorAll("."+e);if(o.evaluate)for(a='.//*[contains(concat(" ", @class, " "), " '+e+' ")]',n=o.evaluate(a,o,null,0,null);l=n.iterateNext();)u.push(l);else for(n=o.getElementsByTagName("*"),a=new RegExp("(^|\\s)"+e+"(\\s|$)"),l=0;l<n.length;l++)a.test(n[l].className)&&u.push(n[l]);return u}function o(e,t,n){e.addEventListener?e.addEventListener(t,n,!1):e.attachEvent&&e.attachEvent("on"+t,n)}function u(e,t,n,a){e=e||"",t=t||{},n=n||"",a=a||function(){};var l=function(e){var t=[];for(var n in e)e.hasOwnProperty(n)&&t.push(n);return t};if("object"==typeof t){for(var o="",u=l(t),c=0;c<u.length;c++)o+=encodeURIComponent(u[c])+"="+encodeURIComponent(t[u[c]]),c!=u.length-1&&(o+="&");e+="?"+o}else"function"==typeof t&&(n=t,a=n);"function"==typeof n&&(a=n,n="callback"),Date.now||(Date.now=function(){return(new Date).getTime()});var r=Date.now(),i="jsonp"+Math.round(r+1000001*Math.random());window[i]=function(e){a(e);try{delete window[i]}catch(t){window[i]=void 0}},e+=e.indexOf("?")===-1?"?":"&";var s=document.createElement("script");s.setAttribute("src",e+n+"="+i),document.getElementsByTagName("head")[0].appendChild(s)}function c(){this.urls=["/ajax/AllBBS","/ajax/SeariesBBS","/ajax/areaBBS","/ajax/ThemeBBS","/ajax/MotorBBS"],this.urlDomain="//club.autohome.com.cn",this.clubData={findHtml:"",brandHtml:"",areaHtml:"",themeHtml:"",motorHtml:""},this.init()}c.prototype={init:function(){var e=this,t=document.getElementById("auto-header-find-club");o(t,"click",function(){e.openClubPop()});var n=document.getElementById("auto-header-clubclose");o(n,"click",function(){e.closeClubPop()});var a=document.getElementById("auto-header-club-tab0");o(a,"click",function(){e.enterClubTab(0)});var l=document.getElementById("auto-header-club-tab1");o(l,"click",function(){e.enterClubTab(1)});var u=document.getElementById("auto-header-club-tab2");o(u,"click",function(){e.enterClubTab(2)});var c=document.getElementById("auto-header-club-tab3");o(c,"click",function(){e.enterClubTab(3)});var r=document.getElementById("auto-header-club-tab4");o(r,"click",function(){e.enterClubTab(4)})},openClubPop:function(){this.changeTab(0),this.showView(this.urlDomain+this.urls[0],0);var e=document.getElementById("auto-header-clubmask"),t=document.getElementById("auto-header-clublayer");"none"==t.style.display&&(t.style.display="",e&&(e.style.display=""))},closeClubPop:function(){var e=document.getElementById("auto-header-clublayer"),t=document.getElementById("auto-header-clubmask");e&&(e.style.display="none"),t&&(t.style.display="none")},enterClubTab:function(e){this.changeTab(e),this.showView(this.urlDomain+this.urls[e],e)},changeTab:function(e){for(var t=0;t<=4;t++)document.getElementById("auto-header-club-tab"+t).className="";document.getElementById("auto-header-club-tab"+e).className="cur"},showView:function(e,t){function n(e){switch(document.getElementById("auto-header-clubhtml").innerHTML=e,t){case 0:a.initClubSearch();break;case 1:a.initClubSeries()}}var a=this,l=["findHtml","brandHtml","areaHtml","themeHtml","motorHtml"],o=l[t];if(o){document.getElementById("auto-header-clubhtml").innerHTML="";var c=a.clubData[o];""!=c?n(c):u(a.urlDomain+a.urls[t],function(e){var t=e.html||"";a.clubData[o]=t,n(t)})}},initClubSearch:function(){function e(e,t){if(2*e.length<=t)return e;for(var n=0,a="",l=0;l<e.length;l++)if(a+=e.charAt(l),e.charCodeAt(l)>128){if(n+=2,n>=t)return a.substring(0,a.length-1)}else if(n+=1,n>=t)return a.substring(0,a.length-2);return a}function t(e){if("none"!=r.style.display){var t=r.getElementsByTagName("li").length;38==e.keyCode&&(i--,i<=0&&(i=t)),40==e.keyCode&&(i++,i>t&&(i=1));for(var n=r.getElementsByTagName("a")[i-1],a=0;a<t;a++)r.getElementsByTagName("a")[a].style.backgroundColor="";n.style.backgroundColor="#e7f0f9",o.value=n.title}}function n(e){var t=o.value.replace(/(^\s*)|(\s*$)/g,"");if(""!=t&&t!=o.getAttribute("lang"))try{u("//sou.api.autohome.com.cn/v2/topicentry/search",{q:escape(t),_appid:"club"},"_callback",function(t){a(e,t)})}catch(n){}}function a(t,n){var a=[],l=[];if(n&&n.result&&"0"==n.returncode&&n.result.hitlist)for(var o=0;o<n.result.hitlist.length&&!(1==t&&a.length+l.length>9);o++){var u=n.result.hitlist[o].data,c=u.bbsname;if(c&&(c=c.indexOf("\u8bba\u575b")>-1?c:c+"\u8bba\u575b",a.push('<li><a target="_blank" href="//club.autohome.com.cn/bbs/forum-'+u.bbs+"-"+u.bbsid+'-1.html" title="'+c+'"  >'+c+"</a></li>")),u.carclub)for(var i=0;i<u.carclub.length;i++){var s=u.carclub[i];if(1==t&&a.length+l.length>9)break;l.push('<li><a target="_blank" href="//club.autohome.com.cn/carclub/index-'+u.bbs+"-"+u.bbsid+"-"+s.id+'-1.html" title="'+s.name+'">'+e(s.name,22)+"</a></li>")}}var d=document.getElementById("searchUl"),m=document.getElementById("searchh3"),h=document.getElementById("searchins");if(0==t){a.length>0?d.innerHTML=a.join(""):d.innerHTML="<span>\u62b1\u6b49\uff0c\u6ca1\u6709\u627e\u5230\u7ed3\u679c\u3002</span>",m.style.display="",d.style.display="",h.style.display="";var b=document.getElementById("_autoclubrecom"),f=b.getElementsByTagName("ul")[0];b.style.display="none",l.length>0&&(f.innerHTML=l.join(""),b.style.display="")}1==t&&(a.length+l.length>0?(r.innerHTML="<ul>"+a.join("")+l.join("")+"</ul>",r.style.display=""):r.style.display="none")}var l=document.getElementById("auto-header-clubhtml"),o=document.getElementById("otherSearch"),c=document.getElementById("otherBtn"),r=document.getElementById("seachtishibox"),i=0;""==o.value&&(o.value=o.getAttribute("lang")),o.onfocus=function(){o.parentNode.setAttribute("class","pf_search_fous"),o.getAttribute("lang")==o.value.replace(/(^\s*)|(\s*$)/g,"")&&(o.value="")},o.onblur=function(){""==o.value.replace(/(^\s*)|(\s*$)/g,"")&&(o.parentNode.setAttribute("class","pf_search"),o.value=o.getAttribute("lang"))},o.onkeydown=function(e){38!=e.keyCode&&40!=e.keyCode||t(e),13==e.keyCode&&(r.style.display="none",n(0))},o.onkeyup=function(e){38!=e.keyCode&&40!=e.keyCode&&13!=e.keyCode&&n(1)},c.onclick=function(){return n(0),r.style.display="none",!1},l.onclick=function(){r.style.display="none"},r.style.display="none"},initClubSeries:function(){function e(e){for(var t,n=c.getElementsByTagName("h4"),a=0;a<n.length;a++)if(t=n[a],t.getAttribute("lang")===e)return t}var t,o,u,c=document.getElementById("auto-header-clubhtml"),r=c.getElementsByTagName("h3")[0].getElementsByTagName("a"),i=l("backtop",c);for(i[0].style.display="none",u=0;u<i.length;u++)o=i[u],o.onclick=function(){c.scrollTop=0};for(u=0;u<r.length;u++)t=r[u],t.onclick=function(){for(var t=0;t<r.length;t++)a(r[t],"cur");n(this,"cur");var l=this.getAttribute("lang"),o=e(l);c.scrollTop=o.offsetTop}}},e.AutoHeaderClub=c,e.autoHeaderClubObj=new c}(this);
</script>
<script type="text/javascript">
    function loadScript(t, e) { var a = document.createElement("script"); a.type = "text/javascript", a.readyState ? a.onreadystatechange = function () { ("loaded" == a.readyState || "complete" == a.readyState) && (a.onreadystatechange = null, e()) } : a.onload = function () { e() }, a.src = t, document.body.appendChild(a) } loadScript("//x.autoimg.cn/space/AutoRequestHeader/zhixun/AutoHeartBeat.js?tv=101", function () { AutoHeartBeat.Main() });
</script>
<script type="text/javascript">
    (function () {
        var cityid = Math.floor(window.readCookie("cookieCityId", window.readCookie("area", 0)) / 100) * 100;
        var showCityId = [110100, 120100, 310100, 320500, 330100, 410100, 420100, 440100, 440300, 500100, 510100, 610100];
        if (showCityId.indexOf(cityid) > -1) {
            document.getElementById('auto-header-channel15').setAttribute("href", "//yc.autohome.com.cn/list?pvareaid=2868121");
            document.getElementById('auto-header-channel15').text = "养车";
        } else {
            document.getElementById('auto-header-channel15').setAttribute("href", "//k.autohome.com.cn/");
            document.getElementById('auto-header-channel15').text = "口碑";
        }
    })();
</script>

    <script type="text/javascript">
        var autoHeaderObj=new AutoHeader();
    </script>
    
	<div class="content">
	   <!---炫景广告开始-->
        <div id="s6378" style="display: none;"></div>
        <!---炫景广告结束-->  
    <div class="monkey monkey_box fn-hide">
      <div id="s2823" data-adparent=".monkey"></div>
    </div>

		<!--导航栏开始-->
		

<div class="subnav">
	<div class="subnav-title fn-clear">
		<div class="subnav-title-name fn-left">
			<h2>资讯文章</h2>
		</div>
        <div class="subnav-title-ad fn-left" id="ad_pdgm">
            
        </div>
		<div class="search search02 fn-right">
			<div class="search-box">
                <form target="_blank" action="//sou.autohome.com.cn/search.aspx" name="soform" id="souform">
                    <input data-toggle="search" data-val="请输入关键字" type="text" class="search-text" value="" autocomplete="off" id="q" name="q" />
                </form>
			</div>
			<a href="javascript:void(0);" onclick="document.getElementById('souform').submit(); return false;" class="btn btn-small btn-blue"><i class="icon16 icon16-search1"></i></a>
            <!--联想层-->
            <div id="autocomplateTip" class="search-pop" style="display:none"></div>
		</div>
	</div>
	<div id="ulNav" class="nav-typebar fn-clear">
	    <ul>
		    <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/all/">最新</a></li>
		    <li class="nav-item current"><a target="_self" href="//www.autohome.com.cn/news/">新闻</a></li>
		    <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/advice/">导购</a></li>
		    <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/drive/">试驾评测</a></li>
		    <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/use/">用车</a></li>
		    <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/culture/">文化</a></li>
		    <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/travels/">游记</a></li>
		    <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/tech/">技术</a></li>
		    <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/tuning/">改装赛事</a></li>
            <li class="nav-item "><a target="_self" href="//www.autohome.com.cn/ev/">新能源</a></li>
	    </ul>
	</div>
</div>
        <!--导航栏结束-->
		
        <div class="row">
			<div class="column grid-13 grid-left">
				<!--焦点图开始-->
				
<div class="news-focus">
    <div class="focusimg focusimg02" id="focus-1">
        <!--图片内容部分-->
        <div class="focusimg-pic">
            <ul>
                
                    <li >
                        <h2><a href="//www.autohome.com.cn/news/201901/928325.html#pvareaid=102623">快评：从Fisker到Karma 加州独角兽归来</a></h2>
                        <p>[汽车之家 新闻]  2007年，一家名为Fisker Automotive汽车公司在美国成立。那是一个没有造车新势力、生态系统、区块链等名词的蛮荒年代，即使是特斯拉也还...</p>
                        <a href="//www.autohome.com.cn/news/201901/928325.html#pvareaid=102623"><img src="//www2.autoimg.cn/newsdfs/g30/M04/57/65/640x320_0_autohomecar__ChcCSVw1n5CAaYl6AAjbnIKCEjQ231.jpg" alt="快评：从Fisker到Karma 加州独角兽归来"></a>
                    </li>
                
                    <li >
                        <h2><a href="//www.autohome.com.cn/news/201901/928310.html#pvareaid=102623">红旗HS5/奔腾D058等 一汽2019新车展望</a></h2>
                        <p>[汽车之家 新闻]  此时此刻的你也许还在留恋2018年，但已经有很多车企立下了2019年的Flag，这当中完成重组后一年的一汽集团将在2019年携旗下三大品牌发布多款新...</p>
                        <a href="//www.autohome.com.cn/news/201901/928310.html#pvareaid=102623"><img src="//www2.autoimg.cn/newsdfs/g30/M01/56/58/640x320_0_autohomecar__ChsEf1w0z4aAeqyoAAXH_Q_cSj8061.jpg" alt="红旗HS5/奔腾D058等 一汽2019新车展望"></a>
                    </li>
                
                    <li id="ad_368_1">
                        <h2><a href="//www.autohome.com.cn/news/201901/927871.html#pvareaid=102623">CS85/逸动ET等 长安2019年新车展望</a></h2>
                        <p>[汽车之家 新闻]  各位网友们大家好，我们的2019年车企新车展望系列文章在新的一年里又和大家见面了！是不是在已经过去的2018年里没有等到让您怦然心动的新车？莫慌莫慌...</p>
                        <a href="//www.autohome.com.cn/news/201901/927871.html#pvareaid=102623"><img src="//www2.autoimg.cn/newsdfs/g26/M03/10/97/640x320_0_autohomecar__ChcCP1wl0feAFDirAAW0NPYZcVk831.jpg" alt="CS85/逸动ET等 长安2019年新车展望"></a>
                    </li>
                
            </ul>
        </div>
        <!--图片进度部分-->
        <div class="focusimg-bt">
            <div class="focusimg-bt-left"><a href="javascript:void(0);" target="_self"></a></div>
            <div class="focusimg-bt-right"><a href="javascript:void(0);" target="_self"></a></div>
        </div>
        <div class="focusimg-focus">
             
            <span class="selected" ><a href="javascript:void(0);" target="_self"></a></span>
             
            <span  ><a href="javascript:void(0);" target="_self"></a></span>
             
            <span  ><a href="javascript:void(0);" target="_self"></a></span>
             
        </div>
    </div>
</div>
				<!--焦点图结束-->
                
                <div class="advlist fn-clear fn-hide">
                    
                    <i class="monkey__iconalone"></i>
                    <ul>
                        <li id="ad_word_t1" data-adparent=".advlist"></li>
                        <li id="ad_word_t2" data-adparent=".advlist"></li>
                        <li id="ad_word_t3" data-adparent=".advlist"></li>
                    </ul>
                </div>
                <a name="liststart" class="aname">&nbsp;</a>
                <div class="monkey monkey_box fn-hide">
                  <div id="ad_760_21" data-adparent=".monkey"></div>
                </div>
                
                <div class="m-nav-title m-nav-title-border">
                    <h3 class="h3cur"><a href="news/?p=s" target="_self">全部</a></h3>
                    <div class="div-fouc">
                        
                        <div class="div-fouc-bt div-fouc-bt-right"><a id="right" class="icon16 icon16-right" href="javascript:void(0);" target="_self"></a></div>
                  	    <div class="div-fouc-bt div-fouc-bt-left"><a id="left" class="icon16 icon16-left" href="javascript:void(0);" target="_self"></a></div>
                        
                        <div id="div-fouc-tx" class="div-fouc-tx">
                                             
                             <ul class='fouc-current'>                      
                                   
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="7" target="_self">行业动态</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="10" target="_self">热点追踪</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="40" target="_self">车闻轶事</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="70" target="_self">国产新车</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="71" target="_self">进口新车</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="87" target="_self">召回碰撞</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="114" target="_self">市场分析</a></li>
                            
                                 </ul>
                                          
                             <ul >                      
                                   
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="115" target="_self">用户调研</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="135" target="_self">高端访谈</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="148" target="_self">零部件</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="149" target="_self">智能网联</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="150" target="_self">行业政策</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="151" target="_self">整车</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="152" target="_self">新能源</a></li>
                            
                        	  <li ''><a data-toggle="tab" href="javascript:void(0);" data-class="153" target="_self">后市场</a></li>
                            
                                 </ul>
                            
                    </div>
                                        
                    </div>
                </div>
                

				<!--文章内容开始-->
		        

<div id="auto-channel-lazyload-article" class="article-wrapper">
    
                     <ul class="article" >
    
                        <li data-artIdAnchor="928831">
                            <a href="//www.autohome.com.cn/news/201901/928831.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g26/M07/77/36/120x90_0_autohomecar__ChsEnFxBecWASpRhAAGtvJTLyVw434.jpg"></div>
                                <h3>年产能30万台 长城日照生产基地开工</h3>
                                <div class="article-bar">
                                    <span class="fn-left">15分钟前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>153</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928831"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  1月18日，长城汽车日照生产基地项目开工，该基地的设计年产能为30万台，未来将主要负责长城旗下高端品牌WEY系列产品的生产任务。...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928797">
                            <a href="//www.autohome.com.cn/news/201901/928797.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g3/M0A/91/2A/120x90_0_autohomecar__ChsEkVxBewGAUW_LAAFIai13Ll4987.jpg"></div>
                                <h3>BYTON空间开业 预计2019年底交付量产车</h3>
                                <div class="article-bar">
                                    <span class="fn-left">18分钟前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>132</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928797"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  1月18日，智能电动汽车品牌拜腾全球首家品牌体验店——BYTON空间在上海举行开业典礼，并将于1月20日正式对公众开放。开业典礼...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928830">
                            <a href="//www.autohome.com.cn/news/201901/928830.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g26/M0B/7C/42/120x90_0_autohomecar__ChsEe1xBd0SAYhVOAAH6S5ESGFc953.jpg"></div>
                                <h3>雷丁汽车100%全资收购野马汽车股份</h3>
                                <div class="article-bar">
                                    <span class="fn-left">31分钟前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>486</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928830"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  2019年1月18日，我们从雷丁汽车官方获悉，雷丁&amp;野马战略重组签约仪式在成都举行，宣布雷丁汽车正式入主野马汽车，并拥有...</p>
                            </a>
                        </li>
    
                        <li id="ad_tw_04" style="display: none;"></li>
    
                        <li data-artIdAnchor="928829">
                            <a href="//www.autohome.com.cn/news/201901/928829.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g26/M00/76/F3/120x90_0_autohomecar__ChsEnFxBbReAQO9LAAEZpO3LnUo344.jpg"></div>
                                <h3>换装全新方向盘 曝新款吉利帝豪GL谍照</h3>
                                <div class="article-bar">
                                    <span class="fn-left">40分钟前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1249</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928829"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从相关渠道获取到了一组新款吉利帝豪GL车型的测试谍照，通过谍照我们发现，该车外观基本维持现款的主体设计风格，仅是在...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928822">
                            <a href="//www.autohome.com.cn/news/201901/928822.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g30/M0B/75/89/120x90_0_autohomecar__ChsEoFxBP0WANwUBAAHS0tyicFs979.jpg"></div>
                                <h3>国内乘用车市场一年召回量超1200万辆</h3>
                                <div class="article-bar">
                                    <span class="fn-left">57分钟前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>150</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928822"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  继2016年、2017年缺陷汽车召回数量突破千万辆后，2018年我国国内乘用车市场汽车召回量再次突破千万规模，召回数量达到125...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928826">
                            <a href="//www.autohome.com.cn/news/201901/928826.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g26/M04/7B/E7/120x90_0_autohomecar__ChsEe1xBZVyATPGCAAFvPMCQn50169.jpg"></div>
                                <h3>售27.88-36.88万元 新款福特撼路者上市</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928826"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  2019年1月18日，2019款江铃福特撼路者正式上市，新车推出搭载2.0T汽油发动机和2.2T柴油发动机的共8款车型，其售...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928825">
                            <a href="//www.autohome.com.cn/news/201901/928825.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g29/M09/79/1B/120x90_0_autohomecar__ChcCSFxBQ72AFi5QAAKON8bjewo444.jpg"></div>
                                <h3>奥迪与高精地图公司HERE达成数据合作</h3>
                                <div class="article-bar">
                                    <span class="fn-left">2小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>285</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928825"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  据外媒报道，高精地图公司HERE Technologies宣布成为奥迪的合作伙伴，从2019年上半年开始，将为奥迪所有北美和欧洲...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928824">
                            <a href="//www.autohome.com.cn/news/201901/928824.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g1/M0A/68/D6/120x90_0_autohomecar__ChcCQ1xBSPKAYEfJAAD-Qaz-880838.jpg"></div>
                                <h3>分时租领企业领航员科技获数百万元融资</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1411</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928824"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  日前，共享出行服务商“领航员科技”宣布获得中海外新能源领投的数百万元的天使轮融资。据悉，融资将主要用于市场拓展、推出新的商务出行...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928813">
                            <a href="//www.autohome.com.cn/news/201901/928813.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g1/M0B/96/9E/120x90_0_autohomecar__ChsEj1xBNTaAOSvsAAEEZFqqqkA213.jpg"></div>
                                <h3>总金额逾8亿 尤夫股份获动力电池订单</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3672</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928813"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  1月17日，尤夫股份公告称，1月15日，公司旗下江苏智航新能源有限公司与河南锂想动力科技有限公司签署销售1亿支三元锂离子电芯的合...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928823">
                            <a href="//www.autohome.com.cn/news/201901/928823.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g2/M0B/67/6D/120x90_0_autohomecar__ChcCRFxBRciAckFKAABhVWkW704387.jpg"></div>
                                <h3>率先搭载宝骏RS-5 宝骏发布全新标识</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>2.4万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928823"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，宝骏汽车正式发布了其全新标识——钻石标，未来将会搭载在其高端系列产品上，与现款标识共存，首款搭载该车标的车型为其全新的紧凑...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928821">
                            <a href="//www.autohome.com.cn/news/201901/928821.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g29/M08/7D/78/120x90_0_autohomecar__ChsEflxBQoyAPnqtAAE8XfzV65k747.jpg"></div>
                                <h3>前景广阔 动力电池回收市场规模达65亿</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1917</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928821"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  “2014年电动车开始规模化，动力电池的使用年限一般5-8年。相当一部分电池面临淘汰临界点，意味着从今明两年动力电池很有可能将进...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928816">
                            <a href="//www.autohome.com.cn/news/201901/928816.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g28/M0A/76/D3/120x90_0_autohomecar__ChsEnlxBPk-AFd3mAAEvvcL3Zhk800.jpg"></div>
                                <h3>福特汽车今年将有5款车型转到国内生产</h3>
                                <div class="article-bar">
                                    <span class="fn-left">3小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>7592</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928816"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  日前，长安汽车对外披露的投资者关系活动记录表显示，福特汽车计划自2019年开始，将5款车型转到中国生产，以满足中国市场的需求。其...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928819">
                            <a href="//www.autohome.com.cn/news/201901/928819.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g27/M0B/7A/EE/120x90_0_autohomecar__ChcCQFxBQFuADuREAAFw814iiAM040.jpg"></div>
                                <h3>又增一家 智行者获北京自动驾驶牌照</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1519</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928819"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  近日，智能车联网站更新北京自动驾驶路测资质信息，资质名单上新增一家企业，为北京智行者科技有限公司（简称“智行者”）。智行者方面指...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928815">
                            <a href="//www.autohome.com.cn/news/201901/928815.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g1/M06/99/1E/120x90_0_autohomecar__ChsEmVxBN6eAfcwiAAFSQdQxQzA602.jpg"></div>
                                <h3>丰富你的选择 曝观致3 EV两厢版申报图</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>2306</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928815"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从国家工信部获得了一组观致3 EV两厢版车型的申报图，新车整体与沿用了观致3燃油版车型的设计风格，仅是细节方面以及...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928820">
                            <a href="//www.autohome.com.cn/news/201901/928820.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g29/M01/79/09/120x90_0_autohomecar__ChcCSFxBP8aAEqhVAAGEVt96u84372.jpg"></div>
                                <h3>部分进口4008/进口C4 Aircross被召回</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1315</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928820"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，神龙汽车有限公司根据《缺陷汽车产品召回管理条例》和《缺陷汽车产品召回管理条例实施办法》的要求，向国家市场监督管理总局备案了...</p>
                            </a>
                        </li>
    
                    </ul>
    
                     <ul class="article" style="display:none;">
    
                        <li data-artIdAnchor="928818">
                            <a href="//www.autohome.com.cn/news/201901/928818.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g2/M02/7D/DE/120x90_0_autohomecar__ChsEkFxBPuSAUKIyAAFVnQEMY1Y820.jpg"></div>
                                <h3>因高田气囊隐患 特斯拉召回部分Model S</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>630</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928818"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，特斯拉汽车（北京）有限公司根据《缺陷汽车产品召回管理条例》和《缺陷汽车产品召回管理条例实施办法》的要求，向国家市场监督管理...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928814">
                            <a href="//www.autohome.com.cn/news/201901/928814.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g27/M01/7C/82/120x90_0_autohomecar__ChsEfFxBO8yAFihhAAGUa7Blbb0921.jpg"></div>
                                <h3>半轴存脱落隐患 奇瑞召回8580辆瑞虎3xe</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1484</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928814"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，奇瑞汽车股份有限公司按照《缺陷汽车产品召回管理条例》和《缺陷汽车产品召回管理条例实施办法》的要求，向国家市场监督管理总局备...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928810">
                            <a href="//www.autohome.com.cn/news/201901/928810.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g26/M03/7A/ED/120x90_0_autohomecar__ChsEe1xBMvuACpeDAAFw6lU0nPU253.jpg"></div>
                                <h3>马斯克：特斯拉将终止车主引荐奖励计划</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1624</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928810"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  1月17日，特斯拉首席执行官埃隆&#183;马斯克在Twitter上发布消息称，特斯拉的客户推荐计划将于2月1日结束。在该计划中...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928807">
                            <a href="//www.autohome.com.cn/news/201901/928807.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g30/M05/7B/10/120x90_0_autohomecar__ChsEf1xBLtOAaDkMAAHXgHZFlBQ963.jpg"></div>
                                <h3>在武汉新建工厂 吉利要国产路特斯？</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1126</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928807"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  近日我们根据吉利招聘广告以及地方政府文件推测，吉利汽车或将在武汉开设新厂用于生产路特斯（莲花Lotus）跑车。    从吉利招聘...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928812">
                            <a href="//www.autohome.com.cn/news/201901/928812.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g27/M09/7C/6C/120x90_0_autohomecar__ChsEfFxBN96AalepAAF1CVV6LJ4682.jpg"></div>
                                <h3>3月上市 国产全新速腾无伪装实车曝光</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>16.8万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928812"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，有网友在北京某商区拍摄到了一汽-大众全新一代速腾的无伪装实车。该车尾部悬挂的牌照显示，全新速腾的官方英文名称为“NEX...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928809">
                            <a href="//www.autohome.com.cn/news/201901/928809.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g1/M06/98/FF/120x90_0_autohomecar__ChsEmVxBMTGAQGsHAAFRUH8yHzg380.jpg"></div>
                                <h3>桩企苦尽甘来？2019年地补或向充电倾斜</h3>
                                <div class="article-bar">
                                    <span class="fn-left">4小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1354</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928809"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  电动车充电基础设施产业已经度过了最难熬的一年，2019年产业环境会大幅改善，整体政策迎来利好。1月18日，中国充电联盟2019年...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928811">
                            <a href="//www.autohome.com.cn/news/201901/928811.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g26/M0A/79/40/120x90_0_autohomecar__ChcCP1xBMvOAd3-YAAGb09vrZV0233.jpg"></div>
                                <h3>售18.88万元起 北汽新能源EX5开启预售</h3>
                                <div class="article-bar">
                                    <span class="fn-left">5小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5995</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928811"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  1月18日，北汽新能源官方正式宣布旗下紧凑型纯电动SUV——EX5正式开启预售，其车系预售价格为18.88万元起。同时官方表示，...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928799">
                            <a href="//www.autohome.com.cn/news/201901/928799.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g2/M0B/7C/4D/120x90_0_autohomecar__ChsEkFxAgAOAYY7CAAEa0ZetBmQ935.jpg"></div>
                                <h3>合作硬蛋网 丰田创建智能汽车生态系统</h3>
                                <div class="article-bar">
                                    <span class="fn-left">5小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>574</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928799"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  据外媒报道，中国科通芯城旗下子公司硬蛋网宣布与丰田汽车公司达成战略协议，将在中国合作创建“丰田硬蛋网创新平台”（Toyota I...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928808">
                            <a href="//www.autohome.com.cn/news/201901/928808.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g29/M03/7C/EE/120x90_0_autohomecar__ChsEflxBKkCAFHWEAAEuvfiMK8M647.jpg"></div>
                                <h3>搭82马力驱动电机 众泰E330申报图曝光</h3>
                                <div class="article-bar">
                                    <span class="fn-left">5小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>4312</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928808"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从国家工信部获得了一组众泰E330申报图，按照新能源车型以往的命名规则来看，EV后面的后缀一般为该车的等速法续航里...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928806">
                            <a href="//www.autohome.com.cn/news/201901/928806.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g29/M09/7C/C7/120x90_0_autohomecar__ChsEflxBH-2AEHroAAEqAZKfdDA143.jpg"></div>
                                <h3>搭1.5L发动机 SWM斯威X2申报图曝光</h3>
                                <div class="article-bar">
                                    <span class="fn-left">6小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>7345</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928806"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从国家工信部获得了一组SWM斯威旗下全新紧凑型SUV——X2的申报信息，该车将搭载一台最大功率为112马力的1.5...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928805">
                            <a href="//www.autohome.com.cn/news/201901/928805.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g30/M07/7A/04/120x90_0_autohomecar__ChcCSVxBG1GAZh6iAAFKSD8zM38431.jpg"></div>
                                <h3>新增1.6T发动机 众泰T500新车型申报图</h3>
                                <div class="article-bar">
                                    <span class="fn-left">6小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1.1万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928805"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从国家工信部获得了一组众泰T500 1.6T车型的申报信息，新车整体设计与现款车型保持一致。未来新车的推出，将进一...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928804">
                            <a href="//www.autohome.com.cn/news/201901/928804.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g2/M03/7D/34/120x90_0_autohomecar__ChsEkFxBGBWAY0C-AAE1JwVKRJE448.jpg"></div>
                                <h3>前脸有变化 新款东风风神AX5申报图曝光</h3>
                                <div class="article-bar">
                                    <span class="fn-left">6小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>8792</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928804"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从国家工信部获得了一组新款东风风神AX5车型申报信息，该车前脸采用了全新的设计风格，使该车时尚感有所提升。　　友情...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928803">
                            <a href="//www.autohome.com.cn/news/201901/928803.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g1/M03/98/9E/120x90_0_autohomecar__ChsEmVxBFMiAHwG2AAEp30EphSU582.jpg"></div>
                                <h3>前脸变化巨大 曝新款江淮瑞风S3申报图</h3>
                                <div class="article-bar">
                                    <span class="fn-left">7小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>8979</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928803"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从国家工信部获得了一组新款江淮瑞风S3的申报图，该车前脸采用了全新的设计风格，整体相比现款要更加具有辨识度。　　友...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928800">
                            <a href="//www.autohome.com.cn/news/201901/928800.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g3/M09/7F/0E/120x90_0_autohomecar__ChcCRVxAl1WAFMF8AAF6P_ZMMkU929.jpg"></div>
                                <h3>布局电池回收 天际汽车与华友循环合作</h3>
                                <div class="article-bar">
                                    <span class="fn-left">8小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3095</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928800"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  1月16日，天际汽车与华友循环签署战略合作协议，双方计划在新能源汽车动力电池梯次利用和材料回收领域展开合作。合作协议显示，天际汽...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928794">
                            <a href="//www.autohome.com.cn/news/201901/928794.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g27/M09/79/4E/120x90_0_autohomecar__ChcCQFxAgruAZAi3AAHOexc8qpo978.jpg"></div>
                                <h3>XT6/探险者等8款 北美车展入华新车展望</h3>
                                <div class="article-bar">
                                    <span class="fn-left">8小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>26.8万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928794"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  2019北美车展缺席了不少重磅汽车品牌，但作为北美最大的汽车展会，首发新车依旧超过15款，其中我们汇总了有望进入中国市场销售的车...</p>
                            </a>
                        </li>
    
                    </ul>
    
                     <ul class="article" style="display:none;">
    
                        <li data-artIdAnchor="928611">
                            <a href="//www.autohome.com.cn/news/201901/928611.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g1/M08/65/58/120x90_0_autohomecar__ChcCQ1xAJYOALkzXAAE0ZlvTmCk782.jpg"></div>
                                <h3>如何用好“捷达”名片？大众欲推新品牌</h3>
                                <div class="article-bar">
                                    <span class="fn-left">9小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928611"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  终于要落地！除大众、奥迪外，一汽-大众要生产和销售第三个汽车品牌的消息已经证实，官方消息是这样的：当地时间2月25-27日，大众...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928796">
                            <a href="//www.autohome.com.cn/news/201901/928796.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g27/M02/74/E1/120x90_0_autohomecar__ChsEnVxAdv6ADuk7AAF-AboX2y4866.jpg"></div>
                                <h3>将于1月22日上市 曝福特领界最新消息</h3>
                                <div class="article-bar">
                                    <span class="fn-left">18小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>11.9万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928796"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，我们从福特官方了解到，旗下全新紧凑型SUV——福特领界将于1月22日正式上市，新车介于福特翼搏和福特翼虎之间。新车先期将提...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928795">
                            <a href="//www.autohome.com.cn/news/201901/928795.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g26/M06/79/6F/120x90_0_autohomecar__ChsEe1xAcd6AYl4xAAFZ58xz7jw893.jpg"></div>
                                <h3>将于3月初上市 曝长安CS85 COUPE新消息</h3>
                                <div class="article-bar">
                                    <span class="fn-left">18小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5.1万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928795"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，我们从长安官方了解到，其旗下全新中型SUV——CS85 COUPE将于3月初正式上市。同时，其2.0T版本车型已于此前开启...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928687">
                            <a href="//www.autohome.com.cn/news/201901/928687.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g27/M06/70/46/120x90_0_autohomecar__ChcCQFw9rIGATPLNAAIAv_gXWtY743.jpg"></div>
                                <h3>伪蓝海还是真黑马 2019年家用MPV会火吗</h3>
                                <div class="article-bar">
                                    <span class="fn-left">19小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928687"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  人们对于美好的愿望总是抱以期待，在汽车行业同样如此，尤其在整体车市负增长的大环境之下，车企们都期待能够有一个细分市场增量能如同十...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928793">
                            <a href="//www.autohome.com.cn/news/201901/928793.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g27/M0B/7A/39/120x90_0_autohomecar__ChsEfFxAUHmAJlxAAADnW5CSRnI726.jpg"></div>
                                <h3>推动产品更新 凯翼汽车公布2019年计划</h3>
                                <div class="article-bar">
                                    <span class="fn-left">20小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>6424</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928793"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，凯翼汽车公布了该品牌2019年的产品计划，根据相关信息我们得知，凯翼汽车将在2019年着重于现有产品的更新以及新产品的推出...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928792">
                            <a href="//www.autohome.com.cn/news/201901/928792.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g3/M04/8D/BF/120x90_0_autohomecar__ChsEkVxAUzOAO614AAHO6nAfaNg929.jpg"></div>
                                <h3>由森雅R7升级而来 一汽森雅R8正式发布</h3>
                                <div class="article-bar">
                                    <span class="fn-left">21小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928792"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车首发]  1月17日，一汽吉林森雅R8车型在2019年度一汽吉林商务年会活动上正式发布。虽然基于森雅R7车型打造而来，但森雅R8针对原...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928791">
                            <a href="//www.autohome.com.cn/news/201901/928791.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g30/M08/73/26/120x90_0_autohomecar__ChsEoFxATpeAZ8gXAADlKh8aQXs550.jpg"></div>
                                <h3>提供3种座椅布局 上汽大通D60新预告图</h3>
                                <div class="article-bar">
                                    <span class="fn-left">21小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928791"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，我们从上汽大通官方获得了一组其旗下全新中型SUV——D60最新预告图，新车可以看作是TARANTULA概念车的量产版。同时...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928789">
                            <a href="//www.autohome.com.cn/news/201901/928789.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g26/M0A/73/87/120x90_0_autohomecar__ChsEnFxAR2WAY3tzAAHX4Ry1Ia0479.jpg"></div>
                                <h3>阿斯顿·马丁DBX将于2019年底在华发布</h3>
                                <div class="article-bar">
                                    <span class="fn-left">21小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>2.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928789"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  2019年1月恰逢阿斯顿&#183;马丁品牌诞生106周年，阿斯顿&#183;马丁中国总裁彭明山透露，旗下首款SUV——DBX车...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928758">
                            <a href="//www.autohome.com.cn/news/201901/928758.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g29/M08/6F/0B/120x90_0_autohomecar__ChsEn1w-4tOALo55AAESvnEjJrs000.jpg"></div>
                                <h3>比亚迪新款元EV补贴后预售11万元起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">22小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1.8万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928758"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  1月17日，比亚迪新款元EV535正式开启预售，新车预售价格区间为11.00-14.00万元（补贴后），同时，预购新车的客户还将...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928787">
                            <a href="//www.autohome.com.cn/news/201901/928787.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g30/M03/72/87/120x90_0_autohomecar__ChsEoFxAM_SABzoCAAGLsjF7uAE498.jpg"></div>
                                <h3>华丽转身？凯翼汽车迁址后首款车下线</h3>
                                <div class="article-bar">
                                    <span class="fn-left">23小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>9471</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928787"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前我们从官方获悉，自2019年伊始，凯翼汽车公司将整体入驻四川宜宾和成都，并在这里正式拥有了独立的生产基地和研发中心，这也意味...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928771">
                            <a href="//www.autohome.com.cn/news/201901/928771.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g1/M03/94/7A/120x90_0_autohomecar__ChsEmVw_2vSAZQcjAAFEigP2Fq4309.jpg"></div>
                                <h3>意美森签署新合作 车载触摸操控成趋势</h3>
                                <div class="article-bar">
                                    <span class="fn-left">23小时前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>515</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928771"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  据外媒报道，当地时间1月15日，意美森公司（Immersion Corporation）宣布与韩国瑞延理化电子有限公司（Seoy...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928715">
                            <a href="//www.autohome.com.cn/news/201901/928715.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g26/M08/75/F4/120x90_0_autohomecar__ChcCP1xAG6iAZpMgAAHCBnOPc7I504.jpg"></div>
                                <h3>售价9.68-12.98万元 欧尚科尚正式上市</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.1万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928715"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车上市]  日前，我们从欧尚汽车官方获悉，旗下全新MPV车型——欧尚COSMOS(科尚)正式上市。新车共推出搭载1.5T发动机的5款车型...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928784">
                            <a href="//www.autohome.com.cn/news/201901/928784.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g27/M06/72/66/120x90_0_autohomecar__ChsEnVw_9oaAKZ7QAAD2RCE_Mq8785.jpg"></div>
                                <h3>1千瓦时20元 深圳首设动力电池回收补贴</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5461</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928784"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  近日，深圳市财政委员会、深圳市发改委联合发布了《深圳市2018年新能源汽车推广应用财政支持政策》（简称《政策》），共设置了三类补...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928786">
                            <a href="//www.autohome.com.cn/news/201901/928786.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g29/M00/74/72/120x90_0_autohomecar__ChcCSFw_67iADUTcAAEQKtQEwOQ495.jpg"></div>
                                <h3>更新头/尾设计 新款吉利远景X3申报图</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.2万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928786"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从国家工信部获取了新款吉利远景X3的申报图，从申报图我们可以看出，新车更新了前/后保险杠的设计，造型显得更加夸张。...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928760">
                            <a href="//www.autohome.com.cn/news/201901/928760.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g1/M03/94/E8/120x90_0_autohomecar__ChsEmVw_7BCADJlTAACqVqCPNug019.jpg"></div>
                                <h3>深化物联网布局 亚马逊再投芯片公司</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3616</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928760"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  亚马逊又投了一家芯片公司。近日，据外媒报道，亚马逊（Amazon）旗下公司亚马逊云计算服务公司（Amazon Web Servi...</p>
                            </a>
                        </li>
    
                    </ul>
    
                     <ul class="article" style="display:none;">
    
                        <li data-artIdAnchor="928779">
                            <a href="//www.autohome.com.cn/news/201901/928779.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g3/M0A/8B/9F/120x90_0_autohomecar__ChsEkVw_7AGARyorAABweqMvBis938.jpg"></div>
                                <h3>GBatteries称15分钟可充满60kWh电池组</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>754</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928779"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  据外媒报道，一家来自硅谷的初创公司GBatteries近日宣称，其可像给燃油车油箱加油一样，快速给电动车充满电。    GBat...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928781">
                            <a href="//www.autohome.com.cn/news/201901/928781.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g2/M0B/AB/D1/120x90_0_autohomecar__ChsEmlw_7uqAH99uAACSOfnCG20730.jpg"></div>
                                <h3>索赔700万欧元 日产或对戈恩提起民诉 </h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>2528</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928781"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  据外媒报道，一位知情人士透露，日产汽车计划对其前董事长卡洛斯&#183;戈恩（Carlos Ghosn）提起民事诉讼，要求其赔偿...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928774">
                            <a href="//www.autohome.com.cn/news/201901/928774.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g2/M07/AB/7C/120x90_0_autohomecar__ChsEmlw_4aeAI2p7AADa_7Z9s3s202.jpg"></div>
                                <h3>麦格纳呼吁减少对电动车/自动驾驶投入</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1416</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928774"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  据外媒报道，全球汽车零部件供应商麦格纳国际首席执行官唐&#183;沃克尔近日表示，全球范围内的汽车及零部件制造商需要减少对电动车...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928778">
                            <a href="//www.autohome.com.cn/news/201901/928778.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g3/M0B/8B/83/120x90_0_autohomecar__ChsEkVw_57uAaDXcAAFfyJWcuTA115.jpg"></div>
                                <h3>创历史新高 劳斯莱斯2018卖出4107辆车</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>4.6万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928778"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  日前，劳斯莱斯正式对外发布2018年全球销量数据。据统计，劳斯莱斯去年在全球50多个国家售出4107辆新车，同比增长22%，创下...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928777">
                            <a href="//www.autohome.com.cn/news/201901/928777.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g27/M02/76/58/120x90_0_autohomecar__ChcCQFw_52WABZnDAAEp55kUPMo496.jpg"></div>
                                <h3>第五款“LT” 迈凯伦600LT Spider官图</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>2.3万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928777"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车官图]  日前，迈凯伦官方正式发布了迈凯伦600LT Spider的官图，新车基于迈凯伦600LT车型打造，采用了折叠式的硬顶敞篷结构...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928776">
                            <a href="//www.autohome.com.cn/news/201901/928776.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g28/M06/76/D7/120x90_0_autohomecar__ChsEfVw_4taAcUgcAAE5P4mMIpM158.jpg"></div>
                                <h3>呕吐要罚钱 滴滴醉酒乘车规则拓至15城</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3769</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928776"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  日前，滴滴宣布“乘客醉酒乘车”规则已从深圳拓展至上海、成都、武汉、广州、南京等总共15个城市。滴滴方面称，上述15个城市的快车、...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928775">
                            <a href="//www.autohome.com.cn/news/201901/928775.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g29/M08/78/9D/120x90_0_autohomecar__ChsEflw_4UCAHKi5AAHcI3uZcvY570.jpg"></div>
                                <h3>下滑6.7% 中国品牌汽车市场占比达42.1%</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5632</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928775"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  2018年国内车市进入“寒冬”，中国品牌的日子还算“过得去”，不过可惜的是，中国品牌弄丢了从合资品牌手中辛苦夺来的市场份额。  ...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928770">
                            <a href="//www.autohome.com.cn/news/201901/928770.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g27/M03/76/08/120x90_0_autohomecar__ChcCQFw_2pKAQ8TpAAGU6Up0ZtQ228.jpg"></div>
                                <h3>同比增11.46% 2018二手车交易1382万辆</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>5554</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928770"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  1月16日，中国汽车流通协会公布了全国二手车交易数据。数据显示，2018年12月二手车共交易121.72万辆，环比下降4.58%...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928767">
                            <a href="//www.autohome.com.cn/news/201901/928767.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g28/M06/76/7C/120x90_0_autohomecar__ChsEfVw_04eAEUfkAAGrFHy8PQo446.jpg"></div>
                                <h3>外观变化不大 奇瑞瑞虎5x电动版申报图</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>2.4万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928767"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 国内谍照]  日前，我们从国家工信部获得了奇瑞瑞虎5x纯电动版车型申报信息。新车在外观部分与瑞虎5x基本保持一致，搭载最大功率为95kW的...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928772">
                            <a href="//www.autohome.com.cn/news/201901/928772.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g30/M06/76/BE/120x90_0_autohomecar__ChsEf1w_332AFxAjAAFpHzi5yw0309.jpg"></div>
                                <h3>或3月18日上市 新一代508L预售16万起</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>16.1万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928772"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  1月17日，东风标致宣布国产新一代标致508L车型正式开启预售。新车将推出1.6T（350THP/360THP）和1.8T（40...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928773">
                            <a href="//www.autohome.com.cn/news/201901/928773.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g30/M01/75/B8/120x90_0_autohomecar__ChcCSVw_2x-AHjTFAABQUBWc2w0375.jpg"></div>
                                <h3>日内瓦车展发布 斯柯达Kosmiq预告发布</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>3.7万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928773"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，斯柯达发布了一张旗下全新小型SUV车型——斯柯达Kosmiq的预告图，从图片中看，新车保留了斯柯达Vision X概念车的...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928761">
                            <a href="//www.autohome.com.cn/news/201901/928761.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g3/M05/79/B9/120x90_0_autohomecar__ChcCRVw-_hWAWjORAAHGXpLEuCY080.jpg"></div>
                                <h3>沃尔沃投资电动汽车高功率无线充电技术</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1160</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928761"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  据外媒报道，当地时间1月15日，沃尔沃集团旗下子公司沃尔沃集团风险投资公司（Volvo Group Venture Capita...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928768">
                            <a href="//www.autohome.com.cn/news/201901/928768.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g27/M03/75/F1/120x90_0_autohomecar__ChcCQFw_1cWAO1AtAAGMhtTUihc536.jpg"></div>
                                <h3>双边四出排气 吉利FY11运动版官图发布</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>30.0万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928768"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新车官图]  日前，吉利官方发布轿跑SUV FY11运动版官图。新车相比普通版车型运动气息更加浓厚，动力搭载来自沃尔沃的2.0TD T5发...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928762">
                            <a href="//www.autohome.com.cn/news/201901/928762.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www3.autoimg.cn/newsdfs/g29/M04/6F/7D/120x90_0_autohomecar__ChsEn1w-9syAcYoqAACK4YWL4qA796.jpg"></div>
                                <h3>或基于VAG旗下车型 Italdesign新车预告</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>1.5万</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928762"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 新闻]  日前，Italdesign品牌发布了旗下全新车型的预告图。据悉，新车将在2019年3月开幕的日内瓦车展正式发布，同时外媒还报道称...</p>
                            </a>
                        </li>
    
                        <li data-artIdAnchor="928766">
                            <a href="//www.autohome.com.cn/news/201901/928766.html#pvareaid=102624">
                                <div class="article-pic"><img src="//www2.autoimg.cn/newsdfs/g1/M0A/63/84/120x90_0_autohomecar__ChcCQ1w_twiAVYZgAADmG6qJkcQ526.jpg"></div>
                                <h3>比亚迪计划在长沙工厂生产微型电动车</h3>
                                <div class="article-bar">
                                    <span class="fn-left">1天前</span>
                                    <span class="fn-right">
                                        <em><i class="icon12 icon12-eye"></i>6384</em>
                                        <em data-class="icon12 icon12-infor" data-articleid="928766"><i class="icon12 icon12-infor"></i>0</em>
                                    </span>
                                </div>
                                <p>[汽车之家 行业]  2019年，比亚迪计划在长沙工厂生产30万辆新能源汽车，产品可能将覆盖e1、e2、e3等多款微小型电动车。与此同时，比亚迪还将加...</p>
                            </a>
                        </li>
    
                    </ul>
    
    
</div>

<a target="_self" style="display:none;" id="btnLoading" class="loading" href="javascript:void(0);"><span class="loading-cont">加载中</span><img src="//www.autohome.com.cn/channel2/channel/images/btn-loading.gif"></a>                                                                                                                        
<div id="channelPage" class="page">
<a class="page-item-prev page-disabled" target="_self" href="javascript:void(0);"><b></b>上一页</a>
<a class="current" href="javascript:void(0);">1</a><a target="_self"  href="/news/2/#liststart">2</a><a target="_self"  href="/news/3/#liststart">3</a><a target="_self"  href="/news/4/#liststart">4</a><a target="_self"  href="/news/5/#liststart">5</a><a target="_self"  href="/news/6/#liststart">6</a><a target="_self"  href="/news/7/#liststart">7</a><a target="_self"  href="/news/8/#liststart">8</a><a target="_self"  href="/news/9/#liststart">9</a><span class="page-item">...</span><a target="_self" href="/news/4546/#liststart">4546</a>
<a class="page-item-next" target="_self" href="/news/2/#liststart">下一页<b></b></a></div>

		        <!--文章内容结束-->
            </div>
			<div class="column grid-7 grid-right">
				<div class="hot">
                    <!--热门文章开始-->
		            
            <div class="hot-title">热门文章</div>
        <div class="hot-article-wrap">
	        <ul>
        
                <li>
			    <h2><a href="//www.autohome.com.cn/news/201901/928557.html#pvareaid=102625">知道你很期待 丰田新Supra官图正式发布</a></h2>
			    <a href="//www.autohome.com.cn/news/201901/928557.html#pvareaid=102625"><img src="//www3.autoimg.cn/newsdfs/g28/M0A/69/3E/120x90_0_autohomecar__ChsEfVw7pHWAQrgRAAEJ-sn2cC0789.jpg" /></a>
			    <p class="hot-intro">[汽车之家 新车官图]  北京时间1月14日，北美车展的前夕，丰田官方发布了全新一代Sup...</p>
		    </li>
        
                <li>
			    <h2><a href="//www.autohome.com.cn/news/201901/928638.html#pvareaid=102625">凯迪拉克XT6领衔 北美车展热门新车汇总</a></h2>
			    <a href="//www.autohome.com.cn/news/201901/928638.html#pvareaid=102625"><img src="//www3.autoimg.cn/newsdfs/g26/M0B/6D/9D/120x90_0_autohomecar__ChsEe1w85mKAYf-wAAGg5B0rLCY234.jpg" /></a>
			    <p class="hot-intro">[汽车之家 新闻]  2019年北美车展正式拉开帷幕，此次车展新车虽然不多，但依然有很多值...</p>
		    </li>
        
                <li>
			    <h2><a href="//www.autohome.com.cn/news/201901/928474.html#pvareaid=102625">售41.78-66.68万 全新奥迪A6L正式上市</a></h2>
			    <a href="//www.autohome.com.cn/news/201901/928474.html#pvareaid=102625"><img src="//www3.autoimg.cn/newsdfs/g30/M0B/71/61/120x90_0_autohomecar__ChsEf1w9y8qAG4GyAAGul1ZZm9s682.jpg" /></a>
			    <p class="hot-intro">[汽车之家 新车上市]  1月15日，全新一代奥迪A6L在广州正式上市，新车共推出搭载2....</p>
		    </li>
        
            </ul>
            </div>
        


	    
		            <!--热门文章结束-->
                    
                    <div class="advbox monkey monkey_box fn-hide">
                      <div id="s2851" data-adparent=".monkey"></div>
                    </div>

                    <!--热门评论开始-->
		            
<style type="text/css">

.hot-more{ float:right; font-weight:normal; font-style:normal; font-size:12px;}

    .hot-article-rec {
        padding-top: 10px;
    }
        .hot-article-rec img {
            vertical-align: top;
        }
        .hot-article-rec li {
            float: left;
            width: 140px;
            margin: 6px 10px 0 0;
            text-align: center;
        }
            .hot-article-rec li p {
                margin: 5px 0;
            }
</style>

<div class="hot">
    
    <div class="hot-title"><a class="hot-more" href="//www.autohome.com.cn/channel2/union/list.html?pvareaid=103651#class_1" target="_blank">更多&gt;&gt;</a>精彩分类</div>
    
    <div class="hot-article-rec fn-clear">
        <ul>
            
             <li>
                 
                                                <a href="//www.autohome.com.cn/11662/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="//www0.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516275343811.jpg" ></a>
                  <p><a href="//www.autohome.com.cn/11662/0/1/conjunction.html#pvareaid=103651">新产品计划</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="//www.autohome.com.cn/1539/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="//www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516193818404.jpg" ></a>
                  <p><a href="//www.autohome.com.cn/1539/0/1/conjunction.html#pvareaid=103651">热点事件挖掘</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="//www.autohome.com.cn/58/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="//www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516170962497.jpg" ></a>
                  <p><a href="//www.autohome.com.cn/58/0/1/conjunction.html#pvareaid=103651">油价变动</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="//www.autohome.com.cn/23379/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="//www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516240349869.jpg" ></a>
                  <p><a href="//www.autohome.com.cn/23379/0/1/conjunction.html#pvareaid=103651">谍影重重</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="//www.autohome.com.cn/25948/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="//www1.autoimg.cn/newspic/2014/8/26/140x80_0_2014082615054173139.jpg" ></a>
                  <p><a href="//www.autohome.com.cn/25948/0/1/conjunction.html#pvareaid=103651">海外车展</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="//www.autohome.com.cn/2448/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="//www3.autoimg.cn/newsdfs/g24/M08/41/8E/140x80_0_autohomecar__wKgHH1rNaEWAZEtmAAA-p5wOSiM862.jpg" ></a>
                  <p><a href="//www.autohome.com.cn/2448/0/1/conjunction.html#pvareaid=103651">摩托车</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="//www.autohome.com.cn/6931/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="//www0.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516263022756.jpg" ></a>
                  <p><a href="//www.autohome.com.cn/6931/0/1/conjunction.html#pvareaid=103651">数据分析</a></p>
                                              
                
             </li>
            
             <li>
                 
                                                <a href="//www.autohome.com.cn/26207/0/1/conjunction.html#pvareaid=103651"><img width="140" height="80" src="//www1.autoimg.cn/newspic/2014/8/25/140x80_0_2014082516222909794.jpg" ></a>
                  <p><a href="//www.autohome.com.cn/26207/0/1/conjunction.html#pvareaid=103651">销量风云榜</a></p>
                                              
                
             </li>
            
        </ul>
    </div>
</div>

		            <!--热门评论结束-->
                    
                    <div class="advbox monkey monkey_box fn-hide">
                      <div id="s2852" data-adparent=".monkey"></div>
                    </div>

                    <!--编辑博客开始-->
					

<div class="editorblog">
	<div class="editorblog-title-container">
		<div class="editor-change" style="display:none;">
			<i class="icon12 icon12-repeat"></i>
			<a id="switchByRan" href="javascript:void(0);" target="_self">换一换</a>
		</div>
		<div class="editorblog-title">编辑博客</div>
	</div>
	<div class="editor-wrap">
		<ul id="tagInfo">
			
                    <li>
				        <a href="//www.autohome.com.cn/ExpertBlog/editor_5070.html#pvareaid=102628"><img src="//www2.autoimg.cn/newsdfs/g25/M0A/A2/81/40x0_0_autohomecar__wKgHIFpwWRuATxDgAAB-bJ9pdhU044.jpg"></a>
				        <div class="editorname"><a href="//www.autohome.com.cn/ExpertBlog/editor_5070.html#pvareaid=102628">耿源</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">责任编辑</div>
			        </li>
                
                    <li>
				        <a href="//www.autohome.com.cn/ExpertBlog/editor_5314.html#pvareaid=102628"><img src="//www2.autoimg.cn/newsdfs/g24/M05/A5/8F/40x0_0_autohomecar__ChcCL1pwWNiADmfRAAByyPeu9t8030.jpg"></a>
				        <div class="editorname"><a href="//www.autohome.com.cn/ExpertBlog/editor_5314.html#pvareaid=102628">陈浩</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">责任编辑</div>
			        </li>
                
                    <li>
				        <a href="//www.autohome.com.cn/ExpertBlog/editor_5868.html#pvareaid=102628"><img src="//www3.autoimg.cn/newsdfs/g19/M13/91/F9/40x0_0_autohomecar__wKgFWFdrORWAXY15AABt_tkqweE990.jpg"></a>
				        <div class="editorname"><a href="//www.autohome.com.cn/ExpertBlog/editor_5868.html#pvareaid=102628">张晓丹</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
                    <li>
				        <a href="//www.autohome.com.cn/ExpertBlog/editor_5927.html#pvareaid=102628"><img src="//www2.autoimg.cn/newsdfs/g12/M0B/A0/B3/40x0_0_autohomecar__wKjBy1gsNDOAVOnoAABzAbQ1vn8807.jpg"></a>
				        <div class="editorname"><a href="//www.autohome.com.cn/ExpertBlog/editor_5927.html#pvareaid=102628">刁昊</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
                    <li>
				        <a href="//www.autohome.com.cn/ExpertBlog/editor_6310.html#pvareaid=102628"><img src="//www2.autoimg.cn/newsdfs/g9/M0D/7A/DB/40x0_0_autohomecar__wKgH0Fm_u5SAA0O_AABuL4_hJ7k869.jpg"></a>
				        <div class="editorname"><a href="//www.autohome.com.cn/ExpertBlog/editor_6310.html#pvareaid=102628">周易</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
                    <li>
				        <a href="//www.autohome.com.cn/ExpertBlog/editor_6708.html#pvareaid=102628"><img src="//www2.autoimg.cn/newsdfs/g29/M07/14/E5/40x0_0_autohomecar__ChcCSFsh9HOAW3pZAABvwqK6qss190.jpg"></a>
				        <div class="editorname"><a href="//www.autohome.com.cn/ExpertBlog/editor_6708.html#pvareaid=102628">张雪莲</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
                    <li>
				        <a href="//www.autohome.com.cn/ExpertBlog/editor_6844.html#pvareaid=102628"><img src="//www3.autoimg.cn/newsdfs/g2/M05/BD/E5/40x0_0_autohomecar__ChsEmlu9uzGAL75QAAA0o2pTXr4465.jpg"></a>
				        <div class="editorname"><a href="//www.autohome.com.cn/ExpertBlog/editor_6844.html#pvareaid=102628">马艾骏</a></div>
				        <div class="dept">新闻</div>
				        <div class="position">编辑</div>
			        </li>
                
		</ul>
		<div class="fn-clear"></div>
	</div>
</div>

                    <!--编辑博客结束-->
                  
				    <div class="advbox monkey monkey_box fn-hide">
				        <div id="s6188" data-adparent=".monkey"></div>
				    </div>

                    
                    <!--合作媒体开始-->
					
<div class="coo-media">
	<div class="hot-title">合作媒体报道<a class="hot-more" href="//www.autohome.com.cn/list/c131-1.html">更多&gt;&gt;</a></div>
	<div class="hot-article-wrap">
		<ul>
			<li>
				<h2><a href="/news/201503/863334.html#pvareaid=103490">[北京晚报] 超7成消费者望提高燃油标准</a></h2>
				<a href="/news/201503/863334.html#pvareaid=103490"><img src="//www2.autoimg.cn/newsdfs/g13/M07/A2/F0/120x90_0_autohomecar__wKgH1FgyrQeAaiznAACOtcnYVA8629.jpg"></a>
				<p class="hot-intro">近日，笼罩在北京乃至我国整个中东部地区的雾霾再次成为大家热议的话题，“雾霾”、“PM2.5...</p>
			</li>
		</ul>
		<div class="media-abstract">
            
                <p><a href="/news/201503/863329.html#pvareaid=103490">[山东商报]雾霾问题到底该不该怨私家车</a></p>
            
                <p><a href="/news/201503/863327.html#pvareaid=103490">[新闻晨报]超7成用户希望提高燃油标准</a></p>
            
                <p><a href="/news/201503/841974.html#pvareaid=103490">【金陵晚报】新车年检政策你了解多少</a></p>
            
		</div>
    </div>
</div>

                    <!--合作媒体结束-->
                    
				</div>
			</div>
		</div>        
	</div>
   
    <style type="text/css">
/***汽车之家 - 公共底部版权***/
	.footer_auto{ width:990px; margin:10px auto 0 auto; padding:7px 0 10px 0; border-top:3px solid #3b5998; text-align:center; color:#7c7c7c; font-size:12px;}
	.footer_auto p{ line-height:24px; margin:0; padding:0;}
	.footer_auto p a{ display:inline-block; margin:0 9px;}
	.footer_auto p a.footimg{ border:1px solid #c2c2c2; margin:5px 5px 0 5px;}
	.footer_auto p a.footimg img{ border:0;}
	.footer_auto p .fline{ color:#bfbfbf; margin:0 3px;}
	.footer_auto p .footarial{ font-family:Arial, Helvetica, sans-serif;}

	.footer_auto .footios,.footer_auto .footand,.footer_auto .footwp,.footer_auto .footphone,.footer_auto .footauto{ display:inline-block; padding-left:19px; background:url(//x.autoimg.cn/news/footicon2.png) no-repeat;}
	.footer_auto .footios{ background-position:0 3px;}
	.footer_auto .footand{ background-position:0 -27px;}
	.footer_auto .footwp{ background-position:0 -57px;}
	.footer_auto .footphone{ background-position:0 -87px;}
	.footer_auto .footauto{ padding:0 22px 0 21px; background-position:0 -117px;}

	.footer_auto p a:link,.footer_auto p a:visited{ color:#7c7c7c; text-decoration:none;}
	.footer_auto p a:hover{ color:#d60000; text-decoration:none;}

</style>
    
<div style="clear:both;"></div>
<div class="footer_auto">
	<p>
		<a href="//www.autohome.com.cn/about/index.html#pvareaid=21256822770" target="_blank">关于我们</a><a href="//www.autohome.com.cn/about/lianxi.html#pvareaid=21256822771" target="_blank">联系我们</a><a href="http://autohome.hirede.com/" target="_blank">招贤纳士</a><span class="fline">|</span><a class="footios" href="//app.autohome.com.cn/apps/main/1.html" target="_blank">iPhone客户端</a>/<a href="//app.autohome.com.cn/apps/main/1.html" target="_blank">iPad客户端</a><a class="footand" href="//app.autohome.com.cn/apps/main/1.html" target="_blank">Android客户端</a><a class="footwp" href="//app.autohome.com.cn/apps/main/1.html" target="_blank">WP客户端</a><a class="footphone" href="//app.autohome.com.cn/apps/main/1.html" target="_blank">手机版</a><span class="fline">|</span><a class="footauto" href="http://weibo.com/qichezhijia" target="_blank">汽车之家</a><span class="fline">|</span><a href="//www.autohome.com.cn/bug/default.aspx" target="_blank">意见反馈</a>
	</p>
	<p>
		<span class="footarial" id="footarial">&copy; 2004-2016 www.autohome.com.cn All Rights Reserved.</span> 汽车之家 版权所有
	</p>
</div>
<script type="text/javascript">
    var __myDate = new Date();
    var __year = __myDate.getFullYear();
    document.getElementById("footarial").innerHTML = '&copy; 2004-' + __year + ' www.autohome.com.cn All Rights Reserved.';
</script><!-- update 1/18/2019 3:18:21 PM r:utf-8 s:utf-8 -->
<!-- hit cache 2019/1/18 15:18:31 Unicode (UTF-8)-->
</body>
    <script type="text/javascript" src="//x.autoimg.cn/as/js-2.0.5/sea.js"></script>
    <script type="text/javascript" src="//sou.autohome.com.cn/js/SouSeriesAndSpec_130708.js?20171017"></script>
    <!--[if IE 6]><script type="text/javascript">
                      seajs.use(['jquery'],function($){
                          $('.news-item .focusimg,.news-item .focusimg-bt').mouseenter(function(){
                              $('.news-item .focusimg-bt-left,.news-item .focusimg-bt-right').show();
                          });
                          $('.news-item .focusimg').mouseleave(function(){
                              $('.news-item .focusimg-bt-left,.news-item .focusimg-bt-right').hide();
                          });
                      });
                  </script><![endif]-->


    <script type="text/javascript">
        seajs.config({version: "201804111425",
            alias: {
                'articlereply': '//x.autoimg.cn/www/common/js/articlereply.js',
                'toolCookie': '//s.autoimg.cn/car/sidebar/common/js/tool-cookie.js', 
                'toolbar': '//s.autoimg.cn/car/sidebar/common/js/toolbar-1.1.0.js?v=20190118'
            }});
       
        seajs.use(["jquery", "focus", "articlereply","toolbar"], function ($, focus, articlereply,toolbar) {
            $('#focus-1').focus({anim: true,keyboard: true,interval: 7000,pause: 'hover'});
            $('#focus-1 li.clone').removeAttr('id');
  

            //初始化右侧工具栏
            toolbar.init({zIndex:99999});
            //搜索js
            var brands='卡罗拉,科鲁兹,新君威,瑞虎3,速腾,新君越,福克斯,POLO,朗逸,景程,蒙迪欧-致胜,风云2,A3,奔腾B50';var ite=brands.split(',');$('#q').val(ite[Math.floor(Math.random()*ite.length)]);$("#q").blur(function(){if($('#q').val()=="")$('#q').val(ite[Math.floor(Math.random()*ite.length)])});$("#q").on("focus",function(){$(this).val("")});function tagContent(){$.ajax({type:"Get",url:"//www.autohome.com.cn/ashx/channel/EditorBlogSwith.ashx?timestamp="+Math.random(),success:function(data){$("#tagInfo").html(decodeURIComponent(data))}})};$("#switchByRan").click(function(){tagContent()});
            //导航栏浮动
            $(function(){var win=$(window),nav=$('#ulNav'),lastTop=win.scrollTop(),isIE6=!!window.ActiveXObject&&!window.XMLHttpRequest,up=false,navTop=155,wtop,timer;win.scroll(function(){timer&&clearTimeout(timer);timer=setTimeout(function(){wtop=win.scrollTop();if(lastTop==wtop){return}up=lastTop>wtop?true:false;lastTop=wtop;if(up&&wtop>navTop){nav.addClass('navFixed');isIE6&&nav.css('top',wtop)}else{nav.removeClass('navFixed');isIE6&&nav.css('top',0)}},13)})});
        
            //二级分类导航左右滚动
            $.fn.switchNavgation = function () {
                return this.each(function () {
                    var $parent = this,
                        $left=$('#left',$parent),
                        $right=$('#right',$parent),
                        $ul = $('.div-fouc-tx ul', $parent);
                    if ($ul.size() == 1) return;
                    var tab = function ($elem, type) {
                        $elem[type]().animate({
                                'opacity': 1
                            },
                            400,
                            function () {
                                $(this).css({
                                    'zIndex': 20,
                                    'filter': 'alpha(opacity=100)'
                                }).addClass('fouc-current');
                            });
                        $elem.animate({
                                'opacity': 0
                            },
                            0,
                            function () {
                                $(this).css('zIndex', 10).removeClass('fouc-current');
                            });
                        type == 'prev' ? $('a', $right).removeClass('disabled') : $('a', $left).removeClass('disabled');
                        if ($elem[type]()[type]().size() == 0) {
                            type == 'prev' ? $('a', $left).addClass('disabled') : $('a', $right).addClass('disabled');
                        }
                    };
                    $left.on('click',
                        function () {
                            var $now = $('ul.fouc-current', $parent);
                            if ($now.prev().size() > 0) {
                                tab($now, 'prev');
                            }
                        });
                    $right.on('click',
                        function () {
                            var $now = $('ul.fouc-current', $parent);
                            if ($now.next().size() > 0) {
                                tab($now, 'next');
                            }
                        });
                    $ul.each(function (i) {
                        if (i == 0) {
                            $(this).css({
                                'opacity': 1,
                                'zIndex': 20,
                                'filter': 'alpha(opacity=100)'
                            }).addClass('fouc-current');
                        } else {
                            $(this).css({
                                'opacity': 0,
                                'zIndex': 10
                            });
                        }
                    });
                });
            };

            
            $('.div-fouc').switchNavgation();
            

            var channelClassId=0,curPage=1,excptArtIds='928325,928310,927871';
            function getQueryString(name) {
                var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
                var r = window.location.search.substr(1).match(reg);
                if (r != null) {
                    return unescape(r[2]);
                }
                return null;
            }
            var p=getQueryString("p");
            if(p)
            {
                $('#div-fouc-tx li').removeClass("current");
                window.location.hash="liststart";
                window.location = window.location;
            }

            
           
            function setPage(container, count, pageindex) {
                if(count==1)
                {
                    return;
                }
                var container = container;
                var count = count;
                var pageindex = pageindex;
                var a = [];
                //总页数少于10 全部显示,大于10 显示前3 后3 中间3 其余....
                if (pageindex == 1) {
                    a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"page-item-prev page-disabled\">上一页</a>";
                } else {
                    a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"page-item-prev\">上一页</a>";
                }
                function setPageList() {
                    if (pageindex == i) {
                        a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"current\">" + i + "</a>";
                    } else {
                        a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\">" + i + "</a>";
                    }
                }
                //总页数小于10
                if (count <= 10) {
                    for (var i = 1; i <= count; i++) {
                        setPageList();
                    }
                }
                //总页数大于10页
                else {
                    if (pageindex <= 4) {
                        for (var i = 1; i <= 5; i++) {
                            setPageList();
                        }
                        a[a.length] = "<span class=\"page-item\">...</span><a href=\"javascript:void(0);\" target=\"_self\">" + count + "</a>";
                    } else if (pageindex >= count - 3) {
                        a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\">1</a><span class=\"page-item\">...</span>";
                        for (var i = count - 4; i <= count; i++) {
                            setPageList();
                        }
                    }
                    else { //当前页在中间部分
                        a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\">1</a><span class=\"page-item\">...</span>";
                        for (var i = pageindex - 2; i <= pageindex + 2; i++) {
                            setPageList();
                        }
                        a[a.length] = "<span class=\"page-item\">...</span><a href=\"javascript:void(0);\" target=\"_self\">" + count + "</a>";
                    }
                }
                if (pageindex == count) {
                    a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"page-item-next page-disabled\">下一页</a>";
                } else {
                    a[a.length] = "<a href=\"javascript:void(0);\" target=\"_self\" class=\"page-item-next\">下一页</a>";
                }
                container.html( a.join(""));
                //事件点击
                var pageClick = function() {
                    var oAlink = container.children("a");
                    var temp=0;
                    var inx = pageindex; //初始的页码
                    oAlink[0].onclick = function() { //点击上一页
                        if (inx == 1) {
                            return false;
                        }
                        inx--;
                        curPage = inx;
                        setPage(container, count, inx);
                        $.fn.AjaxChannelArticles(channelClassId,curPage);
                        return false;
                    }
                    for (var i = 1; i < oAlink.length - 1; i++) { //点击页码
                        oAlink[i].onclick = function() {
                            inx = parseInt(this.innerHTML);
                            curPage =inx;
                            setPage(container, count, inx);
                            $.fn.AjaxChannelArticles(channelClassId,curPage);
                            return false;
                        }
                    }
                    oAlink[oAlink.length - 1].onclick = function() { //点击下一页
                        if (inx == count) {
                            return false;
                        }
                        inx++;
                        curPage =inx;
                        setPage(container, count, inx);
                        $.fn.AjaxChannelArticles(channelClassId,curPage);
                        return false;
                    }
                } ()
            }


            $.fn.AjaxChannelArticles=function(classId)
            {
                var html='<ul class="article">';
                $.get('//www.autohome.com.cn/ashx/channel/AjaxChannelArtList.ashx?20&page='+curPage+'&ExcptArtIds='+excptArtIds+'&class2Id='+classId,function(o){
                    o = eval("("+o+")");
                    if(o[0].Article==undefined)
                    {
                        $("#auto-channel-lazyload-article").empty();
                        $("#btnLoading").hide();
                        $("#channelPage").hide();
                        return;
                    }
                    for (var i = 0; i < o[0].Article.length; i++) {
                        html+="<li><a href=\"//www.autohome.com.cn"+o[0].Article[i].Dir+o[0].Article[i].PublishTime+"/"+o[0].Article[i].Id+(o[0].Article[i].SerializeStartPage==1?"":"-"+o[0].Article[i].SerializeStartPage)+".html#pvareaid=102624\"><div class=\"article-pic\"><img src=\""+o[0].Article[i].Img.replace("http://","//")+"\"></div><h3>"+o[0].Article[i].Title+"</h3><div class=\"article-bar\"><span class=\"fn-left\">"+o[0].Article[i].ShowTime+"</span><span class=\"fn-right\"><em><i class=\"icon12 icon12-eye\"></i>"+o[0].Article[i].ClickCountStr+"</em><em data-articleid=\""+o[0].Article[i].Id+"\" data-class=\"icon12 icon12-infor\"><i class=\"icon12 icon12-infor\"></i>0</em></span></div><p>"+o[0].Article[i].Summary+"</p></a></li>";
                    }
                    html+='</ul>';
                    $('#auto-channel-lazyload-article').html(html);
                    var count=1;
                    if(o[0].Total>60)
                    {
                        count=(o[0].Total-60)%15==0?parseInt((o[0].Total-60)/15+1):parseInt((o[0].Total-60)/15+2);
                    }
                    else
                    {
                        count=1;//(o[0].Total)%15==0?parseInt((o[0].Total)/15):parseInt((o[0].Total)/15+1);
                    }
                    if(count==1)
                    {
                        $("#channelPage").hide();
                        $("#btnLoading").hide();
                    }
                    else
                    {
                        $("#channelPage").show();
                        $("#btnLoading").show();
                    }
                    $("#btnLoading").hide();
                    setPage($('.page'),count,curPage);
                    $(function () {
                        var objs = $("[data-articleid]");
                        var ids = [];

                        for (var i = 0; i < objs.length; i++) {
                            ids.push($(objs[i]).attr('data-articleid'));
                        }

                        if (ids.length > 0) {
                            $.ajax({
                                type: "get",
                                cache: false,
                                url:"//reply.autohome.com.cn/api/getData_ReplyCounts.ashx?appid=1&dateType=jsonp&objids=" + ids.join('.'),
                                dataType: "jsonp",
                                success: function (data) {
                                    if (data == undefined || data.commentlist == null || data.commentlist.length == 0)
                                        return;

                                    var list = data.commentlist;
                                    for (var i = 0; i < list.length; i++) {
                                        var item = list[i];
                                        for (var j = 0; j < objs.length; j++) {
                                            var obj = $(objs[j]);
                                            if (obj.attr('data-articleid') == item.objid)
                                                obj.html('<i class="' + (obj.attr('data-class') ? obj.attr('data-class') : "icon icon-infor") + '"></i>' + item.replycountall);
                                        }
                                    }
                                }
                            });
                        }
                    });
                });
                window.location.hash="liststart";
                window.location = window.location;
            }

            //loazyLoadArticles
            $('#div-fouc-tx [data-toggle="tab"]').on('click', function () {
                var _this = this;
                //var liList =$('#div-fouc-tx [data-toggle="tab"]');
                //var length=liList.length;
                //for (var i = 0; i < length; i++) {
                //    if(_this==liList)
                //    {
                //        $(_this).addClass("current");
                //        break;
                //    }else
                //    {
                //        $(liList[i]).removeClass();
                //    }
                //}
                $("h3.h3cur").removeClass("h3cur");
                $('#div-fouc-tx li').removeClass("current");
                $(_this).parent().addClass("current");
                var classId=_this.getAttribute('data-class');
                channelClassId = classId;
                //tab切换时 改成默认第一页
                curPage=1;
                $.fn.AjaxChannelArticles(classId,curPage);

                //ar.init('auto-index-lazyload-article');
                //autoIndexObj.lazyloadImages($(_this).attr('data-target').replace('#', ''));
               
            });

            var class2Id =0;
            if(class2Id!=0)
            {
                var liList=$('#div-fouc-tx [data-toggle="tab"]');
                var length =liList.length;
                for (var i = 0; i < length; i++) {
                    if(liList[i].getAttribute('data-class')==class2Id)
                    {
                        $(liList[i]).addClass('current');
                        break;
                    }
                }
            }

            
        });
        //懒加载
        Function.prototype.bind=function(bindObj,args){var _self=this;return function(){return _self.apply(bindObj,[].concat(args))}};Object.extend=function(destination,source){for(var property in source){destination[property]=source[property]}return destination};seajs.config({version:"1394506138411"});seajs.use(["jquery"],function($){function LazyLoad(args){this.areaList=args;Object.extend(this,args);this.init()}LazyLoad.prototype={getClient:function(){var l,t,w,h;l=document.documentElement.scrollLeft||document.body.scrollLeft;t=document.documentElement.scrollTop||document.body.scrollTop;w=document.documentElement.clientWidth;h=document.documentElement.clientHeight;return{'left':l,'top':t,'width':w,'height':h}},getSubClient:function(p){var l=0,t=0,w,h;w=p.offsetWidth;h=p.offsetHeight;while(p.offsetParent){l+=p.offsetLeft;t+=p.offsetTop;p=p.offsetParent}return{'left':l,'top':t,'width':w,'height':h}},intens:function(rec1,rec2){var lc1,lc2,tc1,tc2,w1,h1;lc1=rec1.left+rec1.width/2;lc2=rec2.left+rec2.width/2;tc1=rec1.top+rec1.height/2;tc2=rec2.top+rec2.height/2;w1=(rec1.width+rec2.width)/2;h1=(rec1.height+rec2.height)/2;return Math.abs(lc1-lc2)<w1&&Math.abs(tc1-tc2)<h1},autoCheck:function(){var prec1=this.getClient();var prec2;for(var i=this.areaList.length-1;i>=0;i--){var d=document.getElementById(this.areaList[i]);if(d){prec2=this.getSubClient(d);if(this.intens(prec1,prec2)){this.execLoad(d);delete this.areaList[i]}}}},execLoad:function(obj){},init:function(){var _this=this;_this.autoCheck();if(window.addEventListener){window.addEventListener("scroll",_this.autoCheck.bind(_this),false);window.addEventListener("resize",_this.autoCheck.bind(_this),false)}else if(window.attachEvent){window.attachEvent("onscroll",_this.autoCheck.bind(_this));window.attachEvent("onresize",_this.autoCheck.bind(_this))}}};var pageIndex=2,pageCount=4549,objLoading=$("#btnLoading"),objArticle=$("#articleList");var temp=0;$(".page").hide();var _lazy=new LazyLoad({areaList:[],execLoad:function(obj){setTimeout(function(){$(".article-wrapper ul").eq(pageIndex-1).show(0,function(){pageIndex++;if(pageIndex>4){$(".page").show();objLoading.hide()}else{_lazy.areaList.push('btnLoading');$(".article-wrapper ul").eq(pageIndex-1).show();if(pageCount<=4){objLoading.hide()}}})},150)}});$(function(){var Anchor=window.location.hash;if(Anchor.length>0){var artId=Anchor.substring(Anchor.indexOf('=')+1,Anchor.length);$('[data-artIdAnchor]').each(function(index,item){if(artId==$(item).attr('data-artIdAnchor')){var pager=parseInt(index/15,10);if(index%15>0)pager+=1;pageIndex=pager+1;$(".article-wrapper ul:lt("+(pager)+")").show();$(".article-wrapper ul").eq(pager).show(0,function(){$(window).scrollTop($(item).offset().top)})}})}pageIndex<=4&&1==1&&objLoading.show()&&_lazy.areaList.push('btnLoading');pageIndex>4&&$(".page").show()})});
    </script>
   
    <script type="text/javascript" src="//x.autoimg.cn/engine/root/fggxl.js?2015v1"></script>
    <script type="text/javascript">
        var provinceid=Math.floor(autoHeaderObj.cookies.read("cookieCityId", autoHeaderObj.cookies.read("area", 0)) / 10000) * 10000 ;
        _aad.setData({ city: autoHeaderObj.userArea.areaId,province: provinceid });
    </script>

    
          <script type="text/javascript"> _aad.Loader('2823,904,2851,2852,907,908,909,910,911,912,6188,6378','155');</script>
    
</html>

"""
soup = BeautifulSoup(html,'html.parser')

li_list = soup.find(id="auto-channel-lazyload-article").find_all(name='li')

for i in li_list:
    title = i.find(name='h3')
    if not title:
        continue
    lijie = i.find(name='p')
    #url = i.find(name = 'a').attrs['href']
    url = i.find(name = 'a').get('href')
    img = i.find(name = 'img').get('src')
    print (url)
    print ("标题:")
    print (title.text)
    print ("简介:")
    print (lijie.text)
    print ("图片链接")
    print (img)
    print ("=============================================")
    #resing = requests.get(img)
    #file_name = "%s.jpg" %(title)
    #with open(file_name,'wb') as f:
    #    f.open(resing.content)








