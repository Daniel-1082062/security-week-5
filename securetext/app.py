from flask import Flask, render_template, request, flash
from securetext.crypto_core import encrypt_text_with_passphrase, decrypt_text_with_passphrase
app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretsecretkey"

@app.route('/')
def index():
    return render_template('index.html', message="Encryption tool werkt!")

@app.route('/encrypt', methods=['POST', 'GET'])
def encrypt():
    try:
        # Vraag alle input uit het formulier op
        plaintext = request.form.get("plaintext", "").strip()
        mode = request.form.get("mode", "passphrase")
        passphrase = request.form.get("passphrase", "")
        # Geen tekst om te encrypten? Error!!
        if not plaintext:
            flash("Error, please enter a plaintext.", "error")
            return render_template('index.html', enc_output="")
        # Passphrase als key generatie method maar geen wachtwoord ingevoerd? Error!!!!!
        if mode == "passphrase" and not passphrase:
            flash("Error, please enter a passphrase.", "error")
            return render_template('index.html', enc_output="")
        # Anders de pagina weer renderen met nu de encrypted data in het uitvoervak.
        cipher_json = encrypt_text_with_passphrase(plaintext, passphrase)
        flash("Text succesfully encrypted.", "success")
        return render_template('index.html', enc_output=cipher_json, dec_output="")

    except Exception as e:
        flash("Something went wrong.", "error")
        print("Encryption error:", e)
        return render_template("index.html")

@app.route('/decrypt', methods=['POST', 'GET'])
def decrypt():
    try:
        # Vraag alle input uit het formulier op
        cipherjson = request.form.get("cipherjson", "").strip()
        mode_dec = request.form.get("mode_dec", "passphrase")
        passphrase_dec = request.form.get("passphrase_dec", "")
        # Geen JSON package ingevoerd? Error!
        if not cipherjson:
            flash("Error, please submit an encrypted JSON package.", "error")
            return render_template('index.html', dec_output="")
        if mode_dec == "passphrase" and not passphrase_dec:
            flash("Error, please enter a passphrase.", "error")
            return render_template("index.html", dec_output="")
        # Return de pagina met de ontsleutelde tekst in het tekstvak.
        plaintext = decrypt_text_with_passphrase(cipherjson, passphrase_dec)
        flash("Text succesfully decrypted.", "success")
        return render_template("index.html", enc_output="", dec_output=plaintext)
    except Exception as e:
        flash("Something went wrong.", "error")
        print("Decryption error:", e)
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)