No arquivo api.py da biblioteca python-twitter, na linha 2957, deve-se mudar a variavel url para `url = f'{self.base_url}/direct_messages/events/list.json'`, e deve-se adicionar um `return data` antes do `if return_json` pois a função `NewFromJsonDict()` nao ira funcionar.
O arquivo api.py encontra-se em: `C:\Users\user\AppData\Local\Programs\Python\Python38\Lib\site-packages\twitter`
