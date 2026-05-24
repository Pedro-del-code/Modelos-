"""
Gerador de Slides — Modelos Atômicos
Canvas 2D puro — zero dependências externas, funciona offline e no Render
"""
import json, os

MODELOS = [
    {
        "id": "democrito", "nome": "Demócrito", "subtitulo": "O Filósofo do Átomo",
        "ano": "460–370 a.C.", "cor": "#00f5d4", "cor_rgb": "0,245,212", "tipo_2d": "democrito",
        "descricao": "O filósofo grego Demócrito propôs que toda a matéria era composta de partículas indivisíveis chamadas <b>átomos</b> (do grego <i>atomos</i> = indivisível). Ele imaginou que entre os átomos existiria apenas o <b>vazio</b>.",
        "contexto": "Grécia Antiga, escola atomista fundada por Leucipo. Ideia puramente filosófica, sem instrumentos científicos.",
        "caracteristicas": ["Átomos são indivisíveis e eternos","Existem diferentes formas e tamanhos","Átomos se movem livremente no vazio","Modelo puramente filosófico"],
        "limitacoes": "Sem base experimental. Aristóteles rejeitou a ideia, atrasando o desenvolvimento por quase 2.000 anos.",
        "legado": "Primeiro a usar o conceito de átomo — base de toda a química moderna.",
    },
    {
        "id": "dalton", "nome": "John Dalton", "subtitulo": "A Teoria Atômica Científica",
        "ano": "1803", "cor": "#f72585", "cor_rgb": "247,37,133", "tipo_2d": "dalton",
        "descricao": "Dalton retomou o átomo com base científica. Sua <b>Teoria Atômica</b> foi a primeira com suporte experimental, fundamentada nas leis de conservação da massa e das proporções definidas.",
        "contexto": "Revolução Industrial na Inglaterra. Dalton era meteorologista e chegou ao átomo estudando a composição dos gases.",
        "caracteristicas": ["Átomos são esferas maciças e indivisíveis","Átomos do mesmo elemento são idênticos em massa","Compostos = união de átomos diferentes","Reações químicas apenas reorganizam átomos"],
        "limitacoes": "Não explicava eletricidade, luz emitida por gases nem partículas subatômicas.",
        "legado": "Fundou a química moderna como ciência quantitativa.",
    },
    {
        "id": "thomson", "nome": "J.J. Thomson", "subtitulo": "Pudim de Passas",
        "ano": "1897", "cor": "#7209b7", "cor_rgb": "114,9,183", "tipo_2d": "thomson",
        "descricao": "Com a descoberta do <b>elétron</b> em tubos de raios catódicos, Thomson provou que o átomo <b>é divisível</b>. Propôs o Pudim de Passas: esfera de carga positiva com elétrons embutidos.",
        "contexto": "Era da eletricidade. Experimentos com tubos de vidro a vácuo revelaram os raios catódicos.",
        "caracteristicas": ["Átomo contém elétrons de carga negativa","Carga positiva distribuída uniformemente","Elétrons embutidos na carga positiva","Átomo é eletricamente neutro"],
        "limitacoes": "Derrubado por Rutherford (1909), que mostrou a carga positiva concentrada em um núcleo minúsculo.",
        "legado": "Primeira prova de que o átomo tem estrutura interna. Nobel de 1906.",
    },
    {
        "id": "rutherford", "nome": "Rutherford", "subtitulo": "Experimento da Folha de Ouro",
        "ano": "1911", "cor": "#f77f00", "cor_rgb": "247,127,0", "tipo_2d": "rutherford",
        "descricao": "No <b>Experimento da Folha de Ouro</b>, bombardeou ouro com partículas alfa. A maioria atravessou, mas algumas desviaram drasticamente — provando a existência de um <b>núcleo</b> pequeno, denso e positivo.",
        "contexto": "Universidade de Manchester. O resultado surpreendeu até o próprio Rutherford.",
        "caracteristicas": ["Núcleo central pequeno, denso e positivo","Núcleo concentra quase toda a massa","Elétrons orbitam ao redor do núcleo","Átomo é majoritariamente espaço vazio"],
        "limitacoes": "Pela física clássica, elétrons irradiariam energia e colidiriam com o núcleo em ~10⁻⁸ s.",
        "legado": "Descoberta do núcleo atômico. Base de toda a física nuclear.",
    },
    {
        "id": "bohr", "nome": "Niels Bohr", "subtitulo": "Órbitas Quantizadas",
        "ano": "1913", "cor": "#4361ee", "cor_rgb": "67,97,238", "tipo_2d": "bohr",
        "descricao": "Bohr aplicou a <b>teoria quântica</b> ao modelo de Rutherford. Elétrons só existem em <b>órbitas fixas com energias definidas</b>. Saltos entre órbitas emitem ou absorvem fótons de luz.",
        "contexto": "Copenhagen. Bohr trabalhou com Rutherford em Manchester e se inspirou na teoria quântica de Planck.",
        "caracteristicas": ["Elétrons em órbitas circulares fixas","Cada órbita tem energia quantizada","Salto para órbita menor → emissão de fóton","Explica o espectro de emissão do Hidrogênio"],
        "limitacoes": "Falha para átomos com mais de um elétron. Não explica orbitais nem o Princípio da Incerteza.",
        "legado": "Introduziu a quantização de energia nos átomos. Nobel de 1922.",
    },
    {
        "id": "sommerfeld", "nome": "Sommerfeld", "subtitulo": "Órbitas Elípticas e Relatividade",
        "ano": "1916", "cor": "#e9c46a", "cor_rgb": "233,196,106", "tipo_2d": "sommerfeld",
        "descricao": "Sommerfeld aprimorou Bohr adicionando <b>órbitas elípticas</b> e efeitos relativísticos para explicar a <b>estrutura fina</b> dos espectros atômicos.",
        "contexto": "Munique. Sommerfeld foi mentor de Heisenberg, Pauli e outros gigantes da física quântica.",
        "caracteristicas": ["Órbitas elípticas além das circulares","Número quântico azimutal (l)","Correções relativísticas para elétrons rápidos","Explica o desdobramento de linhas espectrais"],
        "limitacoes": "Ainda baseado em trajetórias definidas. Não explica o spin do elétron.",
        "legado": "Transição entre o modelo clássico e a mecânica quântica moderna.",
    },
    {
        "id": "quantum", "nome": "Modelo Quântico", "subtitulo": "A Nuvem de Probabilidade",
        "ano": "1926", "cor": "#06d6a0", "cor_rgb": "6,214,160", "tipo_2d": "quantum",
        "descricao": "Schrödinger, Heisenberg e De Broglie desenvolveram a <b>Mecânica Quântica</b>. O elétron não tem posição definida — existe como <b>nuvem de probabilidade</b> descrita pela função de onda ψ.",
        "contexto": "Europa 1925–1927. Em dois anos, Einstein, Bohr e Heisenberg redefiniriam a física para sempre.",
        "caracteristicas": ["Princípio da Incerteza: Δx·Δp ≥ ℏ/2","Elétron tem natureza dual: onda e partícula","Orbitais s, p, d, f — regiões de probabilidade","4 números quânticos: n, l, mₗ, mₛ"],
        "limitacoes": "Modelo atual — extremamente preciso. Matematicamente muito complexo.",
        "legado": "Base de toda a eletrônica, lasers, semicondutores e tecnologia quântica.",
    },
]

