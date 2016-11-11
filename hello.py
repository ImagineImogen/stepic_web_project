def app (environ, start_response):
    data=''
    for i in environ["QUERY_STRING"].split('&'):
        data = data+i+'\n'
    start_response('200 OK',[('Content-Type', 'text/plain')])
    return data
