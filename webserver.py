from flask import Flask, request, render_template
app = Flask(__name__,static_url_path="/static")

quote_db = {
  'sunday': "Life is about making an impact, not making an income. \
  –Kevin Kruse",
  'monday': "Whatever the mind of man can conceive and believe, it can achieve. \
  –Napoleon Hill",
  'tuesday': "Strive not to be a success, but rather to be of value. \
  –Albert Einstein",
  'wednesday': "You miss 100% of the shots you don’t take. \
  –Wayne Gretzky",
  'thursday': "Every strike brings me closer to the next home run. \
  –Babe Ruth",
  'friday': "We become what we think about. \
  –Earl Nightingale",
  'saturday': "Life is what happens to you while you’re busy making other plans. \
  –John Lennon",
}

@app.route('/', methods = ["GET","POST"])
def quote_of_the_day():
	day_of_week = request.form.get("day_of_week")
	if (day_of_week != None):
		return render_template("index.html", content = "The quote for " + day_of_week + ": " + quote_db[day_of_week])
	else:
		return render_template('index.html')  

if __name__ == '__main__':
	app.run(debug = True)