JS_ANIMATIONS = r"""
// ── Canvas 2D — sem dependências externas ─────────────────────────────────────
var _animHandles = {};

function startCanvas(id, tipo, cor) {
  var canvas = document.getElementById('c-' + id);
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var t = 0;
  var particles = buildParticles(tipo, cor);
  var RAF = null;

  function resize() {
    canvas.width  = canvas.offsetWidth  || canvas.parentElement.offsetWidth  || 280;
    canvas.height = canvas.offsetHeight || canvas.parentElement.offsetHeight || 220;
  }
  resize();
  window.addEventListener('resize', resize);

  function loop() {
    RAF = requestAnimationFrame(loop);
    t += 0.016;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var cx = canvas.width / 2, cy = canvas.height / 2;
    drawModel(ctx, tipo, cor, cx, cy, canvas.width, canvas.height, t);
  }
  if (_animHandles[id]) cancelAnimationFrame(_animHandles[id]);
  RAF = requestAnimationFrame(loop);
  _animHandles[id] = RAF;
}

function hex2rgb(hex) {
  var r = parseInt(hex.slice(1,3),16), g = parseInt(hex.slice(3,5),16), b = parseInt(hex.slice(5,7),16);
  return [r, g, b];
}

function drawGlow(ctx, x, y, r, cor, alpha) {
  var grad = ctx.createRadialGradient(x, y, 0, x, y, r);
  var rgb = hex2rgb(cor);
  grad.addColorStop(0,   'rgba('+rgb+','+alpha+')');
  grad.addColorStop(0.5, 'rgba('+rgb+','+(alpha*0.4)+')');
  grad.addColorStop(1,   'rgba('+rgb+',0)');
  ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI*2);
  ctx.fillStyle = grad; ctx.fill();
}

function drawSphere(ctx, x, y, r, cor, emissive) {
  var grad = ctx.createRadialGradient(x-r*0.3, y-r*0.3, r*0.05, x, y, r);
  var rgb = hex2rgb(cor);
  grad.addColorStop(0,   'rgba('+rgb.map(v=>Math.min(255,v+80))+',1)');
  grad.addColorStop(0.5, 'rgba('+rgb+',1)');
  grad.addColorStop(1,   'rgba('+rgb.map(v=>Math.max(0,v-60))+',1)');
  ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI*2);
  ctx.fillStyle = grad; ctx.fill();
  if (emissive) {
    ctx.beginPath(); ctx.arc(x, y, r*1.35, 0, Math.PI*2);
    ctx.fillStyle = 'rgba('+hex2rgb(cor)+','+(emissive*0.18)+')';
    ctx.fill();
  }
}

function drawOrbit(ctx, cx, cy, rx, ry, rot, cor, alpha) {
  ctx.save();
  ctx.translate(cx, cy); ctx.rotate(rot);
  ctx.beginPath(); ctx.ellipse(0, 0, rx, ry, 0, 0, Math.PI*2);
  ctx.strokeStyle = 'rgba('+hex2rgb(cor)+','+alpha+')';
  ctx.lineWidth = 1.2; ctx.stroke();
  ctx.restore();
}

function drawElectron(ctx, cx, cy, rx, ry, rot, ang, cor, r) {
  var ex = cx + rx * Math.cos(ang);
  var ey = cy + ry * Math.sin(ang);
  // rotacionar
  var dx = ex - cx, dy = ey - cy;
  var nx = dx * Math.cos(rot) - dy * Math.sin(rot) + cx;
  var ny = dx * Math.sin(rot) + dy * Math.cos(rot) + cy;
  drawGlow(ctx, nx, ny, r*3.5, cor, 0.55);
  drawSphere(ctx, nx, ny, r, cor, 0);
  return { x: nx, y: ny };
}

// ── Demócrito: esfera grande + partículas ao redor ──
function drawDemocrito(ctx, cor, cx, cy, W, H, t) {
  var R = Math.min(W, H) * 0.28;
  drawGlow(ctx, cx, cy, R*2.2, cor, 0.12);
  drawSphere(ctx, cx, cy, R, cor, 0.4);
  // grade wireframe sobre a esfera
  ctx.save();
  ctx.globalAlpha = 0.09;
  ctx.strokeStyle = '#ffffff';
  ctx.lineWidth = 1;
  for (var i = 0; i < 6; i++) {
    var a = i / 6 * Math.PI;
    ctx.beginPath();
    ctx.ellipse(cx, cy, R, R * Math.abs(Math.cos(a + t*0.3)), a + t*0.3, 0, Math.PI*2);
    ctx.stroke();
  }
  ctx.restore();
  // partículas orbitando
  for (var i = 0; i < 32; i++) {
    var baseAng = i / 32 * Math.PI * 2 + t * 0.4;
    var dist = R * (1.55 + 0.35 * Math.sin(i * 2.3 + t));
    var px = cx + dist * Math.cos(baseAng);
    var py = cy + dist * Math.sin(baseAng) * 0.45;
    var pr = 2 + Math.sin(i + t*1.5) * 1;
    var alpha = 0.4 + 0.4 * Math.sin(i * 1.7 + t);
    ctx.beginPath(); ctx.arc(px, py, pr, 0, Math.PI*2);
    ctx.fillStyle = 'rgba('+hex2rgb(cor)+','+alpha+')'; ctx.fill();
  }
}

// ── Dalton: esfera maciça + latitudes ──
function drawDalton(ctx, cor, cx, cy, W, H, t) {
  var R = Math.min(W, H) * 0.28;
  drawGlow(ctx, cx, cy, R*1.8, cor, 0.14);
  drawSphere(ctx, cx, cy, R, cor, 0.3);
  ctx.save(); ctx.globalAlpha = 0.18; ctx.strokeStyle = '#fff'; ctx.lineWidth = 1;
  for (var i = 0; i < 5; i++) {
    var lat = (i / 4 - 0.5) * Math.PI;
    var ry = R * Math.cos(lat);
    var yy = cy + R * Math.sin(lat);
    ctx.beginPath(); ctx.ellipse(cx, yy, ry, ry * 0.25, t*0.2, 0, Math.PI*2); ctx.stroke();
  }
  for (var j = 0; j < 4; j++) {
    var rot = j / 4 * Math.PI + t*0.15;
    ctx.beginPath(); ctx.ellipse(cx, cy, R*0.5, R, rot, 0, Math.PI*2); ctx.stroke();
  }
  ctx.restore();
}

// ── Thomson: esfera translúcida + elétrons pulsando ──
function drawThomson(ctx, cor, cx, cy, W, H, t) {
  var R = Math.min(W, H) * 0.28;
  drawGlow(ctx, cx, cy, R*2.0, cor, 0.1);
  // esfera translúcida
  var rgb = hex2rgb(cor);
  ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI*2);
  ctx.fillStyle = 'rgba('+rgb+',0.18)'; ctx.fill();
  ctx.strokeStyle = 'rgba('+rgb+',0.4)'; ctx.lineWidth = 1.5; ctx.stroke();
  // elétrons embutidos
  for (var i = 0; i < 10; i++) {
    var baseAng = i/10*Math.PI*2 + t*0.35;
    var dist = R * (0.35 + 0.5 * ((i%3)/2));
    var pulse = 1 + 0.18*Math.sin(t*2 + i);
    var ex = cx + dist*Math.cos(baseAng)*pulse;
    var ey = cy + dist*Math.sin(baseAng)*pulse*0.6;
    drawGlow(ctx, ex, ey, 14, '#ffdd00', 0.5);
    ctx.beginPath(); ctx.arc(ex, ey, 4.5, 0, Math.PI*2);
    ctx.fillStyle = '#ffdd00'; ctx.fill();
  }
}

// ── Rutherford: núcleo + 3 órbitas elípticas ──
function drawRutherford(ctx, cor, cx, cy, W, H, t) {
  var scale = Math.min(W, H) * 0.42;
  // órbitas
  var orbits = [
    { rx: scale*0.32, ry: scale*0.18, rot: 0.3,  sp: 1.1 },
    { rx: scale*0.52, ry: scale*0.28, rot: -0.8, sp: 0.75 },
    { rx: scale*0.72, ry: scale*0.22, rot: 1.2,  sp: 0.5 },
  ];
  orbits.forEach(function(o) { drawOrbit(ctx, cx, cy, o.rx, o.ry, o.rot, cor, 0.3); });
  // núcleo
  drawGlow(ctx, cx, cy, 28, cor, 0.6);
  drawSphere(ctx, cx, cy, 12, cor, 0.8);
  // elétrons
  orbits.forEach(function(o, i) {
    var ang = t * o.sp + i * 2.1;
    drawElectron(ctx, cx, cy, o.rx, o.ry, o.rot, ang, '#00cfff', 5);
  });
}

// ── Bohr: núcleo + 3 órbitas circulares + elétrons ──
function drawBohr(ctx, cor, cx, cy, W, H, t) {
  var scale = Math.min(W, H) * 0.42;
  var niveis = [
    { r: scale*0.28, n:2, sp:1.1, ecor: '#ffffff' },
    { r: scale*0.50, n:4, sp:0.7, ecor: '#aaddff' },
    { r: scale*0.72, n:6, sp:0.45,ecor: '#8899ff' },
  ];
  niveis.forEach(function(nv) {
    ctx.beginPath(); ctx.arc(cx, cy, nv.r, 0, Math.PI*2);
    ctx.strokeStyle = 'rgba('+hex2rgb(cor)+',0.28)'; ctx.lineWidth=1.2; ctx.stroke();
  });
  drawGlow(ctx, cx, cy, 26, cor, 0.65);
  drawSphere(ctx, cx, cy, 11, cor, 0.9);
  niveis.forEach(function(nv) {
    for (var i = 0; i < nv.n; i++) {
      var ang = t*nv.sp + i/nv.n*Math.PI*2;
      var ex = cx + nv.r*Math.cos(ang), ey = cy + nv.r*Math.sin(ang);
      drawGlow(ctx, ex, ey, 12, nv.ecor, 0.5);
      ctx.beginPath(); ctx.arc(ex, ey, 4, 0, Math.PI*2);
      ctx.fillStyle = nv.ecor; ctx.fill();
    }
  });
}

// ── Sommerfeld: núcleo + órbitas elípticas multicoloridas ──
function drawSommerfeld(ctx, cor, cx, cy, W, H, t) {
  var scale = Math.min(W, H) * 0.42;
  var cfgs = [
    { rx: scale*0.28, ry: scale*0.28, rot: 0,            sp: 1.4, hue: 0.0 },
    { rx: scale*0.50, ry: scale*0.22, rot: Math.PI/4,    sp: 1.0, hue: 0.15 },
    { rx: scale*0.60, ry: scale*0.30, rot: -Math.PI/3,   sp: 0.72, hue: 0.3 },
    { rx: scale*0.72, ry: scale*0.18, rot: Math.PI/1.5,  sp: 0.55, hue: 0.55 },
    { rx: scale*0.40, ry: scale*0.35, rot: Math.PI/2,    sp: 0.9,  hue: 0.7 },
  ];
  cfgs.forEach(function(c2, i) {
    var rgb = hslToRgb(c2.hue, 0.9, 0.62);
    var ecor = 'rgb('+rgb+')';
    drawOrbit(ctx, cx, cy, c2.rx, c2.ry, c2.rot + t*0.04, ecor, 0.4);
    var ang = t*c2.sp + i*1.3;
    var ex = cx + c2.rx*Math.cos(ang + c2.rot);
    var ey = cy + c2.ry*Math.sin(ang)*Math.cos(c2.rot) - c2.ry*Math.cos(ang)*Math.sin(c2.rot)*0.5;
    drawGlow(ctx, ex, ey, 13, ecor, 0.55);
    ctx.beginPath(); ctx.arc(ex, ey, 4.5, 0, Math.PI*2);
    ctx.fillStyle = ecor; ctx.fill();
  });
  drawGlow(ctx, cx, cy, 22, cor, 0.7);
  drawSphere(ctx, cx, cy, 10, cor, 0.85);
}

// ── Quântico: nuvem de pontos + núcleo ──
function drawQuantum(ctx, cor, cx, cy, W, H, t) {
  var scale = Math.min(W, H) * 0.42;
  var rgb = hex2rgb(cor);
  // nuvem de probabilidade — pontos com posição pseudo-aleatória mas determinística
  for (var i = 0; i < 320; i++) {
    var seed = i * 1.618;
    var r_base = scale * (0.12 + Math.pow(fract(seed * 0.37), 0.5) * 0.88);
    var r = r_base + Math.sin(t * 0.4 + seed) * scale * 0.04;
    var th = fract(seed * 0.618) * Math.PI * 2 + t * (0.004 + fract(seed * 0.11) * 0.012);
    var ph = fract(seed * 0.293) * Math.PI;
    var x = cx + r * Math.sin(ph) * Math.cos(th);
    var y = cy + r * Math.sin(ph) * Math.sin(th) * 0.55;
    var alpha = 0.25 + 0.55 * Math.exp(-r / (scale * 0.5)) + 0.2 * Math.sin(t + seed);
    var size = 1.2 + 1.4 * Math.exp(-r / (scale * 0.35));
    ctx.beginPath(); ctx.arc(x, y, size, 0, Math.PI*2);
    ctx.fillStyle = 'rgba('+rgb+','+Math.max(0.05, Math.min(0.9, alpha))+')';
    ctx.fill();
  }
  drawGlow(ctx, cx, cy, 24, cor, 0.8);
  drawSphere(ctx, cx, cy, 9, cor, 1.0);
}

function fract(x) { return x - Math.floor(x); }

function hslToRgb(h, s, l) {
  var r, g, b;
  if (s === 0) { r = g = b = l; }
  else {
    function hue2rgb(p, q, t) {
      if (t < 0) t += 1; if (t > 1) t -= 1;
      if (t < 1/6) return p + (q-p)*6*t;
      if (t < 1/2) return q;
      if (t < 2/3) return p + (q-p)*(2/3-t)*6;
      return p;
    }
    var q = l < 0.5 ? l*(1+s) : l+s-l*s, p = 2*l-q;
    r = hue2rgb(p,q,h+1/3); g = hue2rgb(p,q,h); b = hue2rgb(p,q,h-1/3);
  }
  return [Math.round(r*255), Math.round(g*255), Math.round(b*255)];
}

var DRAWS = {
  democrito: drawDemocrito, dalton: drawDalton, thomson: drawThomson,
  rutherford: drawRutherford, bohr: drawBohr, sommerfeld: drawSommerfeld, quantum: drawQuantum
};

function drawModel(ctx, tipo, cor, cx, cy, W, H, t) {
  DRAWS[tipo](ctx, cor, cx, cy, W, H, t);
}
"""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;background:#070b12;color:#e8eaf0;font-family:'Syne',sans-serif}

