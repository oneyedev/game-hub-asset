#!/usr/bin/env python3
"""Original SVG reference art for Engineer Art Studio; requires CairoSVG."""
from pathlib import Path
import json,math
import cairosvg
root=Path(__file__).resolve().parents[1]/'sets/engineer-v1/projectiles'
for id,color,kind in [('engineer_bolt','#c3c8bd','metal'),('engineer_stone','#b29c7c','stone'),('engineer_shock','#90dbe7','shock')]:
 d=root/id;d.mkdir(parents=True,exist_ok=True);flight=[];impact=[]
 for f in range(4):
  body=f'<path d="M{13+f*3} 31H39M{9+f*3} 35H32" stroke="{color}" stroke-width="2" opacity=".55"/>'
  if kind=='stone':body+='<path d="M35 27L43 23L51 28L53 36L46 41L37 38L32 32Z" fill="#897765" stroke="#3c3831" stroke-width="2"/><path d="M35 28L43 25L48 29L41 32Z" fill="#d5c2a3"/>'
  else:body+='<path d="M32 27L46 25L53 32L46 39L32 37Z" fill="#778388" stroke="#303b3f" stroke-width="2"/><path d="M33 28L46 27L50 31H33Z" fill="#dde3d7"/>'
  if kind=='shock':body+=f'<ellipse cx="42" cy="32" rx="{12+f%2}" ry="11" stroke="{color}" stroke-width="1.5" fill="none" opacity="{.4+f*.12}"/>'
  body+=f'<path d="M{34+f*3} 30h3" stroke="#fff3d5" stroke-width="1.5"/>'
  flight.append(f'<g transform="translate({f*64} 0)">{body}</g>')
  r=[3,7,11,14][f];alpha=[1,.8,.45,.12][f]
  rays=''.join(f'<path d="M{16+math.cos(k*math.pi/3)*r*.45:.2f} {16+math.sin(k*math.pi/3)*r*.45:.2f}L{16+math.cos(k*math.pi/3)*r:.2f} {16+math.sin(k*math.pi/3)*r:.2f}" stroke="{color}" stroke-width="2"/>' for k in range(6))
  body=f'<g opacity="{alpha}"><circle cx="16" cy="16" r="{r}" fill="{color}" opacity=".16"/><circle cx="16" cy="16" r="{max(1,5-f)}" fill="#fff2d4"/>{rays}</g>'
  impact.append(f'<g transform="translate({f*32} 0)">{body}</g>')
 for phase,body,w,h in [('flight',''.join(flight),256,64),('impact',''.join(impact),128,32)]:
  svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">{body}</svg>';p=d/(phase+'.svg');p.write_text(svg);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(d/(phase+'.png')))
 (d/'meta.json').write_text(json.dumps({'id':id,'status':'studio-candidate','flight':{'canvas':[256,64],'cell':[64,64],'frames':4,'pivot':[48,32]},'impact':{'canvas':[128,32],'cell':[32,32],'frames':4,'duration':.24},'provenance':'Original SVG reference. Physical tool slug/stone; cyan marks an actual empowered third shot, never adds damage or stun.'},indent=2)+'\n')
