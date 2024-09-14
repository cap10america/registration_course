from flask import Flask ,request ,redirect ,url_for ,render_template ,Response , jsonify
import mysql.connector
from database import db_config 
import hashlib
import re




app=Flask(__name__)


def get_db_connection():

    return mysql.connector.connect(**db_config)

def hash_password(password):    
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password
  
  






def validate_email(email):
  """Validates an email address using regular expression.

  Args:
    email: The email address to validate.

  Returns:
    True if the email is valid, False otherwise.
  """

  # Simplified regular expression pattern
  email_regex = r"^\w+@\w+\.\w{2,4}$"

  # Check if the email matches the pattern
  if re.match(email_regex, email):
    return True
  else:
    return False

# Example usage
# email = "example@email.com"
# if validate_email(email):
#   print("Valid email")
# else:
#   print("Invalid email")




@app.route('/',methods=['POST','GET'])
def institute_register():
    if request.method =='POST' :
        conn =get_db_connection()
        mycommand =conn.cursor()
        institute =request.form.get('institute_name')
        email =request.form.get('email')
        mobile=request.form.get('mobile')
        username =request.form.get('username')
        password =request.form.get('password')
        address =request.form.get('address')
        contact_details =request.form.get('contact_details')
        
        
        if all([institute ,email ,mobile ,username ,password ,address ,contact_details]):
            if validate_email(email) :
                
                query = "select * from institute_registration where email =%s "
                mycommand.execute(query ,(email ,))
                result =mycommand.fetchall()
                if result :
                    return jsonify({'status_code':400 ,'message' :"the email already  exists"})
                else :
                    query ="select * from institute_registration where name =%s"
                    mycommand.execute(query ,(institute ,) )
                    exists=mycommand.fetchall()
                    if exists :
                        return jsonify({'status_code':400 ,'message':"the institute name already exists"})
                    
                    
                    else :
                        query ="select * from institute_registration where username =%s"
                        mycommand.execute(query ,(username ,))
                        is_exists =mycommand.fetchall()
                        if is_exists :
                            return jsonify({'status_code':400 ,'message':"username already exists "})
                            
                        else :
                            query ="insert into institute_registration (name ,email ,mobile ,username ,password ,address ,contact_details ) values(%s ,%s ,%s ,%s ,%s ,%s ,%s )"
                            mycommand.execute(query ,(institute ,email ,mobile ,username ,hash_password(password) ,address ,contact_details , ))
                            conn.commit()
                            mycommand.close()
                            conn.close()
                            return jsonify({'status_code':201 ,'message':"the institute registration successfully"})
            else :
                return jsonify({'status_code':400,'message':"enter a valid email"})
            
            
        else :
            return jsonify({'status_code':404,'message':"the missing arguments"})
        
    if request.method =='GET' :
        conn=get_db_connection()
        mycommand=conn.cursor()
        query ="select * from institute_registration "
        mycommand.execute(query)
        result =mycommand.fetchall()
        if result :
            return jsonify({'status_code':200 ,'message':result})
        else :
            return jsonify({'status_code':400, 'message':'no records'})




# @app.route('/mainipulation_page',methods=['GET','PUT','DELETE'])
# def show_data():
#     conn =get_db_connection()
#     mycommand =conn.cursor()
    
    
        # -===-=-------------==------------===============---------------------------------------------------
        
# @app.route('/course_type', methods=['POST', 'GET'])  # Specify methods
# def course_type():
#     if request.method == 'POST':
#         conn=get_db_connection()
#         mycommand=conn.cursor()
#         name =request.form.get('name')
#         code =request.form.get('code')
#         if  all([name ,code]) :
#             query ="select * from course_type where name =%s"
#             mycommand.execute(query ,(name,))
#             result1 =mycommand.fetchall()
#             query ="select * from course_type where code =%s"
#             mycommand.execute(query ,(code,))
#             result2 =mycommand.fetchall()
#             if result1 :
#                 mycommand.close()
#                 conn.close()
#                 return jsonify({"status_code":400 ,"message":"the name already exists"})
#             elif result2:

                
                
             
#                     mycommand.close()
#                     conn.close()
#                     return jsonify({'status_code':400 ,"message":"the code already exists"})
#             else :
#                 query ="insert into course_type (name ,code) values (%s ,%s)"
#                 mycommand.execute(query ,(name ,code ,))
#                 conn.commit()
#                 mycommand.close()
#                 conn.close()
#                 return jsonify({'status_code':201 ,"message":"course type inserted successfully"})
        
