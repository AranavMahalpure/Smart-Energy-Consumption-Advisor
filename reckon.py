from flask import Flask,render_template,url_for,request
app = Flask(__name__, template_folder="templates")
from joblib import load

mainmodel = load('models/energy-model.pkl')
scalemodel = load('models/energy-scaler.pkl')
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/daily",methods=['GET', 'POST'])
def daily():
    return render_template("dailyform.html")
@app.route("/monthly",methods=['GET', 'POST'])
def monthly():
    return render_template("monthlyform.html")
@app.route("/Daily_Bill", methods=['POST'])
def Daily_Bill():
    volt=240
    appliances = []
    Microwave=0
    Oven=0
    Dishwasher=0
    Mixer=0
    light=0
    washing=0
    tumble=0
    refrigerator=0
    electricwaterheater=0
    airconditioner=0
    Sub_1 =0
    Sub_2 =0
    Sub_3 =0
    fan = 0
    television =0
    if request.method == 'POST':
        for i in range(1, 4):
            category = f"{i}appliance"
            for j in range(1, 5):
                appliance = f"{category}{j}"
                value = int(request.form.get(appliance, 0))
                appliances.append( value)
    def handle_input(input_value,appliances):
        if i == 0:
            Microwave=8000
            if (appliances[i]>1):
                Microwave+=(appliances[i]-1)*8000/3
        elif i == 1:
            Oven=3000
            if (appliances[i]>1):
                Oven+=(appliances[i]-1)*3000/3
        elif i == 2:
            Dishwasher=1800
            if (appliances[i]>1):
                Dishwasher+=(appliances[i]-1)*1800/3
        elif i == 3:
            Mixer=1000
            if (appliances[i]>1):
                Mixer+=(appliances[i]-1)*500/3
        elif i == 4:
            light=1000
            if (appliances[i]>1):
                light+=(appliances[i]-1)*600/3
        elif i == 5:
            washing=1000
            if (appliances[i]>1):
                washing+=(appliances[i]-1)*900/3
        elif i == 6:
            tumble=900
            if (appliances[i]>1):
                tumble+=(appliances[i]-1)*900/3
        elif i == 7:
            refrigerator=7680
            if (appliances[i]>1):
                refrigerator+=(appliances[i]-1)*7680/3
        elif i == 8:
            electricwaterheater=4000
            if (appliances[i]>1):
                electricwaterheater+=(appliances[i]-1)*4000/3        
        elif i == 9:
            airconditioner=4000
            if (appliances[i]>1):
                airconditioner+=(appliances[i]-1)*4000/3
        elif i == 10:
            fan=1000
            if (appliances[i]>1):
                fan+=(appliances[i]-1)*500/2                        
        elif i == 11:
            televison=1000
            if (appliances[i]>1):
                television+=(appliances[i]-1)*500/2      
    for i in (0,10):
        handle_input(i,appliances)
    Sub_1 = Microwave+Oven+Dishwasher+Mixer
    Sub_2 = light+washing+tumble+refrigerator
    Sub_3 = electricwaterheater+airconditioner+fan+television
    sd = scalemodel.transform([[0, volt, 241.2317, Sub_1, Sub_2, Sub_3]])
    p1 = mainmodel.predict([[sd[0, 1], sd[0, 3], sd[0, 4], sd[0, 5]]])
    sd[0, 0] = p1
    ans = scalemodel.inverse_transform(sd)
    energy =(((ans[0, 0])*1000)/60) - Sub_1 - Sub_2 -Sub_3
    carbonfootprints= (852.3*(energy/1000))
    daybill= (18*(energy/1000))
    return render_template("dailybill.html",cf=carbonfootprints,bill=daybill)
