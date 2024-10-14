## start

seguinte, isso foi trabalohoso pra krl, mas finalmente conseguimos enviar o bagulho sem precisar de login porraaaa
<br>
<br>

### passos dados
primeiranmente, irei colocar as pessoas nos quais foram os ombros nos quais me apoiei:

<br>
As libs: <br>
```sh
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

<br>
<br>

deixa claro sobre a nescessidade de atualização -> https://stackoverflow.com/questions/69561207/httperror-403-when-requesting-none-returned-insufficient-permission
<br>


jeito certo de ler os scopes -> https://stackoverflow.com/questions/56445257/valueerror-client-secrets-must-be-for-a-web-or-installed-app <br>

<br>
a questão salvadora -> https://stackoverflow.com/questions/32143126/how-do-i-get-around-httperror-403-insufficient-permission-gmail-api-python <br>

scopes de gmail (que foi a salvação) -> https://developers.google.com/gmail/api/auth/scopes <br>
(isso merece um artigo mesmo, pqp que bagulho dificil)
<br>

send gmail -> https://developers.google.com/gmail/api/guides/sending


<br>

<br>
tentarei enviar um email html com isso -> https://mailtrap.io/blog/python-send-email-gmail/#:~:text=To%20send%20an%20email%20with%20Python%20via%20Gmail%20SMTP%2C%20you,Transfer%20Protocol%20(SMTP)%20server.

<br>
<br>

### regras

- 1. precisa primeiro baixar o auth json para computador para poder rodar no arquivo new_email.py, que possui as scopes nescessárias para <br>
 para criar as instâncias de validação de envio de email <br> depois que rodar ele, ele vai criar u marquivo token.json, com todas as permissões de gmail da conta que foi logada sobre ele. <br> Esse arquivo será usado no proximo  codigo<br><br>
- 2. rodar o new_mail.py, pois ele é a carroça de todo o codigo.