#         else :
#             conn.close()
#             mycommand.close()
#             return jsonify({'status_code':404 ,"error":"missing arguments"})
        
        
#     if request.method=="GET" :
#         conn= get_db_connection()
#         mycommand =conn.cursor()
#         query ="select * from course_type "
#         mycommand.execute(query)
#         result =mycommand.fetchall()
#         if result :
#             mycommand.close()
#             conn.close()
#             return jsonify({'status_code':200 ,'course_type records':result})
#         else :
#             mycommand.close()
#             conn.close()
#             return jsonify({'status_code':400 ,'message':'the records are empty '})
        
        
        
        
        
# @app.route('/course_type/<int:id>',methods=['PUT','GET','DELETE'])
# def update_course_type(id):
#     if request.method=='PUT' :
#         conn =get_db_connection()
#         mycommand =conn.cursor()
#         name =request.form.get('name')
#         code =request.form.get('code')
#         exists ="select * from course_type where id=%s"
#         mycommand.execute(exists ,(id ,))
#         Is_exists =mycommand.fetchall()
#         if Is_exists :
#             query ="update course_type set name =%s , code =%s where id=%s"
#             if all([name ,code]):
#                 mycommand.execute(query ,(name,code ,id,))
#                 conn.commit()
#                 mycommand.close()
#                 conn.close()
#                 return jsonify({'status_code':202,'message':'the record updated successfully'})
#             else :
#                 return jsonify({'status_code':400,"message":"missing arguments"})
#         else :
#             conn.close()
#             mycommand.close()
#             return jsonify({'status_code':400 ,'message':'record does not exists with the input id value'})
    
    
    
    
#     if request.method=="GET" :
#         conn =get_db_connection()
#         mycommand =conn.cursor(dictionary=True)
#         if id :
#             query ="select * from course_type where id =%s"
#             mycommand.execute(query ,(id,))
#             exists=mycommand.fetchall()
#             if exists :
#                 mycommand.close()
#                 conn.close()
#                 return jsonify({'status_code':200,"data":exists})
#             else :
#                 mycommand.close()
#                 conn.close()
#                 return jsonify({'status_code':400,'message':'the record doesnot exists'})
#         else :
#             mycommand.close()
#             conn.close()
#             return jsonify({'status_code':404,"message":"mossing arguments"})
        
        
#     if request.method=="DELETE" :
#         conn=get_db_connection()
#         mycommand=conn.cursor()
#         if id :
#             exists ="select * from course_type where id =%s"
#             mycommand.execute(exists,(id,))
#             Is_exists =mycommand.fetchall()
#             if Is_exists :                
#                 delete ="delete from course_type where id=%s"
#                 mycommand.execute(delete,(id,))
#                 conn.commit()
#                 return jsonify({'status_code':204 ,"message":"the record deleted successfully"})
#             else :
#                 mycommand.close()
#                 conn.close()
#                 return jsonify({'status_code':400,"message":"the record doest not exists"})
#         else :
#             mycommand.close()
#             conn.close()
#             return jsonify({'status_code':400,"message":"missing arguments"})
        
            
            
            
            
        
@app.route('/course', methods=['POST', 'GET'])  # Specify methods
def course():
    if request.method == 'POST':
        conn=get_db_connection()
        mycommand=conn.cursor()
        name =request.form.get('name')
        code =request.form.get('code')
        if  all([name ,code]) :
            query ="select * from course where name =%s"
            mycommand.execute(query ,(name,))
            result1 =mycommand.fetchall()
            query ="select * from course where code =%s"
            mycommand.execute(query ,(code,))
            result2 =mycommand.fetchall()
            if result1 :
                mycommand.close()
                conn.close()
                return jsonify({"status_code":400 ,"message":"the name already exists"})
            elif result2:

                
                
             
                    mycommand.close()
                    conn.close()
                    return jsonify({'status_code':400 ,"message":"the code already exists"})
            else :
                query ="insert into course (name ,code) values (%s ,%s)"
                mycommand.execute(query ,(name ,code ,))
                conn.commit()
                mycommand.close()
                conn.close()
                return jsonify({'status_code':201 ,"message":"course type inserted successfully"})
        
        else :
            conn.close()
            mycommand.close()
            return jsonify({'status_code':404 ,"error":"missing arguments"})
        
        
    if request.method=="GET" :
        conn= get_db_connection()
        mycommand =conn.cursor()
        query ="select * from course "
        mycommand.execute(query)
        result =mycommand.fetchall()
        if result :
            mycommand.close()
            conn.close()
            return jsonify({'status_code':200 ,'course records':result})
        else :
            mycommand.close()
            conn.close()
            return jsonify({'status_code':400 ,'message':'the records are empty '})
        
        
        
        
        