#prog{position:fixed;top:0;left:0;right:0;height:3px;background:rgba(255,255,255,.05);z-index:200}
#pf{height:100%;width:0;background:#4361ee;transition:width .4s ease,background .4s ease}

#wrap{position:fixed;inset:0;overflow:hidden}
#track{display:flex;height:100%;will-change:transform;transition:transform .42s cubic-bezier(.4,0,.2,1)}

.slide{flex:0 0 100vw;width:100vw;height:100%;display:flex;flex-direction:column;overflow:hidden}

.canvas-area{
  flex:0 0 42%;position:relative;overflow:hidden;
  background:radial-gradient(ellipse at 50% 55%, rgba(var(--cor-rgb),.1) 0%, #070b12 72%);
}
@media(min-height:700px){.canvas-area{flex:0 0 44%}}
@media(min-width:768px){
  .slide{flex-direction:row}
  .canvas-area{flex:0 0 50%;height:100%}
}

.canvas2d{position:absolute;inset:0;width:100%;height:100%;display:block}

.badge{
  position:absolute;top:14px;left:14px;display:flex;align-items:center;gap:8px;
  background:rgba(0,0,0,.6);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border:1px solid rgba(255,255,255,.1);border-radius:99px;padding:6px 14px;z-index:2;
}
.bnum{font-family:'Space Mono',monospace;font-size:10px;color:#6b7280}
.bnome{font-size:12px;font-weight:700;color:var(--cor)}
.ano-tag{position:absolute;bottom:12px;right:14px;font-family:'Space Mono',monospace;font-size:10px;color:rgba(255,255,255,.22);letter-spacing:2px;z-index:2}

.divider{height:1px;background:linear-gradient(90deg,transparent,var(--cor),transparent);opacity:.3;flex-shrink:0}
@media(min-width:768px){
  .divider{display:none}
  .canvas-area::after{content:'';position:absolute;top:0;right:0;width:1px;height:100%;background:linear-gradient(180deg,transparent,var(--cor),transparent);opacity:.3}
}

.info-area{flex:1;overflow-y:auto;padding:20px 18px 100px;display:flex;flex-direction:column;gap:14px;scrollbar-width:none}
.info-area::-webkit-scrollbar{display:none}
@media(min-width:768px){.info-area{padding:28px 32px 40px}}

.subtitulo{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--cor);font-family:'Space Mono',monospace;margin-bottom:4px}
.titulo{font-size:25px;font-weight:800;line-height:1.1;letter-spacing:-.4px}
@media(min-width:768px){.titulo{font-size:30px}}
.desc{font-size:13px;line-height:1.8;color:rgba(232,234,240,.75)}

.contexto-box{background:rgba(255,255,255,.04);border-left:2px solid var(--cor);border-radius:0 8px 8px 0;padding:10px 14px}
.contexto-box p{font-size:12px;color:rgba(232,234,240,.55);line-height:1.6;font-style:italic}

.bloco-label{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--cor);font-family:'Space Mono',monospace;margin-bottom:10px}
.chars{list-style:none;display:flex;flex-direction:column;gap:8px}
.chars li{font-size:12.5px;display:flex;gap:9px;line-height:1.55;align-items:flex-start}
.ck{color:var(--cor);flex-shrink:0;font-size:9px;margin-top:4px}

