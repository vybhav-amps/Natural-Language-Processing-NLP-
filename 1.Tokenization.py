import nltk


para= """Technology is flourishing by leaps and bounds and providing us new avenues while keeping ourselves update with latest news and current affairs. Therefore, a fair amount of people believe, a conventional way of newspaper reading will be disappeared.I do not completely accord on it because conventional newspaper are easiest and cheapest way to get news.

To embark on, there are multiple reasons why the traditional ways of getting news are still popular. First of all, reading newspaper has become ardent habit of many people. Everyone whether from affluent or middle class are seen desperately waiting for paper in morning and enjoy it reading with cup of tea.Moreover, these are the portable, cheapest an easiest way of knowing about the global activities. It can be carried from one place to other in bag and available at economical price. It is so handy and merely by continuing flip of pages can make you omniscient. Secondly,electricity and other appliances are not required. Moreover,the other attachments are like icing on the cake. For instance, the Hindustan times has multiple attachments like women’s fashion, career guide, culinary art and so on.

However, undoubtedly, technology has given the radical approach to reading news, for example, videos provide full and clear view to reading besides that we can download, share and forward it to our relatives and friends. Needless to say that technophobic will be having no place in this ever-advanced modern world.

To conclude, the lives of people are drastically affected by advanced versions of technology yet, in my opinion, it will not be able to pose threat to the existence traditional newspaper and magazines."""

sentences=nltk.sent_tokenize(para)

words=nltk.word_tokenize(para)