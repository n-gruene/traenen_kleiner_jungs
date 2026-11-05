##---------------------------------------##
#  /\_/\   /\_/\   /\_/\   /\_/\   /\_/\  #
# < cᴥc > < oᴥo > < TᴥT > < uᴥu > < xᴥx > #
#-----------------Nas&Nat-----------------#
# Prototyp Berichtsheft-App               #
##---------------------------------------##

from flask import Flask, render_template

app = Flask(__name__)

# pseudodaten fuer die einzelnen karten (wochentage)
TAGE = [
    {"name": "Montag", "datum": "19.10.2026", "stunden": "4.5h",
     "hinweis": "Hinweis des Ausbilders zur Zurückweisung: Nonumy eirmod tempor invidunt.",
     "taetigkeiten": [("Lorem ipsum dolor sit amet", "2h"), ("Et dolore magna aliquyam", "1h")]},
    {"name": "Dienstag", "datum": "20.10.2026", "stunden": "4.5h",
     "taetigkeiten": [("At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.  ", "2h"), ("Sed diam nonumy eirmod", "1h")]},
    {"name": "Mittwoch", "datum": "21.10.2026", "stunden": "4.5h",
     "taetigkeiten": [("Consetetur sadipscing elitr", "2h"), ("Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.", "2h"), ("", "")]},  # nicht ausgefuellte felder sollen gekennzeichnet werden
    {"name": "Donnerstag", "datum": "22.10.2026", "stunden": "4.5h",
     "taetigkeiten": [("Et dolore magna aliquyam", "2h"), ("Nonumy eirmod tempor", "1.5h")]},
    {"name": "Freitag", "datum": "23.10.2026", "stunden": "3h",
     "taetigkeiten": [("Lorem ipsum dolor sit amet", "2h"), ("Et dolore magna aliquyam", "1h")]},
]

# home route; da es sich um einen prototypen handelt, benoetigen wir (vermutlich) keine weitere
@app.route("/")
def index():
    return render_template("index.html", tage=TAGE)

if __name__ == "__main__":
    app.run(debug=True, port=1313)