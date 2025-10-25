Saudação Automática com Python
Scripts que Simplificam – Mindtech
Este projeto mostra como criar um script simples em Python que faz o computador cumprimentar automaticamente conforme o horário do sistema, dizendo “Bom dia”, “Boa tarde” ou “Boa noite”.
O objetivo é demonstrar que a automação pode ser acessível, prática e fácil de aplicar, mesmo para quem está começando a programar. Com apenas algumas linhas de código, você já aprende conceitos básicos de lógica e estruturas condicionais em Python.
 
Sobre o projeto
O script foi desenvolvido por Bruni Marchioro, através da marca Mindtech, como parte da série de conteúdos voltados a automação, acessibilidade e aprendizado de programação.
A ideia é incentivar pessoas a entenderem que automatizar tarefas pequenas pode economizar tempo, reduzir erros e despertar o interesse por tecnologia.
 
Funcionamento
1. O código usa a biblioteca datetime para capturar a hora atual do sistema.
2. Em seguida, compara o valor da hora e decide qual mensagem exibir:
• Antes de 12h: Bom dia
• Entre 12h e 18h: Boa tarde
• Depois de 18h: Boa noite
3. Ao final, exibe uma mensagem indicando que a automação foi concluída com sucesso.
 
Código completo
from datetime import datetime
Captura a hora atual do sistema
hora = datetime.now().hour
Verifica o horário e escolhe a saudação
if hora < 12:
print("Bom dia!")
elif hora < 18:
print("Boa tarde!")
else:
print("Boa noite!")
print("Seu dia está automatizado com Python.")
 
Como executar
1. 
Salve o arquivo com o nome saudacao.py.
2. 
Abra o Prompt de Comando (Windows) ou o Terminal (Linux ou macOS).
3. 
Navegue até a pasta onde o arquivo foi salvo.
Exemplo:
cd C:\Users\usuário\Desktop
4. 
Execute o script com o comando:
python saudacao.py
O programa exibirá automaticamente a saudação correspondente ao horário do seu computador.
 
Explicação das principais linhas
• from datetime import datetime: importa a função que captura a hora atual.
• hora = datetime.now().hour: armazena a hora (0 a 23) na variável hora.
• if, elif e else: estruturas condicionais que decidem a mensagem exibida.
 • print(): exibe o texto final na tela.
 
Acessibilidade
O código foi desenvolvido seguindo boas práticas de acessibilidade digital:
 
 - Compatível com leitores de tela (NVDA, JAWS, VoiceOver e TalkBack).
- Comentários simples e descritivos.
- Linguagem clara e objetiva.
Se quiser que o terminal permaneça aberto após a execução (útil para quem usa leitor de tela), adicione esta linha ao final do código:
input("Pressione Enter para sair...")
 
Autoria
Desenvolvido por Bruni Marchioro
Marca: Mindtech – Soluções Digitais, Automação e Acessibilidade
Repositório principal: https://github.com/bruni-marchioro/mindtech
 
Licença
Este projeto é de uso livre para fins educativos.
Você pode copiar, modificar e redistribuir, desde que mantenha os créditos originais.

"Automatizar é transformar tempo em liberdade".

