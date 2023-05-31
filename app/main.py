from flask import Flask, render_template, request, session, redirect

app=Flask(__name__)
dataLIst = []

#mian page
@app.route('/')
def input():
    return render_template('main.html')

#main page로 이동하되, 초기화 함    
@app.route('/home')
def home():
    global dataLIst
    dataLIst = []
    return render_template('main.html')

#check된 행 삭제
@app.route('/delete', methods=['POST'])
def delete():
    global dataLIst
    if request.method == "POST":
        studentNumber = request.json['student_number']
        new_data_list = [data for data in dataLIst if data['Student Number'] != studentNumber]
        dataLIst = new_data_list
    return render_template('result.html', result=dataLIst)

# GET 데이터를 받아와서 처리하겠다
# post 처리한 데이터를 포스팅(나열) 하겠다 
@app.route('/result', methods=['GET','POST'])
def result():
    global dataLIst
    if request.method == "POST":
        # 딕셔너리 형태로 데이터 저장
        data = {
            "Name": request.form["Name"],
            "Student Number": request.form["Student Number"],
            "Major": request.form["Major"],
            "Email": request.form["Email"] + "@" + request.form["Email_domain"],
            "Gender": request.form.get("Gender"),
            "Programing Language": ", ".join(request.form.getlist("Pro_lang[]"))
        }
        dataLIst.append(data)
        dataLIst = sorted(dataLIst, key=lambda x: x.get('Student Number', '').lower())
    return render_template('result.html', result=dataLIst)

if __name__ =='__main__':
    app.run(debug=True)