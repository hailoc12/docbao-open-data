# Function: show how to fetch open data from Docbao Project
from lib import *
import json

# CLASS
class DocbaoOpenData():
    '''
    Use: object to get data from all json files
    '''
    # Const
    DATA_URL = "http://theodoibaochi.com/export/"
    DATA_PATH = "data"
    EXPORT_PATH = "export"

    KEYWORD_LOG_FILENAME = "keyword_freq_log.json"
    DATABASE_LOG_FILENAME = "log_data.json"
    ARTICLE_FILENAME = "article_data.json"
    KEYWORD_FREQ_FILENAME = "keyword_freq_series.json"
    KEYWORD_CATEGORY_FILENAME = "keyword_dict.json"
    NEW_KEYWORD_FILENAME = "new_keyword.json"
    TREND_FILENAME = "trending_keyword.json"
    FAST_GROW_FILENAME = "fast_growing_keyword.json"
    ERROR_MESSAGE = "Error"

    DATA_FILES = [ARTICLE_FILENAME,KEYWORD_FREQ_FILENAME,KEYWORD_LOG_FILENAME,DATABASE_LOG_FILENAME,KEYWORD_CATEGORY_FILENAME,NEW_KEYWORD_FILENAME, TREND_FILENAME, FAST_GROW_FILENAME]

    MAX_DISPLAY = 10

    def __init__(self, datasource="http://theodoibaochi.com"):
        self.data = dict()
        self.DATA_URL = datasource + "/export/"

    def load_data(self):
        for filename in self.DATA_FILES:
            path = get_independent_os_path([self.DATA_PATH, filename])
            with open_utf8_file_to_read(path) as stream:
                self.data[filename] = json.loads(stream.read())

    def count_newspapers(self):
        return self.data[self.DATABASE_LOG_FILENAME]["newspaper_count"]

    def count_articles(self):
        return self.data[self.DATABASE_LOG_FILENAME]["database_count"]
    
    def get_update_time(self):
        return self.data[self.KEYWORD_LOG_FILENAME]["time"]
    
    def get_trending_keyword_list(self):
        result = list()
        for keyword, count in self.data[self.TREND_FILENAME].items():
            result.append({"keyword":keyword,"count":count})
        return result
            
    def get_new_keywords(self):
        return self.data[self.NEW_KEYWORD_FILENAME]

    def get_fast_growing_keywords(self):
        return self.data[self.FAST_GROW_FILENAME]
    
    def get_article_list(self):
        return self.data[self.ARTICLE_FILENAME]["article_list"]

    def get_articles_contain(self, keyword):
        data = self.data[self.ARTICLE_FILENAME]["article_list"]
        result = list()
        for article in data:
            topic = article["topic"]
            if keyword in topic.lower():
                result.append(article)
        return result

    def fetch_json_data(self, json_name):
        '''
        Download json file to local data folder
        '''
        json_url = self.DATA_URL + json_name 
        data = json.loads(read_url_source_as_html(json_url))
        path = get_independent_os_path([self.DATA_PATH, json_name])
        with open_utf8_file_to_write(path) as stream:
            json.dump(data, stream)
            stream.close()
        return data

    def download_data(self):
        '''
        Check if local data is updated. If not, download new data from server
        '''
        ERROR_MESSAGE = "There are errors in downloading data. Please check internet connection or local data might be not updated"

        log_path = get_independent_os_path([self.DATA_PATH, self.KEYWORD_LOG_FILENAME])
        
        # check if local data is updated
        if os.path.exists(log_path):
            with open_utf8_file_to_read(log_path) as stream:
                data = json.loads(stream.read())
                local_iterator = data["iterator"]
                stream.close()
            try:
                data = self.fetch_json_data(self.KEYWORD_LOG_FILENAME)
            except:
                input(ERROR_MESSAGE)
                
            online_iterator = data["iterator"]
            if local_iterator == online_iterator:
                # is updated
                return 0

        # not updated. Update data
        a=True
        while a==True:
        #try: 
            print("Have new data. Updating......")
            count = 0
            for filename in self.DATA_FILES:
                self.fetch_json_data(filename)
                count += 1
                print("%s %% downloaded" % str(int(count*100/len(self.DATA_FILES))))
            a= False
        #except:
        #   input(self.ERROR_MESSAGE)
     
    def display_list(self, message, keywords=None, articles=None, full_info=True, filename=None):
        '''
        Display list of keywords or articles

        Args:
        - keywords: list of dict in format {"keyword":keyword, "count":count}
        - articles: list of dict in format {"topic": topic, "href": href, "newspaper": newspaper, "publish-time": publish-time, "update-time":update-time}
        '''
        print()
        print(message)
        print()
        total = 0
        display = ""
        
        if keywords is None:
            total = len(articles)
            display = "articles"
        else:
            total = len(keywords)
            display = "keywords"

        stdout = None
        stream = None
        
        if filename is not None:
            stdout = sys.stdout
            path = get_independent_os_path([self.EXPORT_PATH, filename])
            stream = open_utf8_file_to_write(path)
            sys.stdout = stream
        
        count = 0
        
        for i in range(total):
            count += 1
            if display == "keywords":
                line = "%s. %s (%s)" % (str(count), keywords[i]["keyword"], keywords[i]["count"])
                print(line)
            else:
                line = "%s. %s (%s)" % (str(count), articles[i]["topic"], articles[i]["newspaper"])
                print(line)
                if full_info == True:
                    print("Link        : %s" % articles[i]["href"])
                    print("Xuất bản lúc: %s" % articles[i]["publish_time"])

            print()

            if count == self.MAX_DISPLAY and filename is None:
                print()
                if input("Bạn có muốn xem tiếp %s kết quả tiếp theo (y/n) ?: " % self.MAX_DISPLAY) in ["n", "N"]:
                    return 0
                    
        print()
        
        print("Có tất cả %s %s" % (str(total), display))

        if stream is not None:
            stream.close()
            sys.stdout = stdout
    
def display_file(filename):
    '''
    Display file content to screen
    '''
    count = 0
    with open_utf8_file_to_read(filename) as stream:
        while(True):
            print(convert_line_ending(stream.readline()))
            count += 1
            if count == MAX_DISPLAY:
                if input("Do you want to display next lines (y/n): ") in ['n', "N"]:
                    break
                else:
                    count = 0
        stream.close()

       
