# iniciando-git-github
Aprendendo o GIT: Primeiros passos e comandos básicos 

# 1º Etapa #
- Configurar o git (git config --global user.name )
                   (git config --global user.email)
- Verificar configuração (git config --global --list)                   
- Criar um repositório git (git init) - Cria um arquivo .git
   O comando git init inicia um novo repositório Git em um diretório local (máquina). Ele permite que você comece a versionar e controlar as alterações dentro dele.
- Adicionar diretório (mkdir)
- Adicionar arquivos ao repositório (touch/echo nome_do_arquivo.extensão )
- Deixar o arquivo pronto para comitar (git add.)
- Comitar arquivo para salvar mudanças (git commit -m "passar o que é o commit")
- Verifircar o status do repositório (git status)
- Remover do estado standing (git rm --cached)
- Conectar o repositório local ao github (git remote add origiin + endereço_web_do_projeto)

# 2ª Etapa #
Trabalhando com banches
O que são? 
É o local onde fica o projeto (branch main - principal), pode criar várias branches para que um grupo possa mexer ao mesmo tempo em um projeto sem alterar a branch principal, depois é só fundir. 
- Ver branches disponíveis no projeto (git branch)
- Criar uma branch (git branch + nome da branch)
- Deletar uma branch (git -d + nome da branch)
- Fundir branches paralelas a principal (git merge + o nome da branche que quer fundir) obs: tem que estar na branch de destino

# 3ª Etapa #
- Enviar alterações para o GitHub (git push -u origin nome_da_branch)
- Atualizar repositório local com mudanças no github (git pull origin nome_da_branch)
- Projeto apenas no GitHub e eu quero trazer para o repositório local (git clone endereço_web_do_projeto)
