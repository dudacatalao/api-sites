from fastapi import FastAPI, HTTPException, status, Depends, Header, Path
from typing import Optional, Any, List
from modelo import Site
from time import sleep

def fake_db():
  try:
    print('Opening database..')
    sleep(3)
    
  finally:
    print('Closing database..')
    sleep(3)
    

app = FastAPI(description='API de sites úteis para seu projeto front-end', title='API para Desenvolvedores Front-End', version='0.0.1')

sites = { 
  1: {
    'nome': 'Flaticon',
    'url': 'https://www.flaticon.com/',
    'objetivo': 'Oferece Ícones gratuitos e de diversas maneiras diferentes'
  },
  2: {
    'nome': 'Coolors',
    'url': 'https://coolors.co/',
    'objetivo': 'É um website que oferece paletas de cores que combinam, e você também pode crias sua própria paleta'
  },
  3: {
    'nome': 'Color Hunt',
    'url': 'https://colorhunt.co/',
    'objetivo': 'Paletas de cores gratuitas'
  },
  4: {
    'nome': 'Ecomm Design',
    'url': 'https://ecomm.design/',
    'objetivo': 'Site com inspirações de Design para Eccomerce'
  },
  5: {
    'nome': 'Site Inspire',
    'url': 'https://www.siteinspire.com/',
    'objetivo': 'Inspiração de sites criativos'
  },
  6: {
    'nome': 'GSAP',
    'url': 'https://gsap.com/',
    'objetivo': 'Site criativo para inspiração'
  },
  7: {
    'nome': 'UX CRUSH',
    'url': 'https://www.uxcrush.com/',
    'objetivo': 'Modelos Figma, kits de UI e recursos'
  },
  8: {
    'nome': 'CSS2JS',
    'url': 'https://css2js.dotenv.dev/',
    'objetivo': 'Transforma códigos CSS em JSX ou JS'
  },
  9: {
    'nome': 'Sketch',
    'url': 'https://www.sketch.com/',
    'objetivo': 'Uma ferramenta de design vetorial para Mac com foco em interface de usuário e design de aplicativos'
  },
  10: {
    'nome': 'Unsplash',
    'url': 'https://unsplash.com/',
    'objetivo': 'Oferece uma ampla variedade de fotos de alta resolução'
  },
  11: {
    'nome': 'Freepik',
    'url': 'https://www.freepik.com/',
    'objetivo': 'Oferece uma enorme coleção de recursos gráficos gratuitos, incluindo imagens, vetores, ícones, e muito mais'
  },
  12: {
    'nome': 'CSS-Tricks',
    'url': 'https://css-tricks.com/',
    'objetivo': 'Fonte de tutoriais, artigos, truques e dicas sobre CSS, HTML e JavaScript, além de discussões sobre as melhores práticas de desenvolvimento web.'
  },
  13: {
    'nome': 'Smashing Magazine',
    'url': 'https://www.smashingmagazine.com/',
    'objetivo': 'ma revista online e blog que oferece artigos úteis, tutoriais e recursos sobre design web, desenvolvimento front-end e UX/UI'
  },
  14: {
    'nome': 'CodePen',
    'url': 'https://codepen.io/',
    'objetivo': 'Uma plataforma onde os desenvolvedores front-end podem compartilhar e experimentar código HTML, CSS e JavaScript, explorar projetos de outros desenvolvedores e colaborar em desafios de codificação'
  },
  15: {
    'nome': 'Frontend Masters',
    'url': 'https://frontendmasters.com/',
    'objetivo': 'Uma plataforma de educação online que oferece cursos avançados sobre desenvolvimento front-end, incluindo JavaScript, CSS, React, Vue.js e muito mais'
  },
  16: {
    'nome': 'Dev.to',
    'url': 'https://dev.to/',
    'objetivo': 'Uma comunidade de desenvolvedores onde você pode ler e escrever artigos, participar de discussões e interagir com outros profissionais de tecnologia'
  },
  17: {
    'nome': 'Mozilla Developer Network (MDN)',
    'url': 'https://developer.mozilla.org/',
    'objetivo': 'ma excelente referência para documentação e guias sobre HTML, CSS, JavaScript e outros aspectos do desenvolvimento web, mantida pela Mozilla Foundation'
  },
  18: {
    'nome': 'Frontend Mentor',
    'url': 'https://www.frontendmentor.io/',
    'objetivo': 'Oferece desafios de codificação para aprimorar suas habilidades de HTML, CSS e JavaScript, com projetos de design de interfaces de usuário para praticar'
  },
  19: {
    'nome': 'FontAwesome',
    'url': 'https://fontawesome.com/',
    'objetivo': 'Oferece uma ampla variedade de ícones vetoriais e ferramentas para incorporá-los em seus projetos web'
  },
  20: {
    'nome': 'CSS Gradient',
    'url': 'https://cssgradient.io/',
    'objetivo': 'Ferramenta para criar e explorar gradientes CSS personalizados, com opções de personalização avançadas'
  },
}


#método get(visualizar)
@app.get("/")
async def raiz():
    return {'mensagem': 'API encontrada'}

@app.get('/site')
async def get_sites(db: Any = Depends(fake_db)):
    return sites

@app.get('/site/{site_id}')
async def get_site(site_id: int = Path(..., title='Método para buscar o site pelo id', gt=0, lt=30, description='Selecionar site por id, onde o id deve estar entre 0 e 20')):
    if site_id not in sites:
        raise HTTPException(status_code=404, detail="Site não encontrado")
    else:
      return sites[site_id]


#método post(criar)
@app.post('/site', status_code=status.HTTP_201_CREATED)
async def post_site(site: Optional[Site] = None):
    if site.id not in site:
      next_id = len(sites) + 1
      sites[next_id] = site
      del site.id
      return site
    else:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Esse site já existe')

#método put(atualizar)
@app.put('/site/{site_id}')
async def put_site(site_id: int, site: Site):
    if site.id not in sites:
      sites[site_id] = site
      site.id = site_id
      del site.id
      return site
    else:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Não existe um site com esse id')

#método delete(excluir)
@app.delete('/site/{site_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_site(site_id: int):
    if site_id in sites:
      del sites[site_id]
      return
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Não existe um site com esse id')
  
      
if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8000, log_level="info", reload=True)