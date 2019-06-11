import conf,email_conf, json, time, math, statistics
from boltiot import Sms, Bolt,Email
def compute_bounds(history_data,frame_size,factor):
    if len(history_data)<frame_size :
        return None

    if len(history_data)>frame_size :
        del history_data[0:len(history_data)-frame_size]
    Mn=statistics.mean(history_data)
    Variance=0
    for data in history_data :
        Variance += math.pow((data-Mn),2)
    Zn = factor * math.sqrt(Variance / frame_size)
    High_bound = history_data[frame_size-1]+Zn
    Low_bound = history_data[frame_size-1]-Zn
    return [High_bound,Low_bound]

critical_limit = 20 #the critical_value of temperature
maximum_limit = 35 #the maximum_value of temperature
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SSID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
mailer = Email(email_conf.MAILGUN_API_KEY, email_conf.SANDBOXURL, email_conf.SENDER_EMAIL, email_conf.RECIPIENT_EMAIL)
history_data=[]

while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    if data['success'] != 1:
        print("There was an error while retriving the data.")
        print("This is the error:"+data['value'])
        time.sleep(10)
        continue

    print ("This is the value "+data['value'])
    sensor_value=0
    try:
        sensor_value = int(data['value'])
    except e:
        print("There was an error while parsing the response: ",e)
        continue

    bound = compute_bounds(history_data,conf.FRAME_SIZE,conf.MUL_FACTOR)
    if not bound:
        required_data_count=conf.FRAME_SIZE-len(history_data)
        print("Not enough data to compute Z-score. Need ",required_data_count," more data points")
        history_data.append(int(data['value']))
        time.sleep(10)
        continue

    try:
        if sensor_value/10.24 > maximum_limit:
            print ("The Temperature value increased suddenly. Sending an sms.")
            # display the temeprature value in degree celsus
            print ("The Current temperature is: "+str(sensor_value/10.24)+" °C")
            response = sms.send_sms("Alert ! Someone has opened the fridge door")
            response1 = mailer.send_email("Alert !","The level temperature can destroy the tablets.")
        # condition for the temperature value is between  the critical_limit and the maximum_limit
        elif sensor_value/10.24 > critical_limit or sensor_value/10.24 < maximum_limit:
            print("Urgent! Temperature condition can destroy the tablets. Sending an email.")
            #display the temperature value in degree celsus
            print (" The Current temperature is:" +str(sensor_value/10.24)+ "°C")
            response = mailer.send_email("Alert !","The level temperature can destroy the tablets.")
            print("This is the response",response)
        history_data.append(sensor_value)
    except Exception as e:
            print ("Error",e)

    time.sleep(10)







	
	
	



















































