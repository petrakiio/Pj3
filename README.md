<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/API-REST-blue?style=for-the-badge" alt="REST API">
  <img src="https://img.shields.io/badge/JSON-Data-lightgrey?style=for-the-badge&logo=json&logoColor=black" alt="JSON">
</div>

<h1 align="center">🛒 Inventory API - Gestão de Estoque</h1>

<p align="center">
  <strong>O motor de Back-end para sistemas de PDV e E-commerce, focado em manipulação ágil de inventário.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/petrakiio/NOME_DO_REPOSITORIO?style=flat-square" alt="Last Commit">
  <img src="https://img.shields.io/badge/Main_Language-Python-blue?style=flat-square" alt="Language">
</p>

---

### 📦 Sobre o Projeto
Esta API foi desenvolvida com **Flask** para gerenciar catálogos de produtos de forma eficiente. Ela serve como a base lógica para sistemas que precisam de controle de entrada e saída de mercadorias, integrando rotas de manipulação de dados com uma interface de suporte ao usuário.

### 🌟 Destaques Técnicos
* **Padrão RESTful:** Implementação rigorosa dos métodos HTTP (`GET`, `POST`, `DELETE`) para garantir uma comunicação padronizada.
* **Documentação Integrada:** O projeto conta com uma rota exclusiva `/Settings` que renderiza um template HTML explicativo, facilitando o uso por outros desenvolvedores ou integradores de front-end.
* **Tratamento de Erros:** Sistema de respostas inteligentes com retornos `HTTP 404` e validações de recursos, evitando quebras inesperadas na aplicação.
* **Prototipagem Ágil:** Estrutura de persistência otimizada para testes rápidos e validação de regras de negócio em tempo real.

---

### 🛠️ Tecnologias Utilizadas
* **Backend:** Python + Flask.
* **Formatos:** JSON (Troca de dados).
* **Templates:** Jinja2 (Para a documentação de suporte).

---

### 🛣️ Principais Rotas
<table align="center">
  <tr>
    <td><strong>Método</strong></td>
    <td><strong>Rota</strong></td>
    <td><strong>Descrição</strong></td>
  </tr>
  <tr>
    <td><code>GET</code></td>
    <td><code>/products</code></td>
    <td>Lista todo o inventário.</td>
  </tr>
  <tr>
    <td><code>POST</code></td>
    <td><code>/add</code></td>
    <td>Adiciona um novo item ao estoque.</td>
  </tr>
  <tr>
    <td><code>DELETE</code></td>
    <td><code>/remove/&lt;id&gt;</code></td>
    <td>Remove um produto específico.</td>
  </tr>
  <tr>
    <td><code>GET</code></td>
    <td><code>/Settings</code></td>
    <td>Manual de uso e documentação HTML.</td>
  </tr>
</table>

---

<div align="center">
  <p>🚀 Desenvolvendo soluções escaláveis e seguras.</p>
  <a href="https://github.com/petrakiio">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</div>

---

<div align="center">
  <sub>API construída por <a href="https://github.com/petrakiio">Pedro</a> — Especialista em Back-end com Python.</sub>
</div>