@app.route("/monthly_Bill", methods=['POST'])
def monthly_Bill():
    volt=240
    appliances = []
    Microwave=0
    Oven=0
    Dishwasher=0
    Mixer=0
    light=0
    washing=0
    tumble=0
    refrigerator=0
    electricwaterheater=0
    airconditioner=0
    Sub_1 =0
    Sub_2 =0
    Sub_3 =0
    fan = 0
    television =0
    if request.method == 'POST':
        for i in range(1, 4):
            category = f"{i}appliance"
            for j in range(1, 5):
                appliance = f"{category}{j}"
                value = int(request.form.get(appliance, 0))
                appliances.append( value)
    def handle_input(input_value,appliances):
        if i == 0:
            Microwave=8000
            if (appliances[i]>1):
                Microwave+=(appliances[i]-1)*8000/3
        elif i == 1:
            Oven=3000
            if (appliances[i]>1):
                Oven+=(appliances[i]-1)*3000/3
        elif i == 2:
            Dishwasher=1800
            if (appliances[i]>1):
                Dishwasher+=(appliances[i]-1)*1800/3
        elif i == 3:
            Mixer=1000
            if (appliances[i]>1):
                Mixer+=(appliances[i]-1)*500/3
        elif i == 4:
            light=600
            if (appliances[i]>1):
                light+=(appliances[i]-1)*600/3
        elif i == 5:
            washing=900
            if (appliances[i]>1):
                washing+=(appliances[i]-1)*900/3
        elif i == 6:
            tumble=900
            if (appliances[i]>1):
                tumble+=(appliances[i]-1)*900/3
        elif i == 7:
            refrigerator=7680
            if (appliances[i]>1):
                refrigerator+=(appliances[i]-1)*7680/3
        elif i == 8:
            electricwaterheater=4000
            if (appliances[i]>1):
                electricwaterheater+=(appliances[i]-1)*4000/3        
        elif i == 9:
            airconditioner=4000
            if (appliances[i]>1):
                airconditioner+=(appliances[i]-1)*4000/3
        elif i == 10:
            fan=1000
            if (appliances[i]>1):
                fan+=(appliances[i]-1)*500/2                        
        elif i == 11:
            televison=1000
            if (appliances[i]>1):
                television+=(appliances[i]-1)*500/2      
    for i in (0,10):
        handle_input(i,appliances)
    Sub_1 = Microwave+Oven+Dishwasher+Mixer
    Sub_2 = light+washing+tumble+refrigerator
    Sub_3 = electricwaterheater+airconditioner+fan+television
    sd = scalemodel.transform([[0, volt, 241.2317, Sub_1, Sub_2, Sub_3]])
    p1 = mainmodel.predict([[sd[0, 1], sd[0, 3], sd[0, 4], sd[0, 5]]])
    sd[0, 0] = p1
    ans = scalemodel.inverse_transform(sd)
    energy =(((ans[0, 0])*1000)/60) - Sub_1 - Sub_2 -Sub_3
    carbonfootprints= round((852.3*(energy/1000))* 28)
    daybill= round((18*(energy/1000))*28)
    return render_template("monthly_bill.html",cf=carbonfootprints,bill=daybill)    
    
    # volt = 240
    # if request.method == 'POST':
    #      Microwave = int(request.form['1appliance1']) * 800
    #      Oven = int(request.form['1appliance2']) * 3000
    #      Dishwasher = int(request.form['1appliance3']) * 1800
    #      Mixer = int(request.form['1appliance4']) * 500
    #      Sub_1 = Microwave+Oven+Dishwasher+Mixer
    #      light = int(request.form['2appliance1']) * 230
    #      washing= int(request.form['2appliance2']) * 900
    #      tumble = int(request.form['2appliance3']) * 900
    #      refrigerator = int(request.form['2appliance4']) * 7680
    #      Sub_2 = light+washing+tumble+refrigerator
    #      electricwaterheater = int(request.form['3appliance1']) * 4000
    #      airconditioner= int(request.form['3appliance2']) * 25000
    #      Sub_3 = electricwaterheater+airconditioner
    #      sd = scalemodel.transform([[0, volt, 241.2317, Sub_1, Sub_2, Sub_3]])
    #      p1 = mainmodel.predict([[sd[0, 1], sd[0, 3], sd[0, 4], sd[0, 5]]])
    #      sd[0, 0] = p1
    #      ans = scalemodel.inverse_transform(sd)
    # return "The total energy usage in one is : {}".format(ans[0, 0])
app.run(debug=True)
