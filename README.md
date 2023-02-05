# Módulo2_Projeto1_Deumatch!

Case proposto pela Resilia confirme pdf disponibilizado no repositório.
No código importamos a biblioteca pandas para melhor exibição e tratamento onde economizamos tempo e linhas.
Um loop while foi criado para o usuário inserir dados dos candidatos para então criar uma lista deste candidato e guardar em outra lista principal.
Dados inseridos de todos os candidatos, usamos condicional if e else que seria até desnecessário mas como era requisito do case, usei.
Em seguida o def foi criado para realizar a pesquisa conforme os parâmetros que serão passados pelo usuário do código.
A lista que foi passada foi transformada em um data frame usando a biblioteca pandas para melhor tratamento e visualização.
Logo após criamos um novo frame denominado 'dff' onde esse recebe os dados do frame anterior mas com os criterios de busca inseridos pelo usuário.
Na sequência alteramos os nomes das colunas que antes eram numéricas e agora recebem nomes conforme cada conteúdo que há nela.
Conforme solicitado na proposta do projeto, deletamos as colunas onde continham as notas do candidatos deixando apenas a coluna de 'nome' e 'resultado' e chegamos ao fim na função, apenas o return será feito na sequencia.
Na parte final criamos variáveis para servir de parâmetro na hora de chamar a função. Nessas variáveis o usuário irá inserir os parâmetros que desejar para efetuar a pesquisa e encontrar o candidato mais qualificado para vaga.
Finalmente a função é chamada e realiza a pesquisa retornando um data frame com os candidatos aptos para a vaga.
