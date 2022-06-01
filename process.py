import datetime

def process():

    dtNow = datetime.date.today()
    weekday = dtNow.weekday()

    result = ''

    d_week = {'Sun': '日', 'Mon': '月', 'Tue': '火', 'Wed': '水',
          'Thu': '木', 'Fri': '金', 'Sat': '土'}
    
    for i in range(7):
        daysDelta = 7 - weekday + i
        
        next = dtNow + datetime.timedelta(days=daysDelta)

        key = next.strftime('%a')
        w = d_week[key]

        formatDate = next.strftime('%m/%d') + f'({w})'

        result += str(formatDate) + '\n'

    return result