import jieba
import jieba.posseg as pseg #词性标注
import jieba.analyse as anls #关键词提取

f = open("./data/红楼梦.txt",'r',encoding='utf-8')
text = f.read()
jieba.load_userdict('./data/Dream_of_the_Red_Chamber_name.txt')
seg_list = jieba.cut(text,cut_all=False)

doc = open('./data/红楼梦_jieba.txt','w',encoding='utf-8')
print(' '.join(seg_list),file=doc)
doc.close()