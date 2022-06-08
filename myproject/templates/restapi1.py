from flask import Flask

app=Flask(__name__)
@app.route('/')
def show():
    return 'hello world'
#api.add_resource(display,'/hello')   #route

if __name__=='__main__':
    app.run()