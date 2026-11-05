from flask import Flask, render_template, request
import phonenumbers
from phonenumbers import geocoder, carrier

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = None

    if request.method == "POST":

        number = request.form.get("phone", "").strip()

        try:
            phone = phonenumbers.parse(number, None)

            if phonenumbers.is_valid_number(phone):

                result = {
                    "valid": True,
                    "region": geocoder.description_for_number(
                        phone, "en"
                    ) or "Not available",

                    "carrier": carrier.name_for_number(
                        phone, "en"
                    ) or "Not available",

                    "international": phonenumbers.format_number(
                        phone,
                        phonenumbers.PhoneNumberFormat.INTERNATIONAL
                    )
                }

            else:
                error = "Invalid phone number."

        except phonenumbers.NumberParseException:
            error = "Please enter a valid number with country code."

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)