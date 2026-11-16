#!/usr/bin/env python3
"""Original SVG reference art for siege studio. Requires CairoSVG."""
from pathlib import Path
import math,json
import cairosvg
root=Path(__file__).resolve().parents[1]/'sets/siege-v1/projectiles'
for id,color,kind,size in [('siege_shell','#59636b','ball',36),('siege_heavy','#83905d','shell',44),('siege_bolt','#a6c5c9','bolt',58),('siege_circus','#eb5b68','circus',42)]:
 d=root/id;d.mkdir(parents=True,exist_ok=True);fl=[];im=[]
 for f in range(4):
  body=f'<path d="M{14+f*2} 30H36M{10+f} 35H32" stroke="#b5a186" stroke-width="2" opacity=".45"/>'
  if kind=='bolt':body+='<path d="M9 32H47" stroke="#253238" stroke-width="5"/><path d="M11 32H46" stroke="#c2d2d6" stroke-width="2"/><path d="M40 26L53 32L40 38L43 32Z" fill="#d6e1dc" stroke="#475c62"/><path d="M9 26L22 30V34L9 38L12 32Z" fill="#6b8c80"/>'
  elif kind=='shell':body+='<path d="M32 24H45Q55 32 45 40H32Z" fill="#39432e" stroke="#1c2528" stroke-width="2"/><path d="M35 25H45Q50 28 51 31H35Z" fill="#98a579"/><path d="M34 25V39" stroke="#c0a76b" stroke-width="3"/>'
  else:
   body+=f'<circle cx="43" cy="32" r="10" fill="{color}" stroke="#26313b" stroke-width="2"/><ellipse cx="40" cy="28" rx="4" ry="2.5" fill="#edf4e3" opacity=".6"/>'
   if kind=='circus':body+=f'<path d="M{38+f} 24Q{46-f} 32 {39+f} 40" stroke="#f1d66b" stroke-width="3" fill="none"/>'
  body+=f'<path d="M{22+f*4} 31h3" stroke="#fff6cf" stroke-width="1" opacity=".8"/>'
  fl.append(f'<g transform="translate({64*f} 0)">{body}</g>')
  r=[3,7,11,14][f];a=[1,.8,.45,.12][f]
  rays=''.join(f'<path d="M{16+math.cos(k*math.pi/3)*r*.45:.2f} {16+math.sin(k*math.pi/3)*r*.45:.2f}L{16+math.cos(k*math.pi/3)*r:.2f} {16+math.sin(k*math.pi/3)*r:.2f}" stroke="{color if kind in ("circus","bolt") else "#dbb67b"}" stroke-width="2"/>' for k in range(6))
  im.append(f'<g transform="translate({32*f} 0)" opacity="{a}"><circle cx="16" cy="16" r="{r}" fill="#b89d78" opacity=".35"/><circle cx="16" cy="16" r="{max(1,5-f)}" fill="#ffe0a2"/>{rays}</g>')
 for phase,body,w,h in [('flight',''.join(fl),256,64),('impact',''.join(im),128,32)]:
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">{body}</svg>';(d/(phase+'.svg')).write_text(svg);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(d/(phase+'.png')))
 (d/'meta.json').write_text(json.dumps({'id':id,'size':size,'flight':{'canvas':[256,64],'cell':[64,64],'frames':4,'pivot':[48,32]},'impact':{'canvas':[128,32],'cell':[32,32],'frames':4,'duration':.24},'provenance':'Original SVG reference art. Fixed-ground explosion for shells; one effect per actual pierced victim for bolts. No fake bounces or skills.'},indent=2)+'\n')
