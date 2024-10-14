### 13:47, 13/10/2024

- 13:49
1. Eu ainda não rodei o código. Irei rodar o `new_mail.py` novamente, para ver se realmente vai de acordo com o help anterior.

2. Lembro que tem que ser em uma conta que permita login fraco. Mas vou usar a que tiver disponivel no PC

3. Indo testar...

4. Eu instalei as libs que pediu e infelizmente deu erro, pq pediu um token.json e o help.md anterior não especificou como compilar isso ou onde compilar.

5. Eu pesquisei e encontrei o site Master do python gmail `https://developers.google.com/gmail/api/quickstart/python`. ele fala dos passos a passos de como fazer o `tken_json.json`.
    1. Seguindo o manual dele, eu vim parar em um site que cria credenciais de API Cloud Google, `https://console.cloud.google.com/apis/credentials/consent/edit;newAppInternalUser=false?project=hidden-terrain-321821`.
    2. Na tela inicial pede o nome da app, na tela de escopos, pede os escopos que irei colocar. Como no código já tem 'os que deram certos', então iri ignorar isso e só criar.

6. Deu erro afirmando que faltava informação. Usei o gpt e com ele eu vi que o `token.json` é o que ele gera e `credentials.json` é o que ele absorve pra compilar. Olhei o codigo que deu certo, `mail_html.py` e vi que tinha o sendmailreysofts no meio. Abri essa conta e agora vou ver se tem API nela, pq a que criei usando devops fala que tá inválida.

7. Vi que realmente tem algo nele de `10/06/2023`. Irei baixar sua `credentials.json` e testar.

8. O App é seguro, criou o `token.json`. Irei testar o `mail_html.py` agora.

9. Foi! O email foi enviado! Que Foda! O Reinan past é sempre impressionando!! 
