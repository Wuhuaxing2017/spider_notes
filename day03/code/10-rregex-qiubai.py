import requests
import re


url = 'https://www.qiushibaike.com/pic/'

url = 'https://www.qiushibaike.com/pic/page/%d/'


img_url = 'https://www.qiushibaike.com//pic.qiushibaike.com/system/avtnew/3739/37399485/medium/20180401104646.JPEG'
img_url = 'https://www.qiushibaike.com//pic.qiushibaike.com/system/pictures/12048/120488917/medium/app120488917.jpeg'

data = '''<div class="article block untagged mb15" id="qiushi_tag_120488917">

<div class="author clearfix">
<a href="/users/37399485/" target="_blank" rel="nofollow">
<img src="//pic.qiushibaike.com/system/avtnew/3739/37399485/medium/20180401104646.JPEG" alt="社会我萌姐">
</a>
<a href="/users/37399485/" target="_blank" title="社会我萌姐">
<h2>社会我萌姐</h2>
</a>
<div class="articleGender womenIcon">24</div>
</div>



<a href="/article/120488917" target="_blank" class="contentHerf">
<div class="content">



<span>不停的安慰自己，亲生的亲生的[狂躁][狂躁][狂躁]</span>


</div>
</a>




<div class="thumb">

<a href="/article/120488917" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12048/120488917/medium/app120488917.jpeg" alt="不停的安慰自己">
</a>

</div>



<div class="stats">
<span class="stats-vote"><i class="number">47</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/120488917" data-share="/article/120488917" id="c-120488917" class="qiushi_comments" target="_blank">
<i class="number">1</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_120488917" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-120488917" class="up">
<a href="javascript:voting(120488917,1)" class="voting" data-article="120488917" id="up-120488917" rel="nofollow">
<i></i>
<span class="number hidden">47</span>
</a>
</li>
<li id="vote-dn-120488917" class="down">
<a href="javascript:voting(120488917,-1)" class="voting" data-article="120488917" id="dn-120488917" rel="nofollow">
<i></i>
<span class="number hidden">0</span>
</a>
</li>

<li class="comments">
<a href="/article/120488917" id="c-120488917" class="qiushi_comments" target="_blank">
<i></i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>




</div>'''

# data = '''<div class="thumb">
# <a href="/article/120488917" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12048/120488917/medium/app120488917.jpeg" alt="不停的安慰自己">
# </a>
# </div>'''



# ！！！ 刚才的写法：
# 如果 加上re.S 则是将 所有的字符串按一个整体进行匹配
pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?</div>',re.S)

ret = pattern.findall(data)
print(ret)