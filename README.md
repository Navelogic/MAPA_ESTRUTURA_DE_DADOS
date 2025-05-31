# 🥩 Sistema de Controle de Fila - Açougue Bom Preço
Este repositório contém a solução para um estudo de caso prático utilizando a estrutura de dados Fila (Queue) em Python. O objetivo foi analisar um código inicial com erros, compreender os conceitos teóricos e aplicar as correções necessárias, garantindo o funcionamento correto do sistema.

## 📚 Contextualização Teórica
A Fila é uma das estruturas de dados mais importantes e amplamente utilizadas na resolução de problemas do mundo real, principalmente em cenários onde a ordem de chegada deve ser respeitada. Ela segue o princípio FIFO (First In, First Out), onde o primeiro elemento a entrar é o primeiro a sair.

Segundo Cormen. (2012), "as filas são estruturas fundamentais que permitem organizar dados em uma sequência linear, possibilitando operações de inserção em uma extremidade e remoção em outra".

Essa estrutura é amplamente empregada em sistemas de atendimento ao cliente, processamento de tarefas, filas de impressão, sistemas bancários e supermercados. De acordo com Ziviani (2011), "o uso adequado das filas proporciona um controle eficiente no fluxo de dados ou de pessoas, melhorando a experiência do usuário e otimizando os processos de atendimento".

## 🛠️ Estudo de Caso
O Supermercado Bom Preço, localizado na minha cidade, está passando por um processo de modernização. O gerente, Sr. Cláudio Menezes, identificou problemas no setor do açougue, com confusões frequentes sobre quem deve ser atendido primeiro, gerando insatisfação entre os clientes.

O desafio proposto foi analisar um código inicial, identificar os problemas e realizar as correções necessárias para criar um sistema que:

✅ Permita aos clientes retirar uma senha.
✅ Permita ao açougueiro chamar a próxima senha, seguindo a ordem de chegada.
✅ Permita visualizar a fila atual de senhas.

## ❗ Problemas Identificados no Código Original
* A senha era sempre atribuída como 1 para todos os clientes.
* As novas senhas não eram adicionadas corretamente na fila.
* Ao chamar uma senha, a fila não era atualizada, ou seja, não removia a senha chamada.
* A visualização da fila não exibia as senhas corretamente.

## [Código Inicial](https://github.com/Navelogic/MAPA_ESTRUTURA_DE_DADOS/blob/main/mainInicial.py)

## [Código Final](https://github.com/Navelogic/MAPA_ESTRUTURA_DE_DADOS/blob/main/main.py)

## ✅ Correções Realizadas

Linha 22
➡️ Problema: contador_senha = 1 fixava a senha sempre como 1.
✔️ Solução: Alterado para contador_senha += 1 para gerar senhas sequenciais.

Linha 24
➡️ Problema: fila.end(senha) - o método end() não existe.
✔️ Solução: Substituído por fila.append(senha) para adicionar a senha ao final da fila.

Linha 30
➡️ Problema: popleft() estava isolado, sem referência à fila.
✔️ Solução: Corrigido para senha_chamada = fila.popleft().

Linha 38
➡️ Problema: fila.list não é um atributo válido.
✔️ Solução: Utilizado list(fila) para converter e exibir a fila corretamente.



## 📄 Referências
* CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. Algoritmos: Teoria e Prática. 3. ed. Rio de Janeiro: Elsevier, 2012.
* ZIVIANI, N. Projeto de Algoritmos: com Implementações em Pascal e C. 3. ed. Cengage Learning, 2011.
