<h1>Security & Cyberwarfare Week 5 - Encryptie</h1>

<h3>Wat is encryptie?</h3>
Bij encryptie wordt een bericht versleuteld naar een cipher text. Deze cipher text kan vervolgens ook weer ontsleuteld worden met een sleutel, zoals bijvoorbeeld een wachtwoord of een session key. Telkens wanneer je data versleutelt, komt hier een andere cipher text uit. Zelfs wanneer de data en de sleutel telkens hetzelfde zijn als voorheen.

<h3>Encryptie algoritmes</h3>
De data wordt versleuteld op basis van een algoritme. Er zit dus logica achter, en de manier van versleutelen is logisch, waardoor de data met de juiste sleutel ook weer ontsleuteld kan worden. Deze sleutel kan verschillen in eenvoud of complexiteit. En uiteraard geldt, hoe complexer de sleutel, hoe lastiger deze te kraken is.

De sleutel is in praktijk een string van karakters die in een encryptie algoritme gebruikt wordt en zo data modificeert om het random te laten lijken. Volgens het principe van Auguste Kerckhoffs (Nederlands cryptograaf, 1835 - 1903), moet een cryptosysteem nog steeds veilig zijn, zelfs wanneer het volledige systeem, op de sleutel na, publiekelijk in te zien is. Dit principe wordt door cryptografen omarmd en is het tegenovergestelde van het ‘security through obscurity’ principe, wat juist stelt dat er gestreefd moet worden naar een volledig verborgen cryptografie systeem ten behoeve van de beveiliging ervan. Het security through obscurity principe wordt juist afgeraden door cryptografen.


<h3>Symmetrische encryptie</h3>
Encryptie kan zowel symmetrisch als asymmetrisch toegepast worden. Bij symmetrische encryptie is er een gedeelde sleutel die gebruikt wordt voor zowel het versleutelen als het ontsleutelen van een bericht. Zowel de zender als de ontvanger van het bericht zullen dus dezelfde sleutel delen. Dit is ook direct de grootste valkuil bij symmetrische encryptie. Het feit dat beide partijen dezelfde sleutel moeten hebben, is onpraktisch. Bekende encryptie algoritmes zijn bijvoorbeeld AES, 3-DES en SNOW.

<h3>Asymmetrische encryptie</h3>
Asymmetrische encryptie maakt gebruik van twee verschillende sleutels. Een private key en een public key. De sleutels zijn aan elkaar gelinkt, maar alleen de public key mag gedeeld worden. Je kunt het vergelijken met een brievenbus. Iedereen kan het klepje openmaken om een brief erin te doen. Dat klepje zou je kunnen zien als de public key. Iedereen kan dat klepje openen. Om de post echter weer uit de brievenbus te halen, moet je deze aan de andere kant weer openen met een fysieke sleutel. (Tenzij je een brievenbus in je voordeur hebt. In dit voorbeeld ga je uit van een losstaande brievenbus of een postvak in bijvoorbeeld een flat of kantoor. Maar zelfs bij een brievenbus in je voordeur, kun je de post niet pakken zonder de sleutel van het huis)

Het nadeel van asymmetrische cryptografie, is dat het zo’n 1.000 keer langzamer is dan symmetrische cryptografie. Ook kan het aantal keys enorm snel exponentieel oplopen wanneer meerdere clients met elkaar moeten kunnen communiceren. Asymmetrische cryptografie wordt in de praktijk bijna nooit gebruikt voor pure encryptie, maar meer voor key exchange en digital signatures. Veel gebruikte asymmetrische encryptie algoritmes zijn bijvoorbeeld RSA en Elliptic curve cryptography.

<h3>Hybride encryptie</h3>
Vaak wordt er gebruikgemaakt van een hybride encryptie. Dit is een combinatie van symmetrische en asymmetrische encryptie. Er wordt dan asymmetrische encryptie gebruikt om een symmetrische session key versleuteld op te slaan. Deze session key wordt vervolgens gebruikt om data te versleutelen. Hybride encryptie combineert het beste van twee werelden. Doordat je asymmetrische encryptie gebruikt voor de session keys, loopt het aantal keys niet meer exponentieel op bij meerdere gebruikers. Voor het gros van de data gebruik je echter symmetrische encryptie, wat de snelheid ten goede komt.

<h3>Kerckhoffs principe</h3>
Volgens het principe van Auguste Kerckhoffs (Nederlands cryptograaf, 1835 - 1903), moet een cryptosysteem nog steeds veilig zijn, zelfs wanneer het volledige systeem, op de sleutel na, publiekelijk in te zien is. Dit principe wordt door cryptografen omarmd en is het tegenovergestelde van het ‘security through obscurity’ principe, wat juist stelt dat er gestreefd moet worden naar een volledig verborgen cryptografie systeem ten behoeve van de beveiliging ervan. Het security through obscurity principe wordt juist afgeraden door cryptografen.

