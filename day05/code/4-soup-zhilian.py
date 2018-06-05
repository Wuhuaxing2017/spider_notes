import requests
from bs4 import BeautifulSoup


url_base = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&p=%d'


def loadhtml(city, job, p):
    url = url_base%(city,job,p)

    response =requests.get(url = url,verify = False)

    response.encoding = 'utf-8'

    html = response.text

    soup = BeautifulSoup(html,'lxml')

    # 获取工作岗位，薪水，工作地点，公司名称

    tables = soup.select('div.newlist_list_content > table.newlist')

    '''<table cellpadding="0" cellspacing="0" width="853" class="newlist">
                            <tbody><tr>
                                <td class="zwmc" style="width: 250px;">
                                    <input type="checkbox" name="vacancyid" data-monitor="CC120002369J90310835000|2" value="CC120002369J90310835000_538_1_03_409__1_" onclick="zlapply.uncheckAll('allvacancyid')">
                                    <div style="width: 224px;*width: 218px; _width:200px; float: left">
                                        <a style="font-weight: bold" par="ssidkey=y&amp;ss=409&amp;ff=03&amp;sg=fff42e7a6856497cae4ab3121621bb19&amp;so=2" href="http://jobs.zhaopin.com/120002369310835.htm" target="_blank">课程<b>销售</b>/招生顾问（中小学项目）&nbsp;</a><a href="http://e.zhaopin.com/products/1/detail.do" target="_blank" title="点击“顶”字，了解更多"><img src="/assets/images/top.png" border="0" align="absmiddle">&nbsp;<img src="/assets/images/jp.gif" border="0" align="absmiddle"></a>
                                    </div>
                                </td>
                                <td style="width: 60px;" class="fk_lv"><span></span></td>
                                <td class="gsmc"><a href="http://company.zhaopin.com/P7/CC1200/0236/D900/000/CC120002369D90000002000.htm" target="_blank">上海新东方学校</a> <a href="javascript:void(0);" target="_blank" style="vertical-align: top;"><img src="/assets/images/best.png" border="0" align="absmiddle"></a> <a href="http://company.zhaopin.com/P7/CC1200/0236/D900/000/CC120002369D90000002000.htm" target="_blank" style="vertical-align: top;"><img src="//img03.zhaopin.cn/IHRNB/img/souvip1003.png" border="0" align="absmiddle" alt="1003" class="icon_vip"></a></td>
                                <td class="zwyx">8001-10000</td>
                                <td class="gzdd">上海</td>
                                <td class="gxsj"><span>置顶</span><a class="newlist_list_xlbtn" href="javascript:;"></a></td>
                            </tr>
                            <tr style="display: none" class="newlist_tr_detail">
                                <td width="833px" style="line-height: 0;" colspan="6">
                                    <div class="newlist_detail">
                                        <div class="clearfix">
                                            <ul>
                                                <li class="newlist_deatil_two"><span>地点：上海</span><span>公司性质：民营</span><span>公司规模：1000-9999人</span><span>学历：本科</span><span>职位月薪：8001-10000元/月</span></li><li class="newlist_deatil_last">  欢迎有志于在教育培训行业谋求发展的小伙伴加入新东方！  无责任底薪＋高奖金提成 + 广阔的职业发展空间     你的责任：  1． 支持中心负责人进行各个项目的咨询及<b>销售</b>工作，承担并积极完成<b>销售</b>预算；  2． 根据客户需求，为客户进行咨询并设计课程方案，为学生提供合适...</li>
                                                
                                            </ul>
                                            <dl>
                                                <dt>
                                                    <a href="javascript:zlapply.searchjob.ajaxApplyBrig1('CC120002369J90310835000_538','ssi','_1_03_409__2_');searchMonitor.logSingleApplyData('CC120002369J90310835000|2');">
                                                        <img src="/assets/images/newlist_sqimg_03.jpg">
                                                    </a>
                                                </dt>
                                                <dd><a href="javascript:zlapply.searchjob.saveOne('CC120002369J90310835000_538');"><img src="/assets/images/newlist_scimg_06.jpg"></a></dd>
                                            </dl>
                                        </div>
                                    </div>
                            </td></tr>
                        </tbody></table>'''


    '''<td class="zwmc" style="width: 250px;">
                                    <input type="checkbox" name="vacancyid" data-monitor="CC120002369J90310835000|2" value="CC120002369J90310835000_538_1_03_409__1_" onclick="zlapply.uncheckAll('allvacancyid')">
                                    <div style="width: 224px;*width: 218px; _width:200px; float: left">
                                        <a style="font-weight: bold" par="ssidkey=y&amp;ss=409&amp;ff=03&amp;sg=fff42e7a6856497cae4ab3121621bb19&amp;so=2" href="http://jobs.zhaopin.com/120002369310835.htm" target="_blank">课程<b>销售</b>/招生顾问（中小学项目）&nbsp;</a><a href="http://e.zhaopin.com/products/1/detail.do" target="_blank" title="点击“顶”字，了解更多"><img src="/assets/images/top.png" border="0" align="absmiddle">&nbsp;<img src="/assets/images/jp.gif" border="0" align="absmiddle"></a>
                                    </div>
                                </td>'''

    print(len(tables))
    for t in tables[1:]:
        # 公司名称
        # print(t)

        # find方法放回的对象和select 返回的列表
        # find_all方法返回的列表
        gsmc_ = t.find('td', attrs={'class': 'gsmc'})

        company = gsmc_.find('a').string

    #     薪水
        salary = t.select('td.zwyx')[0].get_text()

    #     获取工作地点
        loaction = t.select('td.gzdd')[0].get_text()

    #     获取岗位名称
        job = t.select('td.zwmc > div > a ')[0].get_text()

        print(company,salary,loaction,job)

    pass


if __name__ == '__main__':

    # city = input('请输入查询的城市：')
    # job = input('请输入查询工作：')
    # p = int(input('请输入查询的页码：'))

    loadhtml('上海','Python',1)