@app.route('/course/<int:id>',methods=['PUT','GET','DELETE'])
def update_course_type(id):
    if request.method=='PUT' :
        conn =get_db_connection()
        mycommand =conn.cursor()
        name =request.form.get('name')
        code =request.form.get('code')
        exists ="select * from course where id=%s"
        mycommand.execute(exists ,(id ,))
        Is_exists =mycommand.fetchall()
        if Is_exists :
            query ="select * from course where name=%s and code =%s"
            mycommand.execute(query ,(name ,code ,))
            already =mycommand.fetchall()
            if already :
                mycommand.close()
                conn.close()
                return jsonify({"status_code":400 ,"message":"the record already exists  enter pls enter the new name and  new code  values .../"})
            else :
                
                    
                    if all([name ,code]):
                        # "update course set name =%s and code =%s where id=%s"
                        query ="""UPDATE course
                                    SET name = %s, code = %s
                                        WHERE id = %s;"""
                        mycommand.execute(query ,(name,code ,id,))
                        conn.commit()
                        mycommand.close()
                        conn.close()
                        return jsonify({'status_code':202,'message':'the record updated successfully'})
                    else :
                        mycommand.close()
                        conn.close()
                        return jsonify({'status_code':400,"message":"missing arguments"})
        else :
            conn.close()
            mycommand.close()
            return jsonify({'status_code':400 ,'message':'record does not exists with the input id value'})
    
    
    
    
    if request.method=="GET" :
        conn =get_db_connection()
        mycommand =conn.cursor(dictionary=True)
        
        if id :
            query ="select * from course where id =%s"
            mycommand.execute(query ,(id,))
            exists=mycommand.fetchall()
            if exists :
                mycommand.close()
                conn.close()
                return jsonify({'status_code':200,"data":exists})
            else :
                mycommand.close()
                conn.close()
                return jsonify({'status_code':400,'message':'the record doesnot exists'})
        else :
            mycommand.close()
            conn.close()
            return jsonify({'status_code':404,"message":"mossing arguments"})
        
        
    if request.method=="DELETE" :
        conn=get_db_connection()
        mycommand=conn.cursor()
        if id :
            exists ="select * from course where id =%s"
            mycommand.execute(exists,(id,))
            Is_exists =mycommand.fetchall()
            if Is_exists :                
                delete ="delete from course where id=%s"
                mycommand.execute(delete,(id,))
                conn.commit()
                return jsonify({'status_code':204 ,"message":"the record deleted successfully"})
            else :
                mycommand.close()
                conn.close()
                return jsonify({'status_code':400,"message":"the record doest not exists"})
        else :
            mycommand.close()
            conn.close()
            return jsonify({'status_code':400,"message":"missing arguments"})
        
            
            
            
           
            
                
            
            
        
            
                    
            
            
        
        


# @app.route('/course_type', methods=['POST', 'GET'])  # Specify methods
# def course_type():
#     if request.method == 'POST':
#         # Handle POST request logic here
#         return "hello"
#     else:
#         # Handle GET request logic here
#         return "hi"
        
        
        
        
        
        
    

    
    