<h3>AEAD</h3>
Authenticated Encryption with Associated Data is een cryptografische methode waarbij associated data geauthenticeerd wordt, maar niet versleuteld wordt. Hierdoor kunnen bijvoorbeeld headers in een netwerk response uitgelezen worden, maar wordt wel eerst de authenticiteit ervan geverifieerd.

<h3>Key Derivation Function</h3>
Key Derivation Function (KDF) is een cryptografisch algoritme dat 1 of meerdere complexere secret keys genereert uit één key (bijvoorbeeld een door de gebruiker opgegeven wachtwoord). Deze algoritmes zijn zo ontworpen dat ze veel rekenkracht vereisen, waardoor brute force attacks lastiger uit te voeren zijn. Dit is gedaan door extra’s toe te voegen zoals hashing, salting, iteration en stretching. De sleutel wordt hierdoor ook een stuk complexer. Wanneer je juist met hashing werkt, in plaats van encryptie, helpt KDF ook tegen het gebruik van rainbow tables.

<h3>Waarom is encryptie belangrijk?</h3>
Precies om dezelfde reden waarom je brievenbus op slot zit. Privacy, veiligheid en integriteit. Dankzij encryptie kan niemand anders jouw post, uh ik bedoel data, lezen, behalve jijzelf. Of in ieder geval de persoon voor wie de data bedoeld is of de eigenaar. Aanvallers, internetproviders, overheden of andere kwaadwillenden kunnen versleutelde data niet uitlezen zonder sleutel. De privacy van gebruikers wordt hiermee beschermd. Encryptie helpt ook tegen datalekken. Het biedt extra beveiliging voor de data, zelfs als deze onderschept wordt, dan wel fysiek of digitaal. Bovendien verzekert encryptie je data integriteit. Terwijl je data verzonden wordt of opgeslagen is, kan deze niet zomaar uitgelezen of aangepast worden.

Omdat encryptie zo belangrijk is, is het vaak ook verplicht onder bepaalde regulaties van overheden of bedrijven. Denk bijvoorbeeld aan de GDPR.

<h2>Technische details</h2>

<h3>Welk symmetrisch algoritme gebruik ik?</h3>
Ik maak gebruik van AES-GCM (AEAD) om berichten te versleutelen. Dit is een standaard, goed gewaardeerd algoritme en is eenvoudig te implementeren. Dankzij de GCM tag krijg je niet alleen confidentiality maar ook authenticiteit. Het is ook een algoritme dat snel en efficiënt werkt.

<h3>Hoe komt de sleutel tot stand?</h3>
Ik laat gebruikers een passphrase (wachtwoord) invoeren. Ik pas vervolgens een Key Derivation Function toe op het ingevoerde wachtwoord om de sleutel extra complex te maken. Er wordt een salt toegevoegd aan het wachtwoord en vervolgens wordt het geheel gehashed. Dit houdt bijvoorbeeld bruteforce attacks tegen. Ik gebruik scrypt (uit de Cryptography library) als Key Derivation Function. Dit is een sterke KDF die relatief hardware-intensief is. Daardoor zijn brute-force aanvallen minder efficiënt. Het duurt namelijk lang en vereist veel rekenkracht om deze uit te voeren.

<h3>Hoe wordt de sleutel weer geraadpleegd?</h3>
De sleutel zelf wordt niet bewaard. Wat bewaard wordt is de salt die samen met de passphrase aan Scrypt meegegeven wordt en de n, r, p parameters die Scrypt gebruikt. Scrypt geeft de sleutel en de kdf_meta terug wanneer je de derive_key_from_passphrase function aanroept. De kdf_meta is een dictionary die omgezet kan worden in JSON. Daarin staat niet de sleutel, maar alleen welke KDF er gebruikt is (dus scrypt) en welke salt en parameters er gebruikt zijn. Bij het decrypten haal je deze data weer uit de aangeleverde package en kun je zo samen met de passphrase de key weer achterhalen zodat de ciphertext in de package ontsleuteld kan worden.

<h3>Outputformaat voor ciphertext:</h3>
De versleutelde output wordt gegeven als een JSON package met de ciphertext inclusief noodzakelijke metadata. Met de metadata zoals het gebruikte algoritme, de toegepaste nonce, KDF parameters en natuurlijk de ciphertext zelf, kan het versleutelde bericht ook weer ontsleuteld worden. Zonder de metadata is dit niet mogelijk. De key (passphrase) staat uiteraard niet in de JSON output. Deze dient de gebruiker zelf te onthouden. De rest mag allemaal in de package komen te staan. Dit is in lijn met het principe van Kerckhoff. JSON is een goede optie om zo’n totaalpakketje mee te maken. Het is namelijk goed te verwerken in webapps en is ook nog eens leesbaar voor mensen.

<h3>Link naar mijn Github Repo:</h3>

