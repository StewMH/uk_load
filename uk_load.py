import json

with open("data.json", "r") as read_file:
    data = json.load(read_file)
    for calls in data['x']['calls']:
      if calls['method'] == 'addCircleMarkers':
        args = calls['args']
        #print(args)
        x_list = args[0]
        if type(x_list) != list:
          x_list = [x_list]
        y_list = args[1]
        if type(y_list) != list:
          y_list = [y_list]
        percent = args[4]
        disp = args[5]
        #print(disp)
        color = disp['color'] 
        fillColor = disp['fillColor'] 
        for i, x in enumerate(x_list):
          #if disp['weight'] == 1:
            print(percent, ", ",color, ", ",fillColor, ", ", x, ", ", y_list[i])
        #print(args[0],args[1],args[4])

