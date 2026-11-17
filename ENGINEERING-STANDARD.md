# Padrão Eurekando — Engenharia Limpa e Simplicidade Radical
**Versão oficial: 2026-11-17 · Aplicação: Radar de Editais Eurekando.**

> Princípio: uma criança de 5 anos deve conseguir **encontrar** onde as coisas estão em até 15 segundos. Ela não precisa compreender código. A solução técnica deve ser inteligível a um profissional novo, com exemplos claros e verificações reproduzíveis.

## O que é inegociável
1. **Uma responsabilidade, um lugar.** Toda regra de negócio possui um único dono explícito, sem cópias independentes em UI, automação e SQL. Se a implementação tiver camadas, cada camada protege um contrato distinto (UI orienta, servidor autoriza, banco preserva integridade).
2. **Mínimo necessário.** Não criar abstração, arquivo, tabela, índice, feature, componente, job, API ou biblioteca se não houver caso de uso atual demonstrado. Reutilizar o que já existe, sem acoplar produtos independentes.
3. **Código legível.** Nomes sem ambiguidade, funções com uma tarefa, entrada/saída explícitas, erros úteis e tratados na origem. Evitar estado global mutável, funções gigantes e constantes mágicas; separar interface, regra, persistência e operações quando agregarem clareza.
4. **Banco coerente.** Identidade única, tipos e constraints corretos, chaves estrangeiras indexadas quando o plano exige, transações atômicas, migrações versionadas e reversíveis quando possível, RLS/autorização testadas. Índices "não usados" exigem análise de carga antes de remoção. **Migrações aplicadas são história auditável, não lixo.**
5. **Ambientes isolados.** DEV/HML/PRD identificados; endpoints, segredos, permissões, quotas e deploys separados por aplicação. Nunca colocar segredos no repositório, nem usar dados pessoais reais em testes. Mudanças destrutivas requerem backup, impacto e autorização.
6. **Qualidade antes de publicar.** Checar lint/format, tipagem, testes unitários, integração, contrato de banco, segurança e regressão do fluxo essencial. UI exige teste em viewport real/mobile e desktop, acessibilidade/sem overflow e homologação visual. Um CI verde **não comprova** toda a experiência.
7. **Zero passivo oculto.** Cada desvio encontrado tem proprietário, risco, evidência, correção ou justificativa explícita. Não declarar "zero débito técnico" sem inventário auditado e evidências. Não varrer problemas para debaixo de novos controles ou contadores.
8. **Mudança pequena e segura.** Alterar a menor área necessária, verificar efeitos em fluxos vizinhos, registrar PR/commit, testes, resultados e rollback. Nunca apagar código, registros, índices ou migrações sem comprovar uso, dependências e autorização apropriada.
9. **Uma documentação de verdade.** README indica onde começar, este contrato define o padrão de engenharia, documentos de domínio definem somente regras do produto; automações **apontam para as regras**, sem replicá-las. Explicação de cada componente em três frases: o que faz, por que existe, onde consultar.
10. **Autonomia operacional.** Jobs idempotentes, limites e falhas rastreados, alertas úteis e métricas consistentes, sem exigir que CAOS faça a triagem técnica. Falha deve ser observável sem expor dados pessoais.

## Contrato exclusivo deste projeto
Radar de editais e prestação de serviços PJ da Eurekando; manter fontes oficiais, rastreabilidade, status verificáveis, prazos e filtros. Não confundir oportunidades elegíveis com candidaturas enviadas. Não compartilhar dados ou deploy com os outros produtos.

## Portão de entrega (Definition of Done)
Uma alteração só pode ser chamada **concluída** com: objetivo e impacto claros; revisão de redundância/legado; CI pertinente aprovado; testes reais das regras e integração; verificação de segurança e dados; teste visual quando aplicável; documentação atualizada; evidência de implantação; riscos e pendências declarados; autorização/homologação conforme o fluxo do projeto.

**Relato obrigatório:** "Implementado" (com link de commit/PR), "Validado" (link de teste), "Publicado" (ambiente/versão), "Pendente" (com risco). Nunca transformar apenas status de deploy em homologação. Se algo não foi testado, escrever **não testado**.

## Como qualquer pessoa encontra tudo
- **Começar:** README.md
- **Qualidade e arquitetura:** este arquivo (`ENGINEERING-STANDARD.md`)
- **Regras funcionais:** contrato/documentação do domínio específico
- **Código e testes:** dentro da aplicação que possui o comportamento
- **Automação e CI:** .github/workflows ou sistema de tarefas do serviço, com fonte de regras explicitamente apontada
- **Dados e migrações:** no projeto de banco correspondente, sem cruzamento de aplicações

## Revisão de integridade periódica
Em cada evolução importante, verificar: código órfão; arquivos duplicados; jobs repetidos; migrations incompatíveis; endpoints/segredos/variáveis sem uso; índices sem necessidade; permissões excessivas; erros silenciosos; métricas inconsistentes; regressão mobile; documentação obsoleta. Não apagar só por parecer desnecessário. Guardar decisões relevantes e corrigir com teste de regressão.