.lim-box{background:rgba(255,70,50,.06);border:1px solid rgba(255,70,50,.18);border-radius:10px;padding:12px 14px;display:flex;gap:10px;align-items:flex-start}
.lim-i{color:#ff5040;flex-shrink:0;font-size:14px;margin-top:1px}
.lim-box p{font-size:12px;color:rgba(232,234,240,.65);line-height:1.65}

.legado-box{background:rgba(var(--cor-rgb),.06);border:1px solid rgba(var(--cor-rgb),.22);border-radius:10px;padding:12px 14px;display:flex;gap:10px;align-items:flex-start}
.legado-i{color:var(--cor);flex-shrink:0;font-size:14px;margin-top:1px}
.legado-box p{font-size:12px;color:rgba(232,234,240,.65);line-height:1.65}

#nav-bar{
  position:fixed;bottom:20px;left:50%;transform:translateX(-50%);
  display:flex;align-items:center;gap:8px;
  background:rgba(7,11,18,.88);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);
  border:1px solid rgba(255,255,255,.1);padding:10px 20px;border-radius:99px;z-index:200;
  box-shadow:0 8px 32px rgba(0,0,0,.5);
}
.dot{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.18);cursor:pointer;transition:all .3s;flex-shrink:0}
.dot.active{background:var(--cor,#4361ee);transform:scale(1.45);box-shadow:0 0 8px var(--cor,#4361ee)}

.nav-arrow{display:none;position:fixed;top:50%;transform:translateY(-50%);background:rgba(7,11,18,.7);border:1px solid rgba(255,255,255,.1);border-radius:50%;width:44px;height:44px;font-size:20px;color:rgba(255,255,255,.6);cursor:pointer;align-items:center;justify-content:center;transition:all .2s;z-index:200}
.nav-arrow:hover{background:rgba(67,97,238,.3);color:#fff}
#arr-l{left:16px} #arr-r{right:16px}
@media(min-width:768px){.nav-arrow{display:flex}}
"""

def gerar_html(modelos, js_anim):
    total = len(modelos)
    slides_js = json.dumps([{"id": m["id"], "tipo": m["tipo_2d"], "cor": m["cor"]} for m in modelos])

    slides_html = ""
    for i, m in enumerate(modelos):
        chars = "".join([f'<li><span class="ck">✦</span>{c}</li>' for c in m["caracteristicas"]])
        num = str(i+1).zfill(2)
        slides_html += f"""
<div class="slide" id="slide-{m['id']}" style="--cor:{m['cor']};--cor-rgb:{m['cor_rgb']}">
  <div class="canvas-area">
    <canvas id="c-{m['id']}" class="canvas2d"></canvas>
    <div class="badge"><span class="bnum">{num}/{str(total).zfill(2)}</span><span class="bnome">{m['nome']}</span></div>
    <div class="ano-tag">{m['ano']}</div>
  </div>
  <div class="divider"></div>
  <div class="info-area">
    <div><div class="subtitulo">{m['subtitulo']}</div><h2 class="titulo">{m['nome']}</h2></div>
    <p class="desc">{m['descricao']}</p>
    <div class="contexto-box"><p>📍 {m['contexto']}</p></div>
    <div class="bloco"><div class="bloco-label">Características</div><ul class="chars">{chars}</ul></div>
    <div class="lim-box"><span class="lim-i">⚠</span><p>{m['limitacoes']}</p></div>
    <div class="legado-box"><span class="legado-i">★</span><p>{m['legado']}</p></div>
  </div>
</div>"""

    dots_html = "".join([
        f'<span class="dot {"active" if i==0 else ""}" data-idx="{i}" style="--cor:{m["cor"]}"></span>'
        for i, m in enumerate(modelos)
    ])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<meta name="theme-color" content="#070b12">
<title>Modelos Atômicos</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>

<div id="prog"><div id="pf"></div></div>
<div id="wrap"><div id="track">{slides_html}</div></div>
<div id="nav-bar">{dots_html}</div>
<button class="nav-arrow" id="arr-l">‹</button>
<button class="nav-arrow" id="arr-r">›</button>

<script>
{js_anim}

var MODELOS = {slides_js};
var N = MODELOS.length;
var _idx = 0;
var _iniciados = {{}};
var _track = document.getElementById('track');

function ir(i, anim) {{
  if (i < 0 || i >= N) return;
  _idx = i;
  _track.style.transition = anim === false ? 'none' : 'transform .42s cubic-bezier(.4,0,.2,1)';
  _track.style.transform = 'translateX(' + (-_idx * 100) + 'vw)';
  document.querySelectorAll('.dot').forEach(function(d, j) {{ d.classList.toggle('active', j === _idx); }});
  var pf = document.getElementById('pf');
  pf.style.width = ((_idx+1)/N*100) + '%';
  pf.style.background = MODELOS[_idx].cor;
  [_idx, _idx+1, _idx-1].forEach(function(k) {{
    if (k < 0 || k >= N || _iniciados[MODELOS[k].id]) return;
    _iniciados[MODELOS[k].id] = true;
    var m = MODELOS[k];
    setTimeout(function() {{ startCanvas(m.id, m.tipo, m.cor); }}, 60);
  }});
}}

// Touch
(function() {{
  var tx0=0, ty0=0, sw=false, bx=0;
  var wrap = document.getElementById('wrap');
  wrap.addEventListener('touchstart', function(e) {{ tx0=e.touches[0].clientX; ty0=e.touches[0].clientY; sw=true; bx=-_idx*window.innerWidth; }}, {{passive:true}});
  wrap.addEventListener('touchmove', function(e) {{
    if(!sw) return;
    var dx=e.touches[0].clientX-tx0, dy=e.touches[0].clientY-ty0;
    if(Math.abs(dx)>Math.abs(dy)) {{ e.preventDefault(); _track.style.transition='none'; _track.style.transform='translateX('+(bx+dx)+'px)'; }}
  }}, {{passive:false}});
  wrap.addEventListener('touchend', function(e) {{
    if(!sw) return; sw=false;
    var dx=e.changedTouches[0].clientX-tx0;
    ir(Math.abs(dx)>48?(dx<0?Math.min(_idx+1,N-1):Math.max(_idx-1,0)):_idx);
  }});
}})();

document.addEventListener('keydown', function(e) {{
  if(e.key==='ArrowRight'||e.key==='ArrowDown') ir(_idx+1);
  if(e.key==='ArrowLeft'||e.key==='ArrowUp')    ir(_idx-1);
}});
document.querySelectorAll('.dot').forEach(function(d) {{ d.addEventListener('click', function() {{ ir(+d.dataset.idx); }}); }});
document.getElementById('arr-l').addEventListener('click', function() {{ ir(_idx-1); }});
document.getElementById('arr-r').addEventListener('click', function() {{ ir(_idx+1); }});
window.addEventListener('resize', function() {{
  ir(_idx, false);
  Object.keys(_animHandles).forEach(function(id) {{
    var c = document.getElementById('c-'+id);
    if(c) {{ c.width=c.offsetWidth||280; c.height=c.offsetHeight||220; }}
  }});
}});

// Inicia imediatamente — sem esperar CDN
ir(0, false);
</script>
</body>
</html>"""

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    print("Gerando…")
    html = gerar_html(MODELOS, JS_ANIMATIONS)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {out}  ({len(html.encode())//1024} KB)")
