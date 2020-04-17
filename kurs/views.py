import json
from django.shortcuts import render, redirect
import hashlib

file = open("users.json", "r", encoding="utf-8")
data = json.loads(file.read())
file.close()

file = open("companyList.json", "r", encoding="utf-8")
clist = json.loads(file.read())
file.close()

file = open("stuffList.json", "r", encoding="utf-8")
stufflist = json.loads(file.read())
file.close()

file = open("carsList.json", "r", encoding="utf-8")
carslist = json.loads(file.read())
file.close()

additors = []
directors = []
usernames = []
passwords = []
user_group = ""
user_name = ""

for additor in data["users"]["additors"]:
    if additor["user_role"] == "Системный администратор":
        username_admin = additor["loginn"]
        password_admin = additor["password"]
    elif additor["user_role"] == "Диспетчер":
        username_disp = additor["loginn"]
        password_disp = additor["password"]
    else:
        username_add = additor["loginn"]
        password_add = additor["password"]

for director in data["users"]["directors"]:
    directors.append(director)
    usernames.append(director["loginn"])
    passwords.append(director["password"])
companies = []
for i in clist["companies"]:
    companies.append(i)

def signinRender(request):
    if request.POST:
        global user_group
        global user_name
        username = request.POST["username"]
        user_name = username
        byted = bytes(request.POST["password"], "utf-8")
        hashed = hashlib.sha1(byted)
        password = hashed.hexdigest()
        print(password)
        if username in usernames:
            for director in directors:
                if username == director["loginn"] and password == director["password"]:
                    user_group = "director"
                    return redirect('/companyInfo/'+str(director["companyid"]))
        if username == username_add and password == password_add:
            user_group = "additor"
            return redirect('/companyList/')
        elif username == username_admin and password == password_admin:
            user_group = "sisadmin"
            return redirect('/users/')
        elif username == username_disp and password == password_disp:
            user_group = "dispatcher"
            return redirect('/companyList/')
        else:
            error = "Неправильно введён логин и/или пароль! Попробуйте ещё раз."
            return render(request, 'pages/signin.html', {"error": error})
    else:
        return render(request, 'pages/signin.html')

def signOutRender(request):
    global user_group
    user_group = ""
    return redirect('/')

