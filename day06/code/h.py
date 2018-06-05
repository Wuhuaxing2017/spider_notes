from lxml import etree


with open('./qiushibaike.html','r',encoding='utf-8') as fp:
    html = fp.read()

html_tree = etree.HTML(html)

div_list = html_tree.xpath('//div[contains(@id,"qiushi_tag")]')

print(len(div_list))

for div in div_list:
    header_img_url = div.xpath('.//div[@class="author clearfix"]/a/img/@src')[0]
    nickname = div.xpath('.//div[@class="author clearfix"]/a/img/@alt')[0]

    content = div.xpath('.//div[@class="content"]/span/text()')[0]

    # 好笑
    vote = div.xpath('.//div[@class="stats"]//i/text()')[0]
    print(vote)
    #         评论
    comment = div.xpath('.//div[@class="stats"]//i/text()')[1]
    print(comment)

    item = {}

    item['header_img_url'] = header_img_url
    item['nickname'] = nickname
    item['content'] = content
    item['vote'] = vote
    item['comment'] = comment

    print(item)