@app.route('/course_funding_type',methods =['POST','GET'])
def course_funding_type():
    if request.method=='POST':
        conn=get_db_connection()
        mycommand=conn.cursor()
        name = request.form.get('name')
        if name :
            unique ="select * from course_funding_type where name=%s"
            mycommand.execute(unique ,(name,))
            Is_unique =mycommand.fetchall()
            if Is_unique    :
                mycommand.close()
                conn.close()
                return jsonify({'status_code':400,"message":"the record already exists  "})
            else :
                
            
                insert ="insert into course_funding_type (name) values (%s)"
                mycommand.execute(insert ,(name,))
                conn.commit()
                mycommand.close()
                return jsonify({'status_code':201,"message":"record inserted succesfully"})
        else :
            mycommand.close()
            conn.close()
            return jsonify({"status_code":404,"message":"missing argumnets"})
    
    if request.method=='GET':
        conn=get_db_connection()
        mycommand=conn.cursor(dictionary=True)
        query ="select * from course_funding_type"
        mycommand.execute(query)
        exists =mycommand.fetchall()
        if exists :
                       
            mycommand.close()
            conn.close()
            return jsonify({'stastus_code':200 ,"message":exists})
        else :
            mycommand.close()
            conn.close()
            return jsonify({'status_code':200,"message":"the records are empty"})
        
        
        
        
@app.route('/course_funding_type/<int:id>',methods =['PUT','GET','DELETE'])
def update_course_funding_type(id):
    if request.method =='GET':
        conn=get_db_connection()
        mycommand=conn.cursor()
        if id :
            query ="select * from course_funding_type where id =%s"
            mycommand.execute(query ,(id,))
            Is_exists =mycommand.fetchall()
            if Is_exists :
                mycommand.close()
                conn.close()
                return jsonify({'status_code':200 ,'message':Is_exists})
            else :
                mycommand.close()
                conn.close()
                return jsonify({'status_code':400,'message':'the records are empty '})
        else :
            mycommand.close()
            conn.close()
            return jsonify({'status_code':404,'message':'missing arguments'})
        
        
        
        
    if request.method=='PUT':
        conn=get_db_connection()
        mycommand=conn.cursor()
        name=request.form.get('name')
        if all([ id ,name]) :
            unique ="select * from course_funding_type where name = %s"
            mycommand.execute(unique,(name,))
            Is_unique =mycommand.fetchall()
            if Is_unique :
                    mycommand.close()
                    conn.close()
                    return jsonify({'status_code':400,'message':'the record with same value /name is already exists'})
            else :
                    query ="select * from course_funding_type where id =%s"
                    mycommand.execute(query ,(id,))
                    Is_exists =mycommand.fetchall()
                    if Is_exists :
                        query ="update course_funding_type set name=%s where id=%s "
                        mycommand.execute(query ,(name ,id,))    
                        conn.commit()            
                        mycommand.close()
                        conn.close()
                        return jsonify({'status_code':200 ,'message':"the record updated successfully"})
                    else :
                        mycommand.close()
                        conn.close()
                        return jsonify({'status_code':400,'message':'the records are empty '})
        else :
            mycommand.close()
            conn.close()
            return jsonify({'status_code':404,'message':'missing arguments'})
        
        
        
    if request.method =='DELETE':
        conn=get_db_connection()
        mycommand=conn.cursor()
        if id :
            query ="select * from course_funding_type where id =%s"
            mycommand.execute(query ,(id,))
            Is_exists =mycommand.fetchall()
            if Is_exists :
                delete ="delete from course_funding_type where id=%s"
                mycommand.execute(delete ,(id,))
                conn.commit()
                mycommand.close()
                conn.close()
                return jsonify({'status_code':200 ,'message':"the record deleted successfully"})
            else :
                mycommand.close()
                conn.close()
                return jsonify({'status_code':400,'message':'the records are empty '})
        else :
            mycommand.close()
            conn.close()
            return jsonify({'status_code':404,'message':'missing arguments'})
        
            
            
            
    
    
    
    
        
        
        
        
        
        
            
            
            
        
        
        
        



        
        
        
if __name__=='__main__' :
    app.run(debug=True)
                    
                
            