def usersRender(request):
    global user_group
    if user_group != "":
        return render(request, 'pages/users.html', {
            "data": data
        })
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def editUsersRender(request):
    if request.POST:
        group = request.POST["group"]
        name = request.POST["name"]
        username = request.POST["username"]
        user_role = request.POST["user_role"]
        byted = bytes(request.POST["password"], "utf-8")
        hashed = hashlib.sha1(byted)
        password = hashed.hexdigest()
        companyid = request.POST["companyid"]
        role = request.POST["user_role"]
        if group == "additor" or group == "dispatcher":
            for additor in data["users"]["additors"]:
                if name == additor["name"]:
                    if username != "":
                        additor["loginn"] = username
                    if password != "":
                        additor["password"] = password
                    if role != "":
                        additor["user_role"] = role
        else:
            for director in data["users"]["directors"]:
                if name == director["name"]:
                    if username != "":
                        director["loginn"] = username
                    if password != "":
                        director["password"] = password
                    if role != "":
                        director["user_role"] = role
                    if companyid != "":
                        director["companyid"] = companyid
    global user_group
    if user_group != "":
        return render(request, 'pages/editUser.html')
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def companyListRender(request):
    if request.POST:
        global user_group
        global user_name
        username = request.POST["username"]
        user_name = username
        byted = bytes(request.POST["password"], "utf-8")
        hashed = hashlib.sha1(byted)
        password = hashed.hexdigest()
        if username in usernames:
            for director in directors:
                if (username == director["loginn"]):
                    user_group = "director"
            for additor in additors:
                if (username == additor["loginn"]):
                    user_group = "additor"
        else:
            if username == username_admin and password == password_admin:
                user_group = "sisadmin"
            elif username == username_disp:
                user_group = "dispatcher"
    if user_group != "":
        return render(request, 'pages/companyList.html', {
            "clist": clist,
            "user_group": user_group
        })
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def staffListRender(request, companyid):
    stuff = []
    if request.POST:
        global user_group
        global user_name
        username = request.POST["username"]
        user_name = username
        byted = bytes(request.POST["password"], "utf-8")
        hashed = hashlib.sha1(byted)
        password = hashed.hexdigest()
        if username in usernames:
            for director in directors:
                 if (username == director["loginn"]):
                    user_group = "director"
            for additor in additors:
                if (username == additor["loginn"]):
                    user_group = "additor"
        else:
            if username == username_admin and password == password_admin:
                user_group = "sisadmin"
            elif username == username_disp:
                user_group = "dispatcher"
    for company in stufflist["stuff"]:
        if company["companyid"] == companyid:
            stuff.append(company)
    if user_group != "":
        return render(request, 'pages/staffList.html', {
            "stuff": stuff,
            "companyid": companyid,
            "user_group": user_group
        })
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def carsListRender(request, companyid):
    cars = []
    if request.POST:
        global user_group
        global user_name
        username = request.POST["username"]
        user_name = username
        byted = bytes(request.POST["password"], "utf-8")
        hashed = hashlib.sha1(byted)
        password = hashed.hexdigest()
        if username in usernames:
            for director in directors:
                 if username == director["loginn"]:
                    user_group = "director"
            for additor in additors:
                if username == additor["loginn"]:
                    user_group = "additor"
        else:
            if username == username_admin and password == password_admin:
                user_group = "sisadmin"
            elif username == username_disp:
                user_group = "dispatcher"
    for car in carslist["cars"]:
        if car["companyid"] == companyid:
            cars.append(car)
    if user_group != "":
        return render(request, 'pages/carsList.html', {
            "cars": cars,
            "companyid": companyid,
            "user_group": user_group
        })
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def carInfoRender(request, carid):
    carr = []
    for car in carslist["cars"]:
        if car["id"] == carid:
            carr.append(car)
            print(carr)
    global user_group
    if user_group != "":
        return render(request, 'pages/carInfo.html', {
            "carr": carr
        })
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def companyInfoRender(request, companyid):
    if request.POST:
        global user_group
        global user_name
        username = request.POST["username"]
        user_name = username
        byted = bytes(request.POST["password"], "utf-8")
        hashed = hashlib.sha1(byted)
        password = hashed.hexdigest()
        if username in usernames:
            for director in directors:
                if (username == director["loginn"]):
                    user_group = "director"
            for additor in additors:
                if (username == additor["loginn"]):
                    user_group = "additor"
        else:
            if username == username_admin and password == password_admin:
                user_group = "sisadmin"
            elif username == username_disp:
                user_group = "dispatcher"
    for company in clist["companies"]:
        if company["id"] == companyid:
            name = []
            address = []
            director = []
            fdate = []
            description = []
            for item in company["name"]:
                name.append(item)
            for item in company["address"]:
                address.append(item)
            for item in company["director"]:
                director.append(item)
            for item in company["foundation_date"]:
                fdate.append(item)
            for item in company["description"]:
                description.append(item)
            if user_group != "":
                return render(request, 'pages/companyInfo.html', {
                    "name": name,
                    "address": address,
                    "director": director,
                    "fdate": fdate,
                    "description": description,
                    "companyid": companyid,
                    "user_group": user_group
                })
            else:
                print("Переход незарегестрированного пользователя по ссылке!")
                return redirect('/')
    return render(request,'')

