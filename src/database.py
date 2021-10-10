from pymongo import MongoClient


class nlpDB:
    def __init__(self):
        try:
            self.clientclient = pymongo.MongoClient("mongodb+srv://saif_test1:<Khanbhai12345>@cluster1.yqruc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            #self.client = MongoClient("mongodb+srv://saif_test1:<Khanbhai12345>@cluster1.yqruc.mongodb.net/test")
            self.db = self.client.get_database('myFirstDatabase')
            self.records = self.db['nlp_records']
        except Exception as e:
            print(e)


    # To add new row
    def updateDataBase(self, essay, essay_set, result):
        row = {}
        row['essay_token_pad'] = essay
        row['essay_set'] = essay_set
        # row['sent_count'] = sent_count
        # row['word_count'] = word_count
        row['result'] = result
        self.records.insert_one(row)