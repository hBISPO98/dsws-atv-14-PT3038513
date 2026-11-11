# Autenticação de Usuário 1 🔐

Evolução da aplicação web em Flask com a implementação completa do sistema de autenticação e segurança de utilizadores. O grande objetivo desta versão foi introduzir camadas robustas de segurança, incluindo hashing de senhas com o Werkzeug, gestão de sessões com o Flask-Login, separação de rotas através de Blueprints dedicados e envio de e-mails de confirmação com suporte a múltiplos formatos (HTML e TXT).

---

## 🚀 O que mudou? (Versão Anterior vs. Versão Atual)

**1. Subsistema de Autenticação Modular (`auth` Blueprint)**


- **Isolamento de Rotas:** Criação de um pacote exclusivo (`app/auth/`) para gerir de forma independente as rotas de login, registo, alteração de senha e confirmação de conta sob o prefixo `/auth`.


- **Gestão de Sessão com Flask-Login:** Integração do `LoginManager` e da classe `UserMixin` no modelo de utilizadores para controlar automaticamente o estado de autenticação (`current_user`) e proteger rotas restritas.



**2. Segurança Avançada de Dados**


- **Hashing de Senhas:** Substituição do armazenamento em texto simples por funções criptográficas unidirecionadas do Werkzeug (`generate_password_hash` e `check_password_hash`), garantindo que a senha real nunca seja gravada na base de dados.


- **Confirmação de Conta por E-mail:** Uso de tokens encriptados (`itsdangerous`) e interceptação de requisições (`before_app_request`) para bloquear o acesso total a utilizadores que ainda não validaram o seu endereço de e-mail.



**3. Experiência de Utilizador e Comunicação**


- **Formulários Dinâmicos (Flask-WTF):** Implementação de validações avançadas (como verificação de correspondência de senhas em campos duplicados) e feedback visual através de *flash messages* personalizadas.


- **E-mails Multi-part (`.html` e `.txt`):** Configuração de templates duplos para garantir compatibilidade com diferentes leitores de e-mail e clientes de correio.

---

## ⚙️ O que foi necessário implementar?

- **Modificação do Modelo User (`models.py`):** Adição de propriedades para suporte ao Flask-Login, restrições de unicidade de e-mail/username e métodos de verificação de tokens.


- **Configuração de Fábrica (`app/__init__.py` e `config.py`):** Inicialização do `login_manager`, registo do blueprint de autenticação e parametrization das variáveis de ambiente para envio de e-mails.


- **Interface e Views (`app/auth/views.py`):** Desenvolvimento das funções lógicas para registo, login, logout, redefinição de senha e gestão de utilizadores via console interativo (`flask shell`).

---

## 💡 Boas Práticas Adotadas

- **Separação de Responsabilidades:** Organização modular do código separando a lógica de negócio principal das regras estritas de autenticação.   

- **Proteção contra Acessos Indevidos:** Utilização de decoradores como `@login_required` e validações de estado ativo/confirmado antes de renderizar páginas sensíveis.   


- **Segurança no Controlo de Versões:** Manutenção rigorosa de ficheiros sensíveis (como `.env` e bases de dados `.sqlite`) fora do repositório público através do `.gitignore`.

---

## 👩🏽‍💻 Demonstração
<div align="center">

| Home Principal |
| :---: |
| <img src="https://github.com/user-attachments/assets/323e111f-1e80-439d-a9fd-b122954bca32" /> |

<br>

| Interface de Login - E-mail ou Senha Inválido |
| :---: |
| <img src="https://github.com/user-attachments/assets/6a8a7806-03a7-4301-915e-577c603522b8" /> |

<br>

| Interface Após o Primeiro Login |
| :---: |
| <img src="https://github.com/user-attachments/assets/556fbee8-b020-46ea-b602-69983f5f9969" /> |

<br>

| E-mail para Confirmação de Conta | Pop-up de Feedback |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/95230463-abec-4e0c-9a79-e50430b73d78" width="676" /> | <img src="https://github.com/user-attachments/assets/270904ad-a95e-4ec5-8b1b-1b23120fdb04" width="676" /> 

<br>

| Interface de Alteração de Senha | Pop-up de Feedback |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/48c2b2b7-1c76-4d4c-8e95-28ece7a8b34f" width="400"/> | <img src="https://github.com/user-attachments/assets/7cd68fde-d388-4122-b24c-42fc93fc7244" width="400"/>

<br>

| Caso E-mail já Cadastrado |
| :---: |
| <img src="https://github.com/user-attachments/assets/575365c8-dbaa-4537-9aa3-5047c7d4f61d" /> |

<br>

| E-mail para Confirmação de um Novo Endereço de E-mail | Pop-up de Feedback |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/752276a2-8dde-4505-b6e9-be9c4e9831d4" width="638"/> | <img src="https://github.com/user-attachments/assets/bdd6cc40-5c57-4cc2-8ea0-551df89b4468" width="700" />

<br>

| Home Após Fim da Sessão do Usuário |
| :---: |
| <img src="https://github.com/user-attachments/assets/8d7486a5-1026-46d0-a8d7-9435722f1a16" /> |

</div>