def newUserRender(request):
    if request.POST:
        group = request.POST["group"]
        name = request.POST["name"]
        username = request.POST["username"]
        user_role = request.POST["user_role"]
        byted = bytes(request.POST["password"], "utf-8")
        hashed = hashlib.sha1(byted)
        password = hashed.hexdigest()
        companyid = request.POST["companyid"]
        if username in usernames:
            error = "Данный логин уже занят другим пользователем!"
        elif group == "additor" or group == "dispatcher":
            user = {}
            user.update({"name": name})
            user.update({"loginn": username})
            user.update({"password": password})
            user.update({"user_role": user_role})
            data["users"]["additors"].append(user)
            file = open("users.json", "w", encoding="utf8")
            json.dump(data, file)
            file.close()
        else:
            user = {}
            user.update({"name": name})
            user.update({"loginn": username})
            user.update({"password": password})
            user.update({"user_role": user_role})
            user.update({"companyid": companyid})
            data["users"]["directors"].append(user)
            file = open("users.json", "w", encoding="utf8")
            json.dump(data, file)
    global user_group
    if user_group != "":
        return render(request, 'pages/newuser.html')
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def deleteUserRender(request):
    global user_group
    if request.POST:
        username = request.POST["username"]
        for user in data["users"]["directors"]:
            if user["loginn"] == username:
                data["users"]["directors"].remove(user)
        for user in data["users"]["additors"]:
            if user["loginn"] == username:
                data["users"]["additors"].remove(user)
        file = open("users.json", "w", encoding="utf8")
        json.dump(data, file)
        file.close()
    if user_group != "":
        return render(request, 'pages/deleteUser.html')
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def newCompanyRender(request):
    if request.POST:
        nn = request.POST["nn"]
        companyid = request.POST["companyid"]
        name = request.POST["name"]
        adress = request.POST["adress"]
        director = request.POST["director"]
        fdate = request.POST["fdate"]
        description = request.POST["description"]
        company = {}
        company.update({"number": nn})
        company.update({"name": name})
        company.update({"id": int(companyid)})
        company.update({"address": adress})
        company.update({"director": director})
        company.update({"foundation_date": fdate})
        company.update({"description": description})
        clist["companies"].append(company)
        file = open("companyList.json", "w", encoding="utf8")
        json.dump(clist, file)
        file.close()
    global user_group
    if user_group != "":
        return render(request, 'pages/newCompany.html')
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def deleteCompanyRender(request):
    global user_group
    if request.POST:
        companyid = request.POST["companyid"]
        for company in clist["companies"]:
            if company["id"] == int(companyid):
                clist["companies"].remove(company)
        file = open("companyList.json", "w", encoding="utf8")
        json.dump(clist, file)
        file.close()
    if user_group != "":
        return render(request, 'pages/deleteCompany.html')
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def newWorkerRender(request, companyid):
    if request.POST:
        name = request.POST["name"]
        id = request.POST["id"]
        registration_address = request.POST["registration_address"]
        birthdate = request.POST["birthdate"]
        mobile_phone_number = request.POST["mobile_phone_number"]
        hiring_date = request.POST["hiring_date"]
        firing_date = request.POST["firing_date"]
        driver_license_number = request.POST["driver_license_number"]
        position = request.POST["position"]
        cid = request.POST["companyid"]
        worker = {}
        worker.update({"name": name})
        worker.update({"id": id})
        worker.update({"registration_address": registration_address})
        worker.update({"birthdate": birthdate})
        worker.update({"mobile_phone_number": mobile_phone_number})
        worker.update({"hiring_date": hiring_date})
        worker.update({"firing_date": firing_date})
        worker.update({"driver_license_number": driver_license_number})
        worker.update({"position": position})
        worker.update({"companyid": int(cid)})
        stufflist["stuff"].append(worker)
        file = open("stuffList.json", "w", encoding="utf8")
        json.dump(stufflist, file)
        file.close()
    global user_group
    if user_group != "":
        return render(request, 'pages/newWorker.html', {"companyid": companyid})
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def deleteWorkerRender(request, companyid):
    global user_group
    if request.POST:
        id = request.POST["id"]
        for person in stufflist["stuff"]:
            if person["id"] == id:
                stufflist["stuff"].remove(person)
        file = open("stuffList.json", "w", encoding="utf8")
        json.dump(stufflist, file)
        file.close()
    if user_group != "":
        return render(request, 'pages/deleteWorker.html', {"companyid": companyid})
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def newCarRender(request, companyid):
    if request.POST:
        image = request.POST["image"]
        id = request.POST["id"]
        driverid = request.POST["driverid"]
        cid = request.POST["companyid"]
        brand_name = request.POST["brand_name"]
        model_type = request.POST["model_type"]
        purchase_date = request.POST["purchase_date"]
        registration_number = request.POST["registration_number"]
        technical_inspection_date = request.POST["technical_inspection_date"]
        next_technical_inspection_date = request.POST["next_technical_inspection_date"]
        weight = request.POST["weight"]
        carrying_capacity = request.POST["carrying_capacity"]
        mileage = request.POST["mileage"]
        fuel_consumption_rate = request.POST["fuel_consumption_rate"]
        oil_consumption_rate = request.POST["oil_consumption_rate"]
        dtpdate = request.POST["dtpdate"]
        description = request.POST["description"]
        car = {}
        dtp = {}
        car.update({"id": int(id)})
        car.update({"image": image})
        car.update({"driverid": driverid})
        car.update({"companyid": int(cid)})
        car.update({"brand_name": brand_name})
        car.update({"model_type": model_type})
        car.update({"purchase_date": purchase_date})
        car.update({"registration_number": registration_number})
        car.update({"technical_inspection_date": technical_inspection_date})
        car.update({"next_technical_inspection_date": next_technical_inspection_date})
        car.update({"weight": weight})
        car.update({"carrying_capacity": carrying_capacity})
        car.update({"mileage": mileage})
        car.update({"fuel_consumption_rate": fuel_consumption_rate})
        car.update({"oil_consumption_rate": oil_consumption_rate})
        dtp.update({"date": dtpdate})
        dtp.update({"driver": driverid})
        dtp.update({"description": description})
        car.update({"dtp": dtp})
        carslist["cars"].append(car)
        file = open("carsList.json", "w", encoding="utf8")
        json.dump(carslist, file)
        file.close()
        print("companyid=", companyid)
    global user_group
    if user_group != "":
        return render(request, 'pages/newCar.html', {"companyid": companyid})
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')

def deleteCarRender(request, companyid):
    global user_group
    if request.POST:
        id = int(request.POST["id"])
        for car in carslist["cars"]:
            if car["id"] == id:
                carslist["cars"].remove(car)
        file = open("carsList.json", "w", encoding="utf8")
        json.dump(carslist, file)
        file.close()
    if user_group != "":
        return render(request, 'pages/deleteCar.html', {"companyid": companyid})
    else:
        print("Переход незарегестрированного пользователя по ссылке!")
        return redirect('/')