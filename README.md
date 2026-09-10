# vsys-val.github.io

Landing page pessoal. Um arquivo HTML, sem framework, sem build step, sem tracker.

```
index.html          a página inteira (HTML + CSS + JS num arquivo só)
assets/
  hero.webp         retrato do topo
  sobre.webp        foto da seção "Sobre"
build_artifact.py   opcional: gera uma cópia com as imagens embutidas
```

## Publicar

1. Crie um repositório **público** chamado exatamente `vsys-val.github.io`.
2. Suba estes arquivos na raiz da branch `main`.
3. `Settings → Pages → Build and deployment → Source: Deploy from a branch → main / (root)`.
4. Um ou dois minutos depois: **https://vsys-val.github.io**

```bash
git init
git add .
git commit -m "landing page"
git branch -M main
git remote add origin git@github.com:vsys-val/vsys-val.github.io.git
git push -u origin main
```

## Antes de publicar

- [ ] **ForHouse** aparece sem link. Quando o repositório do grupo estiver público, o `<h3 class="proj-name">ForHouse</h3>` vira um `<a>` como os outros dois.
- [ ] **Reler os textos.** Foram escritos a partir do que você contou, mas a voz precisa ser sua de fato.

## Como editar o conteúdo

A página é **bilíngue por marcação**, não por JavaScript. Todo texto traduzível aparece duas vezes:

```html
<span lang="pt-BR">Problema antes da solução</span>
<span lang="en">Problem before solution</span>
```

O CSS esconde um dos dois conforme o `data-lang` no `<html>`. Para adicionar texto novo, siga o mesmo padrão. Se esquecer a versão em inglês, ela some quando alguém troca o idioma.

> **Cuidado com a cascata.** O bloco `/* i18n */` fica no fim do `<style>` de propósito: ele precisa vencer qualquer regra de `display` declarada antes (foi assim que os bullets do topo apareceram nos dois idiomas na primeira versão). Se você criar uma regra nova que define `display` em algum elemento com `lang=`, teste a troca de idioma.

O idioma inicial vem do `localStorage` ou, na primeira visita, do idioma do navegador.

**Seções**, na ordem do arquivo: `hero`, `metodo`, `projetos`, `ferramentas`, `sobre`, `contato`.

**Um projeto novo** é um bloco `<article class="proj">` copiado de um existente. A estrutura fixa é: nome, tipo, uma linha de contexto e as três células `Decisão / Risco / Evidência`. Se um projeto não tem as três, provavelmente não deveria estar na página. É esse critério que dá sentido à seção.

**Cores e tipografia** ficam nas variáveis CSS no topo do `<style>`:

```css
--ground:#E4E5DF;   /* fundo, calcário frio     */
--ink:#121310;      /* texto                    */
--accent:#1F2ABF;   /* ultramarino              */
--void:#121310;     /* fundo das seções escuras */
```

**Trocar as fotos**: mantenha as proporções (`hero.webp` em 3:4, `sobre.webp` em 4:5) ou ajuste o `aspect-ratio` de `.hero-figure` junto. As duas passam por `filter: grayscale(1)`, o que unifica fotos tiradas em lugares diferentes.

## Detalhes técnicos

- Tipografia: Bricolage Grotesque (display), IBM Plex Sans (texto), IBM Plex Mono (dados), via Google Fonts.
- Animação: GSAP + ScrollTrigger, scroll suave com Lenis, ambos por CDN.
- Sem JavaScript a página continua legível: as animações usam `gsap.from()`, então o estado de repouso do CSS já é o estado final.
- `prefers-reduced-motion: reduce` desliga animação e scroll suave.
- Imagens em WebP, cerca de 200 KB no total.
