from flask import Flask
from flask import request
from markupsafe import escape #this checks for things that are not allowed and replaces them with safe versions


app = Flask(__name__)

@app.route("/")
def hello_world():
    user_input = request.args.get('cprompt', '') #to see this word, go to this url http://127.0.0.1:5000/?key=someKeyWord
    user_input = user_input * 2
    return  f"Safe content: {escape(user_input)}"
    

@app.route("/get_query")
def return_clothes():
    #DISPLAY FORM FOR USER INPUT
    form = """
        <form action="/get_query" method="get">
      <label for="cprompt">What clothing are you looking for?:</label>
      <input type="text" id="cprompt" name="cprompt"><br><br>
      <input type="submit" value="Submit">
    </form>
"""
    #GET USER INPUT
    user_input = request.args.get('cprompt', '')

    #RUN PYTHON SCRIPT ON USER INPUT ******

    link1 = "https://www.amazon.com/Urban-CoCo-Stretchy-Straight-Pockets/dp/B0C778Y4TH/ref=sr_1_3_sspa?dib=eyJ2IjoiMSJ9.7AwCxz2nh_tu5-kUvaFYSZMrFsaWPQf0QGJZpdv_xDS4KWl2-d13ShoyV9G0WUZlTLhl7EPVPlK5aO0GQDBZuw1Ne7UEZfDypg168G6ss29LEuNjOrrJNn6GUmLn3U_by8gyg5XDkhyQK40At3R1Ae113greBf0Y5rXipiCWSM8IvCQwp8C-7mzGcM80LsQQfI-bJdTyGZDCnvXMUYsyAn45U55D-sDxGQKicFUhL-rI1vfWrSKY-jGRw5yhZXUcNFhXLuGKJQVf1_Eg-0a1rOQ7hxaM0On81isG2Fjas4s.x_y6OzXieS0OJZ5fxrmC83RmpPaeIrnQKlijoOExk4U&dib_tag=se&keywords=red+pants&qid=1708362954&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    img1_filepath= "https://m.media-amazon.com/images/I/81zMB7-p9oL._AC_UL640_FMwebp_QL65_.jpg"
    
    user_return = f"""
    <p><a href='{escape(link1)}'>{escape(user_input)}</a></p>
    <p><img src='{img1_filepath}' /></p>
    """


    #ASSEMBLE CONTENT TO RETURN
    page_display = f"{form} \n {user_return}"
    return page_display

@app.route('/many_clothes/<id>')
def f(id):
  return f'{id=}'
    
# To run this in browser:
#1) open terminal
#2) go to folder with code
#3) activate virtual environment 
#4) enter command: flask --app gui run --debug
#5 at this point qebsite should wokr, just go to relevant urls and any time save code the server will automtically update so just need to refresh url
#6 To stop running server it's control-C (this works to kill anything in console)

# WHEN DOING THIS FOR REAL, NEED TO DO BETTER SECURITY
#SET UP https://palletsprojects.com/p/jinja/ 