#encoding: utf-8

import os
import codecs
from models import Reviews


class SplitReview(object):

    @property
    def getFolderDir(self):
        return os.listdir(r'D:\Programming\PyCharm workspace\JDReviewAnalyzePlatform\static\Data')

    @property
    def getTxt(self):
        total = []
        for id in self.getFolderDir:
            try:
                with codecs.open(r'D:/Programming/PyCharm workspace/JDReviewAnalyzePlatform/static/Data/' + id + '/' + 'reviews.txt', 'r', encoding='utf-8') as f:
                    total.append(f.read())
            except UnicodeDecodeError, e:
                continue
        return total

    def getTxtById(self, id):
        for id in self.getFolderDir:
            with codecs.open(r'static/Data/' + id + '/reviews.txt', 'r', encoding='utf-8') as f:
                total = f.read()
        return total

    @property
    def getReviews(self):
        reviews = []
        for one in self.getTxt:
            reviews.append(one.split("-------------------------------------------------------------------------------------------------------------------------------------------------------------"))
        return reviews

    def splitAttributes(self):
        i = 1
        comments = []
        for review in self.getReviews:
            for one in review:
                try:
                    data = one.split('\r\n')
                    content = data[0]                                      # Review content
                    print data[1].split(':')[1].strip()
                    score = int(data[1].split(':')[1].strip())             # Review score
                    creationTime = data[2].split(':')[1]                   # Review creationTime
                    userfulCount = int(data[3].split(':')[1].strip())      # Review usefulCount
                    expValue = int(data[4].split(':')[1].strip())          # Review expValue
                    images = int(data[5].split(':')[1].strip())            # Review images
                    length = int(data[6].split(':')[1].strip())            # Review length
                    count = int(data[7].split(':')[1].strip())             # Review reply count
                    afterComment = int(data[8].split(':')[1].strip())      # IsAfterComment
                    productType = data[9].split(':')[1].strip()            # Review productType
                    comment = Reviews(product_id = '4130043', content = content, score = score, time = creationTime, usefulVoteCount = userfulCount,
                                      userExpValue = expValue, images = images, length = length, replyCount = count, afterComment = afterComment, product_type = productType)  #breakpoint
                    comments.append(comment)
                except IndexError, e:
                    continue
                i += 1
            return comments

if __name__ == '__main__':
    splitReview = SplitReview()
    splitReview.splitAttributes()