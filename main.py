from flask import Flask, render_template, request

import main_operation.file1 as operation1
import main_operation.file2 as operation2


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/suggetion", methods=['post'])
def getSuggetions():

    area = float(request.form['area'])
    prev_crop = request.form['prev_crop']
    pH = request.form['pH']
    soil_type = request.form['soil_type']
    temp = request.form['temp']
    season = request.form['season']

    print(area, prev_crop, pH, soil_type, temp, season)

    data = operation1.alternative_crops(area, prev_crop)
    data2 = operation2.best_crop(pH, soil_type, temp, season)

    print(data)
    print(data2)

    try:
        selected_crop = data[0][0]
        other_suggetions = data
        
        if data2 != None:
            selected_crop = data2[0]

            for crop in data:
                if crop[0] == data2[0]:
                    selected_crop = data2[0]
                
    except:
        selected_crop = None
        if data2 != None:
            selected_crop = data2[0]


    # return "Ok" 
    # try:
    #     selected_crop = data[0][0]
    #     other_suggetions = data
    #     for crop in data:
    #         if data2[0] == crop[0]:
    #             print(data2[0], crop)
    #             selected_crop = data2[0]
    # except:
    #     selected_crop = None
    #     if data2 != None:
    #         selected_crop = data2

    if selected_crop == None:
        result = "Sorry we don't have best crop suggetion for you now. but you can still cultivate the prevois crop {}".format(
            prev_crop.capitalize())
        return render_template("result.html", suggesion=result, other_suggetions=other_suggetions)

    result = '{} would be best for your land'.format(
        selected_crop.capitalize())
    return render_template("result.html", suggesion=result, other_suggetions=other_suggetions)


if __name__ == "__main__":
    app.run(debug=True)


# # farmer inputs

# # Land Location
# area = float(input("area measurement: "))
# prev_crop = input("Previous cultivated crop? ")

# # soil test & environment info
# pH = input("Enter pH? ex. range (4.0...8.0)\n")
# soil_type = input(
#     "Soil Type? ex. high, m-loam, alkail, silts, loam, well-draned-sandy-loamy, clay-loam, fertile, sandy\n")
# temp = input("temperature? ex.(12 .. 35 degree)\n")
# season = input(
#     "what season is? ex. jan, feb, mar, apr, may, jun, jul, aug, sep, pct, nov, dec\n")


#
