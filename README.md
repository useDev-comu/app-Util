# 🗑️ AppClean - Gerenciador de Lixeira para Windows

## 📌 Descrição

**LimpaLixeira** é um utilitário simples em **Python** para limpar a lixeira do Windows de forma segura. Antes de remover os arquivos, o programa solicita confirmação do usuário, garantindo que apenas arquivos desejados sejam excluídos.

---

## 🚀 Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando:

- **Python** - Linguagem de programação principal.
- **winshell** - Biblioteca para manipular recursos do Windows, incluindo a lixeira.
- **pywin32** - Interface para interagir com APIs do Windows.
- **pyinstaller** - Empacotamento do código em um executável `.exe` para facilitar a execução.

---

## 📦 Instalação

### **1️⃣ Clonar o Repositório**

```bash
git clone https://github.com/seu-usuario/app-Util.git
cd limpalixeira
```

### **2️⃣ Instalar Dependências**

Certifique-se de que o Python está instalado e execute:

```bash
pip install winshell pywin32
```

## 🔥 Como Usar

1️⃣ Executando via Python

```bash
python limpalixeira.py
```

O programa solicitará confirmação antes de limpar a lixeira.

2️⃣ Gerando um Executável Caso deseje criar um arquivo .exe para rodar sem precisar do Python instalado:

```bash
pyinstaller --onefile --windowed limpalixeira.py
```

- O executável será gerado na pasta dist/.
- Agora, basta clicar duas vezes no .exe para rodar o programa.

## ⚙️ Automatização no Windows

Caso queira automatizar a execução do programa, você pode:

Adicionar ao "Inicializar" do Windows (shell:startup).
Criar uma Tarefa Agendada no Windows para rodar periodicamente.
Adicionar ao Menu de Contexto via Editor de Registro.

## 🔽 Baixe o Executável

Acesse a última versão:
[⬇️ Download](https://github.com/useDev-comu/app-Util/raw/main/dist/limpar_lixeira.exe)

## 🎯 Contribuições

Sinta-se à vontade para contribuir! Para isso:

1 - Fork no repositório.
2 - Crie uma branch nova.
3 - Faça suas alterações.
4 - Envie um pull request.

## 📜 Licença

Este projeto está sob a licença MIT, permitindo uso livre com modificações.
