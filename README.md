This is the code for the innovative developer challenge from FRA

Find the challenge here: http://challenge.fra.se/ //ctrl+f 'innovativ utvecklare'
Sorry, no direct link, not even an #id... Bad FRA

Description of challange:
Implementera en minimal chatklient och chatserver som använder sig av protobuf-definitionen i chat.proto för kommunikation.

Välj ett programmeringsspråk som du tycker är lämpligt för att lösa uppgiften. Skicka med tillräckligt med dokumentation för att vi ska kunna testa din lösning. 

Tillhör tjänsten "Innovativ utvecklare" (Dnr 16 321:3777/15).


(184 bytes, sha256: 8138e4fa17ce15172ef3078247460b3d140efc21ce366b1d8c20d8004b7b027a)



Drawbacks for the program:

    Not working on windows, because of select() function used.
    
    If user is typing and receiving a message, the received message and the non-complete message goes on the same line and the user will type the rest of the message on a new line. This could be solved by using better terminal libraries.


Possible code improvements:

    The use of command line arguments for choosing host and port.

    MUCH better error handling for sockets.
    
    Handling duplicate nicknames.
