from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from links import *

app = Flask(__name__)
bootstrap = Bootstrap(app)

var = 'https://carnet-my.sharepoint.com/:b:/g/personal/danijel_klarin_skole_hr/'

'''@app.route('/')
def index():
    return render_template('cs-for.html', 
                           var=var,
                           links_it=links_it,
                           links=links, 
                           links_sjwp_u=links_sjwp_u, 
                           links_sjwp_n=links_sjwp_u,
                           software=software,
                           web_dizajn=web_dizajn,
                           flask=flask
                           )'''

@app.route('/frame')
def frame():
    return render_template('frame.html')

link1 = '/pmu_2'
link2 = '/wd_2'

subject1 = 'Programiranje mobilnih uređaja 2'
subject2 = 'Web dizajn 2'

@app.route('/')
def skriptni_jezici_i_web_programiranje_1():
    title = 'Skriptni jezici i web programiranje 1'    
    return render_template('index.html', 
                            var=var, 
                            title=title, 
                            link1=link1, 
                            link2=link2,                             
                            subject1=subject1,
                            subject2=subject2,                          
                            links_it=links_sjwp_1_kodovi,
                            links_lit=links_sjwp_1_literatura
                            )

@app.route('/pmu_2')
def pmu_2():
    title = 'Programiranje mobilnih uređaja 2'   
    return render_template('index.html', 
                            var=var, 
                            title=title, 
                            link1=link1, 
                            link2=link2,                           
                            subject1=subject1,
                            subject2=subject2,                          
                            links_it=links_pmu_2_kodovi,
                            links_lit=links_pmu_2_literatura
                            )

@app.route('/wd_2')
def wd_2():
    title = 'Web dizajn 2'   
    return render_template('index.html', 
                            var=var, 
                            title=title, 
                            link1=link1, 
                            link2=link2,                            
                            subject1=subject1,
                            subject2=subject2,                           
                            links_it=links_wd_2_kodovi,
                            links_lit=links_wd_2_literatura
                            )

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=4000)