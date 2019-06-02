# enigma_rsa
## Simulação de conversa com proteção contra ataques MITM

Certifique-se de que você possui python 3 instalado!

Na pasta raiz, execute:
```bash
make install
```

Caso queira apenas reiniciar a pasta 'private_conversation' (irá gerar novas chaves):
```bash
make reboot
```

## Iniciando simulação

Recomenda-se a quem for utilizar este programa que, neste momento, abra duas janelas do terminal lado a lado. 
Diversos terminais possuem atalhos de teclado para dividir uma janela facilmente, mas você também pode simplesmente abrir duas janelas distintas e posicioná-las como dito.

Após, estando na pasta raiz do programa, ative o ambiente virtual criado pelo comando acima NOS DOIS TERMINAIS:
```bash
source env/bin/activate
```

Em um terminal, entre na pasta:
```bash
private_conversation/sender
```

No outro terminal, entre na pasta:
```bash
private_conversation/receiver
```

Inicie o console do python3 nos dois terminais com o comando:
```bash
python3
```

No console aberto na pasta sender, importe o módulo correspondente com o comando:
```bash
>> import sender
```

Ao fazer esta importação, você receberá a seguinte mensagem:
```sender
>> Copie e cole a linha a seguir: 
>> from sender import encrypt, get_hash, get_sign, send, helpme, public_s, private_s, public_r
```

Este passo é importante para facilitar o uso das funções que o programa fornece, retirando a necessidade de usar o prefixo 'sender.' antes do uso de qualquer função.

Neste momento, realize a mesma importação (mas do módulo 'receiver') no outro terminal.

Pronto! Agora você pode executar todos os comandos disponíveis no programa.

Use o comando 'helpme()' para obter uma lista com descrição de todos os comandos disponíveis.

## Sender

Com o papel de 'sender', suas possibilidades são a de criar uma mensagem, encriptá-la, assiná-la e enviá-la ao receiver.
Todos estes passos são opcionais mas alguns deles garantem que o receiver será capaz de determinar se a mensagem recebida é confiável ou não.

### Pequeno tutorial

Você pode criar uma nova mensagem simplesmente atribuindo uma string a uma variável no console:
```bash
>> msg = "amo criptografia kkk"
```

Com esta mensagem guardada na variável 'msg', podemos encriptar a mensagem com alguma chave (você deve escolher qual a melhor chave para encriptar sua mensagem, baseado nos seus conhecimentos de criptografia):
```bash
>> msg_encriptada = encrypt(msg, <alguma chave>)
```

Você pode ver quais chaves estão disponíveis para sua utilização com o comando 'helpme()'.

Agora cabe a você fazer os próximos passos e garantir o nível de segurança desejado!

Por fim, execute o comando 'send(\<msg\>, opt: \<sign\>)' para enviar a mensagem ao receiver e, opcionalmente, uma assinatura.

## Receiver

Com o papel de 'receiver', você poderá receber uma mensagem enviada pelo sender usando o comando 'get_message()' (lembre-se de conferir o comando de ajuda 'helpme()').

Após obter a mensagem, você pode receber uma assinatura com o comando 'get_signature()', que lhe indicará se a mensagem não veio assinada. 

Use os comandos disponíveis para determinar se a mensagem é confiável ou não!


