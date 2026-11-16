#!/usr/bin/env python3
"""Build original vector reference sprites for the normalized projectile contract.
Requires CairoSVG (pip install cairosvg). Reference samples, not final painted tower artwork.
"""
from pathlib import Path
import json, math
import cairosvg
ROOT = Path(__file__).resolve().parents[1] / 'sets/projectiles-v1'
STYLES = [
 ('arrow','기본 화살','#dec69b',48,'arrow'),('elf','엘프 잎날 화살','#89d975',48,'arrow'),
 ('spirit','정령 화살','#5de6ee',52,'arrow'),('rune','룬 화살','#c694ff',48,'arrow'),
 ('bullet','드워프 총탄','#ffc572',40,'bullet'),('gatling','개틀링 예광탄','#ffb54d',48,'bullet'),
 ('sniper','저격탄','#fff0b4',64,'bullet'),('magic','기본 마법탄','#63baff',44,'orb'),
 ('sorcery','소서리스 마법탄','#69e6ef',48,'orb'),('fire','화염구','#ff8339',60,'fire'),
 ('arcane','비전 지속광선','#cb8cff',44,'beam'),('dark','흑마법탄','#a4ce64',48,'orb'),
 ('curse','저주탄','#ec568f',48,'orb'),('decay','부패탄','#a1d83c',52,'glob')]
def svg(body,w,h):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'
ROOT.mkdir(parents=True,exist_ok=True)
for id,label,color,size,kind in STYLES:
 folder=ROOT/'projectiles'/id;folder.mkdir(parents=True,exist_ok=True)
 flight=[];impact=[]
 for frame in range(4):
  pulse=[.65,1,.8,.5][frame]
  glow=f'<ellipse cx="43" cy="32" rx="14" ry="9" fill="{color}" opacity="{pulse*.22}"/>'
  if kind=='arrow':
   body=f'<path d="M9 32H46" stroke="#382c24" stroke-width="5"/><path d="M9 32H46" stroke="{color}" stroke-width="2.5"/><path d="M8 26L20 30V34L8 38L11 32Z" fill="{color}" stroke="#44352b" stroke-width="1"/><path d="M41 27L51 32L41 37L43 32Z" fill="#f0eee1" stroke="{color}" stroke-width="1"/>'
   if id=='arrow': body+=f'<path d="M{19+frame*5} 31h5" stroke="#fff9dc" opacity="{pulse}"/>'
   if id!='arrow': body=glow+body+f'<path d="M{7+frame*2} 28L27 32L{7+frame*2} 36" fill="none" stroke="{color}" opacity=".6"/>'
   if id=='rune':body+=f'<path d="M34 26L38 32L34 38L30 32Z" fill="{color}"/>'
  elif kind=='bullet':
   tail=5 if id=='sniper' else (9 if id=='gatling' else 23)
   body=glow+f'<path d="M{tail} 32L42 29L51 32L42 35Z" fill="{color}" opacity="{.55+pulse*.4}"/><path d="M39 29H47L52 32L47 35H39Z" fill="#fff6d6"/><path d="M{tail} 32H44" stroke="#fffdf3" stroke-width="1.5"/>'
  elif kind=='beam':
   body=f'<path d="M0 32H64" stroke="{color}" stroke-width="18" opacity=".14"/><path d="M0 32H64" stroke="{color}" stroke-width="8" opacity=".8"/><path d="M0 32H64" stroke="#fff5ff" stroke-width="2.5"/><path d="M0 {26+frame} Q16 {40-frame*2} 32 {26+frame} T64 {26+frame}" fill="none" stroke="{color}" stroke-width="2"/>'
  else:
   body=glow+f'<path d="M7 32Q23 {19-frame} 46 24L53 32L46 40Q22 {43+frame} 7 32Z" fill="{color}" opacity=".35"/>'
   if kind=='fire': body+=f'<path d="M8 32L26 {18+frame}L24 28L40 21L49 25L54 32L48 39L35 43L24 35L16 38L21 31Z" fill="#f25d27"/><ellipse cx="44" cy="32" rx="9" ry="8" fill="#ffc34a"/>'
   elif kind=='glob':body+=f'<path d="M34 23Q47 18 53 30Q57 38 47 42Q34 44 32 34Q28 29 34 23Z" fill="{color}"/><circle cx="24" cy="{28+frame}" r="3" fill="{color}"/>'
   else:body+=f'<ellipse cx="44" cy="32" rx="10" ry="8" fill="{color}"/>'
   body+='<ellipse cx="46" cy="30" rx="4" ry="3" fill="#fff6d9"/>'
   if id=='curse':body+=f'<path d="M44 21L53 32L44 43L35 32Z" fill="none" stroke="{color}" stroke-width="1.5"/>'
  flight.append(f'<g transform="translate({frame*64} 0)">{body}</g>')
  r=[3,7,11,14][frame];a=[1,.8,.45,.12][frame]
  rays=''.join(f'<path d="M{16+math.cos(k*math.pi/3)*r*.45:.2f} {16+math.sin(k*math.pi/3)*r*.45:.2f}L{16+math.cos(k*math.pi/3)*r:.2f} {16+math.sin(k*math.pi/3)*r:.2f}" stroke="{color}" stroke-width="2"/>' for k in range(6))
  body=f'<g opacity="{a}"><circle cx="16" cy="16" r="{r}" fill="{color}" opacity=".2"/><circle cx="16" cy="16" r="{max(1,5-frame)}" fill="#fff5d8"/>{rays}</g>'
  impact.append(f'<g transform="translate({frame*32} 0)">{body}</g>')
 for name,body,w,h in [('flight',''.join(flight),256,64),('impact',''.join(impact),128,32)]:
  source=folder/(name+'.svg');source.write_text(svg(body,w,h))
  cairosvg.svg2png(url=str(source),write_to=str(folder/(name+'.png')))
 meta={'version':1,'id':id,'label':label,'kind':kind,'flight':{'file':'flight.png','canvas':[256,64],'cell':[64,64],'frames':4,'pivot':[48,32],'forward':'+X','fps':12,'draw_size':size},'impact':{'file':'impact.png','canvas':[128,32],'cell':[32,32],'frames':4,'pivot':[16,16],'duration':.24},'provenance':'Original procedural SVG reference artwork; source SVGs included; no external assets. Visual animation never defines combat cadence or damage.'}
 (folder/'meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
(ROOT/'styles.json').write_text(json.dumps([{'id':id,'label':label,'size':size,'beam':kind=='beam'} for id,label,c,size,kind in STYLES],ensure_ascii=False,indent=2)+'\n')
