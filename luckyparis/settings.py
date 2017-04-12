# Global settings

ASP_FORM_ID = ['__VIEWSTATE', '__VIEWSTATEGENERATOR', '__EVENTVALIDATION',
               '__EVENTTARGET', '__EVENTARGUMENT', '__LASTFOCUS']


EDU_URL = 'http://electsys.sjtu.edu.cn/edu'
ELE_LOGIN_URL = EDU_URL + '/login.aspx'
LESSON_URL = EDU_URL+'/lesson/viewLessonArrange.aspx'
ELECT_URL = EDU_URL+'/student/elect'
NORMAL_CHECK_URL_TEMPLATE = ELECT_URL+'/electcheck.aspx?xklc=%d'
REMOVE_URL = ELECT_URL+'/removeLessonFast.aspx'
NORMAL_SUBMIT_URL = ELECT_URL+'/electSubmit.aspx'
RECOMMAND_URL = ELECT_URL+'/RecommandTblOuter.aspx'
SUMMER_URL = ELECT_URL + '/ShortSession.aspx'
SUMMER_CHECK_URL_TEMPLATE = ELECT_URL+'/ShortSessionCheck.aspx?xklc=%d'
SELECT_NORMAL_COURSE_URL = LESSON_URL+'?&xklx=&redirectForm=outSpeltyEp.aspx&kcmk=-1'
SELECT_SUMMER_COURSE_URL = LESSON_URL+'?&xklx=&redirectForm=ShortSession.aspx&kcmk=-1'
SUMMER_SUBMIT_URL = ELECT_URL+'/electSubmitShort.aspx?redirectForm=ShortSession.aspx'
JACCOUNT_URL = 'https://jaccount.sjtu.edu.cn/jaccount/'

TONGSHI_NAMES = ['人文学科', '社会科学', '数学或逻辑', '自然科学与']

CACHE_SESSION_PATH = '/tmp/session.pickle'
COURSE_DATA_PATH = 'data/course.